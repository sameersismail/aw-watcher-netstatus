import sys
import socket
import logging
from time import sleep
from datetime import datetime, timezone

from aw_core.models import Event
from aw_client import ActivityWatchClient

from aw_watcher_netstatus.config import watcher_config
from aw_watcher_netstatus.settings import Settings


logger = logging.getLogger(__name__)


class NetworkWatcher:
    def __init__(self, testing=False):
        config_section = (
            "aw-watcher-netstatus"
            if testing == False
            else "aw-watcher-netstatus-testing"
        )
        self.settings = Settings(watcher_config[config_section])

        self.client = ActivityWatchClient("aw-watcher-netstatus", testing=testing)
        self.bucketname = f"{self.client.client_name}_{self.client.client_hostname}"

    def run(self):
        logger.info("aw-watcher-netstatus started")

        eventtype = "networkstatus"
        self.client.create_bucket(self.bucketname, eventtype, queued=True)

        with self.client:
            self.heartbeat_loop()

    def heartbeat_loop(self):
        while True:
            try:
                online = self.is_online()
                logger.debug(f"aw-watcher-netstatus: online={online}")
                self.ping(online)
                sleep(self.settings.poll_time)
            except KeyboardInterrupt:
                logger.info("aw-watcher-netstatus stopped by keyboard interrupt")
                break

    def ping(self, online: bool):
        data = {"status": "online" if online else "offline"}
        e = Event(timestamp=datetime.now(timezone.utc), data=data)
        # A generous 30s window in which to wait for the next datum
        pulsetime = self.settings.poll_time + 30
        self.client.heartbeat(self.bucketname, e, pulsetime=pulsetime, queued=True)

    def is_online(self) -> bool:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.settings.host, self.settings.port))
            return True
        except ConnectionRefusedError:
            return False
        except socket.gaierror:
            return False
        except BaseException as e:
            logger.warning(f"Unknown exception encountered: {e}")
            return False

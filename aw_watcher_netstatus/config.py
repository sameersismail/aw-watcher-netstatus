from configparser import ConfigParser
from aw_core.config import load_config

default_settings = {
    "poll_time": "30",  # seconds
    "host": "google.com",
    "port": "80",
}

default_testing_settings = {
    "poll_time": "5",  # seconds
    "host": "localhost",
    "port": "8080",
}

default_config = ConfigParser()
default_config["aw-watcher-netstatus"] = default_settings
default_config["aw-watcher-netstatus-testing"] = default_testing_settings
watcher_config = load_config("aw-watcher-netstatus", default_config)

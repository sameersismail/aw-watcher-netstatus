from configparser import ConfigParser


class Settings:
    def __init__(self, config_section: ConfigParser):
        self.poll_time = config_section.getfloat("poll_time")
        self.host = config_section.get("host")
        self.port = config_section.getint("port")

        assert self.poll_time > 0
        assert (
            self.host is not None
        ), "Configuration is missing a valid `host` property."
        assert (
            self.port is not None
        ), "Configuration is missing a valid `port` property."

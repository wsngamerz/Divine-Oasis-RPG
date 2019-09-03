#
# Divine Oasis
# by wsngamerz
# divineoasis/logging.py
#

from logging import getLogger, Logger, addLevelName, DEBUG, INFO, WARNING, ERROR, CRITICAL
from logging.config import dictConfig
from divineoasis.config import Config



class Logging:
    def __init__(self, config: Config):
        self.config = config

        # setup logging config
        dictConfig({
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {
                    "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
                }
            },
            "handlers": {
                "default": {
                    "class": "logging.StreamHandler",
                    "formatter": "standard"
                }
            },
            "loggers": {
                "": {
                    "handlers": ["default"],
                    "propagate": True,
                    "level": self.config.get_option("options.log_level").upper()
                }
            }
        })

        addLevelName(DEBUG, "Debug")
        addLevelName(INFO, "Info")
        addLevelName(WARNING, "Warning")
        addLevelName(ERROR, "Error")
        addLevelName(CRITICAL, "Critical")


    def get_logger(self, name: str) -> Logger:
        return getLogger(name)
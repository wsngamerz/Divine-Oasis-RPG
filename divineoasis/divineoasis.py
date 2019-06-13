#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: divineoasis.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import divineoasis
import logging
import logging.config
import os

from divineoasis.assets import Assets
from divineoasis.config import Config
from divineoasis.colours import Colours


class DivineOasis:
    def __init__(self):
        # Enable Colours using black magic
        os.system("")

        # Setup Logging
        self.logger = self.setup_logging()

        # Basic classes
        self.config = Config()
        self.config.load()

        self.assets = Assets(self.config.get("language"))

    def start(self):
        self.logger.info(f"Starting Divine Oasis { divineoasis.__version__ }")

        large_title = self.assets.get("title.largeTitle")
        large_title.insert(0, "")
        large_title.append("")

        for row in large_title:
            print(row)

    @staticmethod
    def setup_logging():
        logging.basicConfig(level=logging.DEBUG)

        logging.config.dictConfig({
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {
                    "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
                }
            },
            "handlers": {
                "default": {
                    "level": "DEBUG",
                    "class": "logging.StreamHandler",
                    "formatter": "standard"
                }
            },
            "loggers": {
                "": {
                    "handlers": ["default"],
                    "propagate": True
                }
            }
        })

        logging.addLevelName(logging.DEBUG,    Colours.BOLD + Colours.BRIGHT_CYAN   + "DEBUG"   + Colours.RESET)
        logging.addLevelName(logging.INFO,     Colours.BOLD + Colours.BRIGHT_BLUE   + "INFO"    + Colours.RESET)
        logging.addLevelName(logging.WARNING,  Colours.BOLD + Colours.BRIGHT_YELLOW + "WARNING" + Colours.RESET)
        logging.addLevelName(logging.ERROR,    Colours.BOLD + Colours.BRIGHT_RED    + "ERROR"   + Colours.RESET)
        logging.addLevelName(logging.CRITICAL, Colours.BOLD + Colours.BRIGHT_RED    + Colours.BLINK + "CRITICAL" + Colours.RESET)

        return logging.getLogger(__name__)

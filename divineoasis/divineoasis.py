#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: divineoasis.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import logging
import logging.config

from divineoasis.assets import Assets
from divineoasis.config import Config


class DivineOasis:
    def __init__(self):
        # Setup Logging
        self.logger = self.setup_logging()

        # Basic classes
        self.config = Config()
        self.config.load()

        self.assets = Assets(self.config.get("language"))

    def start(self):
        self.logger.info("Starting Divine Oasis")

        large_title = self.assets.get("title", "largeTitle")
        large_title.insert(0, "")
        large_title.append("")
        for row in large_title:
            print(row)

    def setup_logging(self):
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

        return logging.getLogger(__name__)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: config.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import json
import logging
import os
import shutil

from divineoasis.assets import Directories


class Config:
    def __init__(self, application_root: str = None):
        self.logger = logging.getLogger(__name__)
        self.config = None
        self.directories = Directories(application_root)

    def _locate(self):
        self.logger.debug("Trying to find config file")

        try:
            with open(self.directories.config_location) as config_file:
                self.logger.debug("Config file found")
                config_file.close()

            return True
        except FileNotFoundError as error:
            self.logger.debug("Existing config file not found")
            self.logger.debug("Moving template configuration")

            try:
                if not os.path.exists(self.directories.data_directory):
                    os.makedirs(self.directories.data_directory)

                template_config = os.path.join(self.directories.assets_directory, "config.default.json")
                shutil.copyfile(template_config, self.directories.config_location)

                return True
            except Exception as error:
                self.logger.error(error)
                return False

    def load(self):
        self.logger.debug("Loading Configuration")

        if self._locate():
            with open(self.directories.config_location, "r") as config_file:
                self.logger.debug("Loading config file in memory")
                self.config = json.loads(config_file.read())
                self.logger.debug("Loaded config file in memory")
        else:
            self.config_file = None
            self.logger.error("Config file missing")

    def get(self, path: str):
        self.logger.debug(f"Getting { path } from config")
        keylist = path.split(".")

        config_data = self.config

        for key in keylist:
            config_data = config_data[key]

        return config_data

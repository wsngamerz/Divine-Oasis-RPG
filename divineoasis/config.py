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


class Config:
    def __init__(self, application_root=None):
        self.logger = logging.getLogger(__name__)
        self.config = None

        # Directories
        self.application_root = application_root or os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
        self.data_directory = os.path.join(self.application_root, "data")
        self.config_location = os.path.join(self.data_directory, "config.json")

    def _locate(self):
        self.logger.debug("Trying to find config file")

        try:
            with open(self.config_location) as config_file:
                self.logger.debug("Config file found")
                config_file.close()

            return True
        except FileNotFoundError as error:
            self.logger.debug("Existing config file not found")
            self.logger.debug("Moving template configuration")

            try:
                if not os.path.exists(self.data_directory):
                    os.makedirs(self.data_directory)

                template_config = os.path.join(self.application_root, "divineoasis", "assets", "config.default.json")
                shutil.copyfile(template_config, self.config_location)

                return True
            except Exception as error:
                self.logger.error(error)
                return False

    def load(self):
        self.logger.debug("Loading Configuration")
        self.logger.debug(f"Application Directory: { self.application_root }")
        self.logger.debug(f"       Data Directory: { self.data_directory }")
        self.logger.debug(f" Config File Location: { self.config_location }")

        if self._locate():
            with open(self.config_location, "r") as config_file:
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

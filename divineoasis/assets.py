#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: assets.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import json
import logging
import os


class Assets:
    def __init__(self, language: str = "en"):
        self.logger = logging.getLogger(__name__)
        self.lang = language
        self.assets_directory = os.path.abspath(os.path.join(os.path.dirname(__name__), "divineoasis", "assets", language))

        self.logger.debug(f"Setting up assets in language: { self.lang }")
        self.logger.debug(f"Assets path: { self.assets_directory }")

    def get(self, path: str):
        keylist = path.split(".")
        category = keylist[0]
        keylist.pop(0)
        file_location = os.path.join(self.assets_directory, f"{ category }.json")
        file_contents = None

        with open(file_location, "r") as asset_file:
            file_contents = json.loads(asset_file.read())
            asset_file.close()

        asset_data = file_contents
        for key in keylist:
            asset_data = asset_data[key]

        return asset_data

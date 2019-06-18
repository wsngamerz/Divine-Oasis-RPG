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
import pyglet


class Assets:
    def __init__(self, language: str = "en"):
        self.logger = logging.getLogger(__name__)
        self.lang = language
        self.assets_directory = os.path.join(Directories().assets_directory, self.lang)

        self.logger.debug(f"Setting up assets in language: { self.lang }")
        self.logger.debug(f"Assets path: { self.assets_directory }")

    def get(self, path: str) -> str:
        keylist = path.split(".")
        category = keylist[0]
        keylist.pop(0)
        file_location = os.path.join(self.assets_directory, f"{ category }.json")
        file_contents = None

        self.logger.debug(f"Getting { path } from { file_location }")

        with open(file_location, "r") as asset_file:
            file_contents = json.loads(asset_file.read())
            asset_file.close()

        asset_data = file_contents
        for key in keylist:
            asset_data = asset_data[key]

        return asset_data

    def get_pyglet_image(self, path: str) -> pyglet.image.AbstractImage:
        file_path = os.path.join(self.assets_directory, path.replace(".", "/") + ".png")
        pyglet_image = pyglet.image.load(file_path)

        self.logger.debug(f"Getting { file_path }")
        self.logger.debug(f"W: { pyglet_image.width } H: { pyglet_image.height } Anchor X: { pyglet_image.anchor_x } Anchor Y: { pyglet_image.anchor_y }")

        return pyglet_image


class Directories:
    def __init__(self, alternative_root: str = None):
        if alternative_root is not None:
            self.application_root = os.path.normpath(os.path.abspath(alternative_root))
        else:
            self.application_root = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

        self.assets_directory = os.path.join(self.application_root, "divineoasis", "assets")
        self.data_directory = os.path.join(self.application_root, "data")
        self.config_location = os.path.join(self.data_directory, "config.json")

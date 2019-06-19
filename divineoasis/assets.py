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

from pyglet.image import AbstractImage
from pyglet.media import Source


class Assets:
    def __init__(self, language: str = "en"):
        self.logger = logging.getLogger(__name__)
        self.lang = language
        self.assets_directory = os.path.join(Directories().assets_directory)
        self.lang_assets_directory = os.path.join(self.assets_directory, self.lang)

        self.logger.debug(f"Setting up assets in language: { self.lang }")
        self.logger.debug(f"Assets path: { self.assets_directory }")
        self.logger.debug(f"Assets path (w/ Lang): { self.lang_assets_directory }")

    def get(self, path: str) -> str:
        keylist, assets_root = self._language_path(path)
        category = keylist[0]
        keylist.pop(0)

        file_location = os.path.join(assets_root, f"{ category }.json")
        file_contents = None

        self.logger.debug(f"Getting { path } from { file_location }")

        with open(file_location, "r") as asset_file:
            file_contents = json.loads(asset_file.read())
            asset_file.close()

        asset_data = file_contents
        for key in keylist:
            asset_data = asset_data[key]

        return asset_data

    def get_pyglet_image(self, path: str) -> AbstractImage:
        keylist, assets_root = self._language_path(path)
        file_path = os.path.normpath(os.path.join(assets_root, "/".join(keylist) + ".png"))
        pyglet_image = pyglet.image.load(file_path)

        self.logger.debug(f"Getting { file_path }")
        self.logger.debug(f"W: { pyglet_image.width } H: { pyglet_image.height } Anchor X: { pyglet_image.anchor_x } Anchor Y: { pyglet_image.anchor_y }")

        return pyglet_image

    def get_pyglet_media(self, path: str) -> Source:
        keylist, assets_root = self._language_path(path)
        file_path = os.path.normpath(os.path.join(assets_root, "audio", "/".join(keylist) + ".mp3"))
        pyglet_media = pyglet.media.load(file_path)

        self.logger.debug(f"Getting { file_path }")
        self.logger.debug(f"AudioFormat: { pyglet_media.audio_format } VideoFormat: { pyglet_media.video_format }")
        self.logger.debug(f"Audio Info: title={ pyglet_media.info.title } author={ pyglet_media.info.author } copyright={ pyglet_media.info.copyright }")
        self.logger.debug(f"            comment={ pyglet_media.info.comment } album={ pyglet_media.info.album } year={ pyglet_media.info.year }")
        self.logger.debug(f"            track={ pyglet_media.info.track } genre={ pyglet_media.info.genre }")

        return pyglet_media
    
    def _language_path(self, path: str) -> tuple:
        keylist = path.split(".")

        # Test if lang
        assets_root = ""
        if keylist[0] == "lang":
            keylist.pop(0)
            assets_root = self.lang_assets_directory
        else:
            assets_root = self.assets_directory

        return keylist, assets_root


class Directories:
    def __init__(self, alternative_root: str = None):
        if alternative_root is not None:
            self.application_root = os.path.normpath(os.path.abspath(alternative_root))
        else:
            self.application_root = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

        self.assets_directory = os.path.join(self.application_root, "divineoasis", "assets")
        self.data_directory = os.path.join(self.application_root, "data")
        self.config_location = os.path.join(self.data_directory, "config.json")

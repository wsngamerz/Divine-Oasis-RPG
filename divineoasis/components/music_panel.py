#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: components/music_panel.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import logging

from divineoasis.components.component import Component

from pyglet.image import AbstractImage
from pyglet.sprite import Sprite
from pyglet.text import Label
from pyglet.window import Window


class MusicPanel(Component):
    def __init__(self, uid: str, x: int, y: int, width: int, height: int, texture: AbstractImage, song_name: str = "", song_artist: str = ""):
        self.button_logger = logging.getLogger(__name__)

        Component.__init__(self, uid, x, y, width, height)

        self._song_data = {
            "song_name": song_name,
            "song_artist": song_artist
        }

        self._panel_texture = texture
        self._label_x = self._x + 85
        self._name_label_y = self._y + 60
        self._artist_label_y = self._y + 35

        self.song_name_label = None
        self.song_artist_label = None
        self.music_panel_sprite = None

        self.load_labels()
        self.load_sprite()

        self.button_logger.debug("Music Panel Component initiated")

    def load_labels(self):
        self.song_name_label = Label(self._song_data["song_name"], font_size=20, font_name="Hydrophilia Iced",
                                    x=self._label_x, y=self._name_label_y,
                                    anchor_x="left", anchor_y="center")

        self.song_artist_label = Label(self._song_data["song_artist"], font_size=16, font_name="Hydrophilia Iced",
                                    x=self._label_x, y=self._artist_label_y,
                                    anchor_x="left", anchor_y="center")

    def load_sprite(self):
        self.music_panel_sprite = Sprite(self._panel_texture, self._x, self._y)

    def draw(self):
        self.music_panel_sprite.draw()
        self.song_name_label.draw()
        self.song_artist_label.draw()
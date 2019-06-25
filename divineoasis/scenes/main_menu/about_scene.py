#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: scenes/main_menu/about_scene.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import logging

from divineoasis.assets import Assets
from divineoasis.audio_manager import AudioManager

from divineoasis.graphics import Batch, OrderedGroup
from pyglet.window import Window


class AboutScene(Scene):
    def __init__(self, assets: Assets, window: Window, audio_manager: AudioManager):
        self.window = window
        self.assets = assets
        self.audio_manager = audio_manager
        self.logger = logging.getLogger(__name__)

        self.batch = Batch()
        self.background = OrderedGroup(0)
        self.foreground = OrderedGroup(1)

    def start_scene(self):
        pass

    def update(self, dt: float):
        pass

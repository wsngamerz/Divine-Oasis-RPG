#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: scenes/options_scene.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import logging

from divineoasis.assets import Assets
from divineoasis.audio_manager import AudioManager
from divineoasis.scene import Scene

from pyglet.window import Window


class OptionsScene(Scene):
    def __init__(self, assets: Assets, window: Window, audio_manager: AudioManager):
        self.window = window
        self.assets = assets
        self.audio_manager = audio_manager
        self.logger = logging.getLogger(__name__)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        cursor = self.window.get_system_mouse_cursor(self.window.CURSOR_DEFAULT)
        self.window.set_mouse_cursor(cursor)

    def update(self, dt: float):
        self.window.clear()

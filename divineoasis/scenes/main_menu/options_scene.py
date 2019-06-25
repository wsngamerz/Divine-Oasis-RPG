#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: scenes/main_menu/options_scene.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import logging

from divineoasis.assets import Assets
from divineoasis.audio_manager import AudioManager
from divineoasis.scene import Scene

from pyglet.graphics import Batch, OrderedGroup
from pyglet.sprite import Sprite
from pyglet.window import Window, FPSDisplay


class OptionsScene(Scene):
    def __init__(self, assets: Assets, window: Window, audio_manager: AudioManager):
        self.window = window
        self.assets = assets
        self.audio_manager = audio_manager
        self.logger = logging.getLogger(__name__)

        self.batch = Batch()
        self.background = OrderedGroup(0)
        self.foreground = OrderedGroup(1)

        self.images = {}
        self.sprites = {}

    def start_scene(self):
        self.load_sprite_images()
        self.draw_foreground()

    def load_sprite_images(self):
        self.images["back_button"] = self.assets.get_pyglet_image("lang.user_interface.back_button")

    def draw_foreground(self):
        pass

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        cursor = self.window.get_system_mouse_cursor(self.window.CURSOR_DEFAULT)
        self.window.set_mouse_cursor(cursor)

    def update(self, dt: float):
        self.window.clear()
        self.batch.draw()

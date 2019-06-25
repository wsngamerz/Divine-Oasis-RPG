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

        self.button_coords = {
            "back_button": [(512, 104), (768, 40)]
        }

    def start_scene(self):
        self.load_sprite_images()
        self.draw_foreground()

    def load_sprite_images(self):
        self.images["back_button_image"] = self.assets.get_pyglet_image("lang.user_interface.back_button")

    def draw_foreground(self):
        self.sprites["back_sprite"] = Sprite(self.images["back_button_image"],
                x=(self.window.width//2) - (self.images["back_button_image"].width//2),
                y=(self.window.height//2) - 320,
                batch=self.batch, group=self.foreground)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        cursor = self.window.get_system_mouse_cursor(self.window.CURSOR_DEFAULT)

        if x >= self.button_coords["back_button"][0][0] and x <= self.button_coords["back_button"][1][0]:
            if y <= self.button_coords["back_button"][0][1] and y >= self.button_coords["back_button"][1][1]:
                cursor = self.window.get_system_mouse_cursor(self.window.CURSOR_HAND)

        self.window.set_mouse_cursor(cursor)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if x >= self.button_coords["back_button"][0][0] and x <= self.button_coords["back_button"][1][0]:
            if y <= self.button_coords["back_button"][0][1] and y >= self.button_coords["back_button"][1][1]:
                self.logger.debug("Clicked Back Button")
                self.switch_sub_scene("MenuScene")

    def update(self, dt: float):
        self.window.clear()
        self.batch.draw()

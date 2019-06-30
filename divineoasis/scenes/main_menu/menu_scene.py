#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: scenes/main_scene/menu_scene.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import logging
import random
import sys

from divineoasis.assets import Assets
from divineoasis.audio_manager import AudioManager
from divineoasis.components.button import Button
from divineoasis.scene import Scene

from pyglet.graphics import Batch, OrderedGroup
from pyglet.sprite import Sprite
from pyglet.window import Window


class MenuScene(Scene):
    def __init__(self, assets: Assets, window: Window, audio_manager: AudioManager):
        Scene.__init__(self, assets, window, audio_manager)
        self.logger = logging.getLogger(__name__)

        self.batch = Batch()
        self.background = OrderedGroup(0)
        self.foreground = OrderedGroup(1)

        # List of sprites and images
        self.images = {}
        self.sprites = {}

    def start_scene(self):
        self.logger.debug(f"Menu Scene Window -> W: { self.window.width } H: { self.window.height }")
        self.load_sprite_images()
        self.draw_foreground()
        self.start_audio()

        buttons = [
            Button("play_button", 247, 200, 256, 64, self.assets.get_pyglet_image("user_interface.blank_button"), "Play"),
            Button("options_button", 512, 200, 256, 64, self.assets.get_pyglet_image("user_interface.blank_button"), "Options", lambda: self.switch_sub_scene("OptionsScene")),
            Button("quit_button", 777, 200, 256, 64, self.assets.get_pyglet_image("user_interface.blank_button"), "Quit", sys.exit)
        ]
        
        for button in buttons:
            self.gui.add_component(button)

    def load_sprite_images(self):
        self.images["logo_image"] = self.assets.get_pyglet_image("lang.user_interface.logo_v1")

    def start_audio(self):
        songs = [
            "menu.ove_melaa_italo_unlimited",
            "menu.ove_melaa_super_ninja_assasin",
            "menu.ove_melaa_power_of_thy_yes"
        ]

        random.shuffle(songs)
        self.logger.debug(f"Loading menu songs: { songs }")
        self.audio_manager.play_songs(songs, loop=True)

    def draw_foreground(self):
        self.sprites["logo_sprite"] = Sprite(self.images["logo_image"],
                x=(self.window.width//2) - (self.images["logo_image"].width//2),
                y=(self.window.height//2) - 50,
                batch=self.batch, group=self.foreground)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        cursor = self.window.get_system_mouse_cursor(self.window.CURSOR_DEFAULT)
        self.window.set_mouse_cursor(cursor)

    def update(self, dt: float):
        self.window.clear()
        self.batch.draw()
        self.gui.update(dt)

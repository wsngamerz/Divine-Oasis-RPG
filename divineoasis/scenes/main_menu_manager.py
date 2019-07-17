#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: scenes/main_menu_manager.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import logging
import random

from divineoasis.assets import Assets
from divineoasis.audio_manager import AudioManager
from divineoasis.scene import Scene

from divineoasis.scenes.main_menu.menu_scene import MenuScene
from divineoasis.scenes.main_menu.options_scene import OptionsScene

from pyglet.graphics import Batch, OrderedGroup
from pyglet.sprite import Sprite
from pyglet.window import Window, FPSDisplay


class MainMenu(Scene):
    def __init__(self, assets: Assets, window: Window, audio_manager: AudioManager):
        Scene.__init__(self, assets, window, audio_manager)

        self.logger = logging.getLogger(__name__)

        self.current_scene = None
        self.sub_scenes = {}

        self.add_sub_scene(MenuScene(self.assets, self.window, self.audio_manager))
        self.add_sub_scene(OptionsScene(self.assets, self.window, self.audio_manager))

        self.fps_display = FPSDisplay(self.window)
        self.fps_display.label.y = 680
        self.fps_display.label.color = (255, 255, 255, 255)

        # Background sprite & image
        self.background_image = None
        self.background_sprite = None

        # Pos for moving background
        self.bg_pos = [0, 0]

    def start_scene(self):
        # Load the music!
        self.load_audio()

        # Start the main menu scene
        self.switch_sub_scene("MenuScene")

        # Start fancy menu stuff
        self.load_background()
        self.play_audio()

    def add_sub_scene(self, scene: Scene):
        sub_scene_name = scene.__class__.__name__
        scene.switch_sub_scene = self.switch_sub_scene
        self.sub_scenes[sub_scene_name] = scene

    def load_audio(self):
        songs = [
            "menu.ove_melaa_italo_unlimited",
            "menu.ove_melaa_super_ninja_assasin",
            "menu.ove_melaa_power_of_thy_yes"
        ]

        random.shuffle(songs)
        self.logger.debug(f"Loading menu songs: { songs }")
        self.audio_manager.load_songs(songs, loop=True)

    def play_audio(self):
        self.audio_manager.play_songs()

    def load_background(self):
        self.background_image = self.assets.get_pyglet_image("user_interface.background")
        self.initiate_background()

    def initiate_background(self):
        if not self.background_image:
            self.load_background()
        self.background_sprite = Sprite(self.background_image, x=0, y=0,
                batch=self.current_scene.batch, group=self.current_scene.background)

    def switch_sub_scene(self, sub_scene_name: str):
        if sub_scene_name in self.sub_scenes:
            self.window.remove_handlers(self.current_scene)
            self.current_scene = self.sub_scenes[sub_scene_name]
            self.window.push_handlers(self.current_scene)
            self.initiate_background()
            self.current_scene.start_scene()

    def update(self, dt: float):
        self.bg_pos[0] -= 2
        self.bg_pos[1] -= 1

        if self.bg_pos[0] <= -4800:
            self.bg_pos = [0, 0]

        self.background_sprite.update(self.bg_pos[0], self.bg_pos[1])
        self.current_scene.update(dt)
        self.fps_display.draw()

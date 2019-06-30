#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: scenes/main_menu_manager.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import logging

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
        self.fps_display.label.color = (255, 255, 255, 255)

        # List of sprites and images
        self.images = {}
        self.sprites = {}

        # Pos for moving background
        self.bg_pos = [0, 0]

    def start_scene(self):
        # Load and draw background
        self.load_images()

        # Start the main menu scene
        self.switch_sub_scene("MenuScene")
        self.current_scene.start_scene()

    def add_sub_scene(self, scene: Scene):
        sub_scene_name = scene.__class__.__name__
        scene.switch_sub_scene = self.switch_sub_scene
        self.sub_scenes[sub_scene_name] = scene

    def load_images(self):
        self.images["background_image"] = self.assets.get_pyglet_image("user_interface.background")

    def scrolling_background(self):
        self.bg_pos[0] -= 2
        self.bg_pos[1] -= 1

        if self.bg_pos[0] <= -4800:
            self.bg_pos = [0, 0]

        self.sprites["background_sprite"] = Sprite(self.images["background_image"],
                x=round(self.bg_pos[0]), y=round(self.bg_pos[1]),
                batch=self.current_scene.batch, group=self.current_scene.background)

    def switch_sub_scene(self, scene_name: str):
        if scene_name in self.sub_scenes:
            self.window.remove_handlers(self.current_scene)
            self.current_scene = self.sub_scenes[scene_name]
            self.window.push_handlers(self.current_scene)
            self.current_scene.start_scene()

    def update(self, dt: float):
        self.scrolling_background()
        self.current_scene.update(dt)
        self.fps_display.draw()

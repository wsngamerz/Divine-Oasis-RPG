#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: scene_manager.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import logging

from divineoasis.assets import Assets
from divineoasis.audio_manager import AudioManager
from divineoasis.scene import Scene

from divineoasis.scenes.main_menu_manager import MainMenu

from pyglet.window import Window


class SceneManager:
    def __init__(self, assets: Assets, window: Window):
        self.assets = assets
        self.audio_manager = AudioManager(self.assets, channels=8)
        self.window = window
        self.logger = logging.getLogger(__name__)

        # List of scenes
        self.scenes = {}
        self.current_scene: Scene = None

        # Add scenes
        self.add_scene(MainMenu(self.assets, self.window, self.audio_manager))

        self.switch_scene("MainMenu")

    def add_scene(self, scene: Scene):
        scene_name = scene.__class__.__name__
        scene.switch_scene = self.switch_scene
        self.scenes[scene_name] = scene

        self.logger.debug(f"Added { scene_name } to scene list")

    def switch_scene(self, scene_name: str):
        if scene_name in self.scenes:
            self.window.remove_handlers(self.current_scene)
            self.current_scene = self.scenes[scene_name]
            self.window.push_handlers(self.current_scene)
            self.logger.debug(f"Switching to Scene: { scene_name }")
            self.current_scene.start_scene()

    def update(self, dt: float):
        self.current_scene.update(dt)

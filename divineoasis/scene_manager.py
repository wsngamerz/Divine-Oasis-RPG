#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: scene_manager.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

from divineoasis.assets import Assets
from divineoasis.audio_manager import AudioManager
from divineoasis.scene import Scene
from divineoasis.scenes.menu_scene import MenuScene

from pyglet.window import Window


class SceneManager:
    def __init__(self, assets: Assets, window: Window):
        self.assets = assets
        self.audio_manager = AudioManager(self.assets, channels=8)
        self.window = window

        # List of scenes
        self.scenes = {}
        self.current_scene: Scene = None

        # Add scenes
        self.add_scene(MenuScene(self.assets, self.window, self.audio_manager))

        self.switch_scene("MenuScene")

    def add_scene(self, scene: Scene):
        self.scenes[scene.__class__.__name__] = scene

    def switch_scene(self, scene_name: str):
        if scene_name in self.scenes:
            self.current_scene = self.scenes[scene_name]

    def update(self, dt: float):
        self.current_scene.update(dt)

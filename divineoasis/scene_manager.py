#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: scene.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import pyglet

from divineoasis.scene import Scene
from divineoasis.scenes.menu_scene import MenuScene


class SceneManager:
    def __init__(self, window: pyglet.window.Window):
        self.window = window

        # List of scenes
        self.scenes = {}
        self.current_scene: Scene = None

        # Add scenes
        self.add_scene(MenuScene(self.window))

        self.switch_scene("MenuScene")

    def add_scene(self, scene: Scene):
        self.scenes[scene.__class__.__name__] = scene

    def switch_scene(self, scene_name: str):
        if scene_name in self.scenes:
            self.current_scene = self.scenes[scene_name]

    def update(self, dt: float):
        self.current_scene.update(dt)

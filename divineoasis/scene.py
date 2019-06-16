#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: scene.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import pyglet


class Scene:
    def __init__(self):
        pass


class SceneManager:
    def __init__(self, window: pyglet.window.Window):
        self.window = window

        # List of scenes
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, scene: Scene):
        pass

    def switch_scene(self, scene_name: str):
        pass

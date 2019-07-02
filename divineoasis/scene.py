#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: scene.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

from divineoasis.assets import Assets
from divineoasis.audio_manager import AudioManager
from divineoasis.gui_manager import GuiManager

from pyglet.window import Window

class Scene:
    def __init__(self, assets: Assets, window: Window, audio: AudioManager):
        self.assets = assets
        self.audio_manager = audio
        self.window = window
        self.gui = GuiManager(self.window)

    def switch_scene(self, scene_name: str):
        pass

    def switch_sub_scene(self, sub_scene_name: str):
        pass

    def update(self, dt: float):
        pass

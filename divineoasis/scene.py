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

from pyglet.window import Window

class Scene:
    def __init__(self, assets: Assets, window: Window, audio: AudioManager):
        self.assets = assets
        self.audio_manager = audio
        self.window = window

    def update(self, dt: float):
        pass

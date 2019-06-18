#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: scene.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import pyglet

from divineoasis.assets import Assets

class Scene:
    def __init__(self, assets: Assets, window: pyglet.window.Window):
        self.assets = assets
        self.window = window

    def update(self, dt: float):
        pass

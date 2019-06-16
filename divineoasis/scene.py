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
    def __init__(self, window: pyglet.window.Window):
        self.window = window

    def update(self, dt: float):
        pass

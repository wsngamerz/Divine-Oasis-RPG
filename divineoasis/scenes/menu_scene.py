#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: scenes/menu_scene.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import pyglet

from divineoasis.scene import Scene


class MenuScene(Scene):
    def __init__(self, window: pyglet.window.Window):
        super().__init__(window)

        self.window = window

        self.title = pyglet.text.Label("Divine Oasis",
                                        font_size=36,
                                        x=window.height/2,
                                        y=window.height/2,
                                        anchor_x="center",
                                        anchor_y="center")

    def update(self, dt: float):
        self.window.clear()
        self.title.draw()

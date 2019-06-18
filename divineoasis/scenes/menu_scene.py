#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: scenes/menu_scene.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import os
import pyglet

from divineoasis.assets import Assets
from divineoasis.scene import Scene


class MenuScene(Scene):
    def __init__(self, assets: Assets, window: pyglet.window.Window):
        super().__init__(assets, window)

        self.window = window
        self.assets = assets

        self.batch = pyglet.graphics.Batch()
        self.background = pyglet.graphics.OrderedGroup(0)
        self.foreground = pyglet.graphics.OrderedGroup(1)

        logo_image = self.assets.get_pyglet_image("logo")
        self.logo_sprite = pyglet.sprite.Sprite(logo_image,
                x=(window.width//2) - (logo_image.width//2),
                y=(window.height//2) + (logo_image.height//2),
                batch=self.batch, group=self.foreground)

    def update(self, dt: float):
        self.window.clear()
        self.batch.draw()

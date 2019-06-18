#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: scenes/menu_scene.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import logging
import pyglet

from divineoasis.assets import Assets
from divineoasis.scene import Scene


class MenuScene(Scene):
    def __init__(self, assets: Assets, window: pyglet.window.Window):
        super().__init__(assets, window)

        self.window = window
        self.assets = assets
        self.logger = logging.getLogger(__name__)

        self.window.on_mouse_motion = self.handle_mouse

        self.batch = pyglet.graphics.Batch()
        self.background = pyglet.graphics.OrderedGroup(0)
        self.foreground = pyglet.graphics.OrderedGroup(1)

        self.logger.debug(f"Menu Scene Window -> W: { self.window.width } H: { self.window.height }")
        self.draw_background()
        self.draw_foreground()

    def draw_background(self):
        background_image = self.assets.get_pyglet_image("ui.background")
        self.background_sprite = pyglet.sprite.Sprite(background_image,
                batch=self.batch, group=self.background)

    def draw_foreground(self):
        logo_image = self.assets.get_pyglet_image("ui.logo")
        self.logo_sprite = pyglet.sprite.Sprite(logo_image,
                x=(self.window.width//2) - (logo_image.width//2),
                y=(self.window.height//2) + 200,
                batch=self.batch, group=self.foreground)
        
        play_button_image = self.assets.get_pyglet_image("ui.play_button")
        self.play_button_sprite = pyglet.sprite.Sprite(play_button_image,
                x=(self.window.width//2) - (play_button_image.width//2),
                y=(self.window.height//2),
                batch=self.batch, group=self.foreground)

    def handle_mouse(self, x, y, dx, dy):
        # self.logger.debug(f"Mouse -> X: { x } Y: { y } DX: { dx } DY: { dy }")
        # Extremely spammy debug log ^^^^

        # PlayBtn Coords: [(x1, y1), (x2, y2)]
        # Play button = 256x64
        # 640, 360 = centre
        # TODO: Calculate coords of play button and listen for when mouse enters
        # TODO: Listen for click event
        play_button = [(512, 0), (768, 0)]

    def update(self, dt: float):
        self.window.clear()
        self.batch.draw()

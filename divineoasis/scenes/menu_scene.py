#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: scenes/menu_scene.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import logging
import sys

from divineoasis.assets import Assets
from divineoasis.audio_manager import AudioManager
from divineoasis.scene import Scene

from pyglet.graphics import Batch, OrderedGroup
from pyglet.sprite import Sprite
from pyglet.window import Window, FPSDisplay


class MenuScene(Scene):
    def __init__(self, assets: Assets, window: Window, audio_manager: AudioManager):
        self.window = window
        self.assets = assets
        self.audio_manager = audio_manager
        self.logger = logging.getLogger(__name__)

        self.batch = Batch()
        self.background = OrderedGroup(0)
        self.foreground = OrderedGroup(1)

        self.fps_display = FPSDisplay(self.window)
        self.fps_display.label.color = (255, 255, 255, 255)

        # Coordinates of elements for mouse stuff
        self.button_coords = {
            "play_button": [(512, 424), (768, 360)],
            "options_button": [(512, 344), (768, 280)],
            "quit_button": [(512, 264), (768, 180)]
        }

        # List of sprites and images
        self.images = {}
        self.sprites = {}

        # Pos for moving background
        self.bg_pos = [0, 0]

        self.logger.debug(f"Menu Scene Window -> W: { self.window.width } H: { self.window.height }")
        self.load_sprite_images()
        self.draw_background()
        self.draw_foreground()
        self.start_audio()

    def load_sprite_images(self):
        self.images["background_image"] = self.assets.get_pyglet_image("user_interface.background_large")
        self.images["logo_image"] = self.assets.get_pyglet_image("lang.user_interface.logo")
        self.images["play_button_image"] = self.assets.get_pyglet_image("lang.user_interface.play_button")
        self.images["options_button_image"] = self.assets.get_pyglet_image("lang.user_interface.options_button")
        self.images["quit_button_image"] = self.assets.get_pyglet_image("lang.user_interface.quit_button")

    def start_audio(self):
        self.audio_manager.play_song("menu.ove_melaa_italo_unlimited", loop=True)

    def draw_background(self):
        self.bg_pos[0] -= 2
        self.bg_pos[1] -= 1

        if self.bg_pos[0] <= -1280:
            self.bg_pos = [0, 0]

        self.sprites["background_sprite"] = Sprite(self.images["background_image"],
                x=round(self.bg_pos[0]), y=round(self.bg_pos[1]),
                batch=self.batch, group=self.background)

    def draw_foreground(self):
        self.sprites["logo_sprite"] = Sprite(self.images["logo_image"],
                x=(self.window.width//2) - (self.images["logo_image"].width//2),
                y=(self.window.height//2) + 200,
                batch=self.batch, group=self.foreground)

        self.sprites["play_button_sprite"] = Sprite(self.images["play_button_image"],
                x=(self.window.width//2) - (self.images["play_button_image"].width//2),
                y=(self.window.height//2),
                batch=self.batch, group=self.foreground)

        self.sprites["options_button_sprite"] = Sprite(self.images["options_button_image"],
                x=(self.window.width//2) - (self.images["options_button_image"].width//2),
                y=(self.window.height//2) - 80,
                batch=self.batch, group=self.foreground)

        self.sprites["quit_button_sprite"] = Sprite(self.images["quit_button_image"],
                x=(self.window.width//2) - (self.images["quit_button_image"].width//2),
                y=(self.window.height//2) - 160,
                batch=self.batch, group=self.foreground)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        cursor = self.window.get_system_mouse_cursor(self.window.CURSOR_DEFAULT)
        # self.logger.debug(f"Mouse -> X: { x } Y: { y } DX: { dx } DY: { dy }")
        # Extremely spammy debug log ^^^^

        if ((x >= self.button_coords["play_button"][0][0] and x <= self.button_coords["play_button"][1][0] and y <= self.button_coords["play_button"][0][1] and y >= self.button_coords["play_button"][1][1]) or
                (x >= self.button_coords["options_button"][0][0] and x <= self.button_coords["options_button"][1][0] and y <= self.button_coords["options_button"][0][1] and y >= self.button_coords["options_button"][1][1]) or
                (x >= self.button_coords["quit_button"][0][0] and x <= self.button_coords["quit_button"][1][0] and y <= self.button_coords["quit_button"][0][1] and y >= self.button_coords["quit_button"][1][1])):
            cursor = self.window.get_system_mouse_cursor(self.window.CURSOR_HAND)

        self.window.set_mouse_cursor(cursor)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        # self.logger.debug(f"Mouse Click -> X: { x } Y: { y } Button: { button } Modifier: { modifiers }")
        if x >= self.button_coords["play_button"][0][0] and x <= self.button_coords["play_button"][1][0]:
            # Within button area for x
            if y <= self.button_coords["play_button"][0][1] and y >= self.button_coords["play_button"][1][1]:
                # Play button
                self.logger.debug("Clicked Play Button")

            elif y <= self.button_coords["options_button"][0][1] and y >= self.button_coords["options_button"][1][1]:
                # Options Button
                self.logger.debug("Clicked Options Button")
                self.switch_scene("OptionsScene")

            elif y <= self.button_coords["quit_button"][0][1] and y >= self.button_coords["quit_button"][1][1]:
                # Quit button
                self.logger.debug("Clicked Quit Button")
                sys.exit()

    def update(self, dt: float):
        self.window.clear()
        self.draw_background()
        self.batch.draw()
        self.fps_display.draw()

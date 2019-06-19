#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: scenes/menu_scene.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import logging

from divineoasis.assets import Assets
from divineoasis.audio_manager import AudioManager
from divineoasis.scene import Scene

from pyglet.graphics import Batch, OrderedGroup
from pyglet.sprite import Sprite
from pyglet.window import Window


class MenuScene(Scene):
    def __init__(self, assets: Assets, window: Window, audio_manager: AudioManager):
        self.window = window
        self.assets = assets
        self.audio_manager = audio_manager
        self.logger = logging.getLogger(__name__)

        self.window.on_mouse_motion = self.handle_mouse_movement
        self.window.on_mouse_press = self.handle_mouse_click

        self.batch = Batch()
        self.background = OrderedGroup(0)
        self.foreground = OrderedGroup(1)

        # Coordinates of elements for mouse stuff
        self.play_button = [(512, 424), (768, 360)]
        self.options_button = [(512, 344), (768, 280)]
        self.quit_button = [(512, 264), (768, 180)]

        self.logger.debug(f"Menu Scene Window -> W: { self.window.width } H: { self.window.height }")
        self.draw_background()
        self.draw_foreground()
        self.start_audio()

    def start_audio(self):
        self.audio_manager.play_song("menu.ove_melaa_italo_unlimited", loop=True)

    def draw_background(self):
        background_image = self.assets.get_pyglet_image("user_interface.background")
        self.background_sprite = Sprite(background_image,
                batch=self.batch, group=self.background)

    def draw_foreground(self):
        logo_image = self.assets.get_pyglet_image("lang.user_interface.logo")
        self.logo_sprite = Sprite(logo_image,
                x=(self.window.width//2) - (logo_image.width//2),
                y=(self.window.height//2) + 200,
                batch=self.batch, group=self.foreground)
        
        play_button_image = self.assets.get_pyglet_image("lang.user_interface.play_button")
        self.play_button_sprite = Sprite(play_button_image,
                x=(self.window.width//2) - (play_button_image.width//2),
                y=(self.window.height//2),
                batch=self.batch, group=self.foreground)

        options_button_image = self.assets.get_pyglet_image("lang.user_interface.options_button")
        self.options_button_sprite = Sprite(options_button_image,
                x=(self.window.width//2) - (options_button_image.width//2),
                y=(self.window.height//2) - 80,
                batch=self.batch, group=self.foreground)

        quit_button_image = self.assets.get_pyglet_image("lang.user_interface.quit_button")
        self.quit_button_sprite = Sprite(quit_button_image,
                x=(self.window.width//2) - (quit_button_image.width//2),
                y=(self.window.height//2) - 160,
                batch=self.batch, group=self.foreground)

    def handle_mouse_movement(self, x: int, y: int, dx: int, dy: int):
        cursor = self.window.get_system_mouse_cursor(self.window.CURSOR_DEFAULT)
        # self.logger.debug(f"Mouse -> X: { x } Y: { y } DX: { dx } DY: { dy }")
        # Extremely spammy debug log ^^^^

        if ((x >= self.play_button[0][0] and x <= self.play_button[1][0] and y <= self.play_button[0][1] and y >= self.play_button[1][1]) or
                (x >= self.options_button[0][0] and x <= self.options_button[1][0] and y <= self.options_button[0][1] and y >= self.options_button[1][1]) or
                (x >= self.quit_button[0][0] and x <= self.quit_button[1][0] and y <= self.quit_button[0][1] and y >= self.quit_button[1][1])):
            cursor = self.window.get_system_mouse_cursor(self.window.CURSOR_HAND)

        self.window.set_mouse_cursor(cursor)

    def handle_mouse_click(self, x: int, y: int, button: int, modifiers: int):
        # self.logger.debug(f"Mouse Click -> X: { x } Y: { y } Button: { button } Modifier: { modifiers }")
        if x >= self.play_button[0][0] and x <= self.play_button[1][0]:
            # Within button area for x
            if y <= self.play_button[0][1] and y >= self.play_button[1][1]:
                # Play button
                self.logger.debug("Clicked Play Button")

            elif y <= self.options_button[0][1] and y >= self.options_button[1][1]:
                # Options Button
                self.logger.debug("Clicked Options Button")

            elif y <= self.quit_button[0][1] and y >= self.quit_button[1][1]:
                # Quit button
                self.logger.debug("Clicked Quit Button")

    def update(self, dt: float):
        self.window.clear()
        self.batch.draw()

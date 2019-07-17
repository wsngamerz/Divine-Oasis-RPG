#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: components/button.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import logging
import os
import pyglet

from divineoasis.components.component import Component

from pyglet.sprite import Sprite
from pyglet.text import Label
from pyglet.window import Window


class Button(Component):
    def __init__(self, uid: str, x: int, y: int, style: str = "button_blue_large", text: str = "", click_function = None):
        self.button_logger = logging.getLogger(__name__)

        self._text = text
        self._style = style

        self._sprite = None
        self._sprite_normal = None
        self._sprite_hover = None
        self._texture_normal = None
        self._texture_hover = None

        self.load_textures()

        Component.__init__(self, uid, x, y, self._texture_normal.width, self._texture_normal.height)

        self._label = None
        self._label_x = self._x + (self._texture_normal.width // 2)
        self._label_y = (self._y + (self._texture_normal.height // 2)) + 3

        self.is_hovering = False

        self.load_label()
        self.load_sprite()

        if click_function is None:
            self._click_function = lambda: print("No Function Added")
        else:
            self._click_function = click_function

        self.button_logger.debug("Button Component initiated")

    def load_label(self):
        self._label = Label(self._text, font_size=33, font_name="Hydrophilia Iced",
                            x=self._label_x, y=self._label_y,
                            anchor_x="center", anchor_y="center")

    def load_textures(self):
        style_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "assets", "user_interface"))
        self._texture_normal = pyglet.image.load(os.path.join(style_path, f"{ self._style }.png"))
        self._texture_hover = pyglet.image.load(os.path.join(style_path, f"{ self._style }_hover.png"))

    def load_sprite(self):
        self._sprite_normal = Sprite(self._texture_normal, self._x, self._y)
        self._sprite_hover = Sprite(self._texture_hover, self._x, self._y)
        self._sprite = self._sprite_normal

    def on_mouse_enter(self, window: Window, x: int, y: int):
        self.__handle_hover(window, True)

    def on_mouse_motion(self, window: Window, x: int, y: int, dx: int, dy: int):
        self.__handle_hover(window, True)

    def on_mouse_press(self, window: Window, x: int, y: int, button, modifiers):
        self._click_function()

    def on_mouse_leave(self, window: Window, x: int, y: int):
        self.__handle_hover(window, False)

    def on_mouse_release(self, window: Window, x: int, y: int, button, modifiers):
        pass

    def __handle_hover(self, window: Window, hover: bool):
        cursor = None

        if hover:
            cursor = window.get_system_mouse_cursor(window.CURSOR_HAND)
            self._sprite = self._sprite_hover
        else:
            cursor = window.get_system_mouse_cursor(window.CURSOR_DEFAULT)
            self._sprite = self._sprite_normal

        window.set_mouse_cursor(cursor)

    def draw(self):
        self._sprite.draw()
        self._label.draw()
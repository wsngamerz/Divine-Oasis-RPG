#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: components/button.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import logging

from divineoasis.components.component import Component

from pyglet.image import AbstractImage
from pyglet.sprite import Sprite
from pyglet.text import Label
from pyglet.window import Window


class Button(Component):
    def __init__(self, uid: str, x: int, y: int, width: int, height: int, texture: AbstractImage, text: str = "", click_function = None):
        self.button_logger = logging.getLogger(__name__)

        Component.__init__(self, uid, x, y, width, height)

        self._text = text
        self._texture = texture
        self._sprite = None

        self._label = None
        self._label_x = self._x + (self._texture.width // 2)
        self._label_y = (self._y + (self._texture.height // 2)) + 3

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

    def load_sprite(self):
        self._sprite = Sprite(self._texture, self._x, self._y)

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
        else:
            cursor = window.get_system_mouse_cursor(window.CURSOR_DEFAULT)

        window.set_mouse_cursor(cursor)

    def draw(self):
        self._sprite.draw()
        self._label.draw()
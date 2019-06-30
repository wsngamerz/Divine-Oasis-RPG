#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: components/component.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------
from __future__ import annotations

import logging

from pyglet.window import Window


class Component:
    def __init__(self, uid, x: int, y: int, width: int, height: int):
        self.component_logger = logging.getLogger(__name__)

        self._uid = uid
        self._x = x
        self._y = y
        self._width = width
        self._height = height

        self._hidden = False
        self._enabled = True

    def __repr__(self):
        return f"{ self.__class__.__name__ }(id={ self._uid })"

    def add_component(self, component: Component):
        raise NotImplementedError

    def hide(self):
        self._hidden = True

    def show(self):
        self._hidden = False

    def is_hidden(self) -> bool:
        return self._hidden

    def enable(self):
        self._enabled = True

    def disable(self):
        self._enabled = False

    def is_enabled(self) -> bool:
        return self._enabled

    def is_inside(self, x: int, y: int) -> bool:
        return self._x <= x < self._x + self._width and self._y <= y < self._y + self._height

    def on_mouse_press(self, window: Window, x: int, y: int, button, modifiers):
        raise NotImplementedError

    def on_mouse_release(self, window: Window, x: int, y: int, button, modifiers):
        raise NotImplementedError

    def on_mouse_motion(self, window: Window, x: int, y: int, dx: int, dy: int):
        raise NotImplementedError

    def on_mouse_enter(self, window: Window, x: int, y: int):
        raise NotImplementedError

    def on_mouse_leave(self, window: Window, x: int, y: int):
        raise NotImplementedError

    def on_mouse_drag(self, window: Window, x: int, y: int, dx: int, dy: int, buttons, modifiers):
        raise NotImplementedError

    def on_mouse_drag_enter(self, window: Window, x: int, y: int):
        raise NotImplementedError

    def on_mouse_drag_leave(self, window: Window, x: int, y: int):
        raise NotImplementedError

    def on_mouse_scroll(self, window: Window, x: int, y: int, scroll_x: int, scroll_y: int):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError
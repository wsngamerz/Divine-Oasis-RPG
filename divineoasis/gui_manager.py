#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: gui_manager.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import logging

from divineoasis.components.component import Component

from pyglet.window import Window


class GuiManager(Component):
    def __init__(self, window: Window):
        Component.__init__(self, "gui_manager", 0, 0, window.width, window.height)

        self.gui_logger = logging.getLogger(__name__)

        self.window = window
        self.batch = None
        self.group = None

        self._children = []
        self._mouse_inside = {}

        self.window.push_handlers(self)

    def add_component(self, component: Component):
        if repr(component) not in [repr(child) for child in self._children]:
            self._children.append(component)
            self._mouse_inside[component._uid] = False
            self.gui_logger.debug("Added component")

    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons, modifiers):
        pass

    def on_mouse_enter(self, x: int, y: int):
        pass

    def on_mouse_leave(self, x: int, y: int):
        pass

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        for child_component in self._children:
            if child_component.is_inside(x, y):
                if not self._mouse_inside[child_component._uid]:
                    self._mouse_inside[child_component._uid] = True
                    child_component.on_mouse_enter(self.window, x, y)
                child_component.on_mouse_motion(self.window, x, y, dx, dy)
            else:
                if self._mouse_inside[child_component._uid]:
                    self._mouse_inside[child_component._uid] = False
                    child_component.on_mouse_leave(self.window, x, y)

    def on_mouse_press(self, x: int, y: int, button, modifiers):
        for child_component in self._children:
            if child_component.is_inside(x, y):
                child_component.on_mouse_press(self.window, x, y, button, modifiers)

    def on_mouse_release(self, x: int, y: int, button, modifiers):
        for child_component in self._children:
            if child_component.is_inside(x, y):
                child_component.on_mouse_release(self.window, x, y, button, modifiers)

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        pass

    def update(self, dt: float):
        for child_component in self._children:
            child_component.draw()

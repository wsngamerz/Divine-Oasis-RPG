#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: scenes/main_menu/options_scene.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import logging

from divineoasis.assets import Assets
from divineoasis.audio_manager import AudioManager
from divineoasis.components.button import Button
from divineoasis.scene import Scene

from pyglet.graphics import Batch, OrderedGroup
from pyglet.sprite import Sprite
from pyglet.window import Window


class OptionsScene(Scene):
    def __init__(self, assets: Assets, window: Window, audio_manager: AudioManager):
        Scene.__init__(self, assets, window, audio_manager)
        self.logger = logging.getLogger(__name__)

        self.batch = Batch()
        self.background = OrderedGroup(0)
        self.foreground = OrderedGroup(1)

    def start_scene(self):
        back_button = Button(uid="back_button", x=576, y=40, style="button_red_small", text="Back", click_function=lambda: self.switch_sub_scene("MenuScene"))
        self.gui.add_component(back_button)

    def update(self, dt: float):
        self.window.clear()
        self.batch.draw()
        self.gui.update(dt)

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

    def start_scene(self):
        back_button = Button("play_button", 512, 40, 256, 64, self.assets.get_pyglet_image("user_interface.button_blue_large"), "Back", lambda: self.switch_sub_scene("MenuScene"))
        self.gui.add_component(back_button)

    def update(self, dt: float):
        self.window.clear()
        self.batch.draw()
        self.gui.update(dt)

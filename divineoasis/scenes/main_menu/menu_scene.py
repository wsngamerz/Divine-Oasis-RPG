#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: scenes/main_scene/menu_scene.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import divineoasis
import logging
import sys

from divineoasis.assets import Assets
from divineoasis.audio_manager import AudioManager
from divineoasis.components.button import Button
from divineoasis.components.music_panel import MusicPanel
from divineoasis.scene import Scene

from pyglet.graphics import Batch, OrderedGroup
from pyglet.sprite import Sprite
from pyglet.text import Label
from pyglet.window import Window


class MenuScene(Scene):
    def __init__(self, assets: Assets, window: Window, audio_manager: AudioManager):
        Scene.__init__(self, assets, window, audio_manager)
        self.logger = logging.getLogger(__name__)

        self.batch = Batch()
        self.background = OrderedGroup(0)
        self.foreground = OrderedGroup(1)

        # Logo image and sprite
        self.logo_image = None
        self.logo_sprite = None

        # Version and info labels
        self.version_label = Label(f"Version: { divineoasis.__version__ }", x=10, y=30, group=self.foreground, batch=self.batch, font_size=16, font_name="Hydrophilia Iced")
        self.author_label = Label(f"by { divineoasis.__author__ }", x=10, y=10, group=self.foreground, batch=self.batch, font_size=16, font_name="Hydrophilia Iced")

    def start_scene(self):
        self.load_logo()

        elements = [
            Button(uid="play_button", x=247, y=200, style="button_blue_large", text="Play"),
            Button(uid="options_button", x=512, y=200, style="button_blue_large", text="Options", click_function=lambda: self.switch_sub_scene("OptionsScene")),
            Button(uid="quit_button", x=777, y=200, style="button_blue_large", text="Quit", click_function=sys.exit),
            MusicPanel(uid="music_panel", x=1014, y=10, width=256, height=98, texture=self.assets.get_pyglet_image("user_interface.music_panel"), song_name="Song Name", song_artist="Song Artist")
        ]
        
        for element in elements:
            self.gui.add_component(element)

    def load_logo(self):
        self.logo_image = self.assets.get_pyglet_image("lang.user_interface.logo")
        self.logo_sprite = Sprite(self.logo_image,
                x=(self.window.width//2) - (self.logo_image.width//2),
                y=(self.window.height//2) - 50,
                batch=self.batch, group=self.foreground)

    def update(self, dt: float):
        self.window.clear()
        self.batch.draw()
        self.gui.update(dt)

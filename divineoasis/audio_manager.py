#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: assets.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import logging

from divineoasis.assets import Assets

from pyglet.media import Player


class AudioManager:
    def __init__(self, assets: Assets, channels: int):
        self.assets = assets
        self.channels = channels
        self.logger = logging.getLogger(__name__)
        self.music_player = Player()
        self.music_player.volume = 0.75
        self.sfx_players = [Player() for player in range(self.channels)]

    def play_song(self, path: str, loop: bool = False):
        media_file = self.assets.get_pyglet_media(path)
        self.music_player.loop = loop
        self.music_player.queue(media_file)

        if not self.music_player.playing:
            self.music_player.play()
        else:
            self.music_player.next_source()


    def play_sfx(self, path: str):
        pass

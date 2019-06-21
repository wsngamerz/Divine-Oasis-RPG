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

        # TODO: Add songs into class var so that they dont get loaded from the disk every time theyre requested

    def _play(self):
        if not self.music_player.playing:
            self.music_player.play()
        else:
            self.music_player.next_source()

    def play_song(self, path: str, loop: bool = False):
        media_file = self.assets.get_pyglet_media(path)
        self.music_player.loop = loop
        self.music_player.queue(media_file)

        self._play()

    def play_songs(self, paths: list, loop: bool = False):
        for path in paths:
            media_file = self.assets.get_pyglet_media(path)
            self.music_player.queue(media_file)
        
        if loop:
            self.loop_songs_list = paths
            self.music_player.on_player_eos = lambda: self.play_songs(paths, True)

        self._play()

    def play_sfx(self, path: str):
        pass

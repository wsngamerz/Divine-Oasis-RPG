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

from pyglet.media import Player, Source, get_audio_driver, have_ffmpeg


class AudioManager:
    def __init__(self, assets: Assets, channels: int):
        self.assets = assets
        self.channels = channels
        self.logger = logging.getLogger(__name__)

        self.music_player = Player()
        self.sfx_players = [Player() for player in range(self.channels)]

        self.music_player.volume = 0.5
        self.songs = {}

        self._debug_info()

    def _play_song(self):
        if not self.music_player.playing:
            self.music_player.play()
        else:
            self.music_player.next_source()

    def _load_song(self, path: str) -> Source:
        if path not in self.songs:
            self.songs[path] = self.assets.get_pyglet_media(path)

        return self.songs[path]

    def _debug_info(self):
        self.logger.debug("=*=*=*=*=*= Audio Debug Information =*=*=*=*=*=")
        self.logger.debug(f"Audio Driver Class: { get_audio_driver().__class__.__name__ }")
        self.logger.debug(f"  FFmpeg Installed: { have_ffmpeg() }")
        self.logger.debug("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")

    def play_song(self, path: str, loop: bool = False):
        media_file = self._load_song(path)
        self.music_player.loop = loop
        self.music_player.queue(media_file)

        self._play_song()

    def play_songs(self, paths: list, loop: bool = False):
        for path in paths:
            media_file = self._load_song(path)
            self.music_player.queue(media_file)
        
        if loop:
            self.loop_songs_list = paths
            self.music_player.on_player_eos = lambda: self.play_songs(paths, True)

        self._play_song()

    def get_music_volume(self) -> float:
        return self.music_player.volume

    def set_music_volume(self, volume: float):
        self.music_player.volume = volume

    def play_sfx(self, path: str):
        pass

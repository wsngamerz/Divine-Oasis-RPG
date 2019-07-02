#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: game.py
# -------------------
#    Divine Oasis
# Text Based RPG Game
#    By wsngamerz
# -------------------

import divineoasis
import logging
import logging.config
import os
import platform
import pyglet
import sys

from divineoasis.assets import Assets, Directories
from divineoasis.config import Config
from divineoasis.colours import Colours
from divineoasis.scene_manager import SceneManager

from pyglet.window import Window


class DivineOasis:
    def __init__(self, debug: bool = False):
        self.debug = debug

        if self.debug:
            if platform.system() == "Windows":
                # Set larger console
                os.system("mode con: cols=200 lines=9999")

        if platform.system() != "Linux":
            import pyglet_ffmpeg
            pyglet_ffmpeg.load_ffmpeg()

        # Enable Colours using black magic
        os.system("")

        # Setup Logging
        self.game_logger = self.setup_logging(debug)

        # Get basic system information
        self.system_data = {}
        self.system_info()

        # Basic classes
        self.game_config = Config()
        self.game_config.load()

        self.game_assets = Assets(self.game_config.get("language.lang"))

        # setup Pyglet
        pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')
        vsync_enabled = self.game_config.get("graphics.vsync")

        self.window = Window(1280, 720)
        self.window.set_vsync(vsync_enabled)
        # TODO: Fix fullscreen mode
        # self.window.set_fullscreen(self.game_config.get("fullscreen"))
        self.window.set_caption(self.game_assets.get("lang.title.main_title"))

        fps_limit = self.game_config.get("graphics.fps")

        self.scene_manager = SceneManager(self.game_assets, self.window)
        if vsync_enabled:
            pyglet.clock.schedule(self.scene_manager.update)
        else:
            pyglet.clock.schedule_interval(self.scene_manager.update, 1.0 / fps_limit)

    def start(self):
        self.game_logger.info(f"Starting Divine Oasis { divineoasis.__version__ }")

        # Start Pyglet loop
        pyglet.app.run()

    @staticmethod
    def setup_logging(debug: bool):
        if debug:
            level = "DEBUG"
        else:
            level = "INFO"

        logging.config.dictConfig({
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {
                    "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
                }
            },
            "handlers": {
                "default": {
                    "class": "logging.StreamHandler",
                    "formatter": "standard"
                }
            },
            "loggers": {
                "": {
                    "handlers": ["default"],
                    "propagate": True,
                    "level": level
                }
            }
        })

        logging.addLevelName(logging.DEBUG,    Colours.BOLD + Colours.BRIGHT_CYAN   + "DEBUG"   + Colours.RESET)
        logging.addLevelName(logging.INFO,     Colours.BOLD + Colours.BRIGHT_BLUE   + "INFO"    + Colours.RESET)
        logging.addLevelName(logging.WARNING,  Colours.BOLD + Colours.BRIGHT_YELLOW + "WARNING" + Colours.RESET)
        logging.addLevelName(logging.ERROR,    Colours.BOLD + Colours.BRIGHT_RED    + "ERROR"   + Colours.RESET)
        logging.addLevelName(logging.CRITICAL, Colours.BOLD + Colours.BRIGHT_RED    + Colours.BLINK + "CRITICAL" + Colours.RESET)

        return logging.getLogger(__name__)

    def system_info(self):
        self.system_data = {
            "arguments": sys.argv,
            "python_version": sys.version,
            "os": platform.system(),
            "os_release": platform.release(),
            "os_version": platform.version(),
            "os_arch": platform.machine(),
            "os_platform": platform.platform()
        }

        self.game_logger.debug("=*=*=*=*=*=*=*=*=*=*=*= Debug Information =*=*=*=*=*=*=*=*=*=*=*=")
        self.game_logger.debug(f"        Arguments: { self.system_data['arguments'] }")
        self.game_logger.debug(f"   Python Version: { self.system_data['python_version'] }")
        self.game_logger.debug(f"               OS: { self.system_data['os'] }")
        self.game_logger.debug(f"       OS Version: { self.system_data['os_version'] }")
        self.game_logger.debug(f"       OS Release: { self.system_data['os_release'] }")
        self.game_logger.debug(f"  OS Architecture: { self.system_data['os_arch'] }")
        self.game_logger.debug(f"      OS Platform: { self.system_data['os_platform'] }")
        self.game_logger.debug("=*=*=*=*=*=*=*=*=*=*=*=*=* Directories *=*=*=*=*=*=*=*=*=*=*=*=*=")
        self.game_logger.debug(f" Application Root: { Directories().application_root }")
        self.game_logger.debug(f" Assets Directory: { Directories().assets_directory }")
        self.game_logger.debug(f"   Data Directory: { Directories().data_directory }")
        self.game_logger.debug(f"  Config Location: { Directories().config_location }")
        self.game_logger.debug("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")

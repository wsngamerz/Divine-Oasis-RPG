#
# Divine Oasis
# by wsngamerz
# divineoasis/divineoasis.py
#

import divineoasis
import pyglet

from divineoasis.config import Config
from divineoasis.logger import Logging
from divineoasis.scene_manager import SceneManager

from pyglet.app import EventLoop
from pyglet.window import Window, FPSDisplay



class DivineOasis:
    """
    The main game class which handles startup and shutdown of the game
    """
    def __init__(self, config: Config, logger_manager: Logging):
        self.config = config
        self.logger_manager = logger_manager
        self.logger = self.logger_manager.get_logger(__name__)

        self.logger.info(f"Divine Oasis { divineoasis.__version__ } starting")

        # create the window
        width = self.config.get_option_int("options.graphics.window_width")
        height = self.config.get_option_int("options.graphics.window_height")
        self.window = Window(width=width, height=height)
        self.window.set_vsync(self.config.get_option_bool("options.graphics.vsync_enabled"))
        self.window.set_caption(f"Divine Oasis { divineoasis.__version__ }")
        self.logger.debug("Created Window")

        # framerate counter
        self.fps_counter = FPSDisplay(self.window)
        self.logger.debug("Added FPS Counter")

        # ensure 'framerate' is set properly and set the game_loop to be called every 'frame'
        if self.config.get_option_bool("options.graphics.vsync_enabled"):
            pyglet.clock.schedule(self.game_loop)
            self.logger.debug("vsync is enabled")
        else:
            pyglet.clock.schedule_interval(self.game_loop, 1.0 / self.config.get_option_int("options.graphics.framerate_limit"))
            self.logger.debug("vsync is disabled")

        # setup the scene manager
        self.scene_manager = SceneManager(self.window, self.logger_manager)
        self.logger.debug("Scene Manager set up")

        # setup more resource paths
        pyglet.resource.path = []
        pyglet.resource.reindex()

        # run the loop
        self.logger.debug("Starting main loop")
        pyglet.app.run()

        # only ran once loop stopped
        self.game_stop()


    def game_loop(self, dt):
        """
        function is called every frame by the pyglet clock
        """
        self.window.clear()
        self.scene_manager.update()
        self.fps_counter.draw()


    def game_stop(self):
        """
        Handles a graceful shutdown of all services
        """
        self.logger.info("Divine Oasis shutting down")
        pyglet.app.exit()
        self.config.close_config()

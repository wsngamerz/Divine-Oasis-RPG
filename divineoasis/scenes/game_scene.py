#
# Divine Oasis
# by wsngamerz
# divineoasis/scenes/game_scene.py
#

from divineoasis.components.nine_slice import NineSliceImage
from divineoasis.scene import Scene

from pyglet.graphics import Batch
from pyglet.text import Label
from pyglet.window import Window



class GameScene(Scene):
    def __init__(self, window: Window):
        self.window = window
        self.batch = Batch()
        self.logger = self.scene_manager.logger_manager.get_logger(__name__)

        self.logger.debug("GameScene initialised")

        self.tmp = NineSliceImage("divineoasis/assets/img/default_button.png", 200, 200, 512, 128, 64, self.batch)


    def update(self):
        self.batch.draw()

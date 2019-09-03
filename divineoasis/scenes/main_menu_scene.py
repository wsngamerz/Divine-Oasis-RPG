#
# Divine Oasis
# by wsngamerz
# divineoasis/scenes/main_menu_scene.py
#

import sys

from divineoasis.components.button import Button
from divineoasis.scene import Scene

from pyglet.graphics import Batch
from pyglet.image import load as load_image
from pyglet.sprite import Sprite
from pyglet.window import Window, mouse



class MainMenuScene(Scene):
    def __init__(self, window: Window):
        self.window = window
        self.batch = Batch()
        self.logger = self.scene_manager.logger_manager.get_logger(__name__)

        self.logger.debug("MainMenuScene initialised")

        # load logo image and generate its position
        self.logo_image = load_image("divineoasis/assets/img/logo.png")
        self.logo_pos = [(self.window.width//2) - (self.logo_image.width//2), ((self.window.height//2) - (self.logo_image.height//2)) // 0.6]
        self.logo = Sprite(img=self.logo_image, x=self.logo_pos[0], y=self.logo_pos[1], batch=self.batch)

        # stores all the UI elements together
        self.elements = [
            Button(text="Play",    x=((self.window.width)//2) - 450, y=150, width=256, height=64, batch=self.batch, function=lambda: self.scene_manager.switch_scene("game")),
            Button(text="Options", x=((self.window.width)//2) - 128, y=150, width=256, height=64, batch=self.batch, function=lambda: self.scene_manager.switch_scene("options")),
            Button(text="Exit",    x=((self.window.width)//2) + 194, y=150, width=256, height=64, batch=self.batch, function=sys.exit)
        ]


    def update(self):
        self.batch.draw()


    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        # check all elements to see whether the mouse is inside the bounding box
        for element in self.elements:
            if element.contains_coords(x, y):
                element.set_hovering(True)
            else:
                element.set_hovering(False)
            element.update(self.window)


    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        # we are only interested in left clicks
        if button == mouse.LEFT:
            for element in self.elements:
                if element.contains_coords(x, y):
                    element.click(self.window)

#
# Divine Oasis
# by wsngamerz
# divineoasis/scene_manager.py
#

from divineoasis.logger import Logging
from divineoasis.scene import Scene
from divineoasis.scenes.game_scene import GameScene
from divineoasis.scenes.main_menu_scene import MainMenuScene

from pyglet.window import Window

# DEV:
from pyglet.text import Label



class SceneManager:
    """
    SceneManager is used to manage the transition between multiple scenes
    """
    def __init__(self, window: Window, logger_manager: Logging):
        self.window = window
        self.logger_manager = logger_manager
        self.logger = self.logger_manager.get_logger(__name__)

        self.logger.debug("Setting up Scene Manager")

        # used to manage all availible scenes
        self.scenes = {}
        self.current_scene: Scene = None

        # All scenes will be able to access scene manager
        Scene.scene_manager = self

        # Add all scenes
        self.add_scene("main_menu", MainMenuScene(self.window))
        self.add_scene("game", GameScene(self.window))
        self.logger.debug("Added Scenes")

        # switch to main menu scene
        self.switch_scene("main_menu")


    def add_scene(self, scene_name: str, scene_instance: Scene):
        """
        Add a scene to the scene list which is managed by the class
        """
        self.scenes[scene_name] = scene_instance
        self.logger.debug(f"Added scene: { scene_name }")


    def switch_scene(self, scene_name: str):
        """
        Change the currently rendered screen by removing handlers and reapplying them to the new scene
        """
        self.window.remove_handlers(self.current_scene)
        self.current_scene = self.scenes[scene_name]
        self.window.push_handlers(self.current_scene)
        self.logger.debug(f"Switched to scene: { scene_name }")


    def update(self):
        """
        Will update the current scene
        """
        self.current_scene.update()

        # DEV (Displays scene class name at top left corner):
        self.tmp = Label(self.current_scene.__class__.__name__, font_size=16, y=self.window.height - 16, batch=self.current_scene.batch)

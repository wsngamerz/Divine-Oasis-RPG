#
# Divine Oasis
# by wsngamerz
# divineoasis/scene.py
#

from pyglet.window import Window



class Scene:
    """
    A Base class which all other scenes extend from

    event handlers from the window class can also be defined
    """
    scene_manager = None # filled via the scene_manager


    def update(self):
        # This should never be called as the update function should be 
        # overwritten by any scene that extends from this base class
        raise NotImplementedError

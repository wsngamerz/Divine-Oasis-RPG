#
# Divine Oasis
# by wsngamerz
# divineoasis/components/button.py
#

from typing import Callable

from pyglet.gl import GL_QUADS
from pyglet.graphics import Batch, OrderedGroup
from pyglet.text import Label
from pyglet.window import Window



class Button:
    """
    Button: A (usually) rectangular object which can be clicked to perform
            a preset action
    """
    def __init__(self, text: str, x: int, y: int, width: int, height: int, batch: Batch, function: Callable):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.batch = batch

        self.text = text
        self.function = function

        # NOTE: always ensure that the button text level is higher than
        # the background otherwise the label will be drawn over!
        self.group_button_bg = OrderedGroup(10)
        self.group_button_text = OrderedGroup(11)

        # prev hover value should hold the previous value of the hovering variable
        self._prev_hover_val = False
        self.hovering = False

        # styling constants
        self.colour = (0, 0, 0)
        self.colour_normal = (133, 94, 66)
        self.colour_hover = (68, 48, 34)
        self.font = "Hydrophilia Iced"
        self.font_size = 22
        self.default_cursor = Window.get_system_mouse_cursor(Window, Window.CURSOR_DEFAULT)
        self.hover_cursor = Window.get_system_mouse_cursor(Window, Window.CURSOR_HAND)

        # stores the VertexList of the buttons background so that on_hover, the default
        # background can be deleted and the hover background can be drawn
        self.button_bg = None

        # the text of the button which is centered on the button
        self.label = Label(text=self.text, font_name=self.font, font_size=self.font_size,
                           x=self.x + (self.width//2), y=self.y + (self.height//2),
                           anchor_x="center", anchor_y="center", batch=self.batch,
                           group=self.group_button_text)

        # draw the buttons background
        self._draw_bg()


    def _draw_bg(self) -> None:
        """
        Draws the background of the button using gl calls
        """
        # delete old background
        if self.button_bg is not None:
            self.button_bg.delete()

        # set the colours of the background on_hover
        if self.hovering:
            self.colour = self.colour_hover
        else:
            self.colour = self.colour_normal

        self.button_bg = self.batch.add(4, GL_QUADS, self.group_button_bg,
            # coords for points
            ("v2f", (self.x,              self.y,
                    self.x + self.width, self.y,
                    self.x + self.width, self.y + self.height,
                    self.x,              self.y + self.height)),
            # colours for points
            ("c3B", (self.colour[0], self.colour[1], self.colour[2],
                     self.colour[0], self.colour[1], self.colour[2],
                     self.colour[0], self.colour[1], self.colour[2],
                     self.colour[0], self.colour[1], self.colour[2]))
        )

        # used to check for a change in the hover status
        self._prev_hover_val = self.hovering


    def contains_coords(self, x: int, y: int) -> bool:
        """
        A function to check whether the specified coordinates are within the buttons
        bounding box

        If the coordinates are inside the bounding box, True is returned otherwise
        False is returned. (Which is how booleans work!)
        """
        if (x > self.x) and (x < (self.x + self.width)) and (y > self.y) and (y < (self.y + self.height)):
            return True
        else:
            return False


    def click(self, window: Window) -> None:
        """
        This function is called when a button is clicked and is used to call the
        callback function which will have been set on the buttons creation
        """
        if self.function is not None:
            # remeber to reset cursor to default otherwise the cursor would stick
            # if for example, the button was used to switch scenes
            window.set_mouse_cursor(self.default_cursor)

            # call the set function
            self.function()


    def set_hovering(self, value: bool) -> None:
        """
        Used to set the hover state
        """
        # only accept booleans and only set if the value is different
        if (type(value) == bool) and (value != self.hovering):
            self.hovering = value


    def update(self, window: Window) -> None:
        """
        Called when the button needs to be updated. It also checks whether anything
        that would actually require a re-render has changed. if nothing has changed,
        it will just pass over which helps improve performance slightly.
        """
        # ensure that this is only called on_change
        if self._prev_hover_val != self.hovering:
            if self.hovering:
                # set hover cursor
                window.set_mouse_cursor(self.hover_cursor)
            else:
                # set default cursor
                window.set_mouse_cursor(self.default_cursor)

            # the background only needs to be redrawn when the button is hovered over
            self._draw_bg()

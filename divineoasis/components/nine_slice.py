#
# Divine Oasis
# by wsngamerz
# divineoasis/components/nine_slice.py
#

from pyglet.image import load as load_image
from pyglet.graphics import Batch
from pyglet.sprite import Sprite


class NineSliceImage:
    def __init__(self, image_location: str, x: int, y: int, w: int, h: int, corner_size: int, batch: Batch):
        self.image_location = image_location
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.corner_size = corner_size
        self.batch = batch

        self._image = load_image(self.image_location)
        self._centre_size = self._image.width - (self.corner_size * 2)

        # the image which has been split up into its 9 slices
        self._sub_image = [
            self._image.get_region(0                                   , self.corner_size + self._centre_size, self.corner_size , self.corner_size),
            self._image.get_region(self.corner_size                    , self.corner_size + self._centre_size, self._centre_size, self.corner_size),
            self._image.get_region(self.corner_size + self._centre_size, self.corner_size + self._centre_size, self.corner_size , self.corner_size),
            self._image.get_region(0                                   , self.corner_size                    , self.corner_size , self._centre_size),
            self._image.get_region(self.corner_size                    , self.corner_size                    , self._centre_size, self._centre_size),
            self._image.get_region(self.corner_size + self._centre_size, self.corner_size                    , self.corner_size , self._centre_size),
            self._image.get_region(0                                   , 0                                   , self.corner_size , self.corner_size),
            self._image.get_region(self.corner_size                    , 0                                   , self._centre_size, self.corner_size), 
            self._image.get_region(self.corner_size + self._centre_size, 0                                   , self.corner_size , self.corner_size)
        ]

        # Image:
        #    0 1 2
        #    3 4 5
        #    6 7 8

        self._sub_image_height = self.height - (self.corner_size * 2)
        self._sub_image_width = self.width - (self.corner_size * 2)

        self.img0 = Sprite(self._sub_image[0], self.x                                           , self.y + self.corner_size + self._sub_image_height, batch=self.batch)
        self.img1 = Sprite(self._sub_image[1], self.x + self.corner_size                        , self.y + self.corner_size + self._sub_image_height, batch=self.batch)
        self.img2 = Sprite(self._sub_image[2], self.x + self.corner_size + self._sub_image_width, self.y + self.corner_size + self._sub_image_height, batch=self.batch)
        self.img3 = Sprite(self._sub_image[3], self.x                                           , self.y + self.corner_size, batch=self.batch)
        self.img4 = Sprite(self._sub_image[4], self.x + self.corner_size                        , self.y + self.corner_size, batch=self.batch)
        self.img5 = Sprite(self._sub_image[5], self.x + self.corner_size + self._sub_image_width, self.y + self.corner_size, batch=self.batch)
        self.img6 = Sprite(self._sub_image[6], self.x                                           , self.y, batch=self.batch)
        self.img7 = Sprite(self._sub_image[7], self.x + self.corner_size                        , self.y, batch=self.batch)
        self.img8 = Sprite(self._sub_image[8], self.x + self.corner_size + self._sub_image_width, self.y, batch=self.batch)

        self.img1.scale_x = self._sub_image_width
        self.img4.scale_x = self._sub_image_width
        self.img7.scale_x = self._sub_image_width

        self.img3.scale_y = self._sub_image_height
        self.img4.scale_y = self._sub_image_height
        self.img5.scale_y = self._sub_image_height

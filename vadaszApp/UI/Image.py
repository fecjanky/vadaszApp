import math

import cv2
from PIL import ImageTk

from vadaszApp.UI.Canvas import Drawable, Canvas
from vadaszApp.core.Util import get_from_dict


class Image(Drawable):
    def __init__(self, path, canvas: Canvas, **kwargs):
        self.path = path
        canvas.attach(self)
        self.keep_aspect_ratio = get_from_dict(kwargs, "keep_aspect_ratio", True)
        self.original_image = cv2.boxFilter(cv2.imread(path), -1, (5, 5))
        self.original_height, self.original_width, z = self.original_image.shape
        self.portrait = self.original_width < self.original_height
        self.aspect_ratio = float(self.original_width) / float(self.original_height)
        self.image = None

    def calc_scale_factor(self, new_width, new_height):
        scaled_width = int(new_height * self.aspect_ratio)
        scaled_height = int(new_width / self.aspect_ratio)
        if scaled_height > new_height:
            scaled_height = int(scaled_width / self.aspect_ratio)
        elif scaled_width > new_width:
            scaled_width = int(scaled_height * self.aspect_ratio)
        return min(float(scaled_width) / self.original_width, float(scaled_height) / self.original_height)

    @classmethod
    def to_tk_image(cls, cvimage):
        b, g, r = cv2.split(cvimage)
        cvimage = cv2.merge((r, g, b))
        cvimage = ImageTk.Image.fromarray(cvimage)
        return ImageTk.PhotoImage(image=cvimage)

    def draw(self, canvas: Canvas, width, height):
        scale_factor = self.calc_scale_factor(width, height)
        if math.isclose(scale_factor, .0): return
        img = cv2.resize(self.original_image, (0, 0), fx=scale_factor, fy=scale_factor)
        self.image = self.to_tk_image(img)
        canvas.draw_image(self.image)
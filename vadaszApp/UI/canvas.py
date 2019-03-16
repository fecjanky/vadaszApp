import tkinter
from vadaszApp.core.util import get_from_dict


class Drawable:
    def draw(self, canvas, width, height):
        raise NotImplementedError()


class Canvas:
    def __init__(self, master, **kwargs):
        self.width = 640
        self.height = 480
        self.master = master
        self.border = get_from_dict(kwargs, "border", 40)

        if self.border < 0:
            raise ValueError("border must be greater or equal to 0")

        self.canvas = tkinter.Canvas(self.master,
                                     width=self.width,
                                     height=self.height)
        self.canvas.bind("<Configure>", lambda event: self.__configure(event))
        self.drawables = None

    def widget(self):
        return self.canvas

    def attach(self, object: Drawable = None):
        self.drawables = object

    def draw(self, width=None, height=None):
        self.canvas.delete("all")
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if self.drawables is not None:
            self.drawables.draw(self, self.width - self.border, self.height - self.border)

    def draw_image(self, image, *args, **kwargs):
        kwargs.update({"image": image})
        self.canvas.create_image(self.border, self.border, anchor=tkinter.NW, *args, **kwargs)

    def __configure(self, event):
        self.draw(event.width, event.height)

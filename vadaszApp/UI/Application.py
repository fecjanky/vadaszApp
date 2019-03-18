import tkinter as tk
from tkinter import Tk, mainloop, Button, filedialog

from vadaszApp.UI.Canvas import Canvas
from vadaszApp.UI.Image import Image
from vadaszApp.core.Application import Application as CoreApplication, Observer


class Application(Observer):

    def notify_changed(self, application):
        Image(self.application.get_image_path(), self.canvas)
        self.canvas.draw()
        self.status_text.set('/'.join(map(str, self.application.get_status())))

    def show_solution(self):
        self.solution_text.set(self.application.get_solution())

    def next(self):
        self.clear_solution_text()
        self.application.next()

    def prev(self):
        self.clear_solution_text()
        self.application.prev()

    def load(self):
        path = filedialog.askdirectory()
        if path is not None:
            self.application.load(path)

    def shuffle(self):
        self.clear_solution_text()
        self.application.shuffle()

    def clear_solution_text(self):
        self.solution_text.set("")

    def __create_layout(self):
        self.canvas.widget().grid(row=0, column=0, sticky=(tk.N + tk.S + tk.E + tk.W),
                                  rowspan=len(self.controls) - 1 if len(self.controls) > 1 else 1)

        self.solution_label.grid(row=len(self.controls) - 1, column=0, sticky=(tk.N + tk.S + tk.E + tk.W))
        row = 0
        for control in self.controls:
            control.grid(row=row, column=1, padx=20, pady=20)
            row = row + 1

    def __key_pressed(self, event):
        if event.keysym and event.keysym in self.key_mapping:
            self.key_mapping[event.keysym]()

    def __init__(self):
        self.master = Tk()
        self.master.title("vadászApp")
        self.master.bind("<Key>", self.__key_pressed)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.canvas = Canvas(self.master, border=50)
        self.application = CoreApplication(self)
        self.status_text = tk.StringVar()
        self.solution_text = tk.StringVar()
        self.status_label = tk.Label(self.master, textvariable=self.status_text)
        self.solution_label = tk.Label(self.master, textvariable=self.solution_text, justify=tk.LEFT)
        self.labels = [self.solution_label, self.status_label]

        self.controls = [self.status_label,
                         Button(self.master, text="Betöltés", command=self.load),
                         Button(self.master, text="Keverés", command=self.shuffle),
                         Button(self.master, text="Megoldás", command=self.show_solution),
                         Button(self.master, text="Következő", command=self.next),
                         Button(self.master, text="Előző", command=self.prev)]

        for l in self.labels:
            l.config(font="Courier 18 bold")

        self.__create_layout()

        self.key_mapping = {"Return": self.show_solution, "Left": self.prev, "Right": self.next}

    def run(self):
        mainloop()

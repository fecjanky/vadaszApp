import tkinter as tk
from tkinter import Tk, mainloop, Button, BOTH, filedialog
from tkinter.messagebox import showinfo

from vadaszApp.UI.application import Application, Observer
from vadaszApp.UI.canvas import Canvas
from vadaszApp.UI.image import Image


class App(Observer):

    def notify_changed(self, application):
        Image(self.application.get_image_path(), self.canvas)
        self.canvas.draw()

    def show_solution(self):
        self.solution_text.set(self.application.get_solution())

    def next(self):
        self.solution_text.set("")
        self.application.next()

    def load(self):
        path = filedialog.askdirectory()
        if path is not None:
            self.application.load(path)

    def __create_layout(self):
        self.canvas.widget().grid(row=0, column=0, sticky=(tk.N + tk.S + tk.E + tk.W),
                                  rowspan=len(self.buttons) - 1 if len(self.buttons) > 1 else 1)

        self.label.grid(row=1, column=0, sticky=(tk.N + tk.S + tk.E + tk.W))
        row = 0
        for button in self.buttons:
            button.grid(row=row, column=1, padx=20, pady=20)
            row = row + 1

    def __init__(self):
        self.master = Tk()
        self.master.title("vadászApp")
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.canvas = Canvas(self.master, border=50)
        self.application = Application(self)
        self.buttons = [Button(self.master, text="Betöltés", command=self.load),
                        Button(self.master, text="Megoldás", command=self.show_solution),
                        Button(self.master, text="Következő", command=self.next)]
        self.solution_text = tk.StringVar()
        self.label = tk.Label(self.master, textvariable=self.solution_text, justify=tk.LEFT)
        self.label.config(font="Courier 18 bold")
        self.__create_layout()

    def run(self):
        mainloop()

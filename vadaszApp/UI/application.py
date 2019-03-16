import json
import os
from random import shuffle

from vadaszApp.core.Species import Species
from vadaszApp.core.data import TestData


class Observer:
    def notify_changed(self, application):
        raise NotImplementedError


class Application:
    current_test: TestData

    def __init__(self, obsever: Observer, image_extension=".png"):
        self.observer = obsever
        self.current_test = None
        self.path = "."
        self.image_extension = image_extension
        self.current_index = 0
        self.count = 0
        pass

    def load(self, path: str):
        self.path = path.replace("/", os.path.sep)
        with open(os.path.join(path, 'metadata.json'), encoding="utf8") as f:
            testdata = json.load(f)
        with open(os.path.join(path, 'species.json'), encoding="utf8") as f:
            species = json.load(f)
        Species.init_from_JSON(species)
        TestData.init_from_json(testdata)
        self.current_test = None
        self.keys = [k for k, v in TestData.repository().items()]
        self.__shuffle()

    def __shuffle(self):
        shuffle(self.keys)
        if len(self.keys) > 0:
            self.current_index = 1
            self.count = len(self.keys)
        else:
            self.current_index = 0
            self.count = 0
        self.current_test = TestData.repository()[self.keys[self.current_index - 1]]
        self.observer.notify_changed(self)

    def next(self):
        if self.current_index >= self.count:
            self.shuffle()
        else:
            self.current_index = self.current_index + 1
            self.current_test = TestData.repository()[self.keys[self.current_index - 1]]
            self.observer.notify_changed(self)

    def get_solution(self):
        return self.current_test.solution()

    def get_status(self):
        return (self.current_index, self.count)

    def get_image_path(self):
        return os.path.join(self.path, self.current_test.key().strip() + self.image_extension)

    def shuffle(self):
        self.__shuffle()

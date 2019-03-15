import json
import os
from random import randrange

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
        pass

    def load(self, path : str):
        self.path = path.replace("/",os.path.sep)
        with open(os.path.join(path, 'metadata.json'), encoding="utf8") as f:
            testdata = json.load(f)
        with open(os.path.join(path, 'species.json'), encoding="utf8") as f:
            species = json.load(f)
        Species.init_from_JSON(species)
        TestData.init_from_json(testdata)
        self.current_test = None
        self.next()

    def next(self):
        next_test = None
        while next_test is None:
            key = [k for k in TestData.repository().keys()][randrange(len(TestData.repository()))]
            candidate = TestData.repository()[key]
            if self.current_test is None or self.current_test.key() != candidate.key():
                self.current_test = candidate
                break
        self.observer.notify_changed(self)

    def get_solution(self):
        return self.current_test.solution()

    def get_image_path(self):
        return os.path.join(self.path, self.current_test.key().strip() + self.image_extension)

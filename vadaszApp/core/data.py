from vadaszApp.core.Species import Species
from vadaszApp.core.util import add_to_class_repository


class TestData:
    __repo = {}

    @classmethod
    def repository(cls):
        return cls.__repo

    @classmethod
    def init_from_json(cls, db):
        [TestData(key, db[key]) for key in db]

    def __init__(self, name, metadata: dict):
        self.__name = name
        self.__key = self.__name
        self.__species_obj = None
        for key in metadata:
            setattr(self, "__" + key, metadata[key])
        self.repository()[self.key()] = self

    def key(self):
        return self.__key

    def species(self) -> Species:
        if self.__species_obj is None:
            self.__species_obj = Species.lookup(getattr(self, "__species"))
        return self.__species_obj

    def sex(self):
        return getattr(self, "__sex") if hasattr(self, "__sex") else None

    def caption(self):
        return getattr(self, "__caption") if hasattr(self, "__caption") else ""

    def solution(self):
        species: Species = self.species()
        sex = species.instanceName(self.sex())
        return "{} {} {}".format(species.name(), sex, self.caption())

from vadaszApp.core.Species import Species
from vadaszApp.core.util import add_to_class_repository


class TestData:
    __repo = {}

    @classmethod
    def repository(cls):
        return cls.__repo

    @classmethod
    def init_from_json(cls, db):
        cls.repository().clear()
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
        return getattr(self, "__caption") if hasattr(self, "__caption") else None

    def solution(self):
        species: Species = self.species()
        solution_text = []
        if species is not None:
            solution_text.append("faj:{}".format(species.name()))
        if self.sex() is not None:
            solution_text.append("ivar:{}".format(species.instanceName(self.sex())))
        if self.caption() is not None:
            solution_text.append("megoldás:{}".format(self.caption()))
        if species.status() is not None:
            solution_text.append("státusz:{}".format(species.status()))
        solution_text.append("kép sorszám:{}".format(self.key()))
        return "\n".join([s for s in solution_text if s is not None])

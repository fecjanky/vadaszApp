from vadaszApp.core.util import add_to_class_repository
from . import util


class Species:
    __repo = {}

    @classmethod
    def repository(cls):
        return cls.__repo

    @classmethod
    def lookup(cls, name):
        return cls.repository()[name]

    @classmethod
    def init_from_JSON(cls,db):
        [Species(key,db[key]) for key in db]

    def __init__(self, name, data):
        self.__name = name
        self.__male_name = util.get_from_dict(data, "male_name", "hím")
        self.__female_name = util.get_from_dict(data, "female_name", "nőstény")
        self.__young_name = util.get_from_dict(data, "young_name", "fiatal")
        self.repository()[self.name()] = self

    def instanceName(self, sex=None):
        if sex is None:
            return ""
        attrname = "__" + sex + "_name"
        return getattr(self, attrname) if hasattr(self, attrname) else ""

    def name(self):
        return self.__name

    def maleName(self):
        return self.__male_name

    def femaleName(self):
        return self.__female_name

    def youngName(self):
        return self.__young_name

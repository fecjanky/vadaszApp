from . import Util


class Species:
    __repo = {}

    @classmethod
    def repository(cls):
        return cls.__repo

    @classmethod
    def lookup(cls, name):
        return cls.repository()[name]

    @classmethod
    def init_from_json(cls, db):
        cls.repository().clear()
        [Species(key.strip(), db[key]) for key in db]

    def __init__(self, name, data):
        self.__name = name
        self.__male_name = Util.get_from_dict(data, "male_name", "hím")
        self.__female_name = Util.get_from_dict(data, "female_name", "nőstény")
        self.__young_name = Util.get_from_dict(data, "young_name", "fiatal")
        self.__status = Util.get_from_dict(data, "status", None)
        self.repository()[self.name()] = self

    def instanceName(self, sex=None):
        if sex is None:
            return None
        attrname = '_%s__%s_name' % (self.__class__.__name__, sex)
        return getattr(self, attrname) if hasattr(self, attrname) else None

    def name(self):
        return self.__name

    def maleName(self):
        return self.__male_name

    def femaleName(self):
        return self.__female_name

    def youngName(self):
        return self.__young_name

    def status(self):
        return self.__status

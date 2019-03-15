import json
import os

from vadaszApp.core.Species import Species
from vadaszApp.core.data import TestData


def get_db():
    if 'testdb' not in g:
        to_init = {
            Species: "species.json",
            TestData: "metadata.json"
        }
        for cls, file in to_init.items():
            with current_app.open_resource(file) as f:
                cls.init_from_JSON(json.load(f))

        g.testdb = TestData.repository()
    return g.testdb


def close_db(e=None):
    db = g.pop('testdb', None)

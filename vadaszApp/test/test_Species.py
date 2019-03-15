from vadaszApp.core.Species import *
from vadaszApp.core.Species import Species


def test_Species_creation():
    data = {
        "male_name": "gácsér",
        "female_name": "tojó"
    }
    duck = Species("Tőkés réce", data)
    duck_from_repo: Species = Species.repository()["Tőkés réce"]
    assert duck.name() == "Tőkés réce"
    assert duck.maleName() == "gácsér"
    assert duck.femaleName() == "tojó"
    assert duck.youngName() == "fiatal"
    assert duck_from_repo.maleName() == "gácsér"



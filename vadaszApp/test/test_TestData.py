from vadaszApp.core.Species import Species
from vadaszApp.core.TestData import TestData


def test_TestData():
    duck = Species("Tőkés réce", {
        "male_name": "gácsér",
        "female_name": "tojó"
    })
    metadata = {"species": "Tőkés réce", "sex": "female"}
    testdata = TestData("1", metadata)
    assert testdata.species().name() == "Tőkés réce"


def test_TestData_from_JSON():
    Species.init_from_json({"Nagy lilik": {}, "Vetési lúd": {}})
    data = {
        "1  ": {"species": "Nagy lilik"},
        "2  ": {"species": "Nagy lilik"},
        "3  ": {"species": "Nagy lilik"},
        "4  ": {"species": "Vetési lúd"},
        "5  ": {"species": "Vetési lúd"},
        "6  ": {"species": "Vetési lúd"}
    }
    TestData.init_from_json(data)
    assert len(TestData.repository()) == 6
    species = {value.species() for key,value in TestData.repository().items()}
    species_names = {s.name() for s in species}
    assert len(species_names) == 2
    assert "Nagy lilik" in species_names
    assert "Vetési lúd" in species_names

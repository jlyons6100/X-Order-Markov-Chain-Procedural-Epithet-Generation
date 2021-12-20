from context import EpithetGenerator


def test_empty_generation():
    assert EpithetGenerator().generate() == ""

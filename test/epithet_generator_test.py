from epithet_generator.epithet_generator import EpithetGenerator


def test_empty_generation():
    assert EpithetGenerator().generate() == ""

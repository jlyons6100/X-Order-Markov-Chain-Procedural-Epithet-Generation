from epithet_generator.epithet_generator import epithetGenerator


def test_empty_generation():
    assert epithetGenerator().generate() == ""

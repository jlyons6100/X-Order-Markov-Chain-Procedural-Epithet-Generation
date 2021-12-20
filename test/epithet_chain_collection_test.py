from context import EpithetChainCollection


def test_empty_generation():
    assert EpithetChainCollection().generate() == ""

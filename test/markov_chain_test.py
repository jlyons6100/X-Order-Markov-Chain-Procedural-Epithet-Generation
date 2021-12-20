from context import MarkovChain


def test_empty_generation():
    assert MarkovChain().generate() == ""


def test_get_probability():
    chain = MarkovChain()
    chain.add("Sea")
    chain.add("see")
    assert chain.get_probability("se") == 1
    assert chain.get_probability("sea") == 0.5


def test_generation_not_empty():
    chain = MarkovChain()
    chain.add("sea")
    chain.add("sea")
    assert chain.generate() == "sea"


def test_restart_generation():
    chain = MarkovChain()
    chain.add("sea")
    chain.add("sea")
    assert chain.generate("s") == "sea"

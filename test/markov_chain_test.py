from epithet_generator.markov_chain import markovChain


def test_empty_generation():
    assert markovChain().generate() == ""


def test_get_probability():
    chain = markovChain()
    chain.add("Sea")
    chain.add("see")
    assert chain.get_probability("se") == 1
    assert chain.get_probability("sea") == 0.5


def test_generation_not_empty():
    chain = markovChain()
    chain.add("sea")
    chain.add("sea")
    assert chain.generate() == "sea"


def test_restart_generation():
    chain = markovChain()
    chain.add("sea")
    chain.add("sea")
    assert chain.generate("s") == "sea"

from epithet_generator.markov_chain import markovChain


def test_empty_generation():
    assert markovChain().generateWord() == ""


def test_get_probability():
    chain = markovChain()
    chain.addWord("Sea")
    chain.addWord("see")
    assert chain.getProbability("se") == 1
    assert chain.getProbability("sea") == 0.5


def test_generation_not_empty():
    chain = markovChain()
    chain.addWord("sea")
    chain.addWord("sea")
    assert chain.generateWord() == "sea"

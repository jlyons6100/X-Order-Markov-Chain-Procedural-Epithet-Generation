from epithet_generator.markov_chain import markovChain


def test_empty_generation():
    assert markovChain().generateWord() == ""

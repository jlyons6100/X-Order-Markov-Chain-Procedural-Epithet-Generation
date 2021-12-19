from epithet_generator.markov_chain import markovChain


def generateWord():
    chain = markovChain()
    return chain.generateWord()


def test_empty_generation():
    assert markovChain().generateWord() == ""

from epithet_generator.markov_chain import markovChain
CONTINUE_CHANCE = .25


# Continue if chain is broken with some probability
# When to use backup logic
class epithetGenerator:
    def __init__(self):
        # Game of Thrones + Saved Generated Names
        self.chainPrimary = markovChain()
        # Backup chain from dictionary
        self.chainBackup = markovChain()

    # Logic to fill chains
    def add(self, word, chainType):
        if chainType == "primary":
            self.chainPrimary.add(word)
        else:
            self.chainBackup.add(word)

    def generate(self):
        # continue within word (BACKUP + restart primary)
        # continue with additional epithet (restart primary with , separating)
        return ""
e = epithetGenerator()


print(e.chainPrimary)

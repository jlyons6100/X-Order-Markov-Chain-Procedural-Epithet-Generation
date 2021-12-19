from epithet_generator.markov_chain import MarkovChain
CONTINUE_CHANCE = .25


# Continue if chain is broken with some probability
# When to use backup logic
class EpithetGenerator:
    def __init__(self):
        # Game of Thrones + Saved Generated Names
        self.chain_primary = MarkovChain()
        # Backup chain from dictionary
        self.chain_backup = MarkovChain()

    # Logic to fill chains
    def add(self, word, chain_type):
        if chain_type == "primary":
            self.chain_primary.add(word)
        else:
            self.chain_backup.add(word)

    def generate(self):
        # continue within word (BACKUP + restart primary)
        # continue with additional epithet (restart primary with , separating)
        return ""

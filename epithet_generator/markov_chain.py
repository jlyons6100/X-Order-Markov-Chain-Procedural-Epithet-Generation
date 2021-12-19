import random


class markovChain:
    def __init__(self):
        self.root = {}

    def add(self, word):
        node = self.root
        # Populate tree with letter counts
        for letter in word.lower():
            lettersAndCount = node.setdefault(
                letter,
                {"nextLetters": {}, "count": 0})
            node = lettersAndCount["nextLetters"]
            lettersAndCount["count"] += 1

    def generate(self, start=None):
        wordList = []
        node = self.root
        # Restart chain logic
        if start:
            node = node[start]["nextLetters"]
            wordList.append(start)

        while len(node.keys()) != 0:
            weights = [node[key]["count"] for key in node.keys()]
            # Pick random character based on weight
            newChar = random.choices(list(node.keys()), weights)[0]
            wordList.append(newChar)
            # Move to next node
            node = node[newChar]["nextLetters"]
        return "".join(wordList)

    def getProbability(self, prefix):
        node = self.root
        probability = 1
        for letter in prefix.lower():
            if letter not in node:
                return 0
            total = sum([node[key]["count"] for key in node.keys()])
            # Independent events, multiply together for probability
            probability *= ((node[letter]["count"])/(total))
            node = node[letter]["nextLetters"]
        return probability

import random


class markovChain:
    def __init__(self, order=1):
        self.root = {}
        self.order = order

    def _chunker(self, seq, size):
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))

    def add(self, word):
        node = self.root
        # Populate trie with letter-chunks
        for letterChunk in self._chunker(word.lower(), self.order):
            lettersAndCount = node.setdefault(
                letterChunk,
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
        for letterChunk in self._chunker(prefix.lower(), self.order):
            if letterChunk not in node:
                return 0
            total = sum([node[key]["count"] for key in node.keys()])
            # Independent events, multiply together for probability
            probability *= ((node[letterChunk]["count"])/(total))
            node = node[letterChunk]["nextLetters"]
        return probability

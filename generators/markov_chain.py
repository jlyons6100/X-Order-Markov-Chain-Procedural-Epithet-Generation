import random


class MarkovChain:
    def __init__(self, order=1):
        self.root = {}
        self.order = order

    def _chunker(self, seq, size):
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))

    def add(self, word):
        node = self.root
        # Populate trie with letter-chunks
        for letter_chunk in self._chunker(word.lower(), self.order):
            letters_and_count = node.setdefault(
                letter_chunk,
                {"nextLetters": {}, "count": 0})
            node = letters_and_count["nextLetters"]
            letters_and_count["count"] += 1

    def generate(self, start=None):
        word_list = []
        node = self.root
        # Restart chain logic
        if start:
            node = node[start]["nextLetters"]
            word_list.append(start)

        while len(node.keys()) != 0:
            weights = [node[key]["count"] for key in node.keys()]
            # Pick random character based on weight
            new_char = random.choices(list(node.keys()), weights)[0]
            word_list.append(new_char)
            # Move to next node
            node = node[new_char]["nextLetters"]
        return "".join(word_list)

    def get_probability(self, prefix):
        node = self.root
        probability = 1
        for letter_chunk in self._chunker(prefix.lower(), self.order):
            if letter_chunk not in node:
                return 0
            total = sum([node[key]["count"] for key in node.keys()])
            # Independent events, multiply together for probability
            probability *= ((node[letter_chunk]["count"])/(total))
            node = node[letter_chunk]["nextLetters"]
        return probability

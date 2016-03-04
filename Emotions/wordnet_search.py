import os

class WordNet:
    def __init__(self):
        self.word_data = []

        for item in self.load_words("wordnets/EffectWordNet.tff"):
            if item not in self.word_data:
                self.word_data.append(item)
        for item in self.load_words("wordnets/goldStandard.tff"):
            if item not in self.word_data:
                self.word_data.append(item)

    @staticmethod
    def load_words(self, filename):
        words = []
        path = os.path.dirname(__file__)
        response_file = open(os.path.join(path, filename))
        for line in response_file:
            data = line.split()
            words = data.split()[2].split(",")
            effect = data.split()[1]
            if effect == "+Effect":
                effect = 1
            elif effect == "-Effect":
                effect = -1
            else:
                effect = 0
            for word in words:
                words.append({
                    "word": word.lower(),
                    "effect": effect
                })
        response_file.close()
        return words

    def find_word(self, word):
        """
        Find a word
        :param word:
        :return:
        """
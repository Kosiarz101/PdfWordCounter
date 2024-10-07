from typing import Dict

class WordDistribution:
    def __init__(self, counted_words_dict: Dict[str, int], allWordsCount = 0):
        self.counted_words_dict = counted_words_dict
        self.allWordsCount = allWordsCount
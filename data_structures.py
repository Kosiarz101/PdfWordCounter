from typing import Dict

class WordStats:
    def __init__(self, quantity: int, probability: float):
        self.quantity = quantity
        self.probability = probability

class WordDistribution:
    def __init__(self, counted_words_dict: Dict[str, WordStats], allWordsCount = 0):
        self.counted_words_dict = counted_words_dict
        self.allWordsCount = allWordsCount
from enum import Enum
from typing import Dict

class SortMode(Enum):
    WORD = 'word'
    COUNT = 'count'

class WordStats:
    def __init__(self, quantity: int, probability: float):
        self.quantity = quantity
        self.probability = probability

class WordDistribution:
    def __init__(self, counted_words_dict: Dict[str, WordStats], all_words_count = 0, sort_mode: SortMode = SortMode.COUNT):
        self.counted_words_dict = counted_words_dict
        self.all_words_count = all_words_count
        self.sort_mode = sort_mode
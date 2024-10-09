import string
from typing import Dict

from data_structures import WordDistribution, WordStats

def count_words(pages) -> WordDistribution:
    counted_words_dict: Dict[str, WordStats] = {}
    allWordsCounter = 0

    for page in pages:
        text: str = page.extract_text()
        words = text.split()
        for word in words:
            processed_word = _normalise_word(word)
            if processed_word:
                allWordsCounter += 1
                _add_word_to_dict(processed_word, counted_words_dict)

    word_distribution = WordDistribution(counted_words_dict, allWordsCounter)           
    return word_distribution

def calculate_probabilities(word_distribution: WordDistribution, precision: int) -> WordDistribution:
    for word, word_stats in word_distribution.counted_words_dict.items():
        word_stats.probability = (word_stats.quantity / word_distribution.all_words_count) * 100
        word_stats.probability = round(word_stats.probability, precision)  
    return word_distribution

def _add_word_to_dict(word: str, wordDict: Dict[str, WordStats]) -> str:
    if word in wordDict:
        wordDict[word].quantity += 1
    else:
        wordDict[word] = WordStats(1, None)

def _normalise_word(word: str) -> str:
    processed_word: str = _delete_punctuation_signs(word)
    return processed_word.lower()

def _delete_punctuation_signs(word: str) -> str:
    processed_word: str = ""
    punctuation = string.punctuation + '–'
    punctuation_exceptions = ["-", "'"]
    hello = list(filter(lambda x: x in punctuation_exceptions or x not in punctuation, word))
    return processed_word.join(hello)
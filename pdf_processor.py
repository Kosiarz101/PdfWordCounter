import string
from typing import Dict

from words_distribution import WordDistribution

def count_words(pages) -> WordDistribution:
    counted_words_dict: Dict[str, int] = {}
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

def _add_word_to_dict(word: str, wordDict) -> str:
    if word in wordDict:
        wordDict[word] += 1
    else:
        wordDict[word] = 1

def _normalise_word(word: str) -> str:
    processed_word: str = _delete_punctuation_signs(word)
    return processed_word.lower()

def _delete_punctuation_signs(word: str) -> str:
    processed_word: str = ""
    punctuation = string.punctuation
    hello = list(filter(lambda x: x not in punctuation, word))
    return processed_word.join(hello)
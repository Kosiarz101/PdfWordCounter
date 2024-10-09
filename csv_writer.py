import csv

from data_structures import SortMode, WordDistribution

def write(file_path: str, words_distribution: WordDistribution):
    _sort(words_distribution)
    with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, strict=False)
        writer.writerow(['Word', 'Quantity', 'Probability'])
        for word, word_stats in words_distribution.counted_words_dict.items():
            writer.writerow([word, word_stats.quantity, word_stats.probability])

def _sort(words_distribution: WordDistribution):
    counted_words_dict = words_distribution.counted_words_dict
    if words_distribution.sort_mode == SortMode.COUNT:
        words_distribution.counted_words_dict = dict(sorted(counted_words_dict.items(), key=lambda item: item[1].quantity, reverse=True))
    elif words_distribution.sort_mode == SortMode.WORD:
        words_distribution.counted_words_dict = dict(sorted(counted_words_dict.items()))

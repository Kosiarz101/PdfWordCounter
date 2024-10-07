import csv

from words_distribution import WordDistribution

def write(file_path: str, words_distribution: WordDistribution):
    with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, strict=False)
        writer.writerow(['Word', 'Quantity'])
        for word, quantity in words_distribution.counted_words_dict.items():
            writer.writerow([word, quantity])

import string
import sys
from PyPDF2 import PdfReader

import csv_writer
import pdf_processor

wordDict = {}

def print_dict(z: dict):
    sorted_dict = dict(sorted(z.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")

def print_list(y):
    list(map(lambda x: print(x), y))

doc_path = "./test.pdf" if len(sys.argv) <= 1 or not sys.argv[1] else sys.argv[1]
csv_path = "./result.csv"

reader = PdfReader(doc_path)
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

word_distribution = pdf_processor.count_words(reader.pages)
pdf_processor.calculate_probabilities(word_distribution)
word_distribution.counted_words_dict = dict(sorted(word_distribution.counted_words_dict.items(), key=lambda item: item[1].quantity, reverse=True))
csv_writer.write(csv_path, word_distribution)
print(word_distribution.allWordsCount)
import sys
import argparse
from PyPDF2 import PdfReader

import csv_writer
from data_structures import SortMode
import pdf_processor

wordDict = {}

def print_dict(z: dict):
    sorted_dict = dict(sorted(z.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")

def print_list(y):
    list(map(lambda x: print(x), y))

argument_parser = argparse.ArgumentParser(
                    prog='PdfWordCounter',
                    description='Program counts all words in pdf file and calculates it\'s word distribution')
argument_parser.add_argument('filename', help='location to pdf file')
argument_parser.add_argument('-o', '--output', help='location to csv output file', default="./result.csv", required=False, dest='output')
argument_parser.add_argument('-p', '--precision', help='precision of probability rounding', default=2, required=False, dest='precision', type=int, choices={1,2,3,4,5})
argument_parser.add_argument('-s', '--sorting', help='sorting mode', default='count', required=False, dest='sort_mode', type=str, choices={'count', 'word'})
args = argument_parser.parse_args()

doc_path = args.filename
csv_path = args.output
precision = args.precision
sort_mode = SortMode(args.sort_mode)

reader = PdfReader(doc_path)
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

word_distribution = pdf_processor.count_words(reader.pages)
word_distribution.sort_mode = sort_mode
pdf_processor.calculate_probabilities(word_distribution, precision)
csv_writer.write(csv_path, word_distribution)
print(f'all words count in pdf: {word_distribution.all_words_count}')
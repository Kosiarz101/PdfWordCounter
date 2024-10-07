import sys
from PyPDF2 import PdfReader

import csv_writer
import pdf_processor
import words_distribution

wordDict = {}

doc_path = "./test.pdf" if len(sys.argv) <= 1 or not sys.argv[1] else sys.argv[1]
csv_path = "./result.csv"

reader = PdfReader(doc_path)
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

words_distribution = pdf_processor.count_words(reader.pages)
csv_writer.write(csv_path, words_distribution)
print(words_distribution.allWordsCount)
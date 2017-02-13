#!/usr/bin/env python3
"""
This receives text from stdin and does a collocation analysis
"""

import sys
import nltk
from nltk.collocations import *


def read_lines_stdin():
    lines = []
    for line in sys.stdin:
        lines.append(line)
    return lines

if __name__ == '__main__':
    tweets = read_lines_stdin()
    tokens = nltk.wordpunct_tokenize(" ".join(tweets))

    print("Trigrams - 3 words with more than 3 characters each occuring together min. 3x in full text:")
    trigram_measures = nltk.collocations.TrigramAssocMeasures()
    finder = TrigramCollocationFinder.from_words(tokens)
    finder.apply_word_filter(lambda w: len(w) < 3)
    finder.apply_freq_filter(3)
    print(finder.nbest(trigram_measures.pmi, 20))
    print()

    print("Bigrams - 2 words with more than 3 characters each occuring together min. 3x in full text:")
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(tokens)
    finder.apply_word_filter(lambda w: len(w) < 3)
    finder.apply_freq_filter(3)
    print(finder.nbest(bigram_measures.pmi, 20))
    print()

#!/usr/bin/env python3
"""
This receives text from stdin and does a sentiment analysis on each line
"""

import sys
import nltk
from nltk.corpus import stopwords


def read_lines_stdin():
    lines = []
    for line in sys.stdin:
        lines.append(line)
    [line.replace('\n', '') for line in lines]
    return lines

if __name__ == '__main__':
    tweets = read_lines_stdin()
    
    default_stopwords = set(nltk.corpus.stopwords.words('english'))
    words = nltk.word_tokenize(" ".join(tweets))

    # Cleanup
    words = [word for word in words if len(word) > 1]
    words = [word for word in words if not word.isnumeric()]
    words = [word.lower() for word in words]
    words = [word for word in words if word not in default_stopwords]

    # Calculate frequency distribution
    fdist = nltk.FreqDist(words)
    
    # print(words)
    for word, frequency in fdist.most_common(50):
        print(u'{};{}'.format(word, frequency))
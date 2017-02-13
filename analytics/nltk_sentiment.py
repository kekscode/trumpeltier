#!/usr/bin/env python3
"""
This receives text from stdin and does a sentiment analysis on each line
"""

import sys
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def read_lines_stdin():
    lines = []
    for line in sys.stdin:
        lines.append(line)
    [line.replace('\n', '') for line in lines]
    return lines

if __name__ == '__main__':
    tweets = read_lines_stdin()
    sid = SentimentIntensityAnalyzer()
    for tweet in tweets:
        ss = sid.polarity_scores(tweet)
        for k in sorted(ss):
            print('{0}: {1}, '.format(k, ss[k]), end='')
        print(tweet)

    print("All tweets as one document:")
    ss = sid.polarity_scores(" ".join(tweets[:]))
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')

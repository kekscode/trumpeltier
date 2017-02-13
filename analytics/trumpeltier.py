#!/usr/bin/env python3
"""trumpeltier

Usage:
  trumpeltier.py dump
  trumpeltier.py (-h | --help)
  trumpeltier.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
import pymongo
from docopt import docopt


def connect_mongodb(database='trumpeltier_app', collection='tweets'):
    client = pymongo.MongoClient()
    database = client[database]
    collection = database[collection]
    return database, collection


def fetch_tweets(collection, query={"text": {"$regex": ".*" }}):
    return collection.find(query)

if __name__ == '__main__':
    arguments = docopt(__doc__, version='trumpeltier 0.1')
    db, coll = connect_mongodb()

    # Print all tweets
    if arguments['dump']:
        for tweet in fetch_tweets(coll):
            print(tweet['text'])

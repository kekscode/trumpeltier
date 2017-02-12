#!/usr/bin/env python3
"""
This receives json from stdin and stores them to mongodb
"""

import sys
import json
import pymongo
from pymongo.errors import DuplicateKeyError

def read_json_stdin():
    return json.load(sys.stdin)

def save_to_mongodb(docs, database='trumpeltier_app', collection='tweets'):
    client = pymongo.MongoClient()
    db = client[database]
    coll = db[collection]
    coll.create_index('id', unique=True)
    for doc in docs:
        try:
            doc_inserted = coll.insert(doc)
        except DuplicateKeyError as e:
            print(e)
            continue

if __name__ == '__main__':
    docs = read_json_stdin()
    save_to_mongodb(docs)
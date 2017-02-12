#!/usr/bin/env python3
"""
Follow the white house rabbit

This fetches tweets from an user and prints
the full json output from the api.
"""

import os
import sys
import json
from twython import Twython
from twython import TwythonError

CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET_KEY = os.environ.get('TWITTER_CONSUMER_SECRET_KEY')
ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

def query(screen_name='realDonaldTrump'):
    # Requires Authentication as of Twitter API v1.1
    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    try:
        user_timeline = twitter.get_user_timeline(screen_name=screen_name)
    except TwythonError as e:
        print(e)

    print(json.dumps(user_timeline))

if __name__ == '__main__':
    try:
        query(sys.argv[1])
    except IndexError as e:
        print("Missing Twitter user name as first parameter")

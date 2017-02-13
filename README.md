# trumpeltier
A demo how to analyze text snippets in python

## Try

* Start a local mongodb
* Feed the latest tweets from Trump with `./follower/fetch_timeline.py realdonaldtrump | storage/save_to_mongo.py`
* Print all tweets using `python analytics/trumpeltier.py dump`

## Requirements

* Python 3
* twython
* pymongo
* MongoDB
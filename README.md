# trumpeltier
A demo how to analyze text snippets in python

* `follower/fetch_timeline.py` fetches twitter user timelines and printing json from the native api
* `storage/save\_to_mongo.py` saves json from fetch\_timeline into mongodb
* `analytics/trumpeltier.py` prints plain text tweets from database to feed into analytics

## Try

* Start a local mongodb
* Feed the latest tweets from Trump with `./follower/fetch_timeline.py realdonaldtrump | storage/save_to_mongo.py`
* Print all tweets using `python analytics/trumpeltier.py dump`

## Requirements

* Python 3
* twython
* pymongo
* MongoDB
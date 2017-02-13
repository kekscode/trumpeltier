# trumpeltier
A demo how to analyze text snippets in python

* `follower/fetch_timeline.py` fetches twitter user timelines and printing json from the native api
* `storage/save\_to_mongo.py` saves json from fetch\_timeline into mongodb
* `analytics/trumpeltier.py` prints plain text tweets from database to feed into analytics

Some analytics need corpora from NLTK. See [download instructions][1].

## Try

Fetch tweets:

* Start a local mongodb
* Feed the latest tweets from Trump with `./follower/fetch_timeline.py realdonaldtrump | storage/save_to_mongo.py`
* Print all tweets using `python analytics/trumpeltier.py dump`

Analyze tweets:

* `./analytics/trumpeltier.py dump | ./analytics/nltk_wordfreq.py`
* `./analytics/trumpeltier.py dump | ./analytics/nltk_sentiment.py`
* `./analytics/trumpeltier.py dump | ./analytics/nltk_collocations.py`

This should give you - for example for twitter user @realDonaldTrump - this output:

```
$ ./analytics/trumpeltier.py dump | ./analytics/nltk_wordfreq.py
https;51
...;31
``;27
people;27
great;27
'';25
country;22
news;18
u.s.;18
back;16
amp;16
fake;16
today;15
thank;14
n't;13
trump;13
jobs;12
bad;12
america;10
prime;10
many;10
's;10
minister;10
make;10
never;9
big;9
media;9
```

and

```
$ ./analytics/trumpeltier.py dump | ./analytics/nltk_sentiment.py
compound: -0.4621, neg: 0.26, neu: 0.545, pos: 0.195, Just leaving Florida. Big crowds of enthusiastic supporters lining the road that the FAKE NEWS media refuses to mention. Very dishonest!

compound: 0.8516, neg: 0.0, neu: 0.628, pos: 0.372, Congratulations Stephen Miller- on representing me this morning on the various Sunday morningshows. Great job!

compound: -0.6669, neg: 0.212, neu: 0.698, pos: 0.091, I know Mark Cuban well. He backed me big-time but I wasn't interested in taking all of hiscalls.He's not smart enough to run for president!

compound: 0.0, neg: 0.0, neu: 1.0, pos: 0.0, After two days of very productive talks, Prime Minister Abe is heading back to Japan. L

compound: -0.8891, neg: 0.366, neu: 0.634, pos: 0.0, While on FAKE NEWS @CNN, Bernie Sanders was cut off for using the term fake news to describethe network. They said technical difficulties!

compound: 0.1027, neg: 0.0, neu: 0.938, pos: 0.062, 72% of refugees admitted into U.S. (2/3 -2/11) during COURT BREAKDOWN are from 7 countries: SYRIA, IRAQ, SOMALIA, IRAN, SUDAN, LIBYA &amp; YEMEN

[...]

compound: -0.4404, neg: 0.187, neu: 0.733, pos: 0.081, Congressman John Lewis should spend more time on fixing and helping his district, which isin horrible shape and falling apart (not to......

compound: 0.8271, neg: 0.087, neu: 0.557, pos: 0.355, A beautiful funeral today for a real NYC hero, Detective Steven McDonald. Our law enforcement community has my complete and total support.

compound: 0.5411, neg: 0.0, neu: 0.667, pos: 0.333, The "Unaffordable" Care Act will soon be history!

compound: -0.8208, neg: 0.382, neu: 0.45, pos: 0.168, have been allowed to run - guilty as hell. They were VERY nice to her. She lost because shecampaigned in the wrong states - no enthusiasm!

compound: 0.3182, neg: 0.075, neu: 0.795, pos: 0.13, What are Hillary Clinton's people complaining about with respect to the F.B.I. Based on the information they had she should never.....

compound: -0.3595, neg: 0.098, neu: 0.902, pos: 0.0, released by "Intelligence" even knowing there is no proof, and never will be. My people willhave a full report on hacking within 90 days!

compound: 0.5719, neg: 0.0, neu: 0.821, pos: 0.179, Wonderful meeting with Canadian PM @JustinTrudeau and a group of leading CEO's &amp; businesswomen from Canada🇨🇦and th… https://t.co/wAoCOaYeZ6

compound: 0.5093, neg: 0.0, neu: 0.68, pos: 0.32, Welcome to the @WhiteHouse Prime Minister @JustinTrudeau! https://t.co/WKgF8Zo9ri

compound: 0.0, neg: 0.0, neu: 1.0, pos: 0.0, Today I will meet with Canadian PM Trudeau and a group of leading business women to discuss women inthe workforce. https://t.co/bFAHPRXHdP

All tweets as one document:
compound: 0.9992, neg: 0.159, neu: 0.658, pos: 0.183, %
```

and

```
$ ./analytics/trumpeltier.py dump | ./analytics/nltk_collocations.py
Trigrams - 3 words with more than 3 characters each occuring together min. 3x in full text:
[('AMERICA', 'GREAT', 'AGAIN'), ('MAKE', 'AMERICA', 'GREAT'), ('Minister', 'Shinzo', 'Abe'), ('Prime', 'Minister', 'Shinzo'), ('Prime', 'Minister', 'Abe'), ('FAKE', 'NEWS', 'media'), ('bring', 'back', 'our'), ('will', 'bring', 'back'), ('the', 'United', 'States'), ('with', 'Prime', 'Minister'), ('into', 'our', 'country'), ('Thank', 'you', 'for'), ('the', 'FAKE', 'NEWS'), ('...', 'https', '://')]

Bigrams - 2 words with more than 3 characters each occuring together min. 3x in full text:
[('Lincoln', 'Memorial'), ('White', 'House'), ('United', 'States'), ('John', 'Lewis'), ('Supreme', 'Court'), ('Attorney', 'General'), ('daughter', 'Ivanka'), ('MAKE', 'AMERICA'), ('AMERICA', 'GREAT'), ('GREAT', 'AGAIN'), ('Shinzo', 'Abe'), ('Prime', 'Minister'), ('Minister', 'Shinzo'), ('just', 'look'), ('FAKE', 'NEWS'), ('just', 'like'), ('bring', 'back'), ('this', 'morning'), ('Thank', 'you'), ('Minister', 'Abe')]
```

## Python requirements

* Python 3
* twython
* pymongo
* nltk

## Database requirements

* MongoDB

[1]: http://www.nltk.org/data.html
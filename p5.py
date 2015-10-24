import json
import datetime, time

files = ['sample1_period1', 'sample2_period2', 'sample3_period3', 'sample4_period1', 'sample5_period1', 'sample6_period2', 'sample7_period3', 'sample8_period1', 'sample9_period2', 'sample10_period3']
for f in files:
    print f
    tweets = open(r'C:\Users\Manasi\Documents\Winter2015\ee239\Project 3\\' + f + '.txt', 'r')
    line = json.loads(tweets.readline())
    tweets.seek(0, 0)
    start_time = line.get('firstpost_date')
    print start_time
    end_time = 0
    for tweet in tweets:
        t = json.loads(tweet)
        end_time = t.get('firstpost_date')
    print end_time
    tweets.close()


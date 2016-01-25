import json
import tweepy
from tweepy import OAuthHandler
import time
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter

CONSUMER_KEY = 'nRl43wXJIJuUB8pjJRCEgaxhK'
CONSUMER_SECRET = 'b3gOvBgdMLRO2DoIaFQviqScTYyffAvhjm3ekjNAEOOf1rCP3r'
OAUTH_TOKEN = '588663819-xhhPknNBD2UJqDCoy7fpxZzyqr6Zp1QpHjKoVGCX'
OAUTH_TOKEN_SECRET = '5uQl4RxtNkLGeHQdUIsKGClxlVtLThRzeIyvVydnKbsRP'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 50
query = 'Ireland'

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_retweets = 10

pop_tweets = [status
              for status in results
              if status._json['retweet_count'] > min_retweets]

print pop_tweets

tweets_tup = tuple([(tweet._json['text'].encode('utf-8'),
                     tweet._json['retweet_count']) for tweet in pop_tweets])

pop_tweets_set = set(tweets_tup)

sorted_tweet_tup = sorted(pop_tweets_set, key=itemgetter(1), reverse=True)[:5]

table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in sorted_tweet_tup:
    table.add_row([key, val])
    table.max_width['Text'] = 50
    table.align['Text'], table.align['Retweet Count'] = 'l', 'r'

print table

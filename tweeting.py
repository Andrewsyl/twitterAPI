import json
import tweepy
from tweepy import OAuthHandler
import time
from collections import Counter
from prettytable import PrettyTable

CONSUMER_KEY = 'nRl43wXJIJuUB8pjJRCEgaxhK'
CONSUMER_SECRET = 'b3gOvBgdMLRO2DoIaFQviqScTYyffAvhjm3ekjNAEOOf1rCP3r'
OAUTH_TOKEN = '588663819-xhhPknNBD2UJqDCoy7fpxZzyqr6Zp1QpHjKoVGCX'
OAUTH_TOKEN_SECRET = '5uQl4RxtNkLGeHQdUIsKGClxlVtLThRzeIyvVydnKbsRP'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 50
query = 'Dublin'

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [status._json['text'] for status in results]

screen_names = [status._json['user']['screen_name']
                for status in results
                for mention in
                status._json['entities']['user_mentions']]
hashtags = [hashtag['text']
            for status in results
            for hashtag in status._json['entities']['hashtags']]

words = [word for text in status_texts for word in text.split()]

for entry in [screen_names, hashtags, words]:
    counter = Counter(entry)
    print counter.most_common()[:10]
    print

print json.dumps(status_texts[0:5], indent=1)
print json.dumps(screen_names[0:5], indent=1)
print json.dumps(hashtags[0:5], indent=1)
print json.dumps(words[0:5], indent=1)

for label, data in (('Text', status_texts), ('Screen Name', screen_names), ('Word', words)):
    table = PrettyTable(field_names=[label, 'count'])
    counter = Counter(data)
    [table.add_row(entry) for entry in counter.most_common()[:10]]
    table.align[label], table.align['Count'] = 'l', 'r'
    print table

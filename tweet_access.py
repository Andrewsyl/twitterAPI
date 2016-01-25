import json
import tweepy
from tweepy import OAuthHandler
import time

CONSUMER_KEY = 'nRl43wXJIJuUB8pjJRCEgaxhK'
CONSUMER_SECRET = 'b3gOvBgdMLRO2DoIaFQviqScTYyffAvhjm3ekjNAEOOf1rCP3r'
OAUTH_TOKEN = '588663819-xhhPknNBD2UJqDCoy7fpxZzyqr6Zp1QpHjKoVGCX'
OAUTH_TOKEN_SECRET = '5uQl4RxtNkLGeHQdUIsKGClxlVtLThRzeIyvVydnKbsRP'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 10
query = 'CodersInstitute'

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

'''for result in results:
    print json.dumps(result._json,indent=2)'''

for status in results:
    print "USER ID: " + str(status.user.id)
    print "TWEET: " + str(status.text.encode('utf-8'))
    print "TWITTER HANDLE: " + str(status.user.screen_name)
    print "AREA: " + str(status.place)
    print "NO. OF FOLLOWERS: " + str(status.user.followers_count)
    print "TIME OF TWEET: " + str(status.created_at)
    print

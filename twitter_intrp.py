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

'''DUB_WOE_ID = 560743
LON_WOE_ID = 44418
GAL_WOE_ID = 560912
NY_WOE_ID = 2459115'''

ids = [page for page in tweepy.Cursor(api.followers_ids, screen_name="McDonalds").pages(1)]
for id in ids:
    print json.dumps(ids, indent=2)

'''dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)
gal_trends = api.trends_place(GAL_WOE_ID)
NY_trends = api.trends_place(NY_WOE_ID)

print json.dumps(dub_trends, indent=1)
print json.dumps(lon_trends, indent=1)
print common_trends
print json.dumps(NY_trends),
print json.dumps(user, indent=1)'''

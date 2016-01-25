import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'nRl43wXJIJuUB8pjJRCEgaxhK'
CONSUMER_SECRET = 'b3gOvBgdMLRO2DoIaFQviqScTYyffAvhjm3ekjNAEOOf1rCP3r'
OAUTH_TOKEN = '588663819-xhhPknNBD2UJqDCoy7fpxZzyqr6Zp1QpHjKoVGCX'
OAUTH_TOKEN_SECRET = '5uQl4RxtNkLGeHQdUIsKGClxlVtLThRzeIyvVydnKbsRP'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

user = api.get_user('@madonna')

print(user.screen_name)
print(user.followers_count)

for friend in user.friends():
    print
    print(friend.screen_name)
    print(friend.followers_count)


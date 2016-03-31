# coding: utf-8

import tweepy
import sys

if not (
    len(sys.argv)==3 and sys.argv[1]=="/t" or
    len(sys.argv)==3 and sys.argv[1]=="/txt" or
    len(sys.argv)==4 and sys.argv[1]=="/txt"):
    print "%s /t text" % sys.argv[0]
    print "%s /txt [line] filename" % sys.argv[0]
    exit(-1)

if sys.argv[1]=="/t":
    tweet = sys.argv[2]
elif len(sys.argv)==3:
    tweet = open(sys.argv[2]).read()
else:
    tweet = open(sys.argv[3]).read().split("\n")[int(sys.argv[2])-1]
tweet = tweet.decode("cp932")

consumer_key = "M77DR9nVi47c2wWydverHFX8t"
consumer_secret = "Zv3rooFzikSarMLj4Pa7kWWSrYjIG7H7lQgogm0ZBztIYqjxbQ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

try:
    auth_token, auth_secret = open(sys.argv[0]+".txt").read().split()
    auth.set_access_token(auth_token, auth_secret)
except:
    url = auth.get_authorization_url()
    print "Auth URL: "+url

    verifier = raw_input("code: ")

    auth.get_access_token(verifier)
    auth_token = auth.access_token
    auth_secret = auth.access_token_secret

    open(sys.argv[0]+".txt", "w").write(auth_token+"\n"+auth_secret)

api = tweepy.API(auth)
api.update_status(tweet)

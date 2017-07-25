import tweepy
from local_config import *

if __name__ == "__main__":
  auth = tweepy.OAuthHandler(cons_tok, cons_sec)
  auth.set_access_token(app_tok, app_sec)
  twitter_API = tweepy.API(auth)
  
  search_results = tweepy.Cursor(twitter_API.search, q = "Python").items(5)
  for result in search_results:
      print(result.text)

  trends = twitter_API.trends_place(1)
  
  for trend in trends[0]["trends"]:
    print(trend['name'])

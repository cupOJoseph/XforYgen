import tweepy
import random

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here

  keys = [line.strip() for line in open("config.txt")]
  '''
  To use, add keys to a config.txt file. each key alone, 1 per line, no quotes or anything
  '''


  cfg = {
    "consumer_key"        : keys[0],
    "consumer_secret"     : keys[1],
    "access_token"        : keys[2],
    "access_token_secret" : keys[3]
    }
  api = get_api(cfg)

  # Open files
  Xfile = open('X.txt')
  Yfile = open('Y.txt')

  #create lists from files
  X = [line.strip() for line in Xfile]
  Y = [line.strip() for line in Yfile]

  tweet = "The next big thing is: "
  tweet = tweet + random.choice(X) + " for " + random.choice(Y) ". #NextBigThing #startupidea"

  status = api.update_status(status=tweet)


if __name__ == "__main__":
  main()

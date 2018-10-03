import tweepy
import random

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  with open('config.txt') as config_file, open('X.txt') as Xfile, open('Y.txt') as Yfile:
    keys = config_file.read().splitlines()
    X = Xfile.read().splitlines()
    Y = Yfile.read().splitlines()
    
    cfg = {
      "consumer_key"        : keys[0],
      "consumer_secret"     : keys[1],
      "access_token"        : keys[2],
      "access_token_secret" : keys[3]
      }
    
    api = get_api(cfg)
    tweet = "The next big thing is: "
    tweet = tweet + random.choice(X) + " but for " + random.choice(Y) + ". #NextBigThing #startupidea"

    status = api.update_status(status=tweet)


if __name__ == "__main__":
  main()

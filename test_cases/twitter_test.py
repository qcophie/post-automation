import tweepy
import os


def test_twitter_post():
    # Authenticate with the Twitter API using Tweepy
    auth = tweepy.OAuthHandler(os.environ.get("TWITTER_CONSUMER_KEY"), os.environ.get("TWITTER_CONSUMER_SECRET"))
    auth.set_access_token(os.environ.get("TWITTER_ACCESS_TOKEN"), os.environ.get("TWITTER_ACCESS_TOKEN_SECRET"))
    api = tweepy.API(auth)
    
    # Prep the tweet
    tweet = "Hello World"
    
    # Post the tweet
    post_tweet = api.update_status(tweet)
    
    # Assert that the tweet was posted successfully
    assert post_tweet.status_code == 200

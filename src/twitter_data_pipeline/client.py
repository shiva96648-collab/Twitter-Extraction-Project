import tweepy
from .config import Settings


def create_twitter_api(settings: Settings) -> tweepy.API:
    auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
    auth.set_access_token(settings.access_token, settings.access_token_secret)
    return tweepy.API(auth, wait_on_rate_limit=True)

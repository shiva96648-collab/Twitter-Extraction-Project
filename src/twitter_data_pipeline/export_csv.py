from pathlib import Path
import csv
import tweepy
from unidecode import unidecode
from .topics import TOPICS


def export_topic_to_csv(api, query: str, output_file: Path, limit: int = 1000) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["tweet", "user_name", "location"])
        cursor = tweepy.Cursor(api.search_tweets, q=query, lang="en", count=100).items(limit)
        for tweet in cursor:
            writer.writerow([
                unidecode(getattr(tweet, "text", "")),
                getattr(tweet.author, "screen_name", ""),
                getattr(tweet.author, "location", ""),
            ])

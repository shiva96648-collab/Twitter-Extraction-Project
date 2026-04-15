from dataclasses import dataclass
import os


@dataclass
class Settings:
    consumer_key: str
    consumer_secret: str
    access_token: str
    access_token_secret: str
    mongo_uri: str = "mongodb://localhost:27017/"
    database_name: str = "tweet_db"

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            consumer_key=os.getenv("TWITTER_CONSUMER_KEY", ""),
            consumer_secret=os.getenv("TWITTER_CONSUMER_SECRET", ""),
            access_token=os.getenv("TWITTER_ACCESS_TOKEN", ""),
            access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET", ""),
            mongo_uri=os.getenv("MONGO_URI", "mongodb://localhost:27017/"),
            database_name=os.getenv("MONGO_DB_NAME", "tweet_db"),
        )

    def validate(self) -> None:
        required = {
            "TWITTER_CONSUMER_KEY": self.consumer_key,
            "TWITTER_CONSUMER_SECRET": self.consumer_secret,
            "TWITTER_ACCESS_TOKEN": self.access_token,
            "TWITTER_ACCESS_TOKEN_SECRET": self.access_token_secret,
        }
        missing = [name for name, value in required.items() if not value]
        if missing:
            raise ValueError("Missing required environment variables: " + ", ".join(missing))

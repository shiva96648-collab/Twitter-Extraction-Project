from pymongo import ASCENDING, MongoClient
from .topics import TOPICS


def store_search_results(api, mongo_uri: str, database_name: str, limit: int = 10) -> None:
    client = MongoClient(mongo_uri)
    db = client[database_name]
    for collection_name, query in TOPICS.items():
        collection = db[collection_name]
        collection.create_index([("id", ASCENDING)], unique=True)
        results = api.search_tweets(q=query, lang="en", count=limit)
        statuses = results.get("statuses", []) if isinstance(results, dict) else []
        for status in statuses:
            collection.update_one({"id": status["id"]}, {"$set": status}, upsert=True)

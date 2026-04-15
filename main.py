from pathlib import Path
from twitter_data_pipeline.client import create_twitter_api
from twitter_data_pipeline.config import Settings
from twitter_data_pipeline.export_csv import export_topic_to_csv
from twitter_data_pipeline.store_mongo import store_search_results
from twitter_data_pipeline.topics import TOPICS


def main() -> None:
    settings = Settings.from_env()
    settings.validate()
    api = create_twitter_api(settings)

    data_dir = Path("data")
    for name, query in TOPICS.items():
        export_topic_to_csv(api, query, data_dir / f"{name}.csv")

    store_search_results(api, settings.mongo_uri, settings.database_name)


if __name__ == "__main__":
    main()

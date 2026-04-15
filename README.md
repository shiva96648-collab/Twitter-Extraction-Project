# GitHub-Ready Twitter Data Pipeline

This repository is a cleaned and structured version of the original uploaded scripts for collecting Twitter/X search data, exporting tweets to CSV, and storing results in MongoDB.

## Repository Structure

```text
github-ready-twitter-pipeline/
├── LICENSE
├── README.md
├── main.py
├── requirements.txt
└── src/
    └── twitter_data_pipeline/
        ├── __init__.py
        ├── client.py
        ├── config.py
        ├── export_csv.py
        ├── store_mongo.py
        └── topics.py
```

## Setup

1. Create and activate a virtual environment
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `env example` in README to `.env` file and add .gitignore
4. Add your Twitter/X API credentials and MongoDB connection details
5. Run the project
   ```bash
   PYTHONPATH=src python main.py
   ```

## Environment Variables

```Example env file content
TWITTER_CONSUMER_KEY=your_consumer_key
TWITTER_CONSUMER_SECRET=your_consumer_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
MONGO_URI=mongodb://localhost:27017/
MONGO_DB_NAME=tweet_db
```

## Functionality

- Exports tweet text, username, and location to per-topic CSV files
- Stores hashtag search results in MongoDB collections with unique tweet IDs
- Reuses a central topic map for all configured hashtag searches


# GitHub-Ready Twitter Data Pipeline

This repository is a cleaned and structured version of the original uploaded scripts for collecting Twitter/X search data, exporting tweets to CSV, and storing results in MongoDB.

## Why this version is GitHub-ready

- Removes hardcoded API credentials from source code
- Uses environment variables through a `.env.example` template
- Organizes code into reusable modules under `src/`
- Adds repository metadata files such as `.gitignore`, `requirements.txt`, and `LICENSE`
- Provides a single entry point through `main.py`

## Repository Structure

```text
github-ready-twitter-pipeline/
├── .env.example
├── .gitignore
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
3. Copy `.env.example` to `.env`
4. Add your Twitter/X API credentials and MongoDB connection details
5. Run the project
   ```bash
   PYTHONPATH=src python main.py
   ```

## Environment Variables

```env
TWITTER_CONSUMER_KEY=
TWITTER_CONSUMER_SECRET=
TWITTER_ACCESS_TOKEN=
TWITTER_ACCESS_TOKEN_SECRET=
MONGO_URI=mongodb://localhost:27017/
MONGO_DB_NAME=tweet_db
```

## Functionality

- Exports tweet text, username, and location to per-topic CSV files
- Stores hashtag search results in MongoDB collections with unique tweet IDs
- Reuses a central topic map for all configured hashtag searches

## Important Security Note

The original uploaded files contained embedded API credentials. Those credentials should be rotated before any further use.

## Suggested GitHub repo name

`twitter-data-pipeline`

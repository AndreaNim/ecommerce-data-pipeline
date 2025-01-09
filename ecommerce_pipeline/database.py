from pymongo import MongoClient
import pandas as pd
from typing import Optional
from ecommerce_pipeline.config import MONGO_URI, DB_NAME

def get_mongo_client() -> MongoClient:
    """Establish and return a MongoDB client."""
    return MongoClient(MONGO_URI)


def save_to_mongo(collection_name: str, data: pd.DataFrame, db_name: Optional[str] = DB_NAME):
    """Save a DataFrame to a MongoDB collection."""
    client = get_mongo_client()
    db = client[db_name]
    collection = db[collection_name]
    collection.delete_many({})  # Clear previous data
    collection.insert_many(data.to_dict('records'))
    print(f"Saved {len(data)} records to {collection_name} collection in the {db_name} database.")
    client.close()

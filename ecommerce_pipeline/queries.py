from pymongo import MongoClient
from typing import List, Dict
from ecommerce_pipeline.config import MONGO_URI, DB_NAME


def get_mongo_client() -> MongoClient:
    """Establish and return a MongoDB client."""
    return MongoClient(MONGO_URI)


def total_orders_per_product() -> List[Dict]:
    """Query total orders for each product."""
    client = get_mongo_client()
    db = client[DB_NAME]
    pipeline = [
        {"$group": {"_id": "$productId", "totalOrders": {"$sum": "$quantity"}}},
        {"$sort": {"totalOrders": -1}}
    ]
    results = list(db["raw_orders"].aggregate(pipeline))
    client.close()
    return results


def inventory_status() -> List[Dict]:
    """Query inventory status by product."""
    client = get_mongo_client()
    db = client[DB_NAME]
    pipeline = [
        {"$project": {"productId": 1, "availableQuantity": 1, "description": 1}},
    ]
    results = list(db["raw_inventory"].aggregate(pipeline))
    client.close()
    return results


def top_selling_products(limit: int = 10) -> List[Dict]:
    """
    Query to find the top-selling products.
    Args:
        limit (int): The number of top-selling products to return.
    """
    client = get_mongo_client()
    db = client[DB_NAME]

    pipeline = [
        {
            "$group": {
                "_id": "$productId",
                "totalOrders": {"$sum": 1},
            }
        },
        {"$sort": {"totalOrders": -1}},
        {"$limit": limit},
    ]

    top_products = list(db["raw_orders"].aggregate(pipeline))
    client.close()

    return top_products

def low_inventory_products(threshold: int = 10) -> List[Dict]:
    """
    Query MongoDB to find products with inventory below a given threshold.
    Args:
        threshold (int): The inventory level below which products are considered low stock.
    Returns:
        List[Dict]: A list of products with low inventory.
    """
    client = get_mongo_client()
    db = client[DB_NAME]

    pipeline = [
        {"$match": {"quantity": {"$lt": threshold}}},
        {"$project": {"_id": 0, "productId": 1, "productName": 1, "quantity": 1}},
    ]

    low_stock_products = list(db["raw_inventory"].aggregate(pipeline))
    client.close()

    return low_stock_products


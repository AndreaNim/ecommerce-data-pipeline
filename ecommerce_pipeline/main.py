from ecommerce_pipeline.config import ORDERS_FILE_PATH, INVENTORY_FILE_PATH
from ecommerce_pipeline.loader import load_and_validate
from ecommerce_pipeline.database import save_to_mongo
from ecommerce_pipeline.transformer import transform_data
from ecommerce_pipeline.queries import total_orders_per_product, inventory_status, low_inventory_products, top_selling_products



def main():
    """Main function to execute the data pipeline."""
    # Load raw datasets
    inventory = load_and_validate(INVENTORY_FILE_PATH)
    orders = load_and_validate(ORDERS_FILE_PATH)

    # Save raw data to MongoDB
    save_to_mongo("raw_inventory", inventory)
    save_to_mongo("raw_orders", orders)

    # Transform data
    transformed_data = transform_data(orders, inventory)

    # Save transformed data to MongoDB
    save_to_mongo("transformed_data", transformed_data)

    # Run queries and display results
    print("\nTotal Orders Per Product:")
    for result in total_orders_per_product():
        print(result)

    # Query for top-selling products
    top_products = top_selling_products(limit=10)
    print("Top-Selling Products:")
    for product in top_products:
        print(product)

    # Query for low inventory products
    low_stock = low_inventory_products(threshold=10)
    print("Products with Low Inventory:")
    for product in low_stock:
        print(product)

if __name__ == "__main__":
    main()
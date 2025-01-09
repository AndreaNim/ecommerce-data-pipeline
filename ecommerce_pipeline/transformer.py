import pandas as pd

def transform_data(orders: pd.DataFrame, inventory: pd.DataFrame) -> pd.DataFrame:
    """Transform and merge datasets."""
    # Join datasets on productId
    merged = pd.merge(orders, inventory, on="productId", how="inner")
    print(f"Merged dataset contains {len(merged)} records.")
    return merged

import pandas as pd

def load_and_validate(file_path: str) -> pd.DataFrame:
    """Load and validate a CSV file."""
    data = pd.read_csv(file_path)
    print(f"Loaded {len(data)} records from {file_path}")
    return data
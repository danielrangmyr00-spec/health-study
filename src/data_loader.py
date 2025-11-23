import pandas as pd


def load_health_data(path="data/health_study_dataset.csv"):
    """
    Load the health study dataset.

    Args:
        path (str): Relative path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    return pd.read_csv(path)

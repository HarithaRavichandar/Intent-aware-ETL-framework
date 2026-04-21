import pandas as pd
import os

ALLOWED_EXT = ["csv", "xlsx", "xls", "json", "parquet"]

def load_dataset(path):

    ext = os.path.splitext(path)[1].lower().replace(".", "")

    if ext not in ALLOWED_EXT:
        raise ValueError(f"Unsupported file format: {ext}")

    if ext == "csv":
        df = pd.read_csv(path)

    elif ext in ["xlsx", "xls"]:
        df = pd.read_excel(path)

    elif ext == "json":
        df = pd.read_json(path)

    elif ext == "parquet":
        df = pd.read_parquet(path)

    else:
        raise ValueError("File type not supported")

    return df

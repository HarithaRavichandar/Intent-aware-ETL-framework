import pandas as pd


def summarize_dataset(df):
    summary = {}

    # BASIC SHAPE 
    summary["rows"] = int(len(df))
    summary["columns"] = list(df.columns)

    # MISSING VALUES 
    summary["missing_values"] = {
        col: int(df[col].isna().sum())
        for col in df.columns
    }

    # NUMERIC SUMMARY 
    summary["numeric_summary"] = {}

    numeric_df = df.select_dtypes(include="number")

    for col in numeric_df.columns:
        summary["numeric_summary"][col] = {
            "mean": float(numeric_df[col].mean()),
            "min": float(numeric_df[col].min()),
            "max": float(numeric_df[col].max()),
            "std": float(numeric_df[col].std()),
            "nulls": int(numeric_df[col].isna().sum())
        }

    # CATEGORICAL SUMMARY 
    summary["categorical_summary"] = {}

    cat_df = df.select_dtypes(include="object")

    for col in cat_df.columns:
        summary["categorical_summary"][col] = {
            "unique_values": int(cat_df[col].nunique()),
            "top_5_values": cat_df[col].value_counts().head(5).to_dict()
        }

    # TIME COVERAGE 
    if "timestamp" in df.columns:
        ts = pd.to_datetime(df["timestamp"], errors="coerce")

        summary["date_range"] = {
            "start": str(ts.min()) if ts.notna().any() else None,
            "end": str(ts.max()) if ts.notna().any() else None
        }
    else:
        summary["date_range"] = None

    return summary

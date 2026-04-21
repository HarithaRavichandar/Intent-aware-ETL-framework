def require_columns(df, required):
    """
    Check if required columns exist.
    Returns list of missing column names.
    """
    cols = [c.lower() for c in df.columns]
    return [r for r in required if r.lower() not in cols]

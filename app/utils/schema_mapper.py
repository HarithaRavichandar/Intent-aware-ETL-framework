def map_column(df, candidates):
    """
    Returns the first matching column name from candidate list.
    """
    cols = {c.lower(): c for c in df.columns}

    for c in candidates:
        if c.lower() in cols:
            return cols[c.lower()]

    return None

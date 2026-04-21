VALID_MODES = ["none","moderate","strict"]

def clean(df, mode):
    """
    Apply data cleaning rules.

    Modes:
        none      - no cleaning
        moderate  - remove duplicate rows
        strict    - remove rows with missing values + duplicates

    Returns:
        pandas.DataFrame (cleaned copy)
    """
    if mode not in VALID_MODES:
        raise ValueError(f"Unknown cleaning mode: {mode}")

    df = df.copy()

    if mode == "none":
        return df

    if mode == "moderate":
        return df.drop_duplicates()

    if mode == "strict":
        return df.dropna().drop_duplicates()

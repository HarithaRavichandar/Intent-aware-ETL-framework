from app.storage.secure_store_writer import write_secure_raw

def compliance_flow(df, rules):

    # Save RAW data — no cleaning
    file = write_secure_raw(df)

    # Return ORIGINAL dataframe + row count
    return df, len(df)

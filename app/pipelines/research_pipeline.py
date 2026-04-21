from app.utils.cleaning import clean
from app.utils.privacy import apply_privacy
import pandas as pd
import time
import os

def research_flow(df, rules):

    # Light cleaning
    df = clean(df, rules["cleaning"])

    # Anonymize
    df = apply_privacy(df, rules["privacy"])

    # Take sample (50% default)
    df = df.sample(frac=0.5, random_state=1)

    # Ensure folder exists
    os.makedirs("outputs/research", exist_ok=True)

    # Save file
    fname = f"outputs/research/research_{int(time.time())}.csv"
    df.to_csv(fname, index=False)

    # RETURN TWO VALUES
    return df, len(df)

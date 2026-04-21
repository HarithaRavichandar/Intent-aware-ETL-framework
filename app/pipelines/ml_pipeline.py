from app.utils.cleaning import clean
from app.utils.privacy import apply_privacy
from app.storage.feature_store_writer import write_feature_store
from app.storage.database import write_table


def ml_flow(df, rules):
    
    df = clean(df, rules["cleaning"])
    df = apply_privacy(df, rules["privacy"])

    # Optional: remove columns with >60% missing
    df = df.loc[:, df.isnull().mean() < 0.6]

    file = write_feature_store(df)

    write_table(df, "ml_features")

    return df, len(df)

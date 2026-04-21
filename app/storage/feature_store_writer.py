from datetime import datetime, timezone
from app.utils.fs import ensure_dir

def write_feature_store(df):

    ensure_dir("outputs/feature_store")

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H-%M-%S")
    fname = f"outputs/feature_store/features_{timestamp}.csv"

    df.to_csv(fname, index=False, encoding="utf-8")

    return fname

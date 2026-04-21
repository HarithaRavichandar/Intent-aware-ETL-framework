from datetime import datetime, timezone
from app.utils.fs import ensure_dir

def write_secure_raw(df):

    ensure_dir("outputs/secure_raw")

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H-%M-%S")
    fname = f"outputs/secure_raw/raw_{timestamp}.csv"

    df.to_csv(fname, index=False, encoding="utf-8")

    return fname

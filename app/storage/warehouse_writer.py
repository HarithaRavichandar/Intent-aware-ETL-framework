from datetime import datetime, timezone
from app.utils.fs import ensure_dir

def write_warehouse(df):

    ensure_dir("outputs/warehouse")

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H-%M-%S")
    fname = f"outputs/warehouse/report_{timestamp}.csv"

    df.to_csv(fname, index=False, encoding="utf-8")

    return fname

import pandas as pd
from app.utils.cleaning import clean
from app.utils.privacy import apply_privacy
from app.utils.validation import require_columns
from app.storage.warehouse_writer import write_warehouse
from app.storage.database import write_table
from app.utils.schema_mapper import map_column

TIMESTAMP_FIELDS = ["timestamp","date","datetime","txn_time","order_date"]
AMOUNT_FIELDS = ["amount","price","value","sales","revenue","total"]


def reporting_flow(df, rules):
    """
    Execute reporting intent pipeline.

    Steps:
    - validate schema
    - clean dataset
    - mask privacy fields
    - aggregate monthly totals
    - store to warehouse + DB

    Returns:
        (DataFrame, int)
    """

    ts_col = map_column(df, TIMESTAMP_FIELDS)
    amt_col = map_column(df, AMOUNT_FIELDS)

    if not ts_col or not amt_col:
        raise ValueError(
            f"Dataset does not contain usable time "
            f"({TIMESTAMP_FIELDS}) and amount fields ({AMOUNT_FIELDS})."
        )

    df = clean(df, rules["cleaning"])
    df = apply_privacy(df, rules["privacy"])

    df[ts_col] = pd.to_datetime(df[ts_col], errors="coerce")
    df[amt_col] = pd.to_numeric(df[amt_col], errors="coerce")

    df = df.dropna(subset=[ts_col, amt_col])

    result = (
        df.groupby(df[ts_col].dt.to_period("M"))[amt_col]
        .sum()
        .reset_index()
    )

    # Convert Period to string for DB compatibility
    result[ts_col] = result[ts_col].astype(str)

    result = result.rename(columns={ts_col: "month", amt_col: "total_amount"})


    file = write_warehouse(result)
    write_table(result, "reporting_summary")

    return result, len(result)

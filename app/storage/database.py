import sqlite3
import re

DB = "outputs/pipeline.db"

def connect():
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    return conn


def validate_table_name(name):
    if not re.match(r"^[A-Za-z0-9_]+$", name):
        raise ValueError("Invalid table name")
    return name


def write_table(df, table):
    table = validate_table_name(table)

    with connect() as conn:
        df.to_sql(table, conn, if_exists="append", index=False, method="multi", chunksize=2000)

import pandas as pd

PII_FIELDS = [
    "customer_id","cust_id","user_id","userid",
    "email","mail",
    "phone","mobile","contact",
    "name","full_name","firstname","lastname",
    "address"
]

def apply_privacy(df, mode):

    df = df.copy()

    cols = {c.lower(): c for c in df.columns}

    if mode == "masked":
        for key in ["customer_id","cust_id","user_id","email","phone"]:
            if key in cols:
                col = cols[key]

                df[col] = df[col].astype(str)

                if "email" in key:
                    df[col] = df[col].str.replace(
                        r'(^.{2}).*@.*', r'\1***', regex=True
                    )
                else:
                    df[col] = df[col].str[:2] + "***"


    elif mode == "anonymized":
        drop_cols = [cols[c] for c in cols if c in PII_FIELDS]
        df = df.drop(columns=drop_cols, errors="ignore")

    elif mode == "restricted":
        # raw stored in secure folder — no change
        pass

    return df

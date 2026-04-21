import os

def ensure_dir(path: str):
    """
    Ensure a directory exists. Create it if missing.
    Safe to call multiple times.
    """
    os.makedirs(path, exist_ok=True)

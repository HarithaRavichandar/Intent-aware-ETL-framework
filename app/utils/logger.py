import logging
import uuid
import time
import os
from logging.handlers import RotatingFileHandler

os.makedirs("logs", exist_ok=True)

handler = RotatingFileHandler(
    "logs/pipeline.log",
    maxBytes=5_000_000,   # 5 MB
    backupCount=5
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[handler]
)

log = logging.getLogger("pipeline")


def start_run(intent, filename):
    run_id = str(uuid.uuid4())
    start = time.time()

    log.info(f"RUN START — id={run_id}, intent={intent}, file={filename}")

    return run_id, start


def end_run(run_id, rows, start_time):
    duration = round(time.time() - start_time, 2)
    log.info(f"RUN COMPLETE — id={run_id}, rows={rows}, duration={duration}s")


def fail_run(run_id, error):
    log.exception(f"RUN FAILED — id={run_id}, error={error}")

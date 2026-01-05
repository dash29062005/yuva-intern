import logging
from pathlib import Path

LOG_FILE = Path(__file__).parent / "app.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.ERROR,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def log_error(message):
    logging.error(message)

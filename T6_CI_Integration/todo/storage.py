import json
import os
from security.safe_io import validate_tasks_schema

# Always resolve path relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "tasks.json")


def _ensure_file_exists():
    """
    Ensure tasks.json exists.
    If missing or empty, initialize with empty dict.
    """
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump({}, file, indent=4)


def load_tasks():
    """
    Load and return validated task dictionary from disk.
    Raises RuntimeError if JSON is invalid.
    """
    _ensure_file_exists()

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        raise RuntimeError("tasks.json is corrupted or contains invalid JSON.")

    if not isinstance(data, dict):
        raise RuntimeError("tasks.json must contain a dictionary at root level.")

    # ✅ SECURITY HARDENING: validate schema safely
    return validate_tasks_schema(data)


def save_tasks(tasks):
    """
    Persist task dictionary to disk atomically.
    """
    if not isinstance(tasks, dict):
        raise ValueError("tasks must be a dictionary")

    temp_path = FILE_PATH + ".tmp"

    with open(temp_path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)

    os.replace(temp_path, FILE_PATH)

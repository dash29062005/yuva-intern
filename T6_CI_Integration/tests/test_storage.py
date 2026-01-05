import json
import os
import pytest
from todo import storage



def test_load_creates_file_if_missing(tmp_path, monkeypatch):
    """
    If tasks.json does not exist, it should be created
    and initialized as an empty dictionary.
    """
    fake_dir = tmp_path
    fake_file = fake_dir / "tasks.json"

    # Force storage.py to use temp directory
    monkeypatch.setattr(storage, "FILE_PATH", str(fake_file))

    data = storage.load_tasks()

    assert fake_file.exists()
    assert data == {}


def test_save_and_load_tasks(tmp_path, monkeypatch):
    """
    Saving tasks and loading them back should preserve data.
    """
    fake_file = tmp_path / "tasks.json"
    monkeypatch.setattr(storage, "FILE_PATH", str(fake_file))

    tasks = {
        "1": {
            "id": 1,
            "title": "Stored task",
            "priority": "mid",
            "status": "pending",
            "estimated_duration": None
        }
    }

    storage.save_tasks(tasks)
    loaded = storage.load_tasks()

    assert loaded == tasks


def test_corrupted_json_raises_error(tmp_path, monkeypatch):
    """
    Corrupted JSON file should raise RuntimeError.
    """
    fake_file = tmp_path / "tasks.json"
    monkeypatch.setattr(storage, "FILE_PATH", str(fake_file))

    with open(fake_file, "w") as f:
        f.write("{ invalid json }")

    with pytest.raises(RuntimeError):
        storage.load_tasks()

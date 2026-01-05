from todo import storage
from todo.task_manager import TaskManager


def test_add_save_reload_flow(tmp_path, monkeypatch):
    """
    Full integration test:
    add task -> save -> reload -> list
    """
    # Redirect storage to temporary file
    fake_file = tmp_path / "tasks.json"
    monkeypatch.setattr(storage, "FILE_PATH", str(fake_file))

    # Step 1: load empty storage
    raw_tasks = storage.load_tasks()
    manager = TaskManager(raw_tasks)

    # Step 2: add task
    task = manager.add_task("Integration task", priority="high")

    # Step 3: save to disk
    storage.save_tasks(manager.to_dict())

    # Step 4: reload from disk
    reloaded_data = storage.load_tasks()
    new_manager = TaskManager(reloaded_data)

    tasks = new_manager.list_tasks()

    assert len(tasks) == 1
    assert tasks[0].title == "Integration task"
    assert tasks[0].priority == "high"

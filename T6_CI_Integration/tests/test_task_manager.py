import pytest
from todo.task_manager import TaskManager


def test_add_task_assigns_incrementing_ids():
    manager = TaskManager()

    task1 = manager.add_task("Task one")
    task2 = manager.add_task("Task two")

    assert task1.id == 1
    assert task2.id == 2


def test_update_task_changes_only_specified_fields():
    manager = TaskManager()
    task = manager.add_task("Original title", priority="low")

    manager.update_task(task.id, priority="high")

    assert task.title == "Original title"
    assert task.priority == "high"


def test_update_non_existent_task_raises_error():
    manager = TaskManager()

    with pytest.raises(ValueError):
        manager.update_task(99, title="Does not exist")


def test_delete_task_removes_task():
    manager = TaskManager()
    task = manager.add_task("Temporary task")

    manager.delete_task(task.id)

    with pytest.raises(ValueError):
        manager.update_task(task.id, title="Should fail")


def test_complete_task_sets_status_completed():
    manager = TaskManager()
    task = manager.add_task("Finish report")

    manager.complete_task(task.id)

    assert task.status == "completed"

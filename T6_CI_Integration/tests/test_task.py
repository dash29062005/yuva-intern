import pytest
from todo.task import Task


def test_task_creation_with_valid_data():
    task = Task(1, "Read a book", priority="low")
    assert task.id == 1
    assert task.title == "Read a book"
    assert task.priority == "low"
    assert task.status == "pending"


def test_task_creation_with_empty_title_raises_error():
    with pytest.raises(ValueError):
        Task(1, "", priority="mid")


def test_task_creation_with_invalid_priority_raises_error():
    with pytest.raises(ValueError):
        Task(1, "Some task", priority="urgent")


def test_mark_task_complete_changes_status():
    task = Task(1, "Finish assignment")
    task.mark_complete()
    assert task.status == "completed"


def test_completed_task_cannot_be_updated():
    task = Task(1, "Initial title")
    task.mark_complete()

    with pytest.raises(ValueError):
        task.update_fields(title="New title")

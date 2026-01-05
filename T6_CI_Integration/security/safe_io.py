from todo.task import Task

def validate_tasks_schema(data):
    if not isinstance(data, dict):
        raise ValueError("Invalid tasks format.")

    valid_tasks = {}

    for key, value in data.items():
        try:
            task = Task.from_dict(value)
            valid_tasks[str(task.id)] = task.to_dict()
        except Exception:
            continue  # skip corrupted entries safely

    return valid_tasks

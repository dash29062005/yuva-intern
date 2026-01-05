from todo.task import Task


class TaskManager:
    """
    In-memory task manager.
    Business logic only. No I/O.
    """

    def __init__(self, tasks_dict=None):
        """
        tasks_dict: dict[str, dict] from storage
        """
        self.tasks = {}

        if tasks_dict:
            for key, value in tasks_dict.items():
                task = Task.from_dict(value)
                self.tasks[int(task.id)] = task

    # -------------------------------------------------------
    # Internal helpers
    # -------------------------------------------------------

    def _generate_next_id(self):
        if not self.tasks:
            return 1
        return max(self.tasks.keys()) + 1

    def _get_task(self, task_id):
        if not isinstance(task_id, int):
            raise ValueError("Task ID must be an integer.")

        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} does not exist.")

        return self.tasks[task_id]

    # -------------------------------------------------------
    # Core Operations
    # -------------------------------------------------------

    def add_task(self, title, priority="mid", estimated_duration=None):
        task_id = self._generate_next_id()

        task = Task(
            task_id=task_id,
            title=title,
            priority=priority,
            estimated_duration=estimated_duration
        )

        self.tasks[task_id] = task
        return task

    def update_task(self, task_id, title=None, priority=None, estimated_duration=None):
        task = self._get_task(task_id)

        task.update_fields(
            title=title,
            priority=priority,
            estimated_duration=estimated_duration
        )

        return task

    def delete_task(self, task_id):
        self._get_task(task_id)  # validation
        del self.tasks[task_id]

    def complete_task(self, task_id):
        task = self._get_task(task_id)
        task.mark_complete()
        return task

    def list_tasks(self, filter_status=None):
        """
        Returns tasks sorted by ID.
        """
        tasks = sorted(self.tasks.values(), key=lambda t: t.id)

        if filter_status:
            filter_status = filter_status.lower()
            tasks = [t for t in tasks if t.status == filter_status]

        return tasks

    # -------------------------------------------------------
    # Persistence helper
    # -------------------------------------------------------

    def to_dict(self):
        """
        Convert internal tasks to storage-safe dict.
        """
        return {
            str(task_id): task.to_dict()
            for task_id, task in self.tasks.items()
        }

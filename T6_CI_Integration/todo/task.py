from security.validators import validate_title


class Task:
    # -------------------------
    # Class-level constants
    # -------------------------
    VALID_PRIORITIES = {"low", "mid", "high"}
    VALID_STATUS = {"pending", "completed"}

    def __init__(self, task_id, title, priority="mid", status="pending", estimated_duration=None):
        """
        Represents ONE task.
        No CLI logic. No storage logic.
        """
        self.id = task_id

        # ✅ apply validated & sanitized value
        self.title = validate_title(title)

        self.priority = priority.lower() if isinstance(priority, str) else priority
        self.status = status.lower() if isinstance(status, str) else status
        self.estimated_duration = estimated_duration

        self._validate_priority()
        self._validate_status()
        self._validate_duration()

    # -------------------------
    # Validation methods
    # -------------------------

    def _validate_priority(self):
        if self.priority not in self.VALID_PRIORITIES:
            raise ValueError(
                f"Invalid priority '{self.priority}'. "
                f"Must be one of {', '.join(self.VALID_PRIORITIES)}."
            )

    def _validate_status(self):
        if self.status not in self.VALID_STATUS:
            raise ValueError(
                f"Invalid status '{self.status}'. "
                f"Must be one of {', '.join(self.VALID_STATUS)}."
            )

    def _validate_duration(self):
        if self.estimated_duration is not None and not isinstance(self.estimated_duration, str):
            raise ValueError("Estimated duration must be a string or None.")

    # -------------------------
    # Behavior methods
    # -------------------------

    def mark_complete(self):
        """
        Mark task as completed.
        Safe to call multiple times.
        """
        self.status = "completed"

    def update_fields(self, title=None, priority=None, estimated_duration=None):
        """
        Update selected fields of the task.
        Completed tasks are immutable.
        """
        if self.status == "completed":
            raise ValueError("Completed tasks cannot be modified.")

        if title is not None:
            # ✅ apply validated & sanitized value
            self.title = validate_title(title)

        if priority is not None:
            self.priority = priority.lower()
            self._validate_priority()

        if estimated_duration is not None:
            self.estimated_duration = estimated_duration
            self._validate_duration()

    # -------------------------
    # Serialization helpers
    # -------------------------

    def to_dict(self):
        """
        Convert Task object to a JSON-safe dictionary.
        """
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "status": self.status,
            "estimated_duration": self.estimated_duration,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a Task object from stored dictionary data.
        """
        return cls(
            task_id=data["id"],
            title=data["title"],
            priority=data.get("priority", "mid"),
            status=data.get("status", "pending"),
            estimated_duration=data.get("estimated_duration"),
        )

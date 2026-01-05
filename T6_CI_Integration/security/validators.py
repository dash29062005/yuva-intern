def validate_title(title: str) -> str:
    """
    Validate and sanitize task title.
    """
    if not isinstance(title, str):
        raise ValueError("Title must be a string.")

    title = title.strip()

    if not title:
        raise ValueError("Title cannot be empty.")

    if len(title) > 200:
        raise ValueError("Title is too long.")

    return title

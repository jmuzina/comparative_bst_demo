def safe_str_to_int(s: str) -> int:
    """Convert a string to an int, returning None if the string cannot be converted.

    Args:
        s (str): String to convert

    Returns:
        int: The converted string, or None if the string cannot be converted.
    """
    try:
        return int(s)
    except ValueError:
        return None
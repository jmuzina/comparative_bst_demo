def safe_str_to_int(s: str) -> int:
    try:
        return int(s)
    except ValueError:
        return None
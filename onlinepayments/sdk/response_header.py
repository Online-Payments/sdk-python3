from typing import Dict, Optional, Tuple


def get_header_value(headers: Dict[str, str], header_name: str) -> Optional[str]:
    """
    :return: The value of the header with the given name, or None if there was no such header.
    """
    if headers is None:
        return None
    for name, value in headers.items():
        if name.lower() == header_name.lower():
            return value
    return None


def get_header(headers: Dict[str, str], header_name: str) -> Optional[Tuple[str, str]]:
    """
    :return: The header with the given name as a tuple with the name and value, or None if there was no such header.
    """
    if headers is None:
        return None
    for name, value in headers.items():
        if name.lower() == header_name.lower():
            return name, value
    return None

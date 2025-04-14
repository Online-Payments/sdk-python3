from typing import Mapping, Optional, Sequence, Union


class RequestHeader(object):
    """
    A single request header. Immutable.
    """

    def __init__(self, name: str, value: Optional[str]):
        if name is None or not name.strip():
            raise ValueError("name is required")
        self.__name = name
        self.__value = value

    @property
    def name(self) -> str:
        """
        :return: The header name.
        """
        return self.__name

    @property
    def value(self) -> Optional[str]:
        """
        :return: The un-encoded value.
        """
        return self.__value.decode('utf-8') if isinstance(self.__value, bytes) else self.__value

    def __str__(self):
        return self.__name + ":" + str(self.__value)


def get_header_value(headers: Union[Sequence[RequestHeader], Mapping[str, str], None], header_name: str) -> Optional[str]:
    """
    :return: The value of the header with the given name, or None if there was no such header.
    """
    if isinstance(headers, dict):
        for name, value in headers.items():
            if name.lower() == header_name.lower():
                return value
    elif headers is not None:
        for header in headers:
            if header.name.lower() == header_name.lower():
                return header.value
    return None


def get_header(headers: Union[Sequence[RequestHeader], Mapping[str, str], None], header_name: str) -> Optional[RequestHeader]:
    """
    :return: The header with the given name, or None if there was no such header.
    """
    if isinstance(headers, dict):
        for name, value in headers.items():
            if name.lower() == header_name.lower():
                return RequestHeader(name, value)
    elif headers is not None:
        for header in headers:
            if header.name.lower() == header_name.lower():
                return header
    return None

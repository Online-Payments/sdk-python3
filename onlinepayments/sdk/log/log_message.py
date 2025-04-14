from abc import ABC, abstractmethod
from typing import List, Optional, Sequence, Tuple, Union

from .body_obfuscator import BodyObfuscator
from .header_obfuscator import HeaderObfuscator


class LogMessage(ABC):
    """
    A utility class to build log messages.
    """
    __request_id: str = None
    __headers: str = None
    __body: Optional[str] = None
    __content_type: Optional[str] = None
    __header_list: List[Tuple[str, str]] = None
    __body_obfuscator: BodyObfuscator = None
    __header_obfuscator: HeaderObfuscator = None

    def __init__(self, request_id: str,
                 body_obfuscator: BodyObfuscator = BodyObfuscator.default_body_obfuscator(),
                 header_obfuscator: HeaderObfuscator = HeaderObfuscator.default_header_obfuscator()):
        if not request_id:
            raise ValueError("request_id is required")
        if not body_obfuscator:
            raise ValueError("body_obfuscator is required")
        if not header_obfuscator:
            raise ValueError("header_obfuscator is required")
        self.__request_id = request_id
        self.__headers = ""
        self.__header_list = []
        self.__body_obfuscator = body_obfuscator
        self.__header_obfuscator = header_obfuscator

    @property
    def request_id(self) -> str:
        return self.__request_id

    @property
    def headers(self) -> str:
        return str(self.__headers)

    @property
    def body(self) -> Optional[str]:
        return self.__body

    @property
    def content_type(self) -> Optional[str]:
        return self.__content_type

    def add_header(self, name: str, value: Optional[str]) -> None:
        if self.__headers:
            self.__headers += ", "
        self.__headers += name + "=\""
        if value is not None and value.lower() != 'none':
            obfuscated_value = self.__header_obfuscator.obfuscate_header(name, value)
            self.__headers += obfuscated_value
            self.__header_list.append((name, "\"" + obfuscated_value + "\""))
        else:
            self.__header_list.append((name, "\"\""))
        self.__headers += "\""

    def set_body(self, body: Union[str, bytes, None], content_type: Optional[str], charset: Optional[str] = None) -> None:
        self.__content_type = content_type
        if self.__is_binary(content_type):
            self.__body = "<binary content>"
        else:
            self.__body = self.__body_obfuscator.obfuscate_body(body, charset)

    def set_binary_body(self, content_type: Optional[str]) -> None:
        if not self.__is_binary(content_type):
            raise ValueError("Not a binary content type: " + content_type)
        self.__content_type = content_type
        self.__body = "<binary content>"

    @staticmethod
    def __is_binary(content_type: Optional[str]) -> bool:
        if content_type is None:
            return False
        content_type = content_type.lower()
        return not (content_type.startswith("text/") or "json" in content_type or "xml" in content_type)

    @staticmethod
    def empty_if_none(value: Optional[str]) -> str:
        if value is not None:
            return value
        return ""

    @abstractmethod
    def get_message(self) -> str:
        raise NotImplementedError

    def get_header_list(self) -> Sequence[Tuple[str, str]]:
        return self.__header_list

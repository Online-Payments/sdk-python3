from typing import Optional


class RequestParam(object):
    """
    A single request parameter. Immutable.
    """

    def __init__(self, name: str, value: Optional[str]):
        if name is None or not name.strip():
            raise ValueError("name is required")
        self.__name = name
        self.__value = value

    @property
    def name(self) -> str:
        """
        :return: The parameter name.
        """
        return self.__name

    @property
    def value(self) -> Optional[str]:
        """
        :return: The un-encoded value.
        """
        return self.__value

    def __str__(self):
        return self.name + ":" + self.value

from abc import ABC, abstractmethod

from .body_obfuscator import BodyObfuscator
from .header_obfuscator import HeaderObfuscator


class ObfuscationCapable(ABC):
    """
    Classes that extend this class support obfuscating bodies and headers.
    """

    @abstractmethod
    def set_body_obfuscator(self, body_obfuscator: BodyObfuscator) -> None:
        """
        Sets the current body obfuscator to use.
        """
        raise NotImplementedError

    @abstractmethod
    def set_header_obfuscator(self, header_obfuscator: HeaderObfuscator) -> None:
        """
        Sets the current header obfuscator to use.
        """
        raise NotImplementedError

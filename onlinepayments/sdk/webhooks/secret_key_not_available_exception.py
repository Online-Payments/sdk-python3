from typing import Optional

from .signature_validation_exception import SignatureValidationException


class SecretKeyNotAvailableException(SignatureValidationException):
    """
    Represents an error that causes a secret key to not be available.
    """

    def __init__(self, key_id: str, message: Optional[str] = None, cause: Optional[Exception] = None):
        super(SecretKeyNotAvailableException, self).__init__(message=message,
                                                             cause=cause)
        self.__key_id = key_id

    @property
    def key_id(self) -> str:
        return self.__key_id

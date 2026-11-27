#
# This file was automatically generated.
#
from .data_object import DataObject


class ValidateCredentialsRequest(DataObject):

    __slots__ = (
        "__key",
        "__secret",
    )

    __key: str | None
    __secret: str | None

    def __init__(
        self,
        *,
        key: str | None = None,
        secret: str | None = None,
    ) -> None:
        self.key = key
        self.secret = secret

    @property
    def key(self) -> str | None:
        """
        | The webhook key and without any change applied to it.

        Type: str
        """
        return self.__key

    @key.setter
    def key(self, value: str | None) -> None:
        self.__key = value

    @property
    def secret(self) -> str | None:
        """
        | Send here the hashed webhooks key secret in the same way as the check is done in your system. The only difference is instead of providing the current body of the message, use an empty string as body while hashing it.

        Type: str
        """
        return self.__secret

    @secret.setter
    def secret(self, value: str | None) -> None:
        self.__secret = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.key is not None:
            dictionary['key'] = self.key
        if self.secret is not None:
            dictionary['secret'] = self.secret
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ValidateCredentialsRequest':
        super().from_dictionary(dictionary)
        if 'key' in dictionary:
            self.key = dictionary['key']
        if 'secret' in dictionary:
            self.secret = dictionary['secret']
        return self

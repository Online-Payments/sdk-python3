# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class ValidateCredentialsRequest(DataObject):

    __key: Optional[str] = None
    __secret: Optional[str] = None

    @property
    def key(self) -> Optional[str]:
        """
        | The webhook key and without any change applied to it.

        Type: str
        """
        return self.__key

    @key.setter
    def key(self, value: Optional[str]) -> None:
        self.__key = value

    @property
    def secret(self) -> Optional[str]:
        """
        | Send here the hashed webhooks key secret in the same way as the check is done in your system. The only difference is instead of providing the current body of the message, use an empty string as body while hashing it.

        Type: str
        """
        return self.__secret

    @secret.setter
    def secret(self, value: Optional[str]) -> None:
        self.__secret = value

    def to_dictionary(self) -> dict:
        dictionary = super(ValidateCredentialsRequest, self).to_dictionary()
        if self.key is not None:
            dictionary['key'] = self.key
        if self.secret is not None:
            dictionary['secret'] = self.secret
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ValidateCredentialsRequest':
        super(ValidateCredentialsRequest, self).from_dictionary(dictionary)
        if 'key' in dictionary:
            self.key = dictionary['key']
        if 'secret' in dictionary:
            self.secret = dictionary['secret']
        return self

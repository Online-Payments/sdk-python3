# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class SessionDetails(DataObject):

    __id: Optional[str] = None
    __type: Optional[str] = None

    @property
    def id(self) -> Optional[str]:
        """
        | Session identifier from where this payment originates from. Depends on the session type: ex: For PayByLink: id is the corresponding paymentLinkId.

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: Optional[str]) -> None:
        self.__id = value

    @property
    def type(self) -> Optional[str]:
        """
        | Session type. This denotes the origin of the session. For example PayByLink, HostedTokenization, etc.

        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value: Optional[str]) -> None:
        self.__type = value

    def to_dictionary(self) -> dict:
        dictionary = super(SessionDetails, self).to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.type is not None:
            dictionary['type'] = self.type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SessionDetails':
        super(SessionDetails, self).from_dictionary(dictionary)
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'type' in dictionary:
            self.type = dictionary['type']
        return self

# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from datetime import datetime
from typing import Optional

from .data_object import DataObject


class Acceptance(DataObject):

    __acceptance_system_application_id: Optional[str] = None
    __authorization_date: Optional[datetime] = None
    __authorization_message_reference: Optional[str] = None

    @property
    def acceptance_system_application_id(self) -> Optional[str]:
        """
        | Worldline application identifier used to transmit the authorization request. This data is transmitted as provided in the authorization request and in the response. It is named ITP (Terminal Application Identification at the Point of Acceptance) in the CB2A protocol.

        Type: str
        """
        return self.__acceptance_system_application_id

    @acceptance_system_application_id.setter
    def acceptance_system_application_id(self, value: Optional[str]) -> None:
        self.__acceptance_system_application_id = value

    @property
    def authorization_date(self) -> Optional[datetime]:
        """
        | It is the authorization processing date and time of the transaction.

        Type: datetime
        """
        return self.__authorization_date

    @authorization_date.setter
    def authorization_date(self, value: Optional[datetime]) -> None:
        self.__authorization_date = value

    @property
    def authorization_message_reference(self) -> Optional[str]:
        """
        | Identifier shared with the acquirer during the authorization process. For example, this reference data could be sent by the acquirer in the authorization response, then sent (unchanged) in a subsequent authorization reversal message, to the extent that the acquirer is able to match a reversal message to the associated response message.

        Type: str
        """
        return self.__authorization_message_reference

    @authorization_message_reference.setter
    def authorization_message_reference(self, value: Optional[str]) -> None:
        self.__authorization_message_reference = value

    def to_dictionary(self) -> dict:
        dictionary = super(Acceptance, self).to_dictionary()
        if self.acceptance_system_application_id is not None:
            dictionary['acceptanceSystemApplicationId'] = self.acceptance_system_application_id
        if self.authorization_date is not None:
            dictionary['authorizationDate'] = DataObject.format_datetime(self.authorization_date)
        if self.authorization_message_reference is not None:
            dictionary['authorizationMessageReference'] = self.authorization_message_reference
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'Acceptance':
        super(Acceptance, self).from_dictionary(dictionary)
        if 'acceptanceSystemApplicationId' in dictionary:
            self.acceptance_system_application_id = dictionary['acceptanceSystemApplicationId']
        if 'authorizationDate' in dictionary:
            self.authorization_date = DataObject.parse_datetime(dictionary['authorizationDate'])
        if 'authorizationMessageReference' in dictionary:
            self.authorization_message_reference = dictionary['authorizationMessageReference']
        return self

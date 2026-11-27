#
# This file was automatically generated.
#
from datetime import datetime

from .data_object import DataObject


class Acceptance(DataObject):

    __slots__ = (
        "__acceptance_system_application_id",
        "__authorization_date",
        "__authorization_message_reference",
    )

    __acceptance_system_application_id: str | None
    __authorization_date: datetime | None
    __authorization_message_reference: str | None

    def __init__(
        self,
        *,
        acceptance_system_application_id: str | None = None,
        authorization_date: datetime | None = None,
        authorization_message_reference: str | None = None,
    ) -> None:
        self.acceptance_system_application_id = acceptance_system_application_id
        self.authorization_date = authorization_date
        self.authorization_message_reference = authorization_message_reference

    @property
    def acceptance_system_application_id(self) -> str | None:
        """
        | Worldline application identifier used to transmit the authorization request. This data is transmitted as provided in the authorization request and in the response. It is named ITP (Terminal Application Identification at the Point of Acceptance) in the CB2A protocol.

        Type: str
        """
        return self.__acceptance_system_application_id

    @acceptance_system_application_id.setter
    def acceptance_system_application_id(self, value: str | None) -> None:
        self.__acceptance_system_application_id = value

    @property
    def authorization_date(self) -> datetime | None:
        """
        | It is the authorization processing date and time of the transaction.

        Type: datetime
        """
        return self.__authorization_date

    @authorization_date.setter
    def authorization_date(self, value: datetime | None) -> None:
        self.__authorization_date = value

    @property
    def authorization_message_reference(self) -> str | None:
        """
        | Identifier shared with the acquirer during the authorization process. For example, this reference data could be sent by the acquirer in the authorization response, then sent (unchanged) in a subsequent authorization reversal message, to the extent that the acquirer is able to match a reversal message to the associated response message.

        Type: str
        """
        return self.__authorization_message_reference

    @authorization_message_reference.setter
    def authorization_message_reference(self, value: str | None) -> None:
        self.__authorization_message_reference = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.acceptance_system_application_id is not None:
            dictionary['acceptanceSystemApplicationId'] = self.acceptance_system_application_id
        if self.authorization_date is not None:
            dictionary['authorizationDate'] = DataObject.format_datetime(self.authorization_date)
        if self.authorization_message_reference is not None:
            dictionary['authorizationMessageReference'] = self.authorization_message_reference
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'Acceptance':
        super().from_dictionary(dictionary)
        if 'acceptanceSystemApplicationId' in dictionary:
            self.acceptance_system_application_id = dictionary['acceptanceSystemApplicationId']
        if 'authorizationDate' in dictionary:
            self.authorization_date = DataObject.parse_datetime(dictionary['authorizationDate'])
        if 'authorizationMessageReference' in dictionary:
            self.authorization_message_reference = dictionary['authorizationMessageReference']
        return self

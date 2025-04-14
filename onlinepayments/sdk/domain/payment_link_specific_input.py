# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from datetime import datetime
from typing import Optional

from .data_object import DataObject


class PaymentLinkSpecificInput(DataObject):

    __description: Optional[str] = None
    __expiration_date: Optional[datetime] = None
    __recipient_name: Optional[str] = None

    @property
    def description(self) -> Optional[str]:
        """
        | A note related to the created payment link.

        Type: str
        """
        return self.__description

    @description.setter
    def description(self, value: Optional[str]) -> None:
        self.__description = value

    @property
    def expiration_date(self) -> Optional[datetime]:
        """
        | The date after which the payment link will not be usable to complete the payment. The date sent cannot be more than 6 months in the future or a past date. It must also contain the UTC offset.

        Type: datetime
        """
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value: Optional[datetime]) -> None:
        self.__expiration_date = value

    @property
    def recipient_name(self) -> Optional[str]:
        """
        | The payment link recipient name.

        Type: str
        """
        return self.__recipient_name

    @recipient_name.setter
    def recipient_name(self, value: Optional[str]) -> None:
        self.__recipient_name = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentLinkSpecificInput, self).to_dictionary()
        if self.description is not None:
            dictionary['description'] = self.description
        if self.expiration_date is not None:
            dictionary['expirationDate'] = DataObject.format_datetime(self.expiration_date)
        if self.recipient_name is not None:
            dictionary['recipientName'] = self.recipient_name
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentLinkSpecificInput':
        super(PaymentLinkSpecificInput, self).from_dictionary(dictionary)
        if 'description' in dictionary:
            self.description = dictionary['description']
        if 'expirationDate' in dictionary:
            self.expiration_date = DataObject.parse_datetime(dictionary['expirationDate'])
        if 'recipientName' in dictionary:
            self.recipient_name = dictionary['recipientName']
        return self

# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class PaymentLinkEvent(DataObject):
    """
    | Changes related to a payment link status or usage.
    """

    __date_time = None
    __details = None
    __type = None

    @property
    def date_time(self) -> str:
        """
        | The date and time the change occurred. The date will contain the UTC offset.

        Type: str
        """
        return self.__date_time

    @date_time.setter
    def date_time(self, value: str):
        self.__date_time = value

    @property
    def details(self) -> str:
        """
        | Details of the events. Ex.: email address or phone number of the recipient.

        Type: str
        """
        return self.__details

    @details.setter
    def details(self, value: str):
        self.__details = value

    @property
    def type(self) -> str:
        """
        | The type of event that occurred.

        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value: str):
        self.__type = value

    def to_dictionary(self):
        dictionary = super(PaymentLinkEvent, self).to_dictionary()
        if self.date_time is not None:
            dictionary['dateTime'] = self.date_time
        if self.details is not None:
            dictionary['details'] = self.details
        if self.type is not None:
            dictionary['type'] = self.type
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentLinkEvent, self).from_dictionary(dictionary)
        if 'dateTime' in dictionary:
            self.date_time = dictionary['dateTime']
        if 'details' in dictionary:
            self.details = dictionary['details']
        if 'type' in dictionary:
            self.type = dictionary['type']
        return self

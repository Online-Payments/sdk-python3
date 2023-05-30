# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney


class Transaction(DataObject):
    __amount = None
    __local_date_time = None

    @property
    def amount(self) -> AmountOfMoney:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount

    @amount.setter
    def amount(self, value: AmountOfMoney):
        self.__amount = value

    @property
    def local_date_time(self) -> str:
        """
        | This must be the DateTime of the buyer's browser
        | Entered in the following format: YYYY-MM-DDTHH:MM:SS. If the timestamp is more than a day (86400 seconds) away from the current time, the request will be rejected

        Type: str
        """
        return self.__local_date_time

    @local_date_time.setter
    def local_date_time(self, value: str):
        self.__local_date_time = value

    def to_dictionary(self):
        dictionary = super(Transaction, self).to_dictionary()
        if self.amount is not None:
            dictionary['amount'] = self.amount.to_dictionary()
        if self.local_date_time is not None:
            dictionary['localDateTime'] = self.local_date_time
        return dictionary

    def from_dictionary(self, dictionary):
        super(Transaction, self).from_dictionary(dictionary)
        if 'amount' in dictionary:
            if not isinstance(dictionary['amount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amount']))
            value = AmountOfMoney()
            self.amount = value.from_dictionary(dictionary['amount'])
        if 'localDateTime' in dictionary:
            self.local_date_time = dictionary['localDateTime']
        return self

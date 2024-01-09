# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class Discount(DataObject):
    """
    | Object to apply a discount to the total basket by adding a discount line.
    """

    __amount = None

    @property
    def amount(self) -> int:
        """
        | Amount in the smallest currency unit, i.e.:
        
        | * EUR is a 2-decimals currency, the value 1234 will result in EUR 12.34
        
        | * KWD is a 3-decimals currency, the value 1234 will result in KWD 1.234
        
        | * JPY is a zero-decimal currency, the value 1234 will result in JPY 1234

        Type: int
        """
        return self.__amount

    @amount.setter
    def amount(self, value: int):
        self.__amount = value

    def to_dictionary(self):
        dictionary = super(Discount, self).to_dictionary()
        if self.amount is not None:
            dictionary['amount'] = self.amount
        return dictionary

    def from_dictionary(self, dictionary):
        super(Discount, self).from_dictionary(dictionary)
        if 'amount' in dictionary:
            self.amount = dictionary['amount']
        return self

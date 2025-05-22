# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .amount_of_money import AmountOfMoney
from .data_object import DataObject


class SurchargeSpecificInput(DataObject):

    __mode: Optional[str] = None
    __surcharge_amount: Optional[AmountOfMoney] = None

    @property
    def mode(self) -> Optional[str]:
        """
        | The surcharge mode which defines how a merchant will apply surcharging.
        
        * pass-through - Merchant to define and apply surcharge amount for a transaction for processing. This mode is not supported on Create Hosted Checkout Session.
        * on-behalf-of - Merchant to instruct the payment platform to calculate and apply a surcharge amount to a transaction, based on the merchant’s surcharge configuration, net amount, and payment product type.

        Type: str
        """
        return self.__mode

    @mode.setter
    def mode(self, value: Optional[str]) -> None:
        self.__mode = value

    @property
    def surcharge_amount(self) -> Optional[AmountOfMoney]:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__surcharge_amount

    @surcharge_amount.setter
    def surcharge_amount(self, value: Optional[AmountOfMoney]) -> None:
        self.__surcharge_amount = value

    def to_dictionary(self) -> dict:
        dictionary = super(SurchargeSpecificInput, self).to_dictionary()
        if self.mode is not None:
            dictionary['mode'] = self.mode
        if self.surcharge_amount is not None:
            dictionary['surchargeAmount'] = self.surcharge_amount.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SurchargeSpecificInput':
        super(SurchargeSpecificInput, self).from_dictionary(dictionary)
        if 'mode' in dictionary:
            self.mode = dictionary['mode']
        if 'surchargeAmount' in dictionary:
            if not isinstance(dictionary['surchargeAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['surchargeAmount']))
            value = AmountOfMoney()
            self.surcharge_amount = value.from_dictionary(dictionary['surchargeAmount'])
        return self

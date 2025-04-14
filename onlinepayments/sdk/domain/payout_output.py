# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .amount_of_money import AmountOfMoney
from .data_object import DataObject


class PayoutOutput(DataObject):

    __amount_of_money: Optional[AmountOfMoney] = None
    __payout_reason: Optional[str] = None

    @property
    def amount_of_money(self) -> Optional[AmountOfMoney]:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value: Optional[AmountOfMoney]) -> None:
        self.__amount_of_money = value

    @property
    def payout_reason(self) -> Optional[str]:
        """
        | Allows you to additionally specify the reason for initiating the payout for authorization purposes. If this field is not specified, authorisation of the payment will be made according to your merchant profile. Possible values are:
        
        * Gambling
        * Refund
        * Loyalty

        Type: str
        """
        return self.__payout_reason

    @payout_reason.setter
    def payout_reason(self, value: Optional[str]) -> None:
        self.__payout_reason = value

    def to_dictionary(self) -> dict:
        dictionary = super(PayoutOutput, self).to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.payout_reason is not None:
            dictionary['payoutReason'] = self.payout_reason
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PayoutOutput':
        super(PayoutOutput, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'payoutReason' in dictionary:
            self.payout_reason = dictionary['payoutReason']
        return self

# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .amount_of_money import AmountOfMoney
from .data_object import DataObject
from .surcharge_rate import SurchargeRate


class Surcharge(DataObject):

    __net_amount: Optional[AmountOfMoney] = None
    __payment_product_id: Optional[int] = None
    __result: Optional[str] = None
    __surcharge_amount: Optional[AmountOfMoney] = None
    __surcharge_rate: Optional[SurchargeRate] = None
    __total_amount: Optional[AmountOfMoney] = None

    @property
    def net_amount(self) -> Optional[AmountOfMoney]:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__net_amount

    @net_amount.setter
    def net_amount(self, value: Optional[AmountOfMoney]) -> None:
        self.__net_amount = value

    @property
    def payment_product_id(self) -> Optional[int]:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: Optional[int]) -> None:
        self.__payment_product_id = value

    @property
    def result(self) -> Optional[str]:
        """
        | Token describing result. OK - A Surcharge Amount was successfully calculated, NO_SURCHARGE - A configured surcharge rate could not be found for the payment product

        Type: str
        """
        return self.__result

    @result.setter
    def result(self, value: Optional[str]) -> None:
        self.__result = value

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

    @property
    def surcharge_rate(self) -> Optional[SurchargeRate]:
        """
        | A summary of surcharge details used in the calculation of the surcharge amount. null if result = NO_SURCHARGE

        Type: :class:`onlinepayments.sdk.domain.surcharge_rate.SurchargeRate`
        """
        return self.__surcharge_rate

    @surcharge_rate.setter
    def surcharge_rate(self, value: Optional[SurchargeRate]) -> None:
        self.__surcharge_rate = value

    @property
    def total_amount(self) -> Optional[AmountOfMoney]:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value: Optional[AmountOfMoney]) -> None:
        self.__total_amount = value

    def to_dictionary(self) -> dict:
        dictionary = super(Surcharge, self).to_dictionary()
        if self.net_amount is not None:
            dictionary['netAmount'] = self.net_amount.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        if self.result is not None:
            dictionary['result'] = self.result
        if self.surcharge_amount is not None:
            dictionary['surchargeAmount'] = self.surcharge_amount.to_dictionary()
        if self.surcharge_rate is not None:
            dictionary['surchargeRate'] = self.surcharge_rate.to_dictionary()
        if self.total_amount is not None:
            dictionary['totalAmount'] = self.total_amount.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'Surcharge':
        super(Surcharge, self).from_dictionary(dictionary)
        if 'netAmount' in dictionary:
            if not isinstance(dictionary['netAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['netAmount']))
            value = AmountOfMoney()
            self.net_amount = value.from_dictionary(dictionary['netAmount'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'result' in dictionary:
            self.result = dictionary['result']
        if 'surchargeAmount' in dictionary:
            if not isinstance(dictionary['surchargeAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['surchargeAmount']))
            value = AmountOfMoney()
            self.surcharge_amount = value.from_dictionary(dictionary['surchargeAmount'])
        if 'surchargeRate' in dictionary:
            if not isinstance(dictionary['surchargeRate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['surchargeRate']))
            value = SurchargeRate()
            self.surcharge_rate = value.from_dictionary(dictionary['surchargeRate'])
        if 'totalAmount' in dictionary:
            if not isinstance(dictionary['totalAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['totalAmount']))
            value = AmountOfMoney()
            self.total_amount = value.from_dictionary(dictionary['totalAmount'])
        return self

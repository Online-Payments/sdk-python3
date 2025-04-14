# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .order import Order
from .subsequent_card_payment_method_specific_input import SubsequentCardPaymentMethodSpecificInput
from .subsequent_payment_product5001_specific_input import SubsequentPaymentProduct5001SpecificInput


class SubsequentPaymentRequest(DataObject):

    __order: Optional[Order] = None
    __subsequent_payment_product5001_specific_input: Optional[SubsequentPaymentProduct5001SpecificInput] = None
    __subsequentcard_payment_method_specific_input: Optional[SubsequentCardPaymentMethodSpecificInput] = None

    @property
    def order(self) -> Optional[Order]:
        """
        | Order object containing order related data Please note that this object is required to be able to submit the amount.

        Type: :class:`onlinepayments.sdk.domain.order.Order`
        """
        return self.__order

    @order.setter
    def order(self, value: Optional[Order]) -> None:
        self.__order = value

    @property
    def subsequent_payment_product5001_specific_input(self) -> Optional[SubsequentPaymentProduct5001SpecificInput]:
        """
        | specific data required for Bizum subsequent payment

        Type: :class:`onlinepayments.sdk.domain.subsequent_payment_product5001_specific_input.SubsequentPaymentProduct5001SpecificInput`
        """
        return self.__subsequent_payment_product5001_specific_input

    @subsequent_payment_product5001_specific_input.setter
    def subsequent_payment_product5001_specific_input(self, value: Optional[SubsequentPaymentProduct5001SpecificInput]) -> None:
        self.__subsequent_payment_product5001_specific_input = value

    @property
    def subsequentcard_payment_method_specific_input(self) -> Optional[SubsequentCardPaymentMethodSpecificInput]:
        """
        | Object containing the specific input details for subsequent card payments

        Type: :class:`onlinepayments.sdk.domain.subsequent_card_payment_method_specific_input.SubsequentCardPaymentMethodSpecificInput`
        """
        return self.__subsequentcard_payment_method_specific_input

    @subsequentcard_payment_method_specific_input.setter
    def subsequentcard_payment_method_specific_input(self, value: Optional[SubsequentCardPaymentMethodSpecificInput]) -> None:
        self.__subsequentcard_payment_method_specific_input = value

    def to_dictionary(self) -> dict:
        dictionary = super(SubsequentPaymentRequest, self).to_dictionary()
        if self.order is not None:
            dictionary['order'] = self.order.to_dictionary()
        if self.subsequent_payment_product5001_specific_input is not None:
            dictionary['subsequentPaymentProduct5001SpecificInput'] = self.subsequent_payment_product5001_specific_input.to_dictionary()
        if self.subsequentcard_payment_method_specific_input is not None:
            dictionary['subsequentcardPaymentMethodSpecificInput'] = self.subsequentcard_payment_method_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SubsequentPaymentRequest':
        super(SubsequentPaymentRequest, self).from_dictionary(dictionary)
        if 'order' in dictionary:
            if not isinstance(dictionary['order'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['order']))
            value = Order()
            self.order = value.from_dictionary(dictionary['order'])
        if 'subsequentPaymentProduct5001SpecificInput' in dictionary:
            if not isinstance(dictionary['subsequentPaymentProduct5001SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['subsequentPaymentProduct5001SpecificInput']))
            value = SubsequentPaymentProduct5001SpecificInput()
            self.subsequent_payment_product5001_specific_input = value.from_dictionary(dictionary['subsequentPaymentProduct5001SpecificInput'])
        if 'subsequentcardPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['subsequentcardPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['subsequentcardPaymentMethodSpecificInput']))
            value = SubsequentCardPaymentMethodSpecificInput()
            self.subsequentcard_payment_method_specific_input = value.from_dictionary(dictionary['subsequentcardPaymentMethodSpecificInput'])
        return self

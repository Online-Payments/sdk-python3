# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.order import Order
from onlinepayments.sdk.domain.subsequent_card_payment_method_specific_input import SubsequentCardPaymentMethodSpecificInput
from onlinepayments.sdk.domain.subsequent_payment_product5001_specific_input import SubsequentPaymentProduct5001SpecificInput


class SubsequentPaymentRequest(DataObject):
    __order = None
    __subsequent_payment_product5001_specific_input = None
    __subsequentcard_payment_method_specific_input = None

    @property
    def order(self) -> Order:
        """
        | Order object containing order related data 
        |  Please note that this object is required to be able to submit the amount.

        Type: :class:`onlinepayments.sdk.domain.order.Order`
        """
        return self.__order

    @order.setter
    def order(self, value: Order):
        self.__order = value

    @property
    def subsequent_payment_product5001_specific_input(self) -> SubsequentPaymentProduct5001SpecificInput:
        """
        | specific data required for Bizum subsequent payment

        Type: :class:`onlinepayments.sdk.domain.subsequent_payment_product5001_specific_input.SubsequentPaymentProduct5001SpecificInput`
        """
        return self.__subsequent_payment_product5001_specific_input

    @subsequent_payment_product5001_specific_input.setter
    def subsequent_payment_product5001_specific_input(self, value: SubsequentPaymentProduct5001SpecificInput):
        self.__subsequent_payment_product5001_specific_input = value

    @property
    def subsequentcard_payment_method_specific_input(self) -> SubsequentCardPaymentMethodSpecificInput:
        """
        | Object containing the specific input details for subsequent card payments

        Type: :class:`onlinepayments.sdk.domain.subsequent_card_payment_method_specific_input.SubsequentCardPaymentMethodSpecificInput`
        """
        return self.__subsequentcard_payment_method_specific_input

    @subsequentcard_payment_method_specific_input.setter
    def subsequentcard_payment_method_specific_input(self, value: SubsequentCardPaymentMethodSpecificInput):
        self.__subsequentcard_payment_method_specific_input = value

    def to_dictionary(self):
        dictionary = super(SubsequentPaymentRequest, self).to_dictionary()
        if self.order is not None:
            dictionary['order'] = self.order.to_dictionary()
        if self.subsequent_payment_product5001_specific_input is not None:
            dictionary['subsequentPaymentProduct5001SpecificInput'] = self.subsequent_payment_product5001_specific_input.to_dictionary()
        if self.subsequentcard_payment_method_specific_input is not None:
            dictionary['subsequentcardPaymentMethodSpecificInput'] = self.subsequentcard_payment_method_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
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

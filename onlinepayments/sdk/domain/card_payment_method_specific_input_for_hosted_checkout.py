# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from typing import List

from onlinepayments.sdk.data_object import DataObject


class CardPaymentMethodSpecificInputForHostedCheckout(DataObject):
    """
    | Object containing card payment specific data for hosted checkout
    """

    __click_to_pay = None
    __group_cards = None
    __payment_product_preferred_order = None

    @property
    def click_to_pay(self) -> bool:
        """
        | * true - Hosted Checkout will show Click to Pay, with cards grouped as one payment method
        | * false - Default - Hosted Checkout will show cards as separate payment methods without Click to Pay

        Type: bool
        """
        return self.__click_to_pay

    @click_to_pay.setter
    def click_to_pay(self, value: bool):
        self.__click_to_pay = value

    @property
    def group_cards(self) -> bool:
        """
        | * true - Hosted Checkout will allow to show cards grouped as one payment method
        | * false - Default - Hosted Checkout will show cards as separate payment methods

        Type: bool
        """
        return self.__group_cards

    @group_cards.setter
    def group_cards(self, value: bool):
        self.__group_cards = value

    @property
    def payment_product_preferred_order(self) -> List[int]:
        """
        | This array contains the payment product identifiers representing the brands. For co-badged cards, this displays their available brands in the order defined by this array, when groupCards is activated.

        Type: list[int]
        """
        return self.__payment_product_preferred_order

    @payment_product_preferred_order.setter
    def payment_product_preferred_order(self, value: List[int]):
        self.__payment_product_preferred_order = value

    def to_dictionary(self):
        dictionary = super(CardPaymentMethodSpecificInputForHostedCheckout, self).to_dictionary()
        if self.click_to_pay is not None:
            dictionary['clickToPay'] = self.click_to_pay
        if self.group_cards is not None:
            dictionary['groupCards'] = self.group_cards
        if self.payment_product_preferred_order is not None:
            dictionary['paymentProductPreferredOrder'] = []
            for element in self.payment_product_preferred_order:
                if element is not None:
                    dictionary['paymentProductPreferredOrder'].append(element)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardPaymentMethodSpecificInputForHostedCheckout, self).from_dictionary(dictionary)
        if 'clickToPay' in dictionary:
            self.click_to_pay = dictionary['clickToPay']
        if 'groupCards' in dictionary:
            self.group_cards = dictionary['groupCards']
        if 'paymentProductPreferredOrder' in dictionary:
            if not isinstance(dictionary['paymentProductPreferredOrder'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['paymentProductPreferredOrder']))
            self.payment_product_preferred_order = []
            for element in dictionary['paymentProductPreferredOrder']:
                self.payment_product_preferred_order.append(element)
        return self

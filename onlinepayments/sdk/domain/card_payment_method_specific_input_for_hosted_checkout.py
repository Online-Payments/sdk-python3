# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class CardPaymentMethodSpecificInputForHostedCheckout(DataObject):
    """
    | Object containing card payment specific data for hosted checkout
    """

    __group_cards = None

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

    def to_dictionary(self):
        dictionary = super(CardPaymentMethodSpecificInputForHostedCheckout, self).to_dictionary()
        if self.group_cards is not None:
            dictionary['groupCards'] = self.group_cards
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardPaymentMethodSpecificInputForHostedCheckout, self).from_dictionary(dictionary)
        if 'groupCards' in dictionary:
            self.group_cards = dictionary['groupCards']
        return self

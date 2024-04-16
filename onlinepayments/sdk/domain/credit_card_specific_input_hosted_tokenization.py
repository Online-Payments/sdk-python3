# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from typing import List

from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.credit_card_validation_rules_hosted_tokenization import CreditCardValidationRulesHostedTokenization


class CreditCardSpecificInputHostedTokenization(DataObject):
    __validation_rules = None
    __payment_product_preferred_order = None

    @property
    def validation_rules(self) -> CreditCardValidationRulesHostedTokenization:
        """
        Type: :class:`onlinepayments.sdk.domain.credit_card_validation_rules_hosted_tokenization.CreditCardValidationRulesHostedTokenization`
        """
        return self.__validation_rules

    @validation_rules.setter
    def validation_rules(self, value: CreditCardValidationRulesHostedTokenization):
        self.__validation_rules = value

    @property
    def payment_product_preferred_order(self) -> List[int]:
        """
        | This array contains the payment product identifiers representing the brands. For co-badged cards, this displays their available brands in the order defined by this array.

        Type: list[int]
        """
        return self.__payment_product_preferred_order

    @payment_product_preferred_order.setter
    def payment_product_preferred_order(self, value: List[int]):
        self.__payment_product_preferred_order = value

    def to_dictionary(self):
        dictionary = super(CreditCardSpecificInputHostedTokenization, self).to_dictionary()
        if self.validation_rules is not None:
            dictionary['ValidationRules'] = self.validation_rules.to_dictionary()
        if self.payment_product_preferred_order is not None:
            dictionary['paymentProductPreferredOrder'] = []
            for element in self.payment_product_preferred_order:
                if element is not None:
                    dictionary['paymentProductPreferredOrder'].append(element)
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreditCardSpecificInputHostedTokenization, self).from_dictionary(dictionary)
        if 'ValidationRules' in dictionary:
            if not isinstance(dictionary['ValidationRules'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['ValidationRules']))
            value = CreditCardValidationRulesHostedTokenization()
            self.validation_rules = value.from_dictionary(dictionary['ValidationRules'])
        if 'paymentProductPreferredOrder' in dictionary:
            if not isinstance(dictionary['paymentProductPreferredOrder'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['paymentProductPreferredOrder']))
            self.payment_product_preferred_order = []
            for element in dictionary['paymentProductPreferredOrder']:
                self.payment_product_preferred_order.append(element)
        return self

# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .credit_card_validation_rules_hosted_tokenization import CreditCardValidationRulesHostedTokenization
from .data_object import DataObject


class CreditCardSpecificInputHostedTokenization(DataObject):

    __validation_rules: Optional[CreditCardValidationRulesHostedTokenization] = None
    __payment_product_preferred_order: Optional[List[int]] = None

    @property
    def validation_rules(self) -> Optional[CreditCardValidationRulesHostedTokenization]:
        """
        Type: :class:`onlinepayments.sdk.domain.credit_card_validation_rules_hosted_tokenization.CreditCardValidationRulesHostedTokenization`
        """
        return self.__validation_rules

    @validation_rules.setter
    def validation_rules(self, value: Optional[CreditCardValidationRulesHostedTokenization]) -> None:
        self.__validation_rules = value

    @property
    def payment_product_preferred_order(self) -> Optional[List[int]]:
        """
        | This array contains the payment product identifiers representing the brands. For co-badged cards, this displays their available brands in the order defined by this array.

        Type: list[int]
        """
        return self.__payment_product_preferred_order

    @payment_product_preferred_order.setter
    def payment_product_preferred_order(self, value: Optional[List[int]]) -> None:
        self.__payment_product_preferred_order = value

    def to_dictionary(self) -> dict:
        dictionary = super(CreditCardSpecificInputHostedTokenization, self).to_dictionary()
        if self.validation_rules is not None:
            dictionary['ValidationRules'] = self.validation_rules.to_dictionary()
        if self.payment_product_preferred_order is not None:
            dictionary['paymentProductPreferredOrder'] = []
            for element in self.payment_product_preferred_order:
                if element is not None:
                    dictionary['paymentProductPreferredOrder'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreditCardSpecificInputHostedTokenization':
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

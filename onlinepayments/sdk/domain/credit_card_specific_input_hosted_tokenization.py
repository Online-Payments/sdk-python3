# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.credit_card_validation_rules_hosted_tokenization import CreditCardValidationRulesHostedTokenization


class CreditCardSpecificInputHostedTokenization(DataObject):
    __validation_rules = None

    @property
    def validation_rules(self) -> CreditCardValidationRulesHostedTokenization:
        """
        Type: :class:`onlinepayments.sdk.domain.credit_card_validation_rules_hosted_tokenization.CreditCardValidationRulesHostedTokenization`
        """
        return self.__validation_rules

    @validation_rules.setter
    def validation_rules(self, value: CreditCardValidationRulesHostedTokenization):
        self.__validation_rules = value

    def to_dictionary(self):
        dictionary = super(CreditCardSpecificInputHostedTokenization, self).to_dictionary()
        if self.validation_rules is not None:
            dictionary['ValidationRules'] = self.validation_rules.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreditCardSpecificInputHostedTokenization, self).from_dictionary(dictionary)
        if 'ValidationRules' in dictionary:
            if not isinstance(dictionary['ValidationRules'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['ValidationRules']))
            value = CreditCardValidationRulesHostedTokenization()
            self.validation_rules = value.from_dictionary(dictionary['ValidationRules'])
        return self

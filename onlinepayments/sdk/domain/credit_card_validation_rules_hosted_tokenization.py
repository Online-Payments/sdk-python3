# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class CreditCardValidationRulesHostedTokenization(DataObject):

    __cvv_mandatory_for_existing_token: Optional[bool] = None
    __cvv_mandatory_for_new_token: Optional[bool] = None

    @property
    def cvv_mandatory_for_existing_token(self) -> Optional[bool]:
        """
        | Determines whether the Card Verification Value must be provided for existing tokens. This option overrides the payment method configuration for the session.

        Type: bool
        """
        return self.__cvv_mandatory_for_existing_token

    @cvv_mandatory_for_existing_token.setter
    def cvv_mandatory_for_existing_token(self, value: Optional[bool]) -> None:
        self.__cvv_mandatory_for_existing_token = value

    @property
    def cvv_mandatory_for_new_token(self) -> Optional[bool]:
        """
        | Determines whether the Card Verification Value must be provided for new tokens. This option overrides the payment method configuration for the session.

        Type: bool
        """
        return self.__cvv_mandatory_for_new_token

    @cvv_mandatory_for_new_token.setter
    def cvv_mandatory_for_new_token(self, value: Optional[bool]) -> None:
        self.__cvv_mandatory_for_new_token = value

    def to_dictionary(self) -> dict:
        dictionary = super(CreditCardValidationRulesHostedTokenization, self).to_dictionary()
        if self.cvv_mandatory_for_existing_token is not None:
            dictionary['cvvMandatoryForExistingToken'] = self.cvv_mandatory_for_existing_token
        if self.cvv_mandatory_for_new_token is not None:
            dictionary['cvvMandatoryForNewToken'] = self.cvv_mandatory_for_new_token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreditCardValidationRulesHostedTokenization':
        super(CreditCardValidationRulesHostedTokenization, self).from_dictionary(dictionary)
        if 'cvvMandatoryForExistingToken' in dictionary:
            self.cvv_mandatory_for_existing_token = dictionary['cvvMandatoryForExistingToken']
        if 'cvvMandatoryForNewToken' in dictionary:
            self.cvv_mandatory_for_new_token = dictionary['cvvMandatoryForNewToken']
        return self

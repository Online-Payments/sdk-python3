# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class CrmToken(DataObject):

    __unique_account_identifier: Optional[str] = None
    __unique_card_identifier: Optional[str] = None

    @property
    def unique_account_identifier(self) -> Optional[str]:
        """
        | A unique identifier that remains constant across different formats of the same card (whether used via wallets such as Apple Pay, Google Pay, etc., or the physical card), even if the tokenID may differ. The unique account identifier cannot be used to trigger a payment.

        Type: str
        """
        return self.__unique_account_identifier

    @unique_account_identifier.setter
    def unique_account_identifier(self, value: Optional[str]) -> None:
        self.__unique_account_identifier = value

    @property
    def unique_card_identifier(self) -> Optional[str]:
        """
        | A unique identifier for the card that was tokenized. This identifier remains the same for a given card, even if the tokenID may differ. The unique card identifier cannot be used to trigger a payment.

        Type: str
        """
        return self.__unique_card_identifier

    @unique_card_identifier.setter
    def unique_card_identifier(self, value: Optional[str]) -> None:
        self.__unique_card_identifier = value

    def to_dictionary(self) -> dict:
        dictionary = super(CrmToken, self).to_dictionary()
        if self.unique_account_identifier is not None:
            dictionary['uniqueAccountIdentifier'] = self.unique_account_identifier
        if self.unique_card_identifier is not None:
            dictionary['uniqueCardIdentifier'] = self.unique_card_identifier
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CrmToken':
        super(CrmToken, self).from_dictionary(dictionary)
        if 'uniqueAccountIdentifier' in dictionary:
            self.unique_account_identifier = dictionary['uniqueAccountIdentifier']
        if 'uniqueCardIdentifier' in dictionary:
            self.unique_card_identifier = dictionary['uniqueCardIdentifier']
        return self

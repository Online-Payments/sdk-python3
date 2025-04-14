# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class OrderTypeInformation(DataObject):

    __purchase_type: Optional[str] = None
    __transaction_type: Optional[str] = None

    @property
    def purchase_type(self) -> Optional[str]:
        """
        | Possible values are:
        
        * physical (tangible goods shipped to the customers)
        * digital (digital services like ebooks, streaming...)

        Type: str
        """
        return self.__purchase_type

    @purchase_type.setter
    def purchase_type(self, value: Optional[str]) -> None:
        self.__purchase_type = value

    @property
    def transaction_type(self) -> Optional[str]:
        """
        | Identifies the type of transaction being authenticated. Possible values are:
        
        * purchase = The purpose of the transaction is to purchase goods or services (Default)
        * check-acceptance = The purpose of the transaction is to accept a 'check'/'cheque'
        * account-funding = The purpose of the transaction is to fund an account
        * quasi-cash = The purpose of the transaction is to buy a quasi cash type product that is representative of actual cash such as money orders, traveler's checks, foreign currency, lottery tickets or casino gaming chips
        * prepaid-activation-or-load = The purpose of the transaction is to activate or load a prepaid card

        Type: str
        """
        return self.__transaction_type

    @transaction_type.setter
    def transaction_type(self, value: Optional[str]) -> None:
        self.__transaction_type = value

    def to_dictionary(self) -> dict:
        dictionary = super(OrderTypeInformation, self).to_dictionary()
        if self.purchase_type is not None:
            dictionary['purchaseType'] = self.purchase_type
        if self.transaction_type is not None:
            dictionary['transactionType'] = self.transaction_type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'OrderTypeInformation':
        super(OrderTypeInformation, self).from_dictionary(dictionary)
        if 'purchaseType' in dictionary:
            self.purchase_type = dictionary['purchaseType']
        if 'transactionType' in dictionary:
            self.transaction_type = dictionary['transactionType']
        return self

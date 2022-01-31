# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class OrderTypeInformation(DataObject):
    """
    | Object that holds the purchase and usage type indicators
    """

    __purchase_type = None
    __transaction_type = None

    @property
    def purchase_type(self) -> str:
        """
        | Possible values are:
        | * physical (tangible goods shipped to the customers)
        | * digital (digital services like ebooks, streaming...)

        Type: str
        """
        return self.__purchase_type

    @purchase_type.setter
    def purchase_type(self, value: str):
        self.__purchase_type = value

    @property
    def transaction_type(self) -> str:
        """
        | Identifies the type of transaction being authenticated. Possible values are:
        | * purchase = The purpose of the transaction is to purchase goods or services (Default)
        | * check-acceptance = The purpose of the transaction is to accept a 'check'/'cheque'
        | * account-funding = The purpose of the transaction is to fund an account
        | * quasi-cash = The purpose of the transaction is to buy a quasi cash type product that is representative of actual cash such as money orders, traveler's checks, foreign currency, lottery tickets or casino gaming chips
        | * prepaid-activation-or-load = The purpose of the transaction is to activate or load a prepaid card

        Type: str
        """
        return self.__transaction_type

    @transaction_type.setter
    def transaction_type(self, value: str):
        self.__transaction_type = value

    def to_dictionary(self):
        dictionary = super(OrderTypeInformation, self).to_dictionary()
        if self.purchase_type is not None:
            dictionary['purchaseType'] = self.purchase_type
        if self.transaction_type is not None:
            dictionary['transactionType'] = self.transaction_type
        return dictionary

    def from_dictionary(self, dictionary):
        super(OrderTypeInformation, self).from_dictionary(dictionary)
        if 'purchaseType' in dictionary:
            self.purchase_type = dictionary['purchaseType']
        if 'transactionType' in dictionary:
            self.transaction_type = dictionary['transactionType']
        return self

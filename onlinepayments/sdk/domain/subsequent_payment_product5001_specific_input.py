# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class SubsequentPaymentProduct5001SpecificInput(DataObject):

    __authorization_mode: Optional[str] = None
    __subsequent_type: Optional[str] = None

    @property
    def authorization_mode(self) -> Optional[str]:
        """
        | Determines the type of the authorization that will be used. Allowed values:
        
        * FINAL_AUTHORIZATION - The payment creation results in an authorization that is ready for capture. Final authorizations can't be reversed and need to be captured for the full amount within 7 days.
        * SALE - The payment creation results in an authorization that is already captured at the moment of approval

        Type: str
        """
        return self.__authorization_mode

    @authorization_mode.setter
    def authorization_mode(self, value: Optional[str]) -> None:
        self.__authorization_mode = value

    @property
    def subsequent_type(self) -> Optional[str]:
        """
        | Determines the type of the subsequent that will be used. Allowed values:
        
        * recurring - Transactions processed at fixed, regular intervals not to exceed one year between Transactions, representing an agreement between a consumer and a merchant to purchase goods or services provided over a period of time. Note that a recurring MIT transaction is initiated by the merchant (payee) not the customer (payer) and so is out of scope of PSD2. Recurring transactions that are in scope of PSD2 (and therefore may benefit from the recurring transaction exemption) are those that are customer (payer) initiates, e.g. standing orders set up from a bank account.
        * installment - Installment payments describe a single purchase of goods or services billed to a consumer in multiple transactions over a period of time agreed by the consumer and merchant.
        * other - other cases

        Type: str
        """
        return self.__subsequent_type

    @subsequent_type.setter
    def subsequent_type(self, value: Optional[str]) -> None:
        self.__subsequent_type = value

    def to_dictionary(self) -> dict:
        dictionary = super(SubsequentPaymentProduct5001SpecificInput, self).to_dictionary()
        if self.authorization_mode is not None:
            dictionary['authorizationMode'] = self.authorization_mode
        if self.subsequent_type is not None:
            dictionary['subsequentType'] = self.subsequent_type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SubsequentPaymentProduct5001SpecificInput':
        super(SubsequentPaymentProduct5001SpecificInput, self).from_dictionary(dictionary)
        if 'authorizationMode' in dictionary:
            self.authorization_mode = dictionary['authorizationMode']
        if 'subsequentType' in dictionary:
            self.subsequent_type = dictionary['subsequentType']
        return self

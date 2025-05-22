# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class RedirectPaymentProduct5001SpecificInput(DataObject):

    __exemption_request: Optional[str] = None
    __subsequent_type: Optional[str] = None

    @property
    def exemption_request(self) -> Optional[str]:
        """
        | In PSD2, the ExemptionRequest field is used by merchants requesting an exemption when not using authentication on a transaction, in order to keep the conversion up. This field indicates the reason for the authentication exemption request. Allowed values:
        
        * low-value - The transaction amount is below the 30€, with a maximum of 5 transactions or €100 accumulated per customer.
        * transaction-risk-analysis - The transaction has been assessed as low risk by the merchant's fraud prevention system.

        Type: str
        """
        return self.__exemption_request

    @exemption_request.setter
    def exemption_request(self, value: Optional[str]) -> None:
        self.__exemption_request = value

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
        dictionary = super(RedirectPaymentProduct5001SpecificInput, self).to_dictionary()
        if self.exemption_request is not None:
            dictionary['exemptionRequest'] = self.exemption_request
        if self.subsequent_type is not None:
            dictionary['subsequentType'] = self.subsequent_type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct5001SpecificInput':
        super(RedirectPaymentProduct5001SpecificInput, self).from_dictionary(dictionary)
        if 'exemptionRequest' in dictionary:
            self.exemption_request = dictionary['exemptionRequest']
        if 'subsequentType' in dictionary:
            self.subsequent_type = dictionary['subsequentType']
        return self

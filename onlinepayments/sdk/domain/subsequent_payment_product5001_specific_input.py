# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class SubsequentPaymentProduct5001SpecificInput(DataObject):
    """
    | specific data required for Bizum subsequent payment
    """

    __subsequent_type = None

    @property
    def subsequent_type(self) -> str:
        """
        | Determines the type of the subsequent that will be used. Allowed values: 
        |   * recurring - Transactions processed at fixed, regular intervals not to exceed one year between Transactions, representing an agreement between a consumer and a merchant to purchase goods or services provided over a period of time. Note that a recurring MIT transaction is initiated by the merchant (payee) not the customer (payer) and so is out of scope of PSD2. Recurring transactions that are in scope of PSD2 (and therefore may benefit from the recurring transaction exemption) are those that are customer (payer) initiates, e.g. standing orders set up from a bank account. 
        |   * installment - Installment payments describe a single purchase of goods or services billed to a consumer in multiple transactions over a period of time agreed by the consumer and merchant. 
        |   * other - other cases

        Type: str
        """
        return self.__subsequent_type

    @subsequent_type.setter
    def subsequent_type(self, value: str):
        self.__subsequent_type = value

    def to_dictionary(self):
        dictionary = super(SubsequentPaymentProduct5001SpecificInput, self).to_dictionary()
        if self.subsequent_type is not None:
            dictionary['subsequentType'] = self.subsequent_type
        return dictionary

    def from_dictionary(self, dictionary):
        super(SubsequentPaymentProduct5001SpecificInput, self).from_dictionary(dictionary)
        if 'subsequentType' in dictionary:
            self.subsequent_type = dictionary['subsequentType']
        return self

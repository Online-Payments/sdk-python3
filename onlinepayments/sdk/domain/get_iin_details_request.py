# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.payment_context import PaymentContext


class GetIINDetailsRequest(DataObject):
    """
    | Input for the retrieval of the IIN details request
    """

    __bin = None
    __payment_context = None

    @property
    def bin(self) -> str:
        """
        | The first digits of the credit card number from left to right with a minimum of 6 digits. Providing additional digits can result in more co-brands being returned.

        Type: str
        """
        return self.__bin

    @bin.setter
    def bin(self, value: str):
        self.__bin = value

    @property
    def payment_context(self) -> PaymentContext:
        """
        Type: :class:`onlinepayments.sdk.domain.payment_context.PaymentContext`
        """
        return self.__payment_context

    @payment_context.setter
    def payment_context(self, value: PaymentContext):
        self.__payment_context = value

    def to_dictionary(self):
        dictionary = super(GetIINDetailsRequest, self).to_dictionary()
        if self.bin is not None:
            dictionary['bin'] = self.bin
        if self.payment_context is not None:
            dictionary['paymentContext'] = self.payment_context.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(GetIINDetailsRequest, self).from_dictionary(dictionary)
        if 'bin' in dictionary:
            self.bin = dictionary['bin']
        if 'paymentContext' in dictionary:
            if not isinstance(dictionary['paymentContext'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentContext']))
            value = PaymentContext()
            self.payment_context = value.from_dictionary(dictionary['paymentContext'])
        return self

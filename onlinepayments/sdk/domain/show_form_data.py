# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.payment_product5404 import PaymentProduct5404


class ShowFormData(DataObject):
    """
    | Object returned for the SHOW_FORM actionType.
    """

    __payment_product5404 = None

    @property
    def payment_product5404(self) -> PaymentProduct5404:
        """
        | Contains the third party data for payment product 5404 (WeChat Pay)

        Type: :class:`onlinepayments.sdk.domain.payment_product5404.PaymentProduct5404`
        """
        return self.__payment_product5404

    @payment_product5404.setter
    def payment_product5404(self, value: PaymentProduct5404):
        self.__payment_product5404 = value

    def to_dictionary(self):
        dictionary = super(ShowFormData, self).to_dictionary()
        if self.payment_product5404 is not None:
            dictionary['paymentProduct5404'] = self.payment_product5404.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(ShowFormData, self).from_dictionary(dictionary)
        if 'paymentProduct5404' in dictionary:
            if not isinstance(dictionary['paymentProduct5404'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct5404']))
            value = PaymentProduct5404()
            self.payment_product5404 = value.from_dictionary(dictionary['paymentProduct5404'])
        return self

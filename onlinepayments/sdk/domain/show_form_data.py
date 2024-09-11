# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.payment_product3012 import PaymentProduct3012
from onlinepayments.sdk.domain.payment_product5404 import PaymentProduct5404
from onlinepayments.sdk.domain.payment_product5407 import PaymentProduct5407


class ShowFormData(DataObject):
    """
    | Object returned for the SHOW_FORM actionType.
    """

    __payment_product3012 = None
    __payment_product5404 = None
    __payment_product5407 = None

    @property
    def payment_product3012(self) -> PaymentProduct3012:
        """
        | Contains the third party data for payment product 3012 (Bancontact)

        Type: :class:`onlinepayments.sdk.domain.payment_product3012.PaymentProduct3012`
        """
        return self.__payment_product3012

    @payment_product3012.setter
    def payment_product3012(self, value: PaymentProduct3012):
        self.__payment_product3012 = value

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

    @property
    def payment_product5407(self) -> PaymentProduct5407:
        """
        | Contains the third party data for payment product 5407 (Twint)

        Type: :class:`onlinepayments.sdk.domain.payment_product5407.PaymentProduct5407`
        """
        return self.__payment_product5407

    @payment_product5407.setter
    def payment_product5407(self, value: PaymentProduct5407):
        self.__payment_product5407 = value

    def to_dictionary(self):
        dictionary = super(ShowFormData, self).to_dictionary()
        if self.payment_product3012 is not None:
            dictionary['paymentProduct3012'] = self.payment_product3012.to_dictionary()
        if self.payment_product5404 is not None:
            dictionary['paymentProduct5404'] = self.payment_product5404.to_dictionary()
        if self.payment_product5407 is not None:
            dictionary['paymentProduct5407'] = self.payment_product5407.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(ShowFormData, self).from_dictionary(dictionary)
        if 'paymentProduct3012' in dictionary:
            if not isinstance(dictionary['paymentProduct3012'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct3012']))
            value = PaymentProduct3012()
            self.payment_product3012 = value.from_dictionary(dictionary['paymentProduct3012'])
        if 'paymentProduct5404' in dictionary:
            if not isinstance(dictionary['paymentProduct5404'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct5404']))
            value = PaymentProduct5404()
            self.payment_product5404 = value.from_dictionary(dictionary['paymentProduct5404'])
        if 'paymentProduct5407' in dictionary:
            if not isinstance(dictionary['paymentProduct5407'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct5407']))
            value = PaymentProduct5407()
            self.payment_product5407 = value.from_dictionary(dictionary['paymentProduct5407'])
        return self

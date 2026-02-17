# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .payment_product3012 import PaymentProduct3012
from .payment_product350 import PaymentProduct350
from .payment_product5001 import PaymentProduct5001
from .payment_product5404 import PaymentProduct5404
from .payment_product5407 import PaymentProduct5407
from .payment_product840 import PaymentProduct840
from .pending_authentication import PendingAuthentication


class ShowFormData(DataObject):

    __payment_product3012: Optional[PaymentProduct3012] = None
    __payment_product350: Optional[PaymentProduct350] = None
    __payment_product5001: Optional[PaymentProduct5001] = None
    __payment_product5404: Optional[PaymentProduct5404] = None
    __payment_product5407: Optional[PaymentProduct5407] = None
    __payment_product840: Optional[PaymentProduct840] = None
    __pending_authentication: Optional[PendingAuthentication] = None

    @property
    def payment_product3012(self) -> Optional[PaymentProduct3012]:
        """
        | Contains the third party data for payment product 3012 (Bancontact)

        Type: :class:`onlinepayments.sdk.domain.payment_product3012.PaymentProduct3012`
        """
        return self.__payment_product3012

    @payment_product3012.setter
    def payment_product3012(self, value: Optional[PaymentProduct3012]) -> None:
        self.__payment_product3012 = value

    @property
    def payment_product350(self) -> Optional[PaymentProduct350]:
        """
        | Contains the third party data for payment product 350 (Swish)

        Type: :class:`onlinepayments.sdk.domain.payment_product350.PaymentProduct350`
        """
        return self.__payment_product350

    @payment_product350.setter
    def payment_product350(self, value: Optional[PaymentProduct350]) -> None:
        self.__payment_product350 = value

    @property
    def payment_product5001(self) -> Optional[PaymentProduct5001]:
        """
        | Deprecated by pendingAuthentication. Contains the third party data for payment product 5001 (Bizum)

        Type: :class:`onlinepayments.sdk.domain.payment_product5001.PaymentProduct5001`
        """
        return self.__payment_product5001

    @payment_product5001.setter
    def payment_product5001(self, value: Optional[PaymentProduct5001]) -> None:
        self.__payment_product5001 = value

    @property
    def payment_product5404(self) -> Optional[PaymentProduct5404]:
        """
        | Contains the third party data for payment product 5404 (WeChat Pay)

        Type: :class:`onlinepayments.sdk.domain.payment_product5404.PaymentProduct5404`
        """
        return self.__payment_product5404

    @payment_product5404.setter
    def payment_product5404(self, value: Optional[PaymentProduct5404]) -> None:
        self.__payment_product5404 = value

    @property
    def payment_product5407(self) -> Optional[PaymentProduct5407]:
        """
        | Contains the third party data for payment product 5407 (Twint)

        Type: :class:`onlinepayments.sdk.domain.payment_product5407.PaymentProduct5407`
        """
        return self.__payment_product5407

    @payment_product5407.setter
    def payment_product5407(self, value: Optional[PaymentProduct5407]) -> None:
        self.__payment_product5407 = value

    @property
    def payment_product840(self) -> Optional[PaymentProduct840]:
        """
        | Contains the third party data for payment product 840 (PayPal)

        Type: :class:`onlinepayments.sdk.domain.payment_product840.PaymentProduct840`
        """
        return self.__payment_product840

    @payment_product840.setter
    def payment_product840(self, value: Optional[PaymentProduct840]) -> None:
        self.__payment_product840 = value

    @property
    def pending_authentication(self) -> Optional[PendingAuthentication]:
        """
        | Contains the third party data for payment product requiring an external authentication (e.g., Bizum, CV Connect)

        Type: :class:`onlinepayments.sdk.domain.pending_authentication.PendingAuthentication`
        """
        return self.__pending_authentication

    @pending_authentication.setter
    def pending_authentication(self, value: Optional[PendingAuthentication]) -> None:
        self.__pending_authentication = value

    def to_dictionary(self) -> dict:
        dictionary = super(ShowFormData, self).to_dictionary()
        if self.payment_product3012 is not None:
            dictionary['paymentProduct3012'] = self.payment_product3012.to_dictionary()
        if self.payment_product350 is not None:
            dictionary['paymentProduct350'] = self.payment_product350.to_dictionary()
        if self.payment_product5001 is not None:
            dictionary['paymentProduct5001'] = self.payment_product5001.to_dictionary()
        if self.payment_product5404 is not None:
            dictionary['paymentProduct5404'] = self.payment_product5404.to_dictionary()
        if self.payment_product5407 is not None:
            dictionary['paymentProduct5407'] = self.payment_product5407.to_dictionary()
        if self.payment_product840 is not None:
            dictionary['paymentProduct840'] = self.payment_product840.to_dictionary()
        if self.pending_authentication is not None:
            dictionary['pendingAuthentication'] = self.pending_authentication.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ShowFormData':
        super(ShowFormData, self).from_dictionary(dictionary)
        if 'paymentProduct3012' in dictionary:
            if not isinstance(dictionary['paymentProduct3012'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct3012']))
            value = PaymentProduct3012()
            self.payment_product3012 = value.from_dictionary(dictionary['paymentProduct3012'])
        if 'paymentProduct350' in dictionary:
            if not isinstance(dictionary['paymentProduct350'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct350']))
            value = PaymentProduct350()
            self.payment_product350 = value.from_dictionary(dictionary['paymentProduct350'])
        if 'paymentProduct5001' in dictionary:
            if not isinstance(dictionary['paymentProduct5001'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct5001']))
            value = PaymentProduct5001()
            self.payment_product5001 = value.from_dictionary(dictionary['paymentProduct5001'])
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
        if 'paymentProduct840' in dictionary:
            if not isinstance(dictionary['paymentProduct840'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct840']))
            value = PaymentProduct840()
            self.payment_product840 = value.from_dictionary(dictionary['paymentProduct840'])
        if 'pendingAuthentication' in dictionary:
            if not isinstance(dictionary['pendingAuthentication'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['pendingAuthentication']))
            value = PendingAuthentication()
            self.pending_authentication = value.from_dictionary(dictionary['pendingAuthentication'])
        return self

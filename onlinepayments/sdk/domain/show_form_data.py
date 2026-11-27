#
# This file was automatically generated.
#
from .data_object import DataObject
from .payment_product11 import PaymentProduct11
from .payment_product3012 import PaymentProduct3012
from .payment_product350 import PaymentProduct350
from .payment_product5001 import PaymentProduct5001
from .payment_product5404 import PaymentProduct5404
from .payment_product5407 import PaymentProduct5407
from .payment_product5412 import PaymentProduct5412
from .payment_product840 import PaymentProduct840
from .pending_authentication import PendingAuthentication


class ShowFormData(DataObject):

    __slots__ = (
        "__payment_product11",
        "__payment_product3012",
        "__payment_product350",
        "__payment_product5001",
        "__payment_product5404",
        "__payment_product5407",
        "__payment_product5412",
        "__payment_product840",
        "__pending_authentication",
    )

    __payment_product11: PaymentProduct11 | None
    __payment_product3012: PaymentProduct3012 | None
    __payment_product350: PaymentProduct350 | None
    __payment_product5001: PaymentProduct5001 | None
    __payment_product5404: PaymentProduct5404 | None
    __payment_product5407: PaymentProduct5407 | None
    __payment_product5412: PaymentProduct5412 | None
    __payment_product840: PaymentProduct840 | None
    __pending_authentication: PendingAuthentication | None

    def __init__(
        self,
        *,
        payment_product11: PaymentProduct11 | None = None,
        payment_product3012: PaymentProduct3012 | None = None,
        payment_product350: PaymentProduct350 | None = None,
        payment_product5001: PaymentProduct5001 | None = None,
        payment_product5404: PaymentProduct5404 | None = None,
        payment_product5407: PaymentProduct5407 | None = None,
        payment_product5412: PaymentProduct5412 | None = None,
        payment_product840: PaymentProduct840 | None = None,
        pending_authentication: PendingAuthentication | None = None,
    ) -> None:
        self.payment_product11 = payment_product11
        self.payment_product3012 = payment_product3012
        self.payment_product350 = payment_product350
        self.payment_product5001 = payment_product5001
        self.payment_product5404 = payment_product5404
        self.payment_product5407 = payment_product5407
        self.payment_product5412 = payment_product5412
        self.payment_product840 = payment_product840
        self.pending_authentication = pending_authentication

    @property
    def payment_product11(self) -> PaymentProduct11 | None:
        """
        | Contains the third party data for payment product 11 (Offline Bank transfer)

        Type: :class:`onlinepayments.sdk.domain.payment_product11.PaymentProduct11`
        """
        return self.__payment_product11

    @payment_product11.setter
    def payment_product11(self, value: PaymentProduct11 | None) -> None:
        self.__payment_product11 = value

    @property
    def payment_product3012(self) -> PaymentProduct3012 | None:
        """
        | Contains the third party data for payment product 3012 (Bancontact)

        Type: :class:`onlinepayments.sdk.domain.payment_product3012.PaymentProduct3012`
        """
        return self.__payment_product3012

    @payment_product3012.setter
    def payment_product3012(self, value: PaymentProduct3012 | None) -> None:
        self.__payment_product3012 = value

    @property
    def payment_product350(self) -> PaymentProduct350 | None:
        """
        | Contains the third party data for payment product 350 (Swish)

        Type: :class:`onlinepayments.sdk.domain.payment_product350.PaymentProduct350`
        """
        return self.__payment_product350

    @payment_product350.setter
    def payment_product350(self, value: PaymentProduct350 | None) -> None:
        self.__payment_product350 = value

    @property
    def payment_product5001(self) -> PaymentProduct5001 | None:
        """
        | Deprecated by pendingAuthentication. Contains the third party data for payment product 5001 (Bizum)

        Type: :class:`onlinepayments.sdk.domain.payment_product5001.PaymentProduct5001`
        """
        return self.__payment_product5001

    @payment_product5001.setter
    def payment_product5001(self, value: PaymentProduct5001 | None) -> None:
        self.__payment_product5001 = value

    @property
    def payment_product5404(self) -> PaymentProduct5404 | None:
        """
        | Contains the third party data for payment product 5404 (WeChat Pay)

        Type: :class:`onlinepayments.sdk.domain.payment_product5404.PaymentProduct5404`
        """
        return self.__payment_product5404

    @payment_product5404.setter
    def payment_product5404(self, value: PaymentProduct5404 | None) -> None:
        self.__payment_product5404 = value

    @property
    def payment_product5407(self) -> PaymentProduct5407 | None:
        """
        | Contains the third party data for payment product 5407 (Twint)

        Type: :class:`onlinepayments.sdk.domain.payment_product5407.PaymentProduct5407`
        """
        return self.__payment_product5407

    @payment_product5407.setter
    def payment_product5407(self, value: PaymentProduct5407 | None) -> None:
        self.__payment_product5407 = value

    @property
    def payment_product5412(self) -> PaymentProduct5412 | None:
        """
        | Contains the third party data for payment product 5412 (Chèque-Vacances Connect)

        Type: :class:`onlinepayments.sdk.domain.payment_product5412.PaymentProduct5412`
        """
        return self.__payment_product5412

    @payment_product5412.setter
    def payment_product5412(self, value: PaymentProduct5412 | None) -> None:
        self.__payment_product5412 = value

    @property
    def payment_product840(self) -> PaymentProduct840 | None:
        """
        | Contains the third party data for payment product 840 (PayPal)

        Type: :class:`onlinepayments.sdk.domain.payment_product840.PaymentProduct840`
        """
        return self.__payment_product840

    @payment_product840.setter
    def payment_product840(self, value: PaymentProduct840 | None) -> None:
        self.__payment_product840 = value

    @property
    def pending_authentication(self) -> PendingAuthentication | None:
        """
        | Contains the third party data for payment product requiring an external authentication (e.g., Bizum, CV Connect)

        Type: :class:`onlinepayments.sdk.domain.pending_authentication.PendingAuthentication`
        """
        return self.__pending_authentication

    @pending_authentication.setter
    def pending_authentication(self, value: PendingAuthentication | None) -> None:
        self.__pending_authentication = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.payment_product11 is not None:
            dictionary['paymentProduct11'] = self.payment_product11.to_dictionary()
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
        if self.payment_product5412 is not None:
            dictionary['paymentProduct5412'] = self.payment_product5412.to_dictionary()
        if self.payment_product840 is not None:
            dictionary['paymentProduct840'] = self.payment_product840.to_dictionary()
        if self.pending_authentication is not None:
            dictionary['pendingAuthentication'] = self.pending_authentication.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ShowFormData':
        super().from_dictionary(dictionary)
        if 'paymentProduct11' in dictionary:
            if not isinstance(dictionary['paymentProduct11'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct11']))
            value = PaymentProduct11()
            self.payment_product11 = value.from_dictionary(dictionary['paymentProduct11'])
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
        if 'paymentProduct5412' in dictionary:
            if not isinstance(dictionary['paymentProduct5412'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct5412']))
            value = PaymentProduct5412()
            self.payment_product5412 = value.from_dictionary(dictionary['paymentProduct5412'])
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

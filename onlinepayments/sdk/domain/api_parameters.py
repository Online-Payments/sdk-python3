#
# This file was automatically generated.
#
from .amex import Amex
from .data_object import DataObject
from .mastercard import Mastercard
from .payment_product5002default_brand_parameters import PaymentProduct5002defaultBrandParameters
from .visa import Visa


class ApiParameters(DataObject):

    __slots__ = (
        "__amex",
        "__cb",
        "__eftpos",
        "__mastercard",
        "__visa",
    )

    __amex: Amex | None
    __cb: PaymentProduct5002defaultBrandParameters | None
    __eftpos: PaymentProduct5002defaultBrandParameters | None
    __mastercard: Mastercard | None
    __visa: Visa | None

    def __init__(
        self,
        *,
        amex: Amex | None = None,
        cb: PaymentProduct5002defaultBrandParameters | None = None,
        eftpos: PaymentProduct5002defaultBrandParameters | None = None,
        mastercard: Mastercard | None = None,
        visa: Visa | None = None,
    ) -> None:
        self.amex = amex
        self.cb = cb
        self.eftpos = eftpos
        self.mastercard = mastercard
        self.visa = visa

    @property
    def amex(self) -> Amex | None:
        """
        | The following fields need to be provided to the amex field within the configuration.

        Type: :class:`onlinepayments.sdk.domain.amex.Amex`
        """
        return self.__amex

    @amex.setter
    def amex(self, value: Amex | None) -> None:
        self.__amex = value

    @property
    def cb(self) -> PaymentProduct5002defaultBrandParameters | None:
        """
        | The following fields need to be provided to the cb field within the configuration.

        Type: :class:`onlinepayments.sdk.domain.payment_product5002default_brand_parameters.PaymentProduct5002defaultBrandParameters`
        """
        return self.__cb

    @cb.setter
    def cb(self, value: PaymentProduct5002defaultBrandParameters | None) -> None:
        self.__cb = value

    @property
    def eftpos(self) -> PaymentProduct5002defaultBrandParameters | None:
        """
        | The following fields need to be provided to the eftpos field within the configuration.

        Type: :class:`onlinepayments.sdk.domain.payment_product5002default_brand_parameters.PaymentProduct5002defaultBrandParameters`
        """
        return self.__eftpos

    @eftpos.setter
    def eftpos(self, value: PaymentProduct5002defaultBrandParameters | None) -> None:
        self.__eftpos = value

    @property
    def mastercard(self) -> Mastercard | None:
        """
        | The following fields need to be provided to the mastercard field within the configuration.

        Type: :class:`onlinepayments.sdk.domain.mastercard.Mastercard`
        """
        return self.__mastercard

    @mastercard.setter
    def mastercard(self, value: Mastercard | None) -> None:
        self.__mastercard = value

    @property
    def visa(self) -> Visa | None:
        """
        | The following fields need to be provided to the visa field within the configuration.

        Type: :class:`onlinepayments.sdk.domain.visa.Visa`
        """
        return self.__visa

    @visa.setter
    def visa(self, value: Visa | None) -> None:
        self.__visa = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.amex is not None:
            dictionary['amex'] = self.amex.to_dictionary()
        if self.cb is not None:
            dictionary['cb'] = self.cb.to_dictionary()
        if self.eftpos is not None:
            dictionary['eftpos'] = self.eftpos.to_dictionary()
        if self.mastercard is not None:
            dictionary['mastercard'] = self.mastercard.to_dictionary()
        if self.visa is not None:
            dictionary['visa'] = self.visa.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ApiParameters':
        super().from_dictionary(dictionary)
        if 'amex' in dictionary:
            if not isinstance(dictionary['amex'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amex']))
            value = Amex()
            self.amex = value.from_dictionary(dictionary['amex'])
        if 'cb' in dictionary:
            if not isinstance(dictionary['cb'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cb']))
            value = PaymentProduct5002defaultBrandParameters()
            self.cb = value.from_dictionary(dictionary['cb'])
        if 'eftpos' in dictionary:
            if not isinstance(dictionary['eftpos'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['eftpos']))
            value = PaymentProduct5002defaultBrandParameters()
            self.eftpos = value.from_dictionary(dictionary['eftpos'])
        if 'mastercard' in dictionary:
            if not isinstance(dictionary['mastercard'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mastercard']))
            value = Mastercard()
            self.mastercard = value.from_dictionary(dictionary['mastercard'])
        if 'visa' in dictionary:
            if not isinstance(dictionary['visa'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['visa']))
            value = Visa()
            self.visa = value.from_dictionary(dictionary['visa'])
        return self

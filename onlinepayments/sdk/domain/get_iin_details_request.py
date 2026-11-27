#
# This file was automatically generated.
#
from .data_object import DataObject
from .payment_context import PaymentContext


class GetIINDetailsRequest(DataObject):

    __slots__ = (
        "__bin",
        "__payment_context",
    )

    __bin: str | None
    __payment_context: PaymentContext | None

    def __init__(
        self,
        *,
        bin: str | None = None,
        payment_context: PaymentContext | None = None,
    ) -> None:
        self.bin = bin
        self.payment_context = payment_context

    @property
    def bin(self) -> str | None:
        """
        | The first digits of the credit card number from left to right with a minimum of 6 digits. Providing additional digits (up to 19) can result in more co-brands being returned.

        Type: str
        """
        return self.__bin

    @bin.setter
    def bin(self, value: str | None) -> None:
        self.__bin = value

    @property
    def payment_context(self) -> PaymentContext | None:
        """
        | Optional payment context to refine the IIN lookup to filter out payment products not applicable to your payment.

        Type: :class:`onlinepayments.sdk.domain.payment_context.PaymentContext`
        """
        return self.__payment_context

    @payment_context.setter
    def payment_context(self, value: PaymentContext | None) -> None:
        self.__payment_context = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.bin is not None:
            dictionary['bin'] = self.bin
        if self.payment_context is not None:
            dictionary['paymentContext'] = self.payment_context.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'GetIINDetailsRequest':
        super().from_dictionary(dictionary)
        if 'bin' in dictionary:
            self.bin = dictionary['bin']
        if 'paymentContext' in dictionary:
            if not isinstance(dictionary['paymentContext'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentContext']))
            value = PaymentContext()
            self.payment_context = value.from_dictionary(dictionary['paymentContext'])
        return self

#
# This file was automatically generated.
#
from .data_object import DataObject
from .payment_response import PaymentResponse


class AddAuthorizationDetailsResponse(DataObject):

    __slots__ = (
        "__payment",
    )

    __payment: PaymentResponse | None

    def __init__(
        self,
        *,
        payment: PaymentResponse | None = None,
    ) -> None:
        self.payment = payment

    @property
    def payment(self) -> PaymentResponse | None:
        """
        | This object holds the properties related to the payment.

        Type: :class:`onlinepayments.sdk.domain.payment_response.PaymentResponse`
        """
        return self.__payment

    @payment.setter
    def payment(self, value: PaymentResponse | None) -> None:
        self.__payment = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.payment is not None:
            dictionary['payment'] = self.payment.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AddAuthorizationDetailsResponse':
        super().from_dictionary(dictionary)
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = PaymentResponse()
            self.payment = value.from_dictionary(dictionary['payment'])
        return self

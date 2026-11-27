#
# This file was automatically generated.
#
from .data_object import DataObject
from .payment_response import PaymentResponse


class CreatedPaymentOutput(DataObject):

    __slots__ = (
        "__payment",
        "__payment_status_category",
    )

    __payment: PaymentResponse | None
    __payment_status_category: str | None

    def __init__(
        self,
        *,
        payment: PaymentResponse | None = None,
        payment_status_category: str | None = None,
    ) -> None:
        self.payment = payment
        self.payment_status_category = payment_status_category

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

    @property
    def payment_status_category(self) -> str | None:
        """
        Type: str
        """
        return self.__payment_status_category

    @payment_status_category.setter
    def payment_status_category(self, value: str | None) -> None:
        self.__payment_status_category = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.payment is not None:
            dictionary['payment'] = self.payment.to_dictionary()
        if self.payment_status_category is not None:
            dictionary['paymentStatusCategory'] = self.payment_status_category
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreatedPaymentOutput':
        super().from_dictionary(dictionary)
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = PaymentResponse()
            self.payment = value.from_dictionary(dictionary['payment'])
        if 'paymentStatusCategory' in dictionary:
            self.payment_status_category = dictionary['paymentStatusCategory']
        return self

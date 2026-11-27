#
# This file was automatically generated.
#
from .data_object import DataObject
from .payment_product5407_auto_capture import PaymentProduct5407AutoCapture


class RedirectPaymentProduct5407SpecificInput(DataObject):

    __slots__ = (
        "__payment_product5407_auto_capture",
    )

    __payment_product5407_auto_capture: PaymentProduct5407AutoCapture | None

    def __init__(
        self,
        *,
        payment_product5407_auto_capture: PaymentProduct5407AutoCapture | None = None,
    ) -> None:
        self.payment_product5407_auto_capture = payment_product5407_auto_capture

    @property
    def payment_product5407_auto_capture(self) -> PaymentProduct5407AutoCapture | None:
        """
        | Object containing the auto capture configuration for the payment.

        Type: :class:`onlinepayments.sdk.domain.payment_product5407_auto_capture.PaymentProduct5407AutoCapture`
        """
        return self.__payment_product5407_auto_capture

    @payment_product5407_auto_capture.setter
    def payment_product5407_auto_capture(self, value: PaymentProduct5407AutoCapture | None) -> None:
        self.__payment_product5407_auto_capture = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.payment_product5407_auto_capture is not None:
            dictionary['paymentProduct5407AutoCapture'] = self.payment_product5407_auto_capture.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct5407SpecificInput':
        super().from_dictionary(dictionary)
        if 'paymentProduct5407AutoCapture' in dictionary:
            if not isinstance(dictionary['paymentProduct5407AutoCapture'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct5407AutoCapture']))
            value = PaymentProduct5407AutoCapture()
            self.payment_product5407_auto_capture = value.from_dictionary(dictionary['paymentProduct5407AutoCapture'])
        return self

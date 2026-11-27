#
# This file was automatically generated.
#
from .data_object import DataObject
from .payment_product_session302_specific_output import PaymentProductSession302SpecificOutput


class PaymentProductSessionResponse(DataObject):

    __slots__ = (
        "__payment_product_session302_specific_output",
    )

    __payment_product_session302_specific_output: PaymentProductSession302SpecificOutput | None

    def __init__(
        self,
        *,
        payment_product_session302_specific_output: PaymentProductSession302SpecificOutput | None = None,
    ) -> None:
        self.payment_product_session302_specific_output = payment_product_session302_specific_output

    @property
    def payment_product_session302_specific_output(self) -> PaymentProductSession302SpecificOutput | None:
        """
        | The specific output details of the created payment product session for Apple Pay (payment product 302).

        Type: :class:`onlinepayments.sdk.domain.payment_product_session302_specific_output.PaymentProductSession302SpecificOutput`
        """
        return self.__payment_product_session302_specific_output

    @payment_product_session302_specific_output.setter
    def payment_product_session302_specific_output(self, value: PaymentProductSession302SpecificOutput | None) -> None:
        self.__payment_product_session302_specific_output = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.payment_product_session302_specific_output is not None:
            dictionary['paymentProductSession302SpecificOutput'] = self.payment_product_session302_specific_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductSessionResponse':
        super().from_dictionary(dictionary)
        if 'paymentProductSession302SpecificOutput' in dictionary:
            if not isinstance(dictionary['paymentProductSession302SpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProductSession302SpecificOutput']))
            value = PaymentProductSession302SpecificOutput()
            self.payment_product_session302_specific_output = value.from_dictionary(dictionary['paymentProductSession302SpecificOutput'])
        return self

#
# This file was automatically generated.
#
from .data_object import DataObject
from .payment_product_session302_specific_input import PaymentProductSession302SpecificInput


class PaymentProductSessionRequest(DataObject):

    __slots__ = (
        "__payment_product_session302_specific_input",
    )

    __payment_product_session302_specific_input: PaymentProductSession302SpecificInput | None

    def __init__(
        self,
        *,
        payment_product_session302_specific_input: PaymentProductSession302SpecificInput | None = None,
    ) -> None:
        self.payment_product_session302_specific_input = payment_product_session302_specific_input

    @property
    def payment_product_session302_specific_input(self) -> PaymentProductSession302SpecificInput | None:
        """
        | The specific input details needed to create a payment product session for Apple Pay (payment product 302).

        Type: :class:`onlinepayments.sdk.domain.payment_product_session302_specific_input.PaymentProductSession302SpecificInput`
        """
        return self.__payment_product_session302_specific_input

    @payment_product_session302_specific_input.setter
    def payment_product_session302_specific_input(self, value: PaymentProductSession302SpecificInput | None) -> None:
        self.__payment_product_session302_specific_input = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.payment_product_session302_specific_input is not None:
            dictionary['paymentProductSession302SpecificInput'] = self.payment_product_session302_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductSessionRequest':
        super().from_dictionary(dictionary)
        if 'paymentProductSession302SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProductSession302SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProductSession302SpecificInput']))
            value = PaymentProductSession302SpecificInput()
            self.payment_product_session302_specific_input = value.from_dictionary(dictionary['paymentProductSession302SpecificInput'])
        return self

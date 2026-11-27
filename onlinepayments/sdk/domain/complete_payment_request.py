#
# This file was automatically generated.
#
from .complete_payment_card_payment_method_specific_input import CompletePaymentCardPaymentMethodSpecificInput
from .data_object import DataObject
from .order import Order


class CompletePaymentRequest(DataObject):

    __slots__ = (
        "__card_payment_method_specific_input",
        "__order",
    )

    __card_payment_method_specific_input: CompletePaymentCardPaymentMethodSpecificInput | None
    __order: Order | None

    def __init__(
        self,
        *,
        card_payment_method_specific_input: CompletePaymentCardPaymentMethodSpecificInput | None = None,
        order: Order | None = None,
    ) -> None:
        self.card_payment_method_specific_input = card_payment_method_specific_input
        self.order = order

    @property
    def card_payment_method_specific_input(self) -> CompletePaymentCardPaymentMethodSpecificInput | None:
        """
        Type: :class:`onlinepayments.sdk.domain.complete_payment_card_payment_method_specific_input.CompletePaymentCardPaymentMethodSpecificInput`
        """
        return self.__card_payment_method_specific_input

    @card_payment_method_specific_input.setter
    def card_payment_method_specific_input(self, value: CompletePaymentCardPaymentMethodSpecificInput | None) -> None:
        self.__card_payment_method_specific_input = value

    @property
    def order(self) -> Order | None:
        """
        | The order object contains order-related data; Please note that this object is required to submit the amount.

        Type: :class:`onlinepayments.sdk.domain.order.Order`
        """
        return self.__order

    @order.setter
    def order(self, value: Order | None) -> None:
        self.__order = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.card_payment_method_specific_input is not None:
            dictionary['cardPaymentMethodSpecificInput'] = self.card_payment_method_specific_input.to_dictionary()
        if self.order is not None:
            dictionary['order'] = self.order.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CompletePaymentRequest':
        super().from_dictionary(dictionary)
        if 'cardPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificInput']))
            value = CompletePaymentCardPaymentMethodSpecificInput()
            self.card_payment_method_specific_input = value.from_dictionary(dictionary['cardPaymentMethodSpecificInput'])
        if 'order' in dictionary:
            if not isinstance(dictionary['order'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['order']))
            value = Order()
            self.order = value.from_dictionary(dictionary['order'])
        return self

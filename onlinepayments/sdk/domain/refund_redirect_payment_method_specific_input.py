#
# This file was automatically generated.
#
from .data_object import DataObject
from .refund_redirect_payment_product900_specific_input import RefundRedirectPaymentProduct900SpecificInput


class RefundRedirectPaymentMethodSpecificInput(DataObject):

    __slots__ = (
        "__refund_redirect_payment_product900_specific_input",
    )

    __refund_redirect_payment_product900_specific_input: RefundRedirectPaymentProduct900SpecificInput | None

    def __init__(
        self,
        *,
        refund_redirect_payment_product900_specific_input: RefundRedirectPaymentProduct900SpecificInput | None = None,
    ) -> None:
        self.refund_redirect_payment_product900_specific_input = refund_redirect_payment_product900_specific_input

    @property
    def refund_redirect_payment_product900_specific_input(self) -> RefundRedirectPaymentProduct900SpecificInput | None:
        """
        | Object containing specific input required for Wero refunds (Payment product ID 900).

        Type: :class:`onlinepayments.sdk.domain.refund_redirect_payment_product900_specific_input.RefundRedirectPaymentProduct900SpecificInput`
        """
        return self.__refund_redirect_payment_product900_specific_input

    @refund_redirect_payment_product900_specific_input.setter
    def refund_redirect_payment_product900_specific_input(self, value: RefundRedirectPaymentProduct900SpecificInput | None) -> None:
        self.__refund_redirect_payment_product900_specific_input = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.refund_redirect_payment_product900_specific_input is not None:
            dictionary['refundRedirectPaymentProduct900SpecificInput'] = self.refund_redirect_payment_product900_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RefundRedirectPaymentMethodSpecificInput':
        super().from_dictionary(dictionary)
        if 'refundRedirectPaymentProduct900SpecificInput' in dictionary:
            if not isinstance(dictionary['refundRedirectPaymentProduct900SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['refundRedirectPaymentProduct900SpecificInput']))
            value = RefundRedirectPaymentProduct900SpecificInput()
            self.refund_redirect_payment_product900_specific_input = value.from_dictionary(dictionary['refundRedirectPaymentProduct900SpecificInput'])
        return self

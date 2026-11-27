#
# This file was automatically generated.
#
from .data_object import DataObject
from .sepa_direct_debit_payment_product771_specific_input import SepaDirectDebitPaymentProduct771SpecificInput


class SepaDirectDebitPaymentMethodSpecificInput(DataObject):

    __slots__ = (
        "__payment_product771_specific_input",
        "__payment_product_id",
    )

    __payment_product771_specific_input: SepaDirectDebitPaymentProduct771SpecificInput | None
    __payment_product_id: int | None

    def __init__(
        self,
        *,
        payment_product771_specific_input: SepaDirectDebitPaymentProduct771SpecificInput | None = None,
        payment_product_id: int | None = None,
    ) -> None:
        self.payment_product771_specific_input = payment_product771_specific_input
        self.payment_product_id = payment_product_id

    @property
    def payment_product771_specific_input(self) -> SepaDirectDebitPaymentProduct771SpecificInput | None:
        """
        | Object containing information specific to SEPA Direct Debit

        Type: :class:`onlinepayments.sdk.domain.sepa_direct_debit_payment_product771_specific_input.SepaDirectDebitPaymentProduct771SpecificInput`
        """
        return self.__payment_product771_specific_input

    @payment_product771_specific_input.setter
    def payment_product771_specific_input(self, value: SepaDirectDebitPaymentProduct771SpecificInput | None) -> None:
        self.__payment_product771_specific_input = value

    @property
    def payment_product_id(self) -> int | None:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: int | None) -> None:
        self.__payment_product_id = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.payment_product771_specific_input is not None:
            dictionary['paymentProduct771SpecificInput'] = self.payment_product771_specific_input.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SepaDirectDebitPaymentMethodSpecificInput':
        super().from_dictionary(dictionary)
        if 'paymentProduct771SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct771SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct771SpecificInput']))
            value = SepaDirectDebitPaymentProduct771SpecificInput()
            self.payment_product771_specific_input = value.from_dictionary(dictionary['paymentProduct771SpecificInput'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self

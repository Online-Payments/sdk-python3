# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.sepa_direct_debit_payment_product771_specific_input import SepaDirectDebitPaymentProduct771SpecificInput


class SepaDirectDebitPaymentMethodSpecificInput(DataObject):
    """
    | Object containing the specific input details for SEPA direct debit payments
    """

    __payment_product771_specific_input = None
    __payment_product_id = None

    @property
    def payment_product771_specific_input(self) -> SepaDirectDebitPaymentProduct771SpecificInput:
        """
        | Object containing information specific to SEPA Direct Debit

        Type: :class:`onlinepayments.sdk.domain.sepa_direct_debit_payment_product771_specific_input.SepaDirectDebitPaymentProduct771SpecificInput`
        """
        return self.__payment_product771_specific_input

    @payment_product771_specific_input.setter
    def payment_product771_specific_input(self, value: SepaDirectDebitPaymentProduct771SpecificInput):
        self.__payment_product771_specific_input = value

    @property
    def payment_product_id(self) -> int:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: int):
        self.__payment_product_id = value

    def to_dictionary(self):
        dictionary = super(SepaDirectDebitPaymentMethodSpecificInput, self).to_dictionary()
        if self.payment_product771_specific_input is not None:
            dictionary['paymentProduct771SpecificInput'] = self.payment_product771_specific_input.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(SepaDirectDebitPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'paymentProduct771SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct771SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct771SpecificInput']))
            value = SepaDirectDebitPaymentProduct771SpecificInput()
            self.payment_product771_specific_input = value.from_dictionary(dictionary['paymentProduct771SpecificInput'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self

# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .sepa_direct_debit_payment_product771_specific_input_base import SepaDirectDebitPaymentProduct771SpecificInputBase


class SepaDirectDebitPaymentMethodSpecificInputBase(DataObject):

    __payment_product771_specific_input: Optional[SepaDirectDebitPaymentProduct771SpecificInputBase] = None
    __payment_product_id: Optional[int] = None

    @property
    def payment_product771_specific_input(self) -> Optional[SepaDirectDebitPaymentProduct771SpecificInputBase]:
        """
        | Object containing information specific to SEPA Direct Debit

        Type: :class:`onlinepayments.sdk.domain.sepa_direct_debit_payment_product771_specific_input_base.SepaDirectDebitPaymentProduct771SpecificInputBase`
        """
        return self.__payment_product771_specific_input

    @payment_product771_specific_input.setter
    def payment_product771_specific_input(self, value: Optional[SepaDirectDebitPaymentProduct771SpecificInputBase]) -> None:
        self.__payment_product771_specific_input = value

    @property
    def payment_product_id(self) -> Optional[int]:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: Optional[int]) -> None:
        self.__payment_product_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(SepaDirectDebitPaymentMethodSpecificInputBase, self).to_dictionary()
        if self.payment_product771_specific_input is not None:
            dictionary['paymentProduct771SpecificInput'] = self.payment_product771_specific_input.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SepaDirectDebitPaymentMethodSpecificInputBase':
        super(SepaDirectDebitPaymentMethodSpecificInputBase, self).from_dictionary(dictionary)
        if 'paymentProduct771SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct771SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct771SpecificInput']))
            value = SepaDirectDebitPaymentProduct771SpecificInputBase()
            self.payment_product771_specific_input = value.from_dictionary(dictionary['paymentProduct771SpecificInput'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self

# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .data_object import DataObject
from .line_item_detail import LineItemDetail
from .operation_payment_references import OperationPaymentReferences
from .payment_references import PaymentReferences


class CapturePaymentRequest(DataObject):

    __amount: Optional[int] = None
    __is_final: Optional[bool] = None
    __line_item_details: Optional[List[LineItemDetail]] = None
    __operation_references: Optional[OperationPaymentReferences] = None
    __references: Optional[PaymentReferences] = None

    @property
    def amount(self) -> Optional[int]:
        """
        | Here you can specify the amount that you want to capture (specified in cents, where single digit currencies are presumed to have 2 digits). The amount can be lower than the amount that was authorized, but not higher. If left empty, the full amount will be captured and the request will be final. If the full amount is captured, the request will also be final.

        Type: int
        """
        return self.__amount

    @amount.setter
    def amount(self, value: Optional[int]) -> None:
        self.__amount = value

    @property
    def is_final(self) -> Optional[bool]:
        """
        | This property indicates whether this will be the final operation. The default value for this property is false.

        Type: bool
        """
        return self.__is_final

    @is_final.setter
    def is_final(self, value: Optional[bool]) -> None:
        self.__is_final = value

    @property
    def line_item_details(self) -> Optional[List[LineItemDetail]]:
        """
        | List of lineItemIds and quantities for capture/refund/cancellation.

        Type: list[:class:`onlinepayments.sdk.domain.line_item_detail.LineItemDetail`]
        """
        return self.__line_item_details

    @line_item_details.setter
    def line_item_details(self, value: Optional[List[LineItemDetail]]) -> None:
        self.__line_item_details = value

    @property
    def operation_references(self) -> Optional[OperationPaymentReferences]:
        """
        | Object that holds all reference properties that are linked to this transaction

        Type: :class:`onlinepayments.sdk.domain.operation_payment_references.OperationPaymentReferences`
        """
        return self.__operation_references

    @operation_references.setter
    def operation_references(self, value: Optional[OperationPaymentReferences]) -> None:
        self.__operation_references = value

    @property
    def references(self) -> Optional[PaymentReferences]:
        """
        | Object that holds all reference properties that are linked to this transaction. **Deprecated for capture/refund**: Use operationReferences instead.

        Type: :class:`onlinepayments.sdk.domain.payment_references.PaymentReferences`
        """
        return self.__references

    @references.setter
    def references(self, value: Optional[PaymentReferences]) -> None:
        self.__references = value

    def to_dictionary(self) -> dict:
        dictionary = super(CapturePaymentRequest, self).to_dictionary()
        if self.amount is not None:
            dictionary['amount'] = self.amount
        if self.is_final is not None:
            dictionary['isFinal'] = self.is_final
        if self.line_item_details is not None:
            dictionary['lineItemDetails'] = []
            for element in self.line_item_details:
                if element is not None:
                    dictionary['lineItemDetails'].append(element.to_dictionary())
        if self.operation_references is not None:
            dictionary['operationReferences'] = self.operation_references.to_dictionary()
        if self.references is not None:
            dictionary['references'] = self.references.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CapturePaymentRequest':
        super(CapturePaymentRequest, self).from_dictionary(dictionary)
        if 'amount' in dictionary:
            self.amount = dictionary['amount']
        if 'isFinal' in dictionary:
            self.is_final = dictionary['isFinal']
        if 'lineItemDetails' in dictionary:
            if not isinstance(dictionary['lineItemDetails'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['lineItemDetails']))
            self.line_item_details = []
            for element in dictionary['lineItemDetails']:
                value = LineItemDetail()
                self.line_item_details.append(value.from_dictionary(element))
        if 'operationReferences' in dictionary:
            if not isinstance(dictionary['operationReferences'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['operationReferences']))
            value = OperationPaymentReferences()
            self.operation_references = value.from_dictionary(dictionary['operationReferences'])
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = PaymentReferences()
            self.references = value.from_dictionary(dictionary['references'])
        return self

# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .amount_of_money import AmountOfMoney
from .data_object import DataObject
from .operation_payment_references import OperationPaymentReferences
from .payment_references import PaymentReferences
from .payment_status_output import PaymentStatusOutput


class OperationOutput(DataObject):

    __amount_of_money: Optional[AmountOfMoney] = None
    __id: Optional[str] = None
    __operation_references: Optional[OperationPaymentReferences] = None
    __payment_method: Optional[str] = None
    __references: Optional[PaymentReferences] = None
    __status: Optional[str] = None
    __status_output: Optional[PaymentStatusOutput] = None

    @property
    def amount_of_money(self) -> Optional[AmountOfMoney]:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value: Optional[AmountOfMoney]) -> None:
        self.__amount_of_money = value

    @property
    def id(self) -> Optional[str]:
        """
        | Our unique payment transaction identifier

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: Optional[str]) -> None:
        self.__id = value

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
    def payment_method(self) -> Optional[str]:
        """
        | Payment method identifier used by the our payment engine.

        Type: str
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value: Optional[str]) -> None:
        self.__payment_method = value

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

    @property
    def status(self) -> Optional[str]:
        """
        | Current high-level status of the payment in a human-readable form.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: Optional[str]) -> None:
        self.__status = value

    @property
    def status_output(self) -> Optional[PaymentStatusOutput]:
        """
        | This object has the numeric representation of the current payment status, timestamp of last status change and performable action on the current payment resource. In case of failed payments and negative scenarios, detailed error information is listed.

        Type: :class:`onlinepayments.sdk.domain.payment_status_output.PaymentStatusOutput`
        """
        return self.__status_output

    @status_output.setter
    def status_output(self, value: Optional[PaymentStatusOutput]) -> None:
        self.__status_output = value

    def to_dictionary(self) -> dict:
        dictionary = super(OperationOutput, self).to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.operation_references is not None:
            dictionary['operationReferences'] = self.operation_references.to_dictionary()
        if self.payment_method is not None:
            dictionary['paymentMethod'] = self.payment_method
        if self.references is not None:
            dictionary['references'] = self.references.to_dictionary()
        if self.status is not None:
            dictionary['status'] = self.status
        if self.status_output is not None:
            dictionary['statusOutput'] = self.status_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'OperationOutput':
        super(OperationOutput, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'operationReferences' in dictionary:
            if not isinstance(dictionary['operationReferences'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['operationReferences']))
            value = OperationPaymentReferences()
            self.operation_references = value.from_dictionary(dictionary['operationReferences'])
        if 'paymentMethod' in dictionary:
            self.payment_method = dictionary['paymentMethod']
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = PaymentReferences()
            self.references = value.from_dictionary(dictionary['references'])
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'statusOutput' in dictionary:
            if not isinstance(dictionary['statusOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['statusOutput']))
            value = PaymentStatusOutput()
            self.status_output = value.from_dictionary(dictionary['statusOutput'])
        return self

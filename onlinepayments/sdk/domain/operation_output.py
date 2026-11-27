#
# This file was automatically generated.
#
from datetime import datetime

from .amount_of_money import AmountOfMoney
from .data_object import DataObject
from .operation_payment_references import OperationPaymentReferences
from .payment_references import PaymentReferences
from .payment_status_output import PaymentStatusOutput


class OperationOutput(DataObject):

    __slots__ = (
        "__amount_of_money",
        "__id",
        "__operation_references",
        "__payment_method",
        "__references",
        "__status",
        "__status_output",
        "__transaction_date",
    )

    __amount_of_money: AmountOfMoney | None
    __id: str | None
    __operation_references: OperationPaymentReferences | None
    __payment_method: str | None
    __references: PaymentReferences | None
    __status: str | None
    __status_output: PaymentStatusOutput | None
    __transaction_date: datetime | None

    def __init__(
        self,
        *,
        amount_of_money: AmountOfMoney | None = None,
        id: str | None = None,
        operation_references: OperationPaymentReferences | None = None,
        payment_method: str | None = None,
        references: PaymentReferences | None = None,
        status: str | None = None,
        status_output: PaymentStatusOutput | None = None,
        transaction_date: datetime | None = None,
    ) -> None:
        self.amount_of_money = amount_of_money
        self.id = id
        self.operation_references = operation_references
        self.payment_method = payment_method
        self.references = references
        self.status = status
        self.status_output = status_output
        self.transaction_date = transaction_date

    @property
    def amount_of_money(self) -> AmountOfMoney | None:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value: AmountOfMoney | None) -> None:
        self.__amount_of_money = value

    @property
    def id(self) -> str | None:
        """
        | This is our unique payment transaction identifier.

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: str | None) -> None:
        self.__id = value

    @property
    def operation_references(self) -> OperationPaymentReferences | None:
        """
        | Object that holds all reference properties that are linked to this transaction

        Type: :class:`onlinepayments.sdk.domain.operation_payment_references.OperationPaymentReferences`
        """
        return self.__operation_references

    @operation_references.setter
    def operation_references(self, value: OperationPaymentReferences | None) -> None:
        self.__operation_references = value

    @property
    def payment_method(self) -> str | None:
        """
        | Payment method identifier used by the our payment engine.

        Type: str
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value: str | None) -> None:
        self.__payment_method = value

    @property
    def references(self) -> PaymentReferences | None:
        """
        | Object that holds all reference properties that are linked to this transaction. **Deprecated for capture/refund**: Use operationReferences instead.

        Type: :class:`onlinepayments.sdk.domain.payment_references.PaymentReferences`
        """
        return self.__references

    @references.setter
    def references(self, value: PaymentReferences | None) -> None:
        self.__references = value

    @property
    def status(self) -> str | None:
        """
        | Current high-level status of the payment in a human-readable form.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: str | None) -> None:
        self.__status = value

    @property
    def status_output(self) -> PaymentStatusOutput | None:
        """
        | This object has the numeric representation of the current payment status, the timestamp of the last status change, and the performable action on the current payment resource. In case of failed payments and negative scenarios, detailed error information is listed.

        Type: :class:`onlinepayments.sdk.domain.payment_status_output.PaymentStatusOutput`
        """
        return self.__status_output

    @status_output.setter
    def status_output(self, value: PaymentStatusOutput | None) -> None:
        self.__status_output = value

    @property
    def transaction_date(self) -> datetime | None:
        """
        | It is the server-side processing date and time of the transaction.

        Type: datetime
        """
        return self.__transaction_date

    @transaction_date.setter
    def transaction_date(self, value: datetime | None) -> None:
        self.__transaction_date = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
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
        if self.transaction_date is not None:
            dictionary['transactionDate'] = DataObject.format_datetime(self.transaction_date)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'OperationOutput':
        super().from_dictionary(dictionary)
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
        if 'transactionDate' in dictionary:
            self.transaction_date = DataObject.parse_datetime(dictionary['transactionDate'])
        return self

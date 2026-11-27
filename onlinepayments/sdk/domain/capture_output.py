#
# This file was automatically generated.
#
from datetime import datetime

from .amount_of_money import AmountOfMoney
from .card_payment_method_specific_output import CardPaymentMethodSpecificOutput
from .data_object import DataObject
from .mobile_payment_method_specific_output import MobilePaymentMethodSpecificOutput
from .operation_payment_references import OperationPaymentReferences
from .payment_references import PaymentReferences
from .redirect_payment_method_specific_output import RedirectPaymentMethodSpecificOutput
from .sepa_direct_debit_payment_method_specific_output import SepaDirectDebitPaymentMethodSpecificOutput
from .surcharge_specific_output import SurchargeSpecificOutput


class CaptureOutput(DataObject):

    __slots__ = (
        "__acquired_amount",
        "__amount_of_money",
        "__amount_paid",
        "__card_payment_method_specific_output",
        "__merchant_parameters",
        "__mobile_payment_method_specific_output",
        "__operation_references",
        "__payment_creation_date",
        "__payment_method",
        "__redirect_payment_method_specific_output",
        "__references",
        "__sepa_direct_debit_payment_method_specific_output",
        "__surcharge_specific_output",
        "__transaction_date",
    )

    __acquired_amount: AmountOfMoney | None
    __amount_of_money: AmountOfMoney | None
    __amount_paid: int | None
    __card_payment_method_specific_output: CardPaymentMethodSpecificOutput | None
    __merchant_parameters: str | None
    __mobile_payment_method_specific_output: MobilePaymentMethodSpecificOutput | None
    __operation_references: OperationPaymentReferences | None
    __payment_creation_date: datetime | None
    __payment_method: str | None
    __redirect_payment_method_specific_output: RedirectPaymentMethodSpecificOutput | None
    __references: PaymentReferences | None
    __sepa_direct_debit_payment_method_specific_output: SepaDirectDebitPaymentMethodSpecificOutput | None
    __surcharge_specific_output: SurchargeSpecificOutput | None
    __transaction_date: datetime | None

    def __init__(
        self,
        *,
        acquired_amount: AmountOfMoney | None = None,
        amount_of_money: AmountOfMoney | None = None,
        amount_paid: int | None = None,
        card_payment_method_specific_output: CardPaymentMethodSpecificOutput | None = None,
        merchant_parameters: str | None = None,
        mobile_payment_method_specific_output: MobilePaymentMethodSpecificOutput | None = None,
        operation_references: OperationPaymentReferences | None = None,
        payment_creation_date: datetime | None = None,
        payment_method: str | None = None,
        redirect_payment_method_specific_output: RedirectPaymentMethodSpecificOutput | None = None,
        references: PaymentReferences | None = None,
        sepa_direct_debit_payment_method_specific_output: SepaDirectDebitPaymentMethodSpecificOutput | None = None,
        surcharge_specific_output: SurchargeSpecificOutput | None = None,
        transaction_date: datetime | None = None,
    ) -> None:
        self.acquired_amount = acquired_amount
        self.amount_of_money = amount_of_money
        self.amount_paid = amount_paid
        self.card_payment_method_specific_output = card_payment_method_specific_output
        self.merchant_parameters = merchant_parameters
        self.mobile_payment_method_specific_output = mobile_payment_method_specific_output
        self.operation_references = operation_references
        self.payment_creation_date = payment_creation_date
        self.payment_method = payment_method
        self.redirect_payment_method_specific_output = redirect_payment_method_specific_output
        self.references = references
        self.sepa_direct_debit_payment_method_specific_output = sepa_direct_debit_payment_method_specific_output
        self.surcharge_specific_output = surcharge_specific_output
        self.transaction_date = transaction_date

    @property
    def acquired_amount(self) -> AmountOfMoney | None:
        """
        | Amount that has been acquired by the Acquirer

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__acquired_amount

    @acquired_amount.setter
    def acquired_amount(self, value: AmountOfMoney | None) -> None:
        self.__acquired_amount = value

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
    def amount_paid(self) -> int | None:
        """
        | Amount that has been paid. This is deprecated. Use acquiredAmount instead.

        Type: int

        Deprecated; Amount that has been paid. This is deprecated. Use acquiredAmount instead.
        """
        return self.__amount_paid

    @amount_paid.setter
    def amount_paid(self, value: int | None) -> None:
        self.__amount_paid = value

    @property
    def card_payment_method_specific_output(self) -> CardPaymentMethodSpecificOutput | None:
        """
        | Object containing the card payment method details

        Type: :class:`onlinepayments.sdk.domain.card_payment_method_specific_output.CardPaymentMethodSpecificOutput`
        """
        return self.__card_payment_method_specific_output

    @card_payment_method_specific_output.setter
    def card_payment_method_specific_output(self, value: CardPaymentMethodSpecificOutput | None) -> None:
        self.__card_payment_method_specific_output = value

    @property
    def merchant_parameters(self) -> str | None:
        """
        | It allows you to store additional parameters for the transaction in the format you prefer (e.g.-> key-value query string, JSON, etc.) These parameters are then echoed back to you in API GET calls and Webhook notifications. This field must not contain any personal data.

        Type: str
        """
        return self.__merchant_parameters

    @merchant_parameters.setter
    def merchant_parameters(self, value: str | None) -> None:
        self.__merchant_parameters = value

    @property
    def mobile_payment_method_specific_output(self) -> MobilePaymentMethodSpecificOutput | None:
        """
        | Object containing the mobile payment method details

        Type: :class:`onlinepayments.sdk.domain.mobile_payment_method_specific_output.MobilePaymentMethodSpecificOutput`
        """
        return self.__mobile_payment_method_specific_output

    @mobile_payment_method_specific_output.setter
    def mobile_payment_method_specific_output(self, value: MobilePaymentMethodSpecificOutput | None) -> None:
        self.__mobile_payment_method_specific_output = value

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
    def payment_creation_date(self) -> datetime | None:
        """
        | Date and time when the current payment was first created

        Type: datetime
        """
        return self.__payment_creation_date

    @payment_creation_date.setter
    def payment_creation_date(self, value: datetime | None) -> None:
        self.__payment_creation_date = value

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
    def redirect_payment_method_specific_output(self) -> RedirectPaymentMethodSpecificOutput | None:
        """
        | Object containing the redirect payment product details

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_method_specific_output.RedirectPaymentMethodSpecificOutput`
        """
        return self.__redirect_payment_method_specific_output

    @redirect_payment_method_specific_output.setter
    def redirect_payment_method_specific_output(self, value: RedirectPaymentMethodSpecificOutput | None) -> None:
        self.__redirect_payment_method_specific_output = value

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
    def sepa_direct_debit_payment_method_specific_output(self) -> SepaDirectDebitPaymentMethodSpecificOutput | None:
        """
        | Object containing the SEPA direct debit details

        Type: :class:`onlinepayments.sdk.domain.sepa_direct_debit_payment_method_specific_output.SepaDirectDebitPaymentMethodSpecificOutput`
        """
        return self.__sepa_direct_debit_payment_method_specific_output

    @sepa_direct_debit_payment_method_specific_output.setter
    def sepa_direct_debit_payment_method_specific_output(self, value: SepaDirectDebitPaymentMethodSpecificOutput | None) -> None:
        self.__sepa_direct_debit_payment_method_specific_output = value

    @property
    def surcharge_specific_output(self) -> SurchargeSpecificOutput | None:
        """
        | Object containing specific surcharging attributes applied to an order.

        Type: :class:`onlinepayments.sdk.domain.surcharge_specific_output.SurchargeSpecificOutput`
        """
        return self.__surcharge_specific_output

    @surcharge_specific_output.setter
    def surcharge_specific_output(self, value: SurchargeSpecificOutput | None) -> None:
        self.__surcharge_specific_output = value

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
        if self.acquired_amount is not None:
            dictionary['acquiredAmount'] = self.acquired_amount.to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.amount_paid is not None:
            dictionary['amountPaid'] = self.amount_paid
        if self.card_payment_method_specific_output is not None:
            dictionary['cardPaymentMethodSpecificOutput'] = self.card_payment_method_specific_output.to_dictionary()
        if self.merchant_parameters is not None:
            dictionary['merchantParameters'] = self.merchant_parameters
        if self.mobile_payment_method_specific_output is not None:
            dictionary['mobilePaymentMethodSpecificOutput'] = self.mobile_payment_method_specific_output.to_dictionary()
        if self.operation_references is not None:
            dictionary['operationReferences'] = self.operation_references.to_dictionary()
        if self.payment_creation_date is not None:
            dictionary['paymentCreationDate'] = DataObject.format_datetime(self.payment_creation_date)
        if self.payment_method is not None:
            dictionary['paymentMethod'] = self.payment_method
        if self.redirect_payment_method_specific_output is not None:
            dictionary['redirectPaymentMethodSpecificOutput'] = self.redirect_payment_method_specific_output.to_dictionary()
        if self.references is not None:
            dictionary['references'] = self.references.to_dictionary()
        if self.sepa_direct_debit_payment_method_specific_output is not None:
            dictionary['sepaDirectDebitPaymentMethodSpecificOutput'] = self.sepa_direct_debit_payment_method_specific_output.to_dictionary()
        if self.surcharge_specific_output is not None:
            dictionary['surchargeSpecificOutput'] = self.surcharge_specific_output.to_dictionary()
        if self.transaction_date is not None:
            dictionary['transactionDate'] = DataObject.format_datetime(self.transaction_date)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CaptureOutput':
        super().from_dictionary(dictionary)
        if 'acquiredAmount' in dictionary:
            if not isinstance(dictionary['acquiredAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['acquiredAmount']))
            value = AmountOfMoney()
            self.acquired_amount = value.from_dictionary(dictionary['acquiredAmount'])
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'amountPaid' in dictionary:
            self.amount_paid = dictionary['amountPaid']
        if 'cardPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificOutput']))
            value = CardPaymentMethodSpecificOutput()
            self.card_payment_method_specific_output = value.from_dictionary(dictionary['cardPaymentMethodSpecificOutput'])
        if 'merchantParameters' in dictionary:
            self.merchant_parameters = dictionary['merchantParameters']
        if 'mobilePaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['mobilePaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mobilePaymentMethodSpecificOutput']))
            value = MobilePaymentMethodSpecificOutput()
            self.mobile_payment_method_specific_output = value.from_dictionary(dictionary['mobilePaymentMethodSpecificOutput'])
        if 'operationReferences' in dictionary:
            if not isinstance(dictionary['operationReferences'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['operationReferences']))
            value = OperationPaymentReferences()
            self.operation_references = value.from_dictionary(dictionary['operationReferences'])
        if 'paymentCreationDate' in dictionary:
            self.payment_creation_date = DataObject.parse_datetime(dictionary['paymentCreationDate'])
        if 'paymentMethod' in dictionary:
            self.payment_method = dictionary['paymentMethod']
        if 'redirectPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['redirectPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectPaymentMethodSpecificOutput']))
            value = RedirectPaymentMethodSpecificOutput()
            self.redirect_payment_method_specific_output = value.from_dictionary(dictionary['redirectPaymentMethodSpecificOutput'])
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = PaymentReferences()
            self.references = value.from_dictionary(dictionary['references'])
        if 'sepaDirectDebitPaymentMethodSpecificOutput' in dictionary:
            if not isinstance(dictionary['sepaDirectDebitPaymentMethodSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['sepaDirectDebitPaymentMethodSpecificOutput']))
            value = SepaDirectDebitPaymentMethodSpecificOutput()
            self.sepa_direct_debit_payment_method_specific_output = value.from_dictionary(dictionary['sepaDirectDebitPaymentMethodSpecificOutput'])
        if 'surchargeSpecificOutput' in dictionary:
            if not isinstance(dictionary['surchargeSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['surchargeSpecificOutput']))
            value = SurchargeSpecificOutput()
            self.surcharge_specific_output = value.from_dictionary(dictionary['surchargeSpecificOutput'])
        if 'transactionDate' in dictionary:
            self.transaction_date = DataObject.parse_datetime(dictionary['transactionDate'])
        return self

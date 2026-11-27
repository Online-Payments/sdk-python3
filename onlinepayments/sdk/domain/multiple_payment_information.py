#
# This file was automatically generated.
#
from .data_object import DataObject


class MultiplePaymentInformation(DataObject):

    __slots__ = (
        "__payment_pattern",
        "__total_number_of_payments",
    )

    __payment_pattern: str | None
    __total_number_of_payments: int | None

    def __init__(
        self,
        *,
        payment_pattern: str | None = None,
        total_number_of_payments: int | None = None,
    ) -> None:
        self.payment_pattern = payment_pattern
        self.total_number_of_payments = total_number_of_payments

    @property
    def payment_pattern(self) -> str | None:
        """
        | Typology of multiple payment. Allowed values:
        
        * PartialShipment - I-P e-Commerce scenario whereby credentials have been stored to enable subsequent MITs per shipment. For this type of use case, PartialShipment is expected on both the initial CIT and eventual subsequent MITs to complete the order.
        * Recurring - Transactions processed at fixed amount, regular intervals not to exceed one year between Transactions, representing an agreement between a cardholder and a merchant to purchase goods or services provided over a period of time. Note that a recurring MIT transaction is initiated by the merchant (payee) not the customer (payer) and so is out of scope of PSD2. Recurring transactions that are in scope of PSD2 (and therefore may benefit from the recurring transaction exemption) are those that are customer (payer) initiates, e.g. standing orders set up from a bank account.
        * Unscheduled - A transaction using a stored credential for a variable amount that does not occur on a scheduled or regularly occurring transaction date, where the cardholder has provided consent for the merchant to initiate one or more future transactions which are not initiated by the cardholder. This transaction type is based on an agreement with the cardholder and is not to be confused with cardholder initiated transactions performed with stored credentials (CITs are in scope of PSD2 whereas UCOF transactions are MITs and thus out of scope).
        * RecurringVariable - Transactions processed at variable amount, regular intervals not to exceed one year between Transactions, representing an agreement between a cardholder and a merchant to purchase goods or services provided over a period of time. Note that a recurring MIT transaction is initiated by the merchant (payee) not the customer (payer) and so is out of scope of PSD2. Recurring transactions that are in scope of PSD2 (and therefore may benefit from the recurring transaction exemption) are those that are customer (payer) initiates, e.g. standing orders set up from a bank account.
        * UnscheduledFixed - A transaction using a stored credential for a fixed amount that does not occur on a scheduled or regularly occurring transaction date, where the cardholder has provided consent for the merchant to initiate one or more future transactions which are not initiated by the cardholder. This transaction type is based on an agreement with the cardholder and is not to be confused with cardholder initiated transactions performed with stored credentials (CITs are in scope of PSD2 whereas UCOF transactions are MITs and thus out of scope).
        * Installment - Installment payments describe a single purchase of goods or services billed to a cardholder in multiple transactions over a period of time agreed by the cardholder and merchant.

        Type: str
        """
        return self.__payment_pattern

    @payment_pattern.setter
    def payment_pattern(self, value: str | None) -> None:
        self.__payment_pattern = value

    @property
    def total_number_of_payments(self) -> int | None:
        """
        | Total number of payments. If a payment is implied by this call, it implicitly has ordinal number 1.

        Type: int
        """
        return self.__total_number_of_payments

    @total_number_of_payments.setter
    def total_number_of_payments(self, value: int | None) -> None:
        self.__total_number_of_payments = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.payment_pattern is not None:
            dictionary['paymentPattern'] = self.payment_pattern
        if self.total_number_of_payments is not None:
            dictionary['totalNumberOfPayments'] = self.total_number_of_payments
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MultiplePaymentInformation':
        super().from_dictionary(dictionary)
        if 'paymentPattern' in dictionary:
            self.payment_pattern = dictionary['paymentPattern']
        if 'totalNumberOfPayments' in dictionary:
            self.total_number_of_payments = dictionary['totalNumberOfPayments']
        return self

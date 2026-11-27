#
# This file was automatically generated.
#
from .data_object import DataObject


class RedirectPaymentProduct5301SpecificInput(DataObject):

    __slots__ = (
        "__payment_method_type",
    )

    __payment_method_type: str | None

    def __init__(
        self,
        *,
        payment_method_type: str | None = None,
    ) -> None:
        self.payment_method_type = payment_method_type

    @property
    def payment_method_type(self) -> str | None:
        """
        * invoice - The transaction is an invoice payment, transaction amount should be greater than €10 and less than €1500. * direct_debit - The transaction is a direct debit payment, transaction amount should be greater than €10 and less than €1500.

        Type: str
        """
        return self.__payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, value: str | None) -> None:
        self.__payment_method_type = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.payment_method_type is not None:
            dictionary['paymentMethodType'] = self.payment_method_type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct5301SpecificInput':
        super().from_dictionary(dictionary)
        if 'paymentMethodType' in dictionary:
            self.payment_method_type = dictionary['paymentMethodType']
        return self

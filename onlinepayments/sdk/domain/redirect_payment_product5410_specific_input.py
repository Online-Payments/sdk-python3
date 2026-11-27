#
# This file was automatically generated.
#
from datetime import date

from .data_object import DataObject


class RedirectPaymentProduct5410SpecificInput(DataObject):

    __slots__ = (
        "__second_installment_payment_date",
    )

    __second_installment_payment_date: date | None

    def __init__(
        self,
        *,
        second_installment_payment_date: date | None = None,
    ) -> None:
        self.second_installment_payment_date = second_installment_payment_date

    @property
    def second_installment_payment_date(self) -> date | None:
        """
        | The date of the second installment (YYYYMMDD)

        Type: date
        """
        return self.__second_installment_payment_date

    @second_installment_payment_date.setter
    def second_installment_payment_date(self, value: date | None) -> None:
        self.__second_installment_payment_date = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.second_installment_payment_date is not None:
            dictionary['secondInstallmentPaymentDate'] = DataObject.format_date(self.second_installment_payment_date)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct5410SpecificInput':
        super().from_dictionary(dictionary)
        if 'secondInstallmentPaymentDate' in dictionary:
            self.second_installment_payment_date = DataObject.parse_date(dictionary['secondInstallmentPaymentDate'])
        return self

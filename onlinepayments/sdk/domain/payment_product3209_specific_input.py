#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentProduct3209SpecificInput(DataObject):

    __slots__ = (
        "__merchant_finance_code",
    )

    __merchant_finance_code: str | None

    def __init__(
        self,
        *,
        merchant_finance_code: str | None = None,
    ) -> None:
        self.merchant_finance_code = merchant_finance_code

    @property
    def merchant_finance_code(self) -> str | None:
        """
        | This field indicates the finance code provided by the merchant after the buyer has selected the proper financing option.

        Type: str
        """
        return self.__merchant_finance_code

    @merchant_finance_code.setter
    def merchant_finance_code(self, value: str | None) -> None:
        self.__merchant_finance_code = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.merchant_finance_code is not None:
            dictionary['merchantFinanceCode'] = self.merchant_finance_code
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct3209SpecificInput':
        super().from_dictionary(dictionary)
        if 'merchantFinanceCode' in dictionary:
            self.merchant_finance_code = dictionary['merchantFinanceCode']
        return self

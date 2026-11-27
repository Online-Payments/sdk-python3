#
# This file was automatically generated.
#
from .data_object import DataObject


class CustomerPaymentActivity(DataObject):

    __slots__ = (
        "__number_of_payment_attempts_last24_hours",
        "__number_of_payment_attempts_last_year",
        "__number_of_purchases_last6_months",
    )

    __number_of_payment_attempts_last24_hours: int | None
    __number_of_payment_attempts_last_year: int | None
    __number_of_purchases_last6_months: int | None

    def __init__(
        self,
        *,
        number_of_payment_attempts_last24_hours: int | None = None,
        number_of_payment_attempts_last_year: int | None = None,
        number_of_purchases_last6_months: int | None = None,
    ) -> None:
        self.number_of_payment_attempts_last24_hours = number_of_payment_attempts_last24_hours
        self.number_of_payment_attempts_last_year = number_of_payment_attempts_last_year
        self.number_of_purchases_last6_months = number_of_purchases_last6_months

    @property
    def number_of_payment_attempts_last24_hours(self) -> int | None:
        """
        | Number of payment attempts (so including unsuccessful ones) made by this customer with you in the last 24 hours

        Type: int
        """
        return self.__number_of_payment_attempts_last24_hours

    @number_of_payment_attempts_last24_hours.setter
    def number_of_payment_attempts_last24_hours(self, value: int | None) -> None:
        self.__number_of_payment_attempts_last24_hours = value

    @property
    def number_of_payment_attempts_last_year(self) -> int | None:
        """
        | Number of payment attempts (so including unsuccessful ones) made by this customer with you in the last 12 months

        Type: int
        """
        return self.__number_of_payment_attempts_last_year

    @number_of_payment_attempts_last_year.setter
    def number_of_payment_attempts_last_year(self, value: int | None) -> None:
        self.__number_of_payment_attempts_last_year = value

    @property
    def number_of_purchases_last6_months(self) -> int | None:
        """
        | Number of successful purchases made by this customer with you in the last 6 months

        Type: int
        """
        return self.__number_of_purchases_last6_months

    @number_of_purchases_last6_months.setter
    def number_of_purchases_last6_months(self, value: int | None) -> None:
        self.__number_of_purchases_last6_months = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.number_of_payment_attempts_last24_hours is not None:
            dictionary['numberOfPaymentAttemptsLast24Hours'] = self.number_of_payment_attempts_last24_hours
        if self.number_of_payment_attempts_last_year is not None:
            dictionary['numberOfPaymentAttemptsLastYear'] = self.number_of_payment_attempts_last_year
        if self.number_of_purchases_last6_months is not None:
            dictionary['numberOfPurchasesLast6Months'] = self.number_of_purchases_last6_months
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CustomerPaymentActivity':
        super().from_dictionary(dictionary)
        if 'numberOfPaymentAttemptsLast24Hours' in dictionary:
            self.number_of_payment_attempts_last24_hours = dictionary['numberOfPaymentAttemptsLast24Hours']
        if 'numberOfPaymentAttemptsLastYear' in dictionary:
            self.number_of_payment_attempts_last_year = dictionary['numberOfPaymentAttemptsLastYear']
        if 'numberOfPurchasesLast6Months' in dictionary:
            self.number_of_purchases_last6_months = dictionary['numberOfPurchasesLast6Months']
        return self

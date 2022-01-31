# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class CustomerPaymentActivity(DataObject):
    """
    | Object containing data on the purchase history of the customer with you
    """

    __number_of_payment_attempts_last24_hours = None
    __number_of_payment_attempts_last_year = None
    __number_of_purchases_last6_months = None

    @property
    def number_of_payment_attempts_last24_hours(self) -> int:
        """
        | Number of payment attempts (so including unsuccessful ones) made by this customer with you in the last 24 hours

        Type: int
        """
        return self.__number_of_payment_attempts_last24_hours

    @number_of_payment_attempts_last24_hours.setter
    def number_of_payment_attempts_last24_hours(self, value: int):
        self.__number_of_payment_attempts_last24_hours = value

    @property
    def number_of_payment_attempts_last_year(self) -> int:
        """
        | Number of payment attempts (so including unsuccessful ones) made by this customer with you in the last 12 months

        Type: int
        """
        return self.__number_of_payment_attempts_last_year

    @number_of_payment_attempts_last_year.setter
    def number_of_payment_attempts_last_year(self, value: int):
        self.__number_of_payment_attempts_last_year = value

    @property
    def number_of_purchases_last6_months(self) -> int:
        """
        | Number of successful purchases made by this customer with you in the last 6 months

        Type: int
        """
        return self.__number_of_purchases_last6_months

    @number_of_purchases_last6_months.setter
    def number_of_purchases_last6_months(self, value: int):
        self.__number_of_purchases_last6_months = value

    def to_dictionary(self):
        dictionary = super(CustomerPaymentActivity, self).to_dictionary()
        if self.number_of_payment_attempts_last24_hours is not None:
            dictionary['numberOfPaymentAttemptsLast24Hours'] = self.number_of_payment_attempts_last24_hours
        if self.number_of_payment_attempts_last_year is not None:
            dictionary['numberOfPaymentAttemptsLastYear'] = self.number_of_payment_attempts_last_year
        if self.number_of_purchases_last6_months is not None:
            dictionary['numberOfPurchasesLast6Months'] = self.number_of_purchases_last6_months
        return dictionary

    def from_dictionary(self, dictionary):
        super(CustomerPaymentActivity, self).from_dictionary(dictionary)
        if 'numberOfPaymentAttemptsLast24Hours' in dictionary:
            self.number_of_payment_attempts_last24_hours = dictionary['numberOfPaymentAttemptsLast24Hours']
        if 'numberOfPaymentAttemptsLastYear' in dictionary:
            self.number_of_payment_attempts_last_year = dictionary['numberOfPaymentAttemptsLastYear']
        if 'numberOfPurchasesLast6Months' in dictionary:
            self.number_of_purchases_last6_months = dictionary['numberOfPurchasesLast6Months']
        return self

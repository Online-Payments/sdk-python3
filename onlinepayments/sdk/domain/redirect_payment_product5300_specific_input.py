# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class RedirectPaymentProduct5300SpecificInput(DataObject):

    __birth_city: Optional[str] = None
    __birth_country: Optional[str] = None
    __birth_zip_code: Optional[str] = None
    __channel: Optional[str] = None
    __loyalty_card_number: Optional[str] = None
    __second_installment_payment_date: Optional[str] = None
    __session_duration: Optional[int] = None

    @property
    def birth_city(self) -> Optional[str]:
        """
        | The city of the address where the customer was born

        Type: str
        """
        return self.__birth_city

    @birth_city.setter
    def birth_city(self, value: Optional[str]) -> None:
        self.__birth_city = value

    @property
    def birth_country(self) -> Optional[str]:
        """
        | ISO 3166-1 alpha-2 country code of the address where the customer was born

        Type: str
        """
        return self.__birth_country

    @birth_country.setter
    def birth_country(self, value: Optional[str]) -> None:
        self.__birth_country = value

    @property
    def birth_zip_code(self) -> Optional[str]:
        """
        | The zip code of the address where the customer was born

        Type: str
        """
        return self.__birth_zip_code

    @birth_zip_code.setter
    def birth_zip_code(self, value: Optional[str]) -> None:
        self.__birth_zip_code = value

    @property
    def channel(self) -> Optional[str]:
        """
        | The channel used by the customer

        Type: str
        """
        return self.__channel

    @channel.setter
    def channel(self, value: Optional[str]) -> None:
        self.__channel = value

    @property
    def loyalty_card_number(self) -> Optional[str]:
        """
        | The number of customer's loyalty card or program

        Type: str
        """
        return self.__loyalty_card_number

    @loyalty_card_number.setter
    def loyalty_card_number(self, value: Optional[str]) -> None:
        self.__loyalty_card_number = value

    @property
    def second_installment_payment_date(self) -> Optional[str]:
        """
        | The date of the second installment (YYYYMMDD)

        Type: str
        """
        return self.__second_installment_payment_date

    @second_installment_payment_date.setter
    def second_installment_payment_date(self, value: Optional[str]) -> None:
        self.__second_installment_payment_date = value

    @property
    def session_duration(self) -> Optional[int]:
        """
        | The duration of the session in seconds

        Type: int
        """
        return self.__session_duration

    @session_duration.setter
    def session_duration(self, value: Optional[int]) -> None:
        self.__session_duration = value

    def to_dictionary(self) -> dict:
        dictionary = super(RedirectPaymentProduct5300SpecificInput, self).to_dictionary()
        if self.birth_city is not None:
            dictionary['birthCity'] = self.birth_city
        if self.birth_country is not None:
            dictionary['birthCountry'] = self.birth_country
        if self.birth_zip_code is not None:
            dictionary['birthZipCode'] = self.birth_zip_code
        if self.channel is not None:
            dictionary['channel'] = self.channel
        if self.loyalty_card_number is not None:
            dictionary['loyaltyCardNumber'] = self.loyalty_card_number
        if self.second_installment_payment_date is not None:
            dictionary['secondInstallmentPaymentDate'] = self.second_installment_payment_date
        if self.session_duration is not None:
            dictionary['sessionDuration'] = self.session_duration
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct5300SpecificInput':
        super(RedirectPaymentProduct5300SpecificInput, self).from_dictionary(dictionary)
        if 'birthCity' in dictionary:
            self.birth_city = dictionary['birthCity']
        if 'birthCountry' in dictionary:
            self.birth_country = dictionary['birthCountry']
        if 'birthZipCode' in dictionary:
            self.birth_zip_code = dictionary['birthZipCode']
        if 'channel' in dictionary:
            self.channel = dictionary['channel']
        if 'loyaltyCardNumber' in dictionary:
            self.loyalty_card_number = dictionary['loyaltyCardNumber']
        if 'secondInstallmentPaymentDate' in dictionary:
            self.second_installment_payment_date = dictionary['secondInstallmentPaymentDate']
        if 'sessionDuration' in dictionary:
            self.session_duration = dictionary['sessionDuration']
        return self

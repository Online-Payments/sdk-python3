#
# This file was automatically generated.
#
from datetime import datetime

from .data_object import DataObject


class RedirectPaymentProduct5300SpecificInput(DataObject):

    __slots__ = (
        "__birth_city",
        "__birth_country",
        "__birth_zip_code",
        "__channel",
        "__loyalty_card_number",
        "__second_installment_payment_date",
        "__session_duration",
        "__title",
        "__transaction_expiration_date_time",
    )

    __birth_city: str | None
    __birth_country: str | None
    __birth_zip_code: str | None
    __channel: str | None
    __loyalty_card_number: str | None
    __second_installment_payment_date: str | None
    __session_duration: int | None
    __title: str | None
    __transaction_expiration_date_time: datetime | None

    def __init__(
        self,
        *,
        birth_city: str | None = None,
        birth_country: str | None = None,
        birth_zip_code: str | None = None,
        channel: str | None = None,
        loyalty_card_number: str | None = None,
        second_installment_payment_date: str | None = None,
        session_duration: int | None = None,
        title: str | None = None,
        transaction_expiration_date_time: datetime | None = None,
    ) -> None:
        self.birth_city = birth_city
        self.birth_country = birth_country
        self.birth_zip_code = birth_zip_code
        self.channel = channel
        self.loyalty_card_number = loyalty_card_number
        self.second_installment_payment_date = second_installment_payment_date
        self.session_duration = session_duration
        self.title = title
        self.transaction_expiration_date_time = transaction_expiration_date_time

    @property
    def birth_city(self) -> str | None:
        """
        | The city of the address where the customer was born

        Type: str
        """
        return self.__birth_city

    @birth_city.setter
    def birth_city(self, value: str | None) -> None:
        self.__birth_city = value

    @property
    def birth_country(self) -> str | None:
        """
        | ISO 3166-1 alpha-2 country code of the address where the customer was born

        Type: str
        """
        return self.__birth_country

    @birth_country.setter
    def birth_country(self, value: str | None) -> None:
        self.__birth_country = value

    @property
    def birth_zip_code(self) -> str | None:
        """
        | The zip code of the address where the customer was born

        Type: str
        """
        return self.__birth_zip_code

    @birth_zip_code.setter
    def birth_zip_code(self, value: str | None) -> None:
        self.__birth_zip_code = value

    @property
    def channel(self) -> str | None:
        """
        | The channel used by the customer

        Type: str
        """
        return self.__channel

    @channel.setter
    def channel(self, value: str | None) -> None:
        self.__channel = value

    @property
    def loyalty_card_number(self) -> str | None:
        """
        | The number of customer's loyalty card or program

        Type: str
        """
        return self.__loyalty_card_number

    @loyalty_card_number.setter
    def loyalty_card_number(self, value: str | None) -> None:
        self.__loyalty_card_number = value

    @property
    def second_installment_payment_date(self) -> str | None:
        """
        | The date of the second installment (YYYYMMDD)

        Type: str
        """
        return self.__second_installment_payment_date

    @second_installment_payment_date.setter
    def second_installment_payment_date(self, value: str | None) -> None:
        self.__second_installment_payment_date = value

    @property
    def session_duration(self) -> int | None:
        """
        | The duration of the session in seconds

        Type: int
        """
        return self.__session_duration

    @session_duration.setter
    def session_duration(self, value: int | None) -> None:
        self.__session_duration = value

    @property
    def title(self) -> str | None:
        """
        | Descriptive text that is used towards the customer, either during an online checkout at a third party or on the customer's statement.

        Type: str
        """
        return self.__title

    @title.setter
    def title(self, value: str | None) -> None:
        self.__title = value

    @property
    def transaction_expiration_date_time(self) -> datetime | None:
        """
        | The date and time after which the transaction will expire in UTC (format YYYY-MM-DDTHH:mm:ssZ)

        Type: datetime
        """
        return self.__transaction_expiration_date_time

    @transaction_expiration_date_time.setter
    def transaction_expiration_date_time(self, value: datetime | None) -> None:
        self.__transaction_expiration_date_time = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
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
        if self.title is not None:
            dictionary['title'] = self.title
        if self.transaction_expiration_date_time is not None:
            dictionary['transactionExpirationDateTime'] = DataObject.format_datetime(self.transaction_expiration_date_time)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct5300SpecificInput':
        super().from_dictionary(dictionary)
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
        if 'title' in dictionary:
            self.title = dictionary['title']
        if 'transactionExpirationDateTime' in dictionary:
            self.transaction_expiration_date_time = DataObject.parse_datetime(dictionary['transactionExpirationDateTime'])
        return self

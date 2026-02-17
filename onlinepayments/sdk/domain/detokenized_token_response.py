# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class DetokenizedTokenResponse(DataObject):

    __card_brand: Optional[str] = None
    __card_expiry_date: Optional[str] = None
    __card_holder_name: Optional[str] = None
    __encrypted_card_number: Optional[str] = None
    __payment_id: Optional[str] = None
    __scheme_reference_data: Optional[str] = None
    __token: Optional[str] = None

    @property
    def card_brand(self) -> Optional[str]:
        """
        | The brand of the card (e.g., VISA, MasterCard).

        Type: str
        """
        return self.__card_brand

    @card_brand.setter
    def card_brand(self, value: Optional[str]) -> None:
        self.__card_brand = value

    @property
    def card_expiry_date(self) -> Optional[str]:
        """
        | The expiration date of the card in MMYY format, where MM represents the two-digit month and YY represents the two-digit year. For example, a value of 0529 indicates that the card expires in May 2029.

        Type: str
        """
        return self.__card_expiry_date

    @card_expiry_date.setter
    def card_expiry_date(self, value: Optional[str]) -> None:
        self.__card_expiry_date = value

    @property
    def card_holder_name(self) -> Optional[str]:
        """
        | The full name of the cardholder as it appears on the card.

        Type: str
        """
        return self.__card_holder_name

    @card_holder_name.setter
    def card_holder_name(self, value: Optional[str]) -> None:
        self.__card_holder_name = value

    @property
    def encrypted_card_number(self) -> Optional[str]:
        """
        | The card number, encrypted and Base64 encoded for secure transport.

        Type: str
        """
        return self.__encrypted_card_number

    @encrypted_card_number.setter
    def encrypted_card_number(self, value: Optional[str]) -> None:
        self.__encrypted_card_number = value

    @property
    def payment_id(self) -> Optional[str]:
        """
        | The unique identifier for the payment associated with the token is necessary for tracking.

        Type: str
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value: Optional[str]) -> None:
        self.__payment_id = value

    @property
    def scheme_reference_data(self) -> Optional[str]:
        """
        | Reference data associated with the payment scheme for the credentials on file.

        Type: str
        """
        return self.__scheme_reference_data

    @scheme_reference_data.setter
    def scheme_reference_data(self, value: Optional[str]) -> None:
        self.__scheme_reference_data = value

    @property
    def token(self) -> Optional[str]:
        """
        | The unique identifier for the token is required for processing.

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: Optional[str]) -> None:
        self.__token = value

    def to_dictionary(self) -> dict:
        dictionary = super(DetokenizedTokenResponse, self).to_dictionary()
        if self.card_brand is not None:
            dictionary['cardBrand'] = self.card_brand
        if self.card_expiry_date is not None:
            dictionary['cardExpiryDate'] = self.card_expiry_date
        if self.card_holder_name is not None:
            dictionary['cardHolderName'] = self.card_holder_name
        if self.encrypted_card_number is not None:
            dictionary['encryptedCardNumber'] = self.encrypted_card_number
        if self.payment_id is not None:
            dictionary['paymentId'] = self.payment_id
        if self.scheme_reference_data is not None:
            dictionary['schemeReferenceData'] = self.scheme_reference_data
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DetokenizedTokenResponse':
        super(DetokenizedTokenResponse, self).from_dictionary(dictionary)
        if 'cardBrand' in dictionary:
            self.card_brand = dictionary['cardBrand']
        if 'cardExpiryDate' in dictionary:
            self.card_expiry_date = dictionary['cardExpiryDate']
        if 'cardHolderName' in dictionary:
            self.card_holder_name = dictionary['cardHolderName']
        if 'encryptedCardNumber' in dictionary:
            self.encrypted_card_number = dictionary['encryptedCardNumber']
        if 'paymentId' in dictionary:
            self.payment_id = dictionary['paymentId']
        if 'schemeReferenceData' in dictionary:
            self.scheme_reference_data = dictionary['schemeReferenceData']
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self

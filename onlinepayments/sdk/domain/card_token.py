# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class CardToken(DataObject):

    __cardholder_name: Optional[str] = None
    __expiry_date: Optional[str] = None
    __logo_url: Optional[str] = None
    __masked_pan: Optional[str] = None
    __payment_product_id: Optional[int] = None
    __product_name: Optional[str] = None
    __token: Optional[str] = None

    @property
    def cardholder_name(self) -> Optional[str]:
        """
        | The card holder's name on the card.

        Type: str
        """
        return self.__cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, value: Optional[str]) -> None:
        self.__cardholder_name = value

    @property
    def expiry_date(self) -> Optional[str]:
        """
        | Expiry date of the card Format: MMYY

        Type: str
        """
        return self.__expiry_date

    @expiry_date.setter
    def expiry_date(self, value: Optional[str]) -> None:
        self.__expiry_date = value

    @property
    def logo_url(self) -> Optional[str]:
        """
        | URL to the card product logo.

        Type: str
        """
        return self.__logo_url

    @logo_url.setter
    def logo_url(self, value: Optional[str]) -> None:
        self.__logo_url = value

    @property
    def masked_pan(self) -> Optional[str]:
        """
        | The masked Primary Account Number (PAN).

        Type: str
        """
        return self.__masked_pan

    @masked_pan.setter
    def masked_pan(self, value: Optional[str]) -> None:
        self.__masked_pan = value

    @property
    def payment_product_id(self) -> Optional[int]:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: Optional[int]) -> None:
        self.__payment_product_id = value

    @property
    def product_name(self) -> Optional[str]:
        """
        | Product name of the card

        Type: str
        """
        return self.__product_name

    @product_name.setter
    def product_name(self, value: Optional[str]) -> None:
        self.__product_name = value

    @property
    def token(self) -> Optional[str]:
        """
        | This is a validated card token available for later use.

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: Optional[str]) -> None:
        self.__token = value

    def to_dictionary(self) -> dict:
        dictionary = super(CardToken, self).to_dictionary()
        if self.cardholder_name is not None:
            dictionary['cardholderName'] = self.cardholder_name
        if self.expiry_date is not None:
            dictionary['expiryDate'] = self.expiry_date
        if self.logo_url is not None:
            dictionary['logoUrl'] = self.logo_url
        if self.masked_pan is not None:
            dictionary['maskedPan'] = self.masked_pan
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        if self.product_name is not None:
            dictionary['productName'] = self.product_name
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardToken':
        super(CardToken, self).from_dictionary(dictionary)
        if 'cardholderName' in dictionary:
            self.cardholder_name = dictionary['cardholderName']
        if 'expiryDate' in dictionary:
            self.expiry_date = dictionary['expiryDate']
        if 'logoUrl' in dictionary:
            self.logo_url = dictionary['logoUrl']
        if 'maskedPan' in dictionary:
            self.masked_pan = dictionary['maskedPan']
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'productName' in dictionary:
            self.product_name = dictionary['productName']
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self

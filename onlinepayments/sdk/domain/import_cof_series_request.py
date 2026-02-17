# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .card_data_without_cvv import CardDataWithoutCvv
from .data_object import DataObject


class ImportCofSeriesRequest(DataObject):

    __card: Optional[CardDataWithoutCvv] = None
    __currency_code: Optional[str] = None
    __payment_product_id: Optional[int] = None
    __scheme_reference_data: Optional[str] = None
    __token_id: Optional[str] = None

    @property
    def card(self) -> Optional[CardDataWithoutCvv]:
        """
        | Object containing card details, which should be used if a tokenID is not provided.

        Type: :class:`onlinepayments.sdk.domain.card_data_without_cvv.CardDataWithoutCvv`
        """
        return self.__card

    @card.setter
    def card(self, value: Optional[CardDataWithoutCvv]) -> None:
        self.__card = value

    @property
    def currency_code(self) -> Optional[str]:
        """
        | Three-letter ISO currency code representing the currency for the initial payment.

        Type: str
        """
        return self.__currency_code

    @currency_code.setter
    def currency_code(self, value: Optional[str]) -> None:
        self.__currency_code = value

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
    def scheme_reference_data(self) -> Optional[str]:
        """
        | Scheme Reference Data (SRD) used for scheme-level routing or identification.

        Type: str
        """
        return self.__scheme_reference_data

    @scheme_reference_data.setter
    def scheme_reference_data(self, value: Optional[str]) -> None:
        self.__scheme_reference_data = value

    @property
    def token_id(self) -> Optional[str]:
        """
        | ID of the token to use to create the payment series.

        Type: str
        """
        return self.__token_id

    @token_id.setter
    def token_id(self, value: Optional[str]) -> None:
        self.__token_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(ImportCofSeriesRequest, self).to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.currency_code is not None:
            dictionary['currencyCode'] = self.currency_code
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        if self.scheme_reference_data is not None:
            dictionary['schemeReferenceData'] = self.scheme_reference_data
        if self.token_id is not None:
            dictionary['tokenId'] = self.token_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ImportCofSeriesRequest':
        super(ImportCofSeriesRequest, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = CardDataWithoutCvv()
            self.card = value.from_dictionary(dictionary['card'])
        if 'currencyCode' in dictionary:
            self.currency_code = dictionary['currencyCode']
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'schemeReferenceData' in dictionary:
            self.scheme_reference_data = dictionary['schemeReferenceData']
        if 'tokenId' in dictionary:
            self.token_id = dictionary['tokenId']
        return self

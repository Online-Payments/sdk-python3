# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from datetime import date
from typing import List, Optional

from .data_object import DataObject
from .iin_detail import IINDetail


class GetIINDetailsResponse(DataObject):

    __card_corporate_indicator: Optional[bool] = None
    __card_effective_date: Optional[date] = None
    __card_effective_date_indicator: Optional[bool] = None
    __card_pan_type: Optional[str] = None
    __card_product_code: Optional[str] = None
    __card_product_usage_label: Optional[str] = None
    __card_scheme: Optional[str] = None
    __card_type: Optional[str] = None
    __co_brands: Optional[List[IINDetail]] = None
    __country_code: Optional[str] = None
    __is_allowed_in_context: Optional[bool] = None
    __issuer_code: Optional[str] = None
    __issuer_name: Optional[str] = None
    __issuing_country_code: Optional[str] = None
    __pan_length_max: Optional[int] = None
    __pan_length_min: Optional[int] = None
    __pan_luhn_check: Optional[bool] = None
    __payment_product_id: Optional[int] = None

    @property
    def card_corporate_indicator(self) -> Optional[bool]:
        """
        | Indicates whether the card is an Enterprise / Commercial card or not

        Type: bool
        """
        return self.__card_corporate_indicator

    @card_corporate_indicator.setter
    def card_corporate_indicator(self, value: Optional[bool]) -> None:
        self.__card_corporate_indicator = value

    @property
    def card_effective_date(self) -> Optional[date]:
        """
        | The card effective date (YYYY-MM-DD)

        Type: date
        """
        return self.__card_effective_date

    @card_effective_date.setter
    def card_effective_date(self, value: Optional[date]) -> None:
        self.__card_effective_date = value

    @property
    def card_effective_date_indicator(self) -> Optional[bool]:
        """
        | Indicator of existence of a card effective date

        Type: bool
        """
        return self.__card_effective_date_indicator

    @card_effective_date_indicator.setter
    def card_effective_date_indicator(self, value: Optional[bool]) -> None:
        self.__card_effective_date_indicator = value

    @property
    def card_pan_type(self) -> Optional[str]:
        """
        | PAN type sent
        
        * ``dpan`` Digital PAN
        * ``pan`` Real PAN

        Type: str
        """
        return self.__card_pan_type

    @card_pan_type.setter
    def card_pan_type(self, value: Optional[str]) -> None:
        self.__card_pan_type = value

    @property
    def card_product_code(self) -> Optional[str]:
        """
        | Product code of the card

        Type: str
        """
        return self.__card_product_code

    @card_product_code.setter
    def card_product_code(self, value: Optional[str]) -> None:
        self.__card_product_code = value

    @property
    def card_product_usage_label(self) -> Optional[str]:
        """
        | Profile name of the card which is displayed on payment electronic ticket in accordance with MPADS requirements
        
        * ``commercial`` Business card
        * ``credit`` Credit card
        * ``debit`` Debit card
        * ``prepaid`` Prepaid card

        Type: str
        """
        return self.__card_product_usage_label

    @card_product_usage_label.setter
    def card_product_usage_label(self, value: Optional[str]) -> None:
        self.__card_product_usage_label = value

    @property
    def card_scheme(self) -> Optional[str]:
        """
        | Network name associated with the card that is informational only and not to be coded against
        
        * ``AmericanExpress`` American Express scheme
        * ``Bancontact`` Bancontact scheme
        * ``Cb`` Cartes Bancaires scheme
        * ``Cup`` China UnionPay scheme
        * ``Dankort`` Dankort scheme
        * ``DinersDiscover`` Diners Discover scheme
        * ``Eftpos`` eftpos scheme
        * ``Jcb`` Japan Credit Bureau scheme
        * ``Mastercard`` Mastercard scheme
        * ``Oney`` Oney scheme
        * ``Uatp`` Universal Air Travel Plan scheme
        * ``Visa`` Visa scheme

        Type: str
        """
        return self.__card_scheme

    @card_scheme.setter
    def card_scheme(self, value: Optional[str]) -> None:
        self.__card_scheme = value

    @property
    def card_type(self) -> Optional[str]:
        """
        | The card's type as categorised by the payment method. Possible values are:
        
        * Credit
        * Debit
        * Prepaid

        Type: str
        """
        return self.__card_type

    @card_type.setter
    def card_type(self, value: Optional[str]) -> None:
        self.__card_type = value

    @property
    def co_brands(self) -> Optional[List[IINDetail]]:
        """
        | List of IIN details

        Type: list[:class:`onlinepayments.sdk.domain.iin_detail.IINDetail`]
        """
        return self.__co_brands

    @co_brands.setter
    def co_brands(self, value: Optional[List[IINDetail]]) -> None:
        self.__co_brands = value

    @property
    def country_code(self) -> Optional[str]:
        """
        | The ISO 3166-1 alpha-2 country code of the country where the card was issued. If we do not know where the card was issued, then the countryCode will return the value '99'.

        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value: Optional[str]) -> None:
        self.__country_code = value

    @property
    def is_allowed_in_context(self) -> Optional[bool]:
        """
        | Populated only if you submitted a payment context.
        
        * true - The payment product is allowed in the submitted context.
        * false - The payment product is not allowed in the submitted context. Note that in this case, none of the brands of the card will be allowed in the submitted context.

        Type: bool
        """
        return self.__is_allowed_in_context

    @is_allowed_in_context.setter
    def is_allowed_in_context(self, value: Optional[bool]) -> None:
        self.__is_allowed_in_context = value

    @property
    def issuer_code(self) -> Optional[str]:
        """
        | Issuer code of the card

        Type: str
        """
        return self.__issuer_code

    @issuer_code.setter
    def issuer_code(self, value: Optional[str]) -> None:
        self.__issuer_code = value

    @property
    def issuer_name(self) -> Optional[str]:
        """
        | Issuer name of the card

        Type: str
        """
        return self.__issuer_name

    @issuer_name.setter
    def issuer_name(self, value: Optional[str]) -> None:
        self.__issuer_name = value

    @property
    def issuing_country_code(self) -> Optional[str]:
        """
        | ISO 3166-1 alpha-2 country code in which the card has been issued

        Type: str
        """
        return self.__issuing_country_code

    @issuing_country_code.setter
    def issuing_country_code(self, value: Optional[str]) -> None:
        self.__issuing_country_code = value

    @property
    def pan_length_max(self) -> Optional[int]:
        """
        | Maximum length of the PAN

        Type: int
        """
        return self.__pan_length_max

    @pan_length_max.setter
    def pan_length_max(self, value: Optional[int]) -> None:
        self.__pan_length_max = value

    @property
    def pan_length_min(self) -> Optional[int]:
        """
        | Minimal length of the PAN

        Type: int
        """
        return self.__pan_length_min

    @pan_length_min.setter
    def pan_length_min(self, value: Optional[int]) -> None:
        self.__pan_length_min = value

    @property
    def pan_luhn_check(self) -> Optional[bool]:
        """
        | Indicates whether the PAN is controlled with Lühn Key algorithm

        Type: bool
        """
        return self.__pan_luhn_check

    @pan_luhn_check.setter
    def pan_luhn_check(self, value: Optional[bool]) -> None:
        self.__pan_luhn_check = value

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

    def to_dictionary(self) -> dict:
        dictionary = super(GetIINDetailsResponse, self).to_dictionary()
        if self.card_corporate_indicator is not None:
            dictionary['cardCorporateIndicator'] = self.card_corporate_indicator
        if self.card_effective_date is not None:
            dictionary['cardEffectiveDate'] = DataObject.format_date(self.card_effective_date)
        if self.card_effective_date_indicator is not None:
            dictionary['cardEffectiveDateIndicator'] = self.card_effective_date_indicator
        if self.card_pan_type is not None:
            dictionary['cardPanType'] = self.card_pan_type
        if self.card_product_code is not None:
            dictionary['cardProductCode'] = self.card_product_code
        if self.card_product_usage_label is not None:
            dictionary['cardProductUsageLabel'] = self.card_product_usage_label
        if self.card_scheme is not None:
            dictionary['cardScheme'] = self.card_scheme
        if self.card_type is not None:
            dictionary['cardType'] = self.card_type
        if self.co_brands is not None:
            dictionary['coBrands'] = []
            for element in self.co_brands:
                if element is not None:
                    dictionary['coBrands'].append(element.to_dictionary())
        if self.country_code is not None:
            dictionary['countryCode'] = self.country_code
        if self.is_allowed_in_context is not None:
            dictionary['isAllowedInContext'] = self.is_allowed_in_context
        if self.issuer_code is not None:
            dictionary['issuerCode'] = self.issuer_code
        if self.issuer_name is not None:
            dictionary['issuerName'] = self.issuer_name
        if self.issuing_country_code is not None:
            dictionary['issuingCountryCode'] = self.issuing_country_code
        if self.pan_length_max is not None:
            dictionary['panLengthMax'] = self.pan_length_max
        if self.pan_length_min is not None:
            dictionary['panLengthMin'] = self.pan_length_min
        if self.pan_luhn_check is not None:
            dictionary['panLuhnCheck'] = self.pan_luhn_check
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'GetIINDetailsResponse':
        super(GetIINDetailsResponse, self).from_dictionary(dictionary)
        if 'cardCorporateIndicator' in dictionary:
            self.card_corporate_indicator = dictionary['cardCorporateIndicator']
        if 'cardEffectiveDate' in dictionary:
            self.card_effective_date = DataObject.parse_date(dictionary['cardEffectiveDate'])
        if 'cardEffectiveDateIndicator' in dictionary:
            self.card_effective_date_indicator = dictionary['cardEffectiveDateIndicator']
        if 'cardPanType' in dictionary:
            self.card_pan_type = dictionary['cardPanType']
        if 'cardProductCode' in dictionary:
            self.card_product_code = dictionary['cardProductCode']
        if 'cardProductUsageLabel' in dictionary:
            self.card_product_usage_label = dictionary['cardProductUsageLabel']
        if 'cardScheme' in dictionary:
            self.card_scheme = dictionary['cardScheme']
        if 'cardType' in dictionary:
            self.card_type = dictionary['cardType']
        if 'coBrands' in dictionary:
            if not isinstance(dictionary['coBrands'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['coBrands']))
            self.co_brands = []
            for element in dictionary['coBrands']:
                value = IINDetail()
                self.co_brands.append(value.from_dictionary(element))
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'isAllowedInContext' in dictionary:
            self.is_allowed_in_context = dictionary['isAllowedInContext']
        if 'issuerCode' in dictionary:
            self.issuer_code = dictionary['issuerCode']
        if 'issuerName' in dictionary:
            self.issuer_name = dictionary['issuerName']
        if 'issuingCountryCode' in dictionary:
            self.issuing_country_code = dictionary['issuingCountryCode']
        if 'panLengthMax' in dictionary:
            self.pan_length_max = dictionary['panLengthMax']
        if 'panLengthMin' in dictionary:
            self.pan_length_min = dictionary['panLengthMin']
        if 'panLuhnCheck' in dictionary:
            self.pan_luhn_check = dictionary['panLuhnCheck']
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self

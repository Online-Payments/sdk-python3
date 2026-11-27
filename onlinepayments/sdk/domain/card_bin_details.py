#
# This file was automatically generated.
#
from datetime import date

from .data_object import DataObject


class CardBinDetails(DataObject):

    __slots__ = (
        "__card_corporate_indicator",
        "__card_effective_date",
        "__card_effective_date_indicator",
        "__card_pan_type",
        "__card_product_code",
        "__card_product_name",
        "__card_product_usage_label",
        "__card_scheme",
        "__card_type",
        "__country_code",
        "__issuer_code",
        "__issuer_name",
        "__issuer_principal_member_code",
        "__issuer_principal_member_name",
        "__issuer_region_code",
        "__issuing_country_code",
        "__pan_length_max",
        "__pan_length_min",
        "__pan_luhn_check",
        "__virtual_card_indicator",
    )

    __card_corporate_indicator: bool | None
    __card_effective_date: date | None
    __card_effective_date_indicator: bool | None
    __card_pan_type: str | None
    __card_product_code: str | None
    __card_product_name: str | None
    __card_product_usage_label: str | None
    __card_scheme: str | None
    __card_type: str | None
    __country_code: str | None
    __issuer_code: str | None
    __issuer_name: str | None
    __issuer_principal_member_code: str | None
    __issuer_principal_member_name: str | None
    __issuer_region_code: str | None
    __issuing_country_code: str | None
    __pan_length_max: int | None
    __pan_length_min: int | None
    __pan_luhn_check: bool | None
    __virtual_card_indicator: bool | None

    def __init__(
        self,
        *,
        card_corporate_indicator: bool | None = None,
        card_effective_date: date | None = None,
        card_effective_date_indicator: bool | None = None,
        card_pan_type: str | None = None,
        card_product_code: str | None = None,
        card_product_name: str | None = None,
        card_product_usage_label: str | None = None,
        card_scheme: str | None = None,
        card_type: str | None = None,
        country_code: str | None = None,
        issuer_code: str | None = None,
        issuer_name: str | None = None,
        issuer_principal_member_code: str | None = None,
        issuer_principal_member_name: str | None = None,
        issuer_region_code: str | None = None,
        issuing_country_code: str | None = None,
        pan_length_max: int | None = None,
        pan_length_min: int | None = None,
        pan_luhn_check: bool | None = None,
        virtual_card_indicator: bool | None = None,
    ) -> None:
        self.card_corporate_indicator = card_corporate_indicator
        self.card_effective_date = card_effective_date
        self.card_effective_date_indicator = card_effective_date_indicator
        self.card_pan_type = card_pan_type
        self.card_product_code = card_product_code
        self.card_product_name = card_product_name
        self.card_product_usage_label = card_product_usage_label
        self.card_scheme = card_scheme
        self.card_type = card_type
        self.country_code = country_code
        self.issuer_code = issuer_code
        self.issuer_name = issuer_name
        self.issuer_principal_member_code = issuer_principal_member_code
        self.issuer_principal_member_name = issuer_principal_member_name
        self.issuer_region_code = issuer_region_code
        self.issuing_country_code = issuing_country_code
        self.pan_length_max = pan_length_max
        self.pan_length_min = pan_length_min
        self.pan_luhn_check = pan_luhn_check
        self.virtual_card_indicator = virtual_card_indicator

    @property
    def card_corporate_indicator(self) -> bool | None:
        """
        | Indicates whether the card is an Enterprise / Commercial card or not

        Type: bool
        """
        return self.__card_corporate_indicator

    @card_corporate_indicator.setter
    def card_corporate_indicator(self, value: bool | None) -> None:
        self.__card_corporate_indicator = value

    @property
    def card_effective_date(self) -> date | None:
        """
        | The card effective date (YYYY-MM-DD)

        Type: date
        """
        return self.__card_effective_date

    @card_effective_date.setter
    def card_effective_date(self, value: date | None) -> None:
        self.__card_effective_date = value

    @property
    def card_effective_date_indicator(self) -> bool | None:
        """
        | Indicator of existence of a card effective date

        Type: bool
        """
        return self.__card_effective_date_indicator

    @card_effective_date_indicator.setter
    def card_effective_date_indicator(self, value: bool | None) -> None:
        self.__card_effective_date_indicator = value

    @property
    def card_pan_type(self) -> str | None:
        """
        | PAN type sent
        
        * ``dpan`` Digital PAN
        * ``pan`` Real PAN

        Type: str
        """
        return self.__card_pan_type

    @card_pan_type.setter
    def card_pan_type(self, value: str | None) -> None:
        self.__card_pan_type = value

    @property
    def card_product_code(self) -> str | None:
        """
        | Product code of the card

        Type: str
        """
        return self.__card_product_code

    @card_product_code.setter
    def card_product_code(self, value: str | None) -> None:
        self.__card_product_code = value

    @property
    def card_product_name(self) -> str | None:
        """
        | Product name of the card

        Type: str
        """
        return self.__card_product_name

    @card_product_name.setter
    def card_product_name(self, value: str | None) -> None:
        self.__card_product_name = value

    @property
    def card_product_usage_label(self) -> str | None:
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
    def card_product_usage_label(self, value: str | None) -> None:
        self.__card_product_usage_label = value

    @property
    def card_scheme(self) -> str | None:
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
    def card_scheme(self, value: str | None) -> None:
        self.__card_scheme = value

    @property
    def card_type(self) -> str | None:
        """
        | The card's type as categorised by the payment method. Possible values are:
        
        * Credit
        * Debit
        * Prepaid

        Type: str
        """
        return self.__card_type

    @card_type.setter
    def card_type(self, value: str | None) -> None:
        self.__card_type = value

    @property
    def country_code(self) -> str | None:
        """
        | ISO 3166-1 alpha-2 country code of the card issuer

        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value: str | None) -> None:
        self.__country_code = value

    @property
    def issuer_code(self) -> str | None:
        """
        | Issuer code of the card

        Type: str
        """
        return self.__issuer_code

    @issuer_code.setter
    def issuer_code(self, value: str | None) -> None:
        self.__issuer_code = value

    @property
    def issuer_name(self) -> str | None:
        """
        | Issuer name of the card

        Type: str
        """
        return self.__issuer_name

    @issuer_name.setter
    def issuer_name(self, value: str | None) -> None:
        self.__issuer_name = value

    @property
    def issuer_principal_member_code(self) -> str | None:
        """
        | Code that identifies the principal member within an issuer group

        Type: str
        """
        return self.__issuer_principal_member_code

    @issuer_principal_member_code.setter
    def issuer_principal_member_code(self, value: str | None) -> None:
        self.__issuer_principal_member_code = value

    @property
    def issuer_principal_member_name(self) -> str | None:
        """
        | Name that identifies the principal member within an issuer group

        Type: str
        """
        return self.__issuer_principal_member_name

    @issuer_principal_member_name.setter
    def issuer_principal_member_name(self, value: str | None) -> None:
        self.__issuer_principal_member_name = value

    @property
    def issuer_region_code(self) -> str | None:
        """
        | Region code of the card issuer
        
        * ``1`` USA: California, Hawaii, Nevada
        * ``2`` USA: West except California, Hawaii, Nevada
        * ``3`` USA: Central North
        * ``4`` USA: Central South
        * ``5`` USA: Great Lakes states
        * ``6`` USA: South East
        * ``7`` USA: Extreme North East
        * ``8`` USA: North East
        * ``9`` USA: Florida and Georgia
        * ``a`` Canada
        * ``b`` South America
        * ``c`` Oceania and Asia
        * ``d`` Europe
        * ``e`` Africa and Middle East

        Type: str
        """
        return self.__issuer_region_code

    @issuer_region_code.setter
    def issuer_region_code(self, value: str | None) -> None:
        self.__issuer_region_code = value

    @property
    def issuing_country_code(self) -> str | None:
        """
        | ISO 3166-1 alpha-2 country code in which the card has been issued

        Type: str
        """
        return self.__issuing_country_code

    @issuing_country_code.setter
    def issuing_country_code(self, value: str | None) -> None:
        self.__issuing_country_code = value

    @property
    def pan_length_max(self) -> int | None:
        """
        | Maximum length of the PAN

        Type: int
        """
        return self.__pan_length_max

    @pan_length_max.setter
    def pan_length_max(self, value: int | None) -> None:
        self.__pan_length_max = value

    @property
    def pan_length_min(self) -> int | None:
        """
        | Minimal length of the PAN

        Type: int
        """
        return self.__pan_length_min

    @pan_length_min.setter
    def pan_length_min(self, value: int | None) -> None:
        self.__pan_length_min = value

    @property
    def pan_luhn_check(self) -> bool | None:
        """
        | Indicates whether the PAN is controlled with Lühn Key algorithm

        Type: bool
        """
        return self.__pan_luhn_check

    @pan_luhn_check.setter
    def pan_luhn_check(self, value: bool | None) -> None:
        self.__pan_luhn_check = value

    @property
    def virtual_card_indicator(self) -> bool | None:
        """
        | Indicates whether the card is a virtual card

        Type: bool
        """
        return self.__virtual_card_indicator

    @virtual_card_indicator.setter
    def virtual_card_indicator(self, value: bool | None) -> None:
        self.__virtual_card_indicator = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
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
        if self.card_product_name is not None:
            dictionary['cardProductName'] = self.card_product_name
        if self.card_product_usage_label is not None:
            dictionary['cardProductUsageLabel'] = self.card_product_usage_label
        if self.card_scheme is not None:
            dictionary['cardScheme'] = self.card_scheme
        if self.card_type is not None:
            dictionary['cardType'] = self.card_type
        if self.country_code is not None:
            dictionary['countryCode'] = self.country_code
        if self.issuer_code is not None:
            dictionary['issuerCode'] = self.issuer_code
        if self.issuer_name is not None:
            dictionary['issuerName'] = self.issuer_name
        if self.issuer_principal_member_code is not None:
            dictionary['issuerPrincipalMemberCode'] = self.issuer_principal_member_code
        if self.issuer_principal_member_name is not None:
            dictionary['issuerPrincipalMemberName'] = self.issuer_principal_member_name
        if self.issuer_region_code is not None:
            dictionary['issuerRegionCode'] = self.issuer_region_code
        if self.issuing_country_code is not None:
            dictionary['issuingCountryCode'] = self.issuing_country_code
        if self.pan_length_max is not None:
            dictionary['panLengthMax'] = self.pan_length_max
        if self.pan_length_min is not None:
            dictionary['panLengthMin'] = self.pan_length_min
        if self.pan_luhn_check is not None:
            dictionary['panLuhnCheck'] = self.pan_luhn_check
        if self.virtual_card_indicator is not None:
            dictionary['virtualCardIndicator'] = self.virtual_card_indicator
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardBinDetails':
        super().from_dictionary(dictionary)
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
        if 'cardProductName' in dictionary:
            self.card_product_name = dictionary['cardProductName']
        if 'cardProductUsageLabel' in dictionary:
            self.card_product_usage_label = dictionary['cardProductUsageLabel']
        if 'cardScheme' in dictionary:
            self.card_scheme = dictionary['cardScheme']
        if 'cardType' in dictionary:
            self.card_type = dictionary['cardType']
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'issuerCode' in dictionary:
            self.issuer_code = dictionary['issuerCode']
        if 'issuerName' in dictionary:
            self.issuer_name = dictionary['issuerName']
        if 'issuerPrincipalMemberCode' in dictionary:
            self.issuer_principal_member_code = dictionary['issuerPrincipalMemberCode']
        if 'issuerPrincipalMemberName' in dictionary:
            self.issuer_principal_member_name = dictionary['issuerPrincipalMemberName']
        if 'issuerRegionCode' in dictionary:
            self.issuer_region_code = dictionary['issuerRegionCode']
        if 'issuingCountryCode' in dictionary:
            self.issuing_country_code = dictionary['issuingCountryCode']
        if 'panLengthMax' in dictionary:
            self.pan_length_max = dictionary['panLengthMax']
        if 'panLengthMin' in dictionary:
            self.pan_length_min = dictionary['panLengthMin']
        if 'panLuhnCheck' in dictionary:
            self.pan_luhn_check = dictionary['panLuhnCheck']
        if 'virtualCardIndicator' in dictionary:
            self.virtual_card_indicator = dictionary['virtualCardIndicator']
        return self

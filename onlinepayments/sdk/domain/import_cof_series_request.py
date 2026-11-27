#
# This file was automatically generated.
#
from .card_data_without_cvv import CardDataWithoutCvv
from .data_object import DataObject
from .network_token_data import NetworkTokenData
from .sub_merchant import SubMerchant


class ImportCofSeriesRequest(DataObject):

    __slots__ = (
        "__card",
        "__currency_code",
        "__network_token_data",
        "__payment_product_id",
        "__scheme_reference_data",
        "__sub_merchant",
        "__token_id",
        "__transaction_link_identifier",
    )

    __card: CardDataWithoutCvv | None
    __currency_code: str | None
    __network_token_data: NetworkTokenData | None
    __payment_product_id: int | None
    __scheme_reference_data: str | None
    __sub_merchant: SubMerchant | None
    __token_id: str | None
    __transaction_link_identifier: str | None

    def __init__(
        self,
        *,
        card: CardDataWithoutCvv | None = None,
        currency_code: str | None = None,
        network_token_data: NetworkTokenData | None = None,
        payment_product_id: int | None = None,
        scheme_reference_data: str | None = None,
        sub_merchant: SubMerchant | None = None,
        token_id: str | None = None,
        transaction_link_identifier: str | None = None,
    ) -> None:
        self.card = card
        self.currency_code = currency_code
        self.network_token_data = network_token_data
        self.payment_product_id = payment_product_id
        self.scheme_reference_data = scheme_reference_data
        self.sub_merchant = sub_merchant
        self.token_id = token_id
        self.transaction_link_identifier = transaction_link_identifier

    @property
    def card(self) -> CardDataWithoutCvv | None:
        """
        | Object containing card details, which should be used if a tokenID is not provided.

        Type: :class:`onlinepayments.sdk.domain.card_data_without_cvv.CardDataWithoutCvv`
        """
        return self.__card

    @card.setter
    def card(self, value: CardDataWithoutCvv | None) -> None:
        self.__card = value

    @property
    def currency_code(self) -> str | None:
        """
        | Three-letter ISO currency code representing the currency for the initial payment.

        Type: str
        """
        return self.__currency_code

    @currency_code.setter
    def currency_code(self, value: str | None) -> None:
        self.__currency_code = value

    @property
    def network_token_data(self) -> NetworkTokenData | None:
        """
        | Object containing Network Token details

        Type: :class:`onlinepayments.sdk.domain.network_token_data.NetworkTokenData`
        """
        return self.__network_token_data

    @network_token_data.setter
    def network_token_data(self, value: NetworkTokenData | None) -> None:
        self.__network_token_data = value

    @property
    def payment_product_id(self) -> int | None:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: int | None) -> None:
        self.__payment_product_id = value

    @property
    def scheme_reference_data(self) -> str | None:
        """
        | Scheme Reference Data (SRD) used for scheme-level routing or identification.

        Type: str
        """
        return self.__scheme_reference_data

    @scheme_reference_data.setter
    def scheme_reference_data(self, value: str | None) -> None:
        self.__scheme_reference_data = value

    @property
    def sub_merchant(self) -> SubMerchant | None:
        """
        | When a company decides to operate as a payment facilitator, it obtains a payment facilitator account from an acquirer and aggregates payment transactions for its merchant portfolio through that account. For this reason, payment facilitators’ merchant customers are known as submerchants.

        Type: :class:`onlinepayments.sdk.domain.sub_merchant.SubMerchant`
        """
        return self.__sub_merchant

    @sub_merchant.setter
    def sub_merchant(self, value: SubMerchant | None) -> None:
        self.__sub_merchant = value

    @property
    def token_id(self) -> str | None:
        """
        | ID of the token to use to create the payment series.

        Type: str
        """
        return self.__token_id

    @token_id.setter
    def token_id(self, value: str | None) -> None:
        self.__token_id = value

    @property
    def transaction_link_identifier(self) -> str | None:
        """
        | The Transaction Link Identifier (TLID) of the original Consumer-Initiated Transaction (CIT).

        Type: str
        """
        return self.__transaction_link_identifier

    @transaction_link_identifier.setter
    def transaction_link_identifier(self, value: str | None) -> None:
        self.__transaction_link_identifier = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.currency_code is not None:
            dictionary['currencyCode'] = self.currency_code
        if self.network_token_data is not None:
            dictionary['networkTokenData'] = self.network_token_data.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        if self.scheme_reference_data is not None:
            dictionary['schemeReferenceData'] = self.scheme_reference_data
        if self.sub_merchant is not None:
            dictionary['subMerchant'] = self.sub_merchant.to_dictionary()
        if self.token_id is not None:
            dictionary['tokenId'] = self.token_id
        if self.transaction_link_identifier is not None:
            dictionary['transactionLinkIdentifier'] = self.transaction_link_identifier
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ImportCofSeriesRequest':
        super().from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = CardDataWithoutCvv()
            self.card = value.from_dictionary(dictionary['card'])
        if 'currencyCode' in dictionary:
            self.currency_code = dictionary['currencyCode']
        if 'networkTokenData' in dictionary:
            if not isinstance(dictionary['networkTokenData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['networkTokenData']))
            value = NetworkTokenData()
            self.network_token_data = value.from_dictionary(dictionary['networkTokenData'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'schemeReferenceData' in dictionary:
            self.scheme_reference_data = dictionary['schemeReferenceData']
        if 'subMerchant' in dictionary:
            if not isinstance(dictionary['subMerchant'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['subMerchant']))
            value = SubMerchant()
            self.sub_merchant = value.from_dictionary(dictionary['subMerchant'])
        if 'tokenId' in dictionary:
            self.token_id = dictionary['tokenId']
        if 'transactionLinkIdentifier' in dictionary:
            self.transaction_link_identifier = dictionary['transactionLinkIdentifier']
        return self

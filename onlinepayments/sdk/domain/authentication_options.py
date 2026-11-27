#
# This file was automatically generated.
#
from .data_object import DataObject


class AuthenticationOptions(DataObject):

    __slots__ = (
        "__acquirer_bin",
        "__acquirer_merchant_id",
        "__merchant_category_code",
        "__merchant_country_code",
    )

    __acquirer_bin: str | None
    __acquirer_merchant_id: str | None
    __merchant_category_code: str | None
    __merchant_country_code: str | None

    def __init__(
        self,
        *,
        acquirer_bin: str | None = None,
        acquirer_merchant_id: str | None = None,
        merchant_category_code: str | None = None,
        merchant_country_code: str | None = None,
    ) -> None:
        self.acquirer_bin = acquirer_bin
        self.acquirer_merchant_id = acquirer_merchant_id
        self.merchant_category_code = merchant_category_code
        self.merchant_country_code = merchant_country_code

    @property
    def acquirer_bin(self) -> str | None:
        """
        | Acquiring institution identification code as assigned by the 3DS Directory Server receiving the AReq message.

        Type: str
        """
        return self.__acquirer_bin

    @acquirer_bin.setter
    def acquirer_bin(self, value: str | None) -> None:
        self.__acquirer_bin = value

    @property
    def acquirer_merchant_id(self) -> str | None:
        """
        | Acquiring institution identification code.

        Type: str
        """
        return self.__acquirer_merchant_id

    @acquirer_merchant_id.setter
    def acquirer_merchant_id(self, value: str | None) -> None:
        self.__acquirer_merchant_id = value

    @property
    def merchant_category_code(self) -> str | None:
        """
        | Code representing merchant’s type of business, product or service.

        Type: str
        """
        return self.__merchant_category_code

    @merchant_category_code.setter
    def merchant_category_code(self, value: str | None) -> None:
        self.__merchant_category_code = value

    @property
    def merchant_country_code(self) -> str | None:
        """
        | ISO-3166 country code of the merchant.

        Type: str
        """
        return self.__merchant_country_code

    @merchant_country_code.setter
    def merchant_country_code(self, value: str | None) -> None:
        self.__merchant_country_code = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.acquirer_bin is not None:
            dictionary['acquirerBIN'] = self.acquirer_bin
        if self.acquirer_merchant_id is not None:
            dictionary['acquirerMerchantId'] = self.acquirer_merchant_id
        if self.merchant_category_code is not None:
            dictionary['merchantCategoryCode'] = self.merchant_category_code
        if self.merchant_country_code is not None:
            dictionary['merchantCountryCode'] = self.merchant_country_code
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AuthenticationOptions':
        super().from_dictionary(dictionary)
        if 'acquirerBIN' in dictionary:
            self.acquirer_bin = dictionary['acquirerBIN']
        if 'acquirerMerchantId' in dictionary:
            self.acquirer_merchant_id = dictionary['acquirerMerchantId']
        if 'merchantCategoryCode' in dictionary:
            self.merchant_category_code = dictionary['merchantCategoryCode']
        if 'merchantCountryCode' in dictionary:
            self.merchant_country_code = dictionary['merchantCountryCode']
        return self

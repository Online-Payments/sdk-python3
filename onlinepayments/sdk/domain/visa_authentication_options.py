#
# This file was automatically generated.
#
from .data_object import DataObject


class VisaAuthenticationOptions(DataObject):

    __slots__ = (
        "__acquirer_bin",
        "__acquirer_merchant_id",
        "__merchant_name",
    )

    __acquirer_bin: str | None
    __acquirer_merchant_id: str | None
    __merchant_name: str | None

    def __init__(
        self,
        *,
        acquirer_bin: str | None = None,
        acquirer_merchant_id: str | None = None,
        merchant_name: str | None = None,
    ) -> None:
        self.acquirer_bin = acquirer_bin
        self.acquirer_merchant_id = acquirer_merchant_id
        self.merchant_name = merchant_name

    @property
    def acquirer_bin(self) -> str | None:
        """
        | Acquirer identification code as assigned by the Directory Server.

        Type: str
        """
        return self.__acquirer_bin

    @acquirer_bin.setter
    def acquirer_bin(self, value: str | None) -> None:
        self.__acquirer_bin = value

    @property
    def acquirer_merchant_id(self) -> str | None:
        """
        | Acquirer-assigned Merchant identifier.

        Type: str
        """
        return self.__acquirer_merchant_id

    @acquirer_merchant_id.setter
    def acquirer_merchant_id(self, value: str | None) -> None:
        self.__acquirer_merchant_id = value

    @property
    def merchant_name(self) -> str | None:
        """
        | Merchant name assigned by the Acquirer or Payment System.

        Type: str
        """
        return self.__merchant_name

    @merchant_name.setter
    def merchant_name(self, value: str | None) -> None:
        self.__merchant_name = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.acquirer_bin is not None:
            dictionary['acquirerBIN'] = self.acquirer_bin
        if self.acquirer_merchant_id is not None:
            dictionary['acquirerMerchantId'] = self.acquirer_merchant_id
        if self.merchant_name is not None:
            dictionary['merchantName'] = self.merchant_name
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'VisaAuthenticationOptions':
        super().from_dictionary(dictionary)
        if 'acquirerBIN' in dictionary:
            self.acquirer_bin = dictionary['acquirerBIN']
        if 'acquirerMerchantId' in dictionary:
            self.acquirer_merchant_id = dictionary['acquirerMerchantId']
        if 'merchantName' in dictionary:
            self.merchant_name = dictionary['merchantName']
        return self

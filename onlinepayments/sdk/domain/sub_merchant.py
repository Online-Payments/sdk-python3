#
# This file was automatically generated.
#
from .address import Address
from .data_object import DataObject


class SubMerchant(DataObject):

    __slots__ = (
        "__address",
        "__company_identification_number",
        "__company_name",
        "__merchant_category_code",
        "__merchant_id",
        "__website",
    )

    __address: Address | None
    __company_identification_number: str | None
    __company_name: str | None
    __merchant_category_code: str | None
    __merchant_id: str | None
    __website: str | None

    def __init__(
        self,
        *,
        address: Address | None = None,
        company_identification_number: str | None = None,
        company_name: str | None = None,
        merchant_category_code: str | None = None,
        merchant_id: str | None = None,
        website: str | None = None,
    ) -> None:
        self.address = address
        self.company_identification_number = company_identification_number
        self.company_name = company_name
        self.merchant_category_code = merchant_category_code
        self.merchant_id = merchant_id
        self.website = website

    @property
    def address(self) -> Address | None:
        """
        | Object containing billing address details.

        Type: :class:`onlinepayments.sdk.domain.address.Address`
        """
        return self.__address

    @address.setter
    def address(self, value: Address | None) -> None:
        self.__address = value

    @property
    def company_identification_number(self) -> str | None:
        """
        | Business Establishment Directory Identification System

        Type: str
        """
        return self.__company_identification_number

    @company_identification_number.setter
    def company_identification_number(self, value: str | None) -> None:
        self.__company_identification_number = value

    @property
    def company_name(self) -> str | None:
        """
        | Name of the sales establishment requesting the transaction.

        Type: str
        """
        return self.__company_name

    @company_name.setter
    def company_name(self, value: str | None) -> None:
        self.__company_name = value

    @property
    def merchant_category_code(self) -> str | None:
        """
        | MCC is a four-digit number that classifies the type of goods or services a business offers.

        Type: str
        """
        return self.__merchant_category_code

    @merchant_category_code.setter
    def merchant_category_code(self, value: str | None) -> None:
        self.__merchant_category_code = value

    @property
    def merchant_id(self) -> str | None:
        """
        | Merchant Identifier is a value defined by the acquirer.

        Type: str
        """
        return self.__merchant_id

    @merchant_id.setter
    def merchant_id(self, value: str | None) -> None:
        self.__merchant_id = value

    @property
    def website(self) -> str | None:
        """
        | Website address of the submerchant.

        Type: str
        """
        return self.__website

    @website.setter
    def website(self, value: str | None) -> None:
        self.__website = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.address is not None:
            dictionary['address'] = self.address.to_dictionary()
        if self.company_identification_number is not None:
            dictionary['companyIdentificationNumber'] = self.company_identification_number
        if self.company_name is not None:
            dictionary['companyName'] = self.company_name
        if self.merchant_category_code is not None:
            dictionary['merchantCategoryCode'] = self.merchant_category_code
        if self.merchant_id is not None:
            dictionary['merchantId'] = self.merchant_id
        if self.website is not None:
            dictionary['website'] = self.website
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SubMerchant':
        super().from_dictionary(dictionary)
        if 'address' in dictionary:
            if not isinstance(dictionary['address'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['address']))
            value = Address()
            self.address = value.from_dictionary(dictionary['address'])
        if 'companyIdentificationNumber' in dictionary:
            self.company_identification_number = dictionary['companyIdentificationNumber']
        if 'companyName' in dictionary:
            self.company_name = dictionary['companyName']
        if 'merchantCategoryCode' in dictionary:
            self.merchant_category_code = dictionary['merchantCategoryCode']
        if 'merchantId' in dictionary:
            self.merchant_id = dictionary['merchantId']
        if 'website' in dictionary:
            self.website = dictionary['website']
        return self

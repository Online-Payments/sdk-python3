#
# This file was automatically generated.
#
from .data_object import DataObject


class DirectoryEntry(DataObject):

    __slots__ = (
        "__issuer_id",
        "__issuer_list",
        "__issuer_name",
    )

    __issuer_id: str | None
    __issuer_list: str | None
    __issuer_name: str | None

    def __init__(
        self,
        *,
        issuer_id: str | None = None,
        issuer_list: str | None = None,
        issuer_name: str | None = None,
    ) -> None:
        self.issuer_id = issuer_id
        self.issuer_list = issuer_list
        self.issuer_name = issuer_name

    @property
    def issuer_id(self) -> str | None:
        """
        | Deprecated. Unique ID of the issuing bank of the customer

        Type: str
        """
        return self.__issuer_id

    @issuer_id.setter
    def issuer_id(self, value: str | None) -> None:
        self.__issuer_id = value

    @property
    def issuer_list(self) -> str | None:
        """
        | To be used to sort the issuers. short - These issuers should be presented at the top of the list long - These issuers should be presented after the issuers marked as short Note this is only filled if supported by the payment product. Currently only iDeal (809) support this. Sorting within the groups should be done alphabetically

        Type: str
        """
        return self.__issuer_list

    @issuer_list.setter
    def issuer_list(self, value: str | None) -> None:
        self.__issuer_list = value

    @property
    def issuer_name(self) -> str | None:
        """
        | Name of the issuing bank as it should be presented to the customer

        Type: str
        """
        return self.__issuer_name

    @issuer_name.setter
    def issuer_name(self, value: str | None) -> None:
        self.__issuer_name = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.issuer_id is not None:
            dictionary['issuerId'] = self.issuer_id
        if self.issuer_list is not None:
            dictionary['issuerList'] = self.issuer_list
        if self.issuer_name is not None:
            dictionary['issuerName'] = self.issuer_name
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DirectoryEntry':
        super().from_dictionary(dictionary)
        if 'issuerId' in dictionary:
            self.issuer_id = dictionary['issuerId']
        if 'issuerList' in dictionary:
            self.issuer_list = dictionary['issuerList']
        if 'issuerName' in dictionary:
            self.issuer_name = dictionary['issuerName']
        return self

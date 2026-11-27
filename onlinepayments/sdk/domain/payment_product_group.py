#
# This file was automatically generated.
#
from .account_on_file import AccountOnFile
from .data_object import DataObject
from .payment_product_display_hints import PaymentProductDisplayHints


class PaymentProductGroup(DataObject):

    __slots__ = (
        "__account_on_file",
        "__display_hints",
        "__display_hints_list",
        "__id",
    )

    __account_on_file: AccountOnFile | None
    __display_hints: PaymentProductDisplayHints | None
    __display_hints_list: list[PaymentProductDisplayHints] | None
    __id: str | None

    def __init__(
        self,
        *,
        account_on_file: AccountOnFile | None = None,
        display_hints: PaymentProductDisplayHints | None = None,
        display_hints_list: list[PaymentProductDisplayHints] | None = None,
        id: str | None = None,
    ) -> None:
        self.account_on_file = account_on_file
        self.display_hints = display_hints
        self.display_hints_list = display_hints_list
        self.id = id

    @property
    def account_on_file(self) -> AccountOnFile | None:
        """
        Type: :class:`onlinepayments.sdk.domain.account_on_file.AccountOnFile`
        """
        return self.__account_on_file

    @account_on_file.setter
    def account_on_file(self, value: AccountOnFile | None) -> None:
        self.__account_on_file = value

    @property
    def display_hints(self) -> PaymentProductDisplayHints | None:
        """
        | Deprecated: field is replaced by displayHintsList

        Type: :class:`onlinepayments.sdk.domain.payment_product_display_hints.PaymentProductDisplayHints`
        """
        return self.__display_hints

    @display_hints.setter
    def display_hints(self, value: PaymentProductDisplayHints | None) -> None:
        self.__display_hints = value

    @property
    def display_hints_list(self) -> list[PaymentProductDisplayHints] | None:
        """
        | List of display hints

        Type: list[:class:`onlinepayments.sdk.domain.payment_product_display_hints.PaymentProductDisplayHints`]
        """
        return self.__display_hints_list

    @display_hints_list.setter
    def display_hints_list(self, value: list[PaymentProductDisplayHints] | None) -> None:
        self.__display_hints_list = value

    @property
    def id(self) -> str | None:
        """
        | The ID of the payment product group in our system

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: str | None) -> None:
        self.__id = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.account_on_file is not None:
            dictionary['accountOnFile'] = self.account_on_file.to_dictionary()
        if self.display_hints is not None:
            dictionary['displayHints'] = self.display_hints.to_dictionary()
        if self.display_hints_list is not None:
            dictionary['displayHintsList'] = []
            for element in self.display_hints_list:
                if element is not None:
                    dictionary['displayHintsList'].append(element.to_dictionary())
        if self.id is not None:
            dictionary['id'] = self.id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductGroup':
        super().from_dictionary(dictionary)
        if 'accountOnFile' in dictionary:
            if not isinstance(dictionary['accountOnFile'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['accountOnFile']))
            value = AccountOnFile()
            self.account_on_file = value.from_dictionary(dictionary['accountOnFile'])
        if 'displayHints' in dictionary:
            if not isinstance(dictionary['displayHints'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['displayHints']))
            value = PaymentProductDisplayHints()
            self.display_hints = value.from_dictionary(dictionary['displayHints'])
        if 'displayHintsList' in dictionary:
            if not isinstance(dictionary['displayHintsList'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['displayHintsList']))
            self.display_hints_list = []
            for element in dictionary['displayHintsList']:
                value = PaymentProductDisplayHints()
                self.display_hints_list.append(value.from_dictionary(element))
        if 'id' in dictionary:
            self.id = dictionary['id']
        return self

# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .account_on_file import AccountOnFile
from .data_object import DataObject
from .payment_product_display_hints import PaymentProductDisplayHints


class PaymentProductGroup(DataObject):

    __account_on_file: Optional[AccountOnFile] = None
    __display_hints: Optional[PaymentProductDisplayHints] = None
    __display_hints_list: Optional[List[PaymentProductDisplayHints]] = None
    __id: Optional[str] = None

    @property
    def account_on_file(self) -> Optional[AccountOnFile]:
        """
        Type: :class:`onlinepayments.sdk.domain.account_on_file.AccountOnFile`
        """
        return self.__account_on_file

    @account_on_file.setter
    def account_on_file(self, value: Optional[AccountOnFile]) -> None:
        self.__account_on_file = value

    @property
    def display_hints(self) -> Optional[PaymentProductDisplayHints]:
        """
        | Object containing display hints like the order of the product when shown in a list, the name of the product and the logo

        Type: :class:`onlinepayments.sdk.domain.payment_product_display_hints.PaymentProductDisplayHints`
        """
        return self.__display_hints

    @display_hints.setter
    def display_hints(self, value: Optional[PaymentProductDisplayHints]) -> None:
        self.__display_hints = value

    @property
    def display_hints_list(self) -> Optional[List[PaymentProductDisplayHints]]:
        """
        Type: list[:class:`onlinepayments.sdk.domain.payment_product_display_hints.PaymentProductDisplayHints`]
        """
        return self.__display_hints_list

    @display_hints_list.setter
    def display_hints_list(self, value: Optional[List[PaymentProductDisplayHints]]) -> None:
        self.__display_hints_list = value

    @property
    def id(self) -> Optional[str]:
        """
        | The ID of the payment product group in our system

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: Optional[str]) -> None:
        self.__id = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProductGroup, self).to_dictionary()
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
        super(PaymentProductGroup, self).from_dictionary(dictionary)
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

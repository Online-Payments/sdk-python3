# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .account_on_file import AccountOnFile
from .data_object import DataObject
from .payment_product302_specific_data import PaymentProduct302SpecificData
from .payment_product320_specific_data import PaymentProduct320SpecificData
from .payment_product_display_hints import PaymentProductDisplayHints
from .payment_product_field import PaymentProductField


class PaymentProduct(DataObject):

    __accounts_on_file: Optional[List[AccountOnFile]] = None
    __allows_authentication: Optional[bool] = None
    __allows_recurring: Optional[bool] = None
    __allows_tokenization: Optional[bool] = None
    __display_hints: Optional[PaymentProductDisplayHints] = None
    __display_hints_list: Optional[List[PaymentProductDisplayHints]] = None
    __fields: Optional[List[PaymentProductField]] = None
    __id: Optional[int] = None
    __payment_method: Optional[str] = None
    __payment_product302_specific_data: Optional[PaymentProduct302SpecificData] = None
    __payment_product320_specific_data: Optional[PaymentProduct320SpecificData] = None
    __payment_product_group: Optional[str] = None
    __uses_redirection_to3rd_party: Optional[bool] = None

    @property
    def accounts_on_file(self) -> Optional[List[AccountOnFile]]:
        """
        | List of tokens for that payment product

        Type: list[:class:`onlinepayments.sdk.domain.account_on_file.AccountOnFile`]
        """
        return self.__accounts_on_file

    @accounts_on_file.setter
    def accounts_on_file(self, value: Optional[List[AccountOnFile]]) -> None:
        self.__accounts_on_file = value

    @property
    def allows_authentication(self) -> Optional[bool]:
        """
        | True when 3DS authentication is supported or required for the product

        Type: bool
        """
        return self.__allows_authentication

    @allows_authentication.setter
    def allows_authentication(self, value: Optional[bool]) -> None:
        self.__allows_authentication = value

    @property
    def allows_recurring(self) -> Optional[bool]:
        """
        | Indicates if the product supports recurring payments
        
        * true - This payment product supports recurring payments
        * false - This payment product does not support recurring transactions and can only be used for one-off payments

        Type: bool
        """
        return self.__allows_recurring

    @allows_recurring.setter
    def allows_recurring(self, value: Optional[bool]) -> None:
        self.__allows_recurring = value

    @property
    def allows_tokenization(self) -> Optional[bool]:
        """
        | Indicates if the payment details can be tokenized for future re-use
        
        * true - Payment details from payments done with this payment product can be tokenized for future re-use
        * false - Payment details from payments done with this payment product can not be tokenized

        Type: bool
        """
        return self.__allows_tokenization

    @allows_tokenization.setter
    def allows_tokenization(self, value: Optional[bool]) -> None:
        self.__allows_tokenization = value

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
    def fields(self) -> Optional[List[PaymentProductField]]:
        """
        | Object containing all the fields and their details that are associated with this payment product. If you are not interested in the data on the fields you should have us filter them our (using filter=fields in the query-string)

        Type: list[:class:`onlinepayments.sdk.domain.payment_product_field.PaymentProductField`]
        """
        return self.__fields

    @fields.setter
    def fields(self, value: Optional[List[PaymentProductField]]) -> None:
        self.__fields = value

    @property
    def id(self) -> Optional[int]:
        """
        | The ID of the payment product in our system

        Type: int
        """
        return self.__id

    @id.setter
    def id(self, value: Optional[int]) -> None:
        self.__id = value

    @property
    def payment_method(self) -> Optional[str]:
        """
        | Payment method identifier used by the our payment engine.

        Type: str
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value: Optional[str]) -> None:
        self.__payment_method = value

    @property
    def payment_product302_specific_data(self) -> Optional[PaymentProduct302SpecificData]:
        """
        Type: :class:`onlinepayments.sdk.domain.payment_product302_specific_data.PaymentProduct302SpecificData`
        """
        return self.__payment_product302_specific_data

    @payment_product302_specific_data.setter
    def payment_product302_specific_data(self, value: Optional[PaymentProduct302SpecificData]) -> None:
        self.__payment_product302_specific_data = value

    @property
    def payment_product320_specific_data(self) -> Optional[PaymentProduct320SpecificData]:
        """
        Type: :class:`onlinepayments.sdk.domain.payment_product320_specific_data.PaymentProduct320SpecificData`
        """
        return self.__payment_product320_specific_data

    @payment_product320_specific_data.setter
    def payment_product320_specific_data(self, value: Optional[PaymentProduct320SpecificData]) -> None:
        self.__payment_product320_specific_data = value

    @property
    def payment_product_group(self) -> Optional[str]:
        """
        | The payment product group that has this payment product, if there is any. Not populated otherwise. Currently only one payment product group is supported:
        
        * cards

        Type: str
        """
        return self.__payment_product_group

    @payment_product_group.setter
    def payment_product_group(self, value: Optional[str]) -> None:
        self.__payment_product_group = value

    @property
    def uses_redirection_to3rd_party(self) -> Optional[bool]:
        """
        | Indicates whether the payment product requires redirection to a third party to complete the payment. You can use this to filter out products that require a redirect if you do not want to support that.
        
        * true - Redirection is required
        * false - No redirection is required

        Type: bool
        """
        return self.__uses_redirection_to3rd_party

    @uses_redirection_to3rd_party.setter
    def uses_redirection_to3rd_party(self, value: Optional[bool]) -> None:
        self.__uses_redirection_to3rd_party = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct, self).to_dictionary()
        if self.accounts_on_file is not None:
            dictionary['accountsOnFile'] = []
            for element in self.accounts_on_file:
                if element is not None:
                    dictionary['accountsOnFile'].append(element.to_dictionary())
        if self.allows_authentication is not None:
            dictionary['allowsAuthentication'] = self.allows_authentication
        if self.allows_recurring is not None:
            dictionary['allowsRecurring'] = self.allows_recurring
        if self.allows_tokenization is not None:
            dictionary['allowsTokenization'] = self.allows_tokenization
        if self.display_hints is not None:
            dictionary['displayHints'] = self.display_hints.to_dictionary()
        if self.display_hints_list is not None:
            dictionary['displayHintsList'] = []
            for element in self.display_hints_list:
                if element is not None:
                    dictionary['displayHintsList'].append(element.to_dictionary())
        if self.fields is not None:
            dictionary['fields'] = []
            for element in self.fields:
                if element is not None:
                    dictionary['fields'].append(element.to_dictionary())
        if self.id is not None:
            dictionary['id'] = self.id
        if self.payment_method is not None:
            dictionary['paymentMethod'] = self.payment_method
        if self.payment_product302_specific_data is not None:
            dictionary['paymentProduct302SpecificData'] = self.payment_product302_specific_data.to_dictionary()
        if self.payment_product320_specific_data is not None:
            dictionary['paymentProduct320SpecificData'] = self.payment_product320_specific_data.to_dictionary()
        if self.payment_product_group is not None:
            dictionary['paymentProductGroup'] = self.payment_product_group
        if self.uses_redirection_to3rd_party is not None:
            dictionary['usesRedirectionTo3rdParty'] = self.uses_redirection_to3rd_party
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct':
        super(PaymentProduct, self).from_dictionary(dictionary)
        if 'accountsOnFile' in dictionary:
            if not isinstance(dictionary['accountsOnFile'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['accountsOnFile']))
            self.accounts_on_file = []
            for element in dictionary['accountsOnFile']:
                value = AccountOnFile()
                self.accounts_on_file.append(value.from_dictionary(element))
        if 'allowsAuthentication' in dictionary:
            self.allows_authentication = dictionary['allowsAuthentication']
        if 'allowsRecurring' in dictionary:
            self.allows_recurring = dictionary['allowsRecurring']
        if 'allowsTokenization' in dictionary:
            self.allows_tokenization = dictionary['allowsTokenization']
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
        if 'fields' in dictionary:
            if not isinstance(dictionary['fields'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['fields']))
            self.fields = []
            for element in dictionary['fields']:
                value = PaymentProductField()
                self.fields.append(value.from_dictionary(element))
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'paymentMethod' in dictionary:
            self.payment_method = dictionary['paymentMethod']
        if 'paymentProduct302SpecificData' in dictionary:
            if not isinstance(dictionary['paymentProduct302SpecificData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct302SpecificData']))
            value = PaymentProduct302SpecificData()
            self.payment_product302_specific_data = value.from_dictionary(dictionary['paymentProduct302SpecificData'])
        if 'paymentProduct320SpecificData' in dictionary:
            if not isinstance(dictionary['paymentProduct320SpecificData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct320SpecificData']))
            value = PaymentProduct320SpecificData()
            self.payment_product320_specific_data = value.from_dictionary(dictionary['paymentProduct320SpecificData'])
        if 'paymentProductGroup' in dictionary:
            self.payment_product_group = dictionary['paymentProductGroup']
        if 'usesRedirectionTo3rdParty' in dictionary:
            self.uses_redirection_to3rd_party = dictionary['usesRedirectionTo3rdParty']
        return self

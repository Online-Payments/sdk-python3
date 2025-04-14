# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .empty_validator import EmptyValidator
from .fixed_list_validator import FixedListValidator
from .length_validator import LengthValidator
from .range_validator import RangeValidator
from .regular_expression_validator import RegularExpressionValidator


class PaymentProductFieldValidators(DataObject):

    __email_address: Optional[EmptyValidator] = None
    __expiration_date: Optional[EmptyValidator] = None
    __fixed_list: Optional[FixedListValidator] = None
    __iban: Optional[EmptyValidator] = None
    __length: Optional[LengthValidator] = None
    __luhn: Optional[EmptyValidator] = None
    __range: Optional[RangeValidator] = None
    __regular_expression: Optional[RegularExpressionValidator] = None
    __terms_and_conditions: Optional[EmptyValidator] = None

    @property
    def email_address(self) -> Optional[EmptyValidator]:
        """
        Type: :class:`onlinepayments.sdk.domain.empty_validator.EmptyValidator`
        """
        return self.__email_address

    @email_address.setter
    def email_address(self, value: Optional[EmptyValidator]) -> None:
        self.__email_address = value

    @property
    def expiration_date(self) -> Optional[EmptyValidator]:
        """
        Type: :class:`onlinepayments.sdk.domain.empty_validator.EmptyValidator`
        """
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value: Optional[EmptyValidator]) -> None:
        self.__expiration_date = value

    @property
    def fixed_list(self) -> Optional[FixedListValidator]:
        """
        Type: :class:`onlinepayments.sdk.domain.fixed_list_validator.FixedListValidator`
        """
        return self.__fixed_list

    @fixed_list.setter
    def fixed_list(self, value: Optional[FixedListValidator]) -> None:
        self.__fixed_list = value

    @property
    def iban(self) -> Optional[EmptyValidator]:
        """
        Type: :class:`onlinepayments.sdk.domain.empty_validator.EmptyValidator`
        """
        return self.__iban

    @iban.setter
    def iban(self, value: Optional[EmptyValidator]) -> None:
        self.__iban = value

    @property
    def length(self) -> Optional[LengthValidator]:
        """
        Type: :class:`onlinepayments.sdk.domain.length_validator.LengthValidator`
        """
        return self.__length

    @length.setter
    def length(self, value: Optional[LengthValidator]) -> None:
        self.__length = value

    @property
    def luhn(self) -> Optional[EmptyValidator]:
        """
        Type: :class:`onlinepayments.sdk.domain.empty_validator.EmptyValidator`
        """
        return self.__luhn

    @luhn.setter
    def luhn(self, value: Optional[EmptyValidator]) -> None:
        self.__luhn = value

    @property
    def range(self) -> Optional[RangeValidator]:
        """
        Type: :class:`onlinepayments.sdk.domain.range_validator.RangeValidator`
        """
        return self.__range

    @range.setter
    def range(self, value: Optional[RangeValidator]) -> None:
        self.__range = value

    @property
    def regular_expression(self) -> Optional[RegularExpressionValidator]:
        """
        Type: :class:`onlinepayments.sdk.domain.regular_expression_validator.RegularExpressionValidator`
        """
        return self.__regular_expression

    @regular_expression.setter
    def regular_expression(self, value: Optional[RegularExpressionValidator]) -> None:
        self.__regular_expression = value

    @property
    def terms_and_conditions(self) -> Optional[EmptyValidator]:
        """
        Type: :class:`onlinepayments.sdk.domain.empty_validator.EmptyValidator`
        """
        return self.__terms_and_conditions

    @terms_and_conditions.setter
    def terms_and_conditions(self, value: Optional[EmptyValidator]) -> None:
        self.__terms_and_conditions = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProductFieldValidators, self).to_dictionary()
        if self.email_address is not None:
            dictionary['emailAddress'] = self.email_address.to_dictionary()
        if self.expiration_date is not None:
            dictionary['expirationDate'] = self.expiration_date.to_dictionary()
        if self.fixed_list is not None:
            dictionary['fixedList'] = self.fixed_list.to_dictionary()
        if self.iban is not None:
            dictionary['iban'] = self.iban.to_dictionary()
        if self.length is not None:
            dictionary['length'] = self.length.to_dictionary()
        if self.luhn is not None:
            dictionary['luhn'] = self.luhn.to_dictionary()
        if self.range is not None:
            dictionary['range'] = self.range.to_dictionary()
        if self.regular_expression is not None:
            dictionary['regularExpression'] = self.regular_expression.to_dictionary()
        if self.terms_and_conditions is not None:
            dictionary['termsAndConditions'] = self.terms_and_conditions.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductFieldValidators':
        super(PaymentProductFieldValidators, self).from_dictionary(dictionary)
        if 'emailAddress' in dictionary:
            if not isinstance(dictionary['emailAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['emailAddress']))
            value = EmptyValidator()
            self.email_address = value.from_dictionary(dictionary['emailAddress'])
        if 'expirationDate' in dictionary:
            if not isinstance(dictionary['expirationDate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['expirationDate']))
            value = EmptyValidator()
            self.expiration_date = value.from_dictionary(dictionary['expirationDate'])
        if 'fixedList' in dictionary:
            if not isinstance(dictionary['fixedList'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fixedList']))
            value = FixedListValidator()
            self.fixed_list = value.from_dictionary(dictionary['fixedList'])
        if 'iban' in dictionary:
            if not isinstance(dictionary['iban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['iban']))
            value = EmptyValidator()
            self.iban = value.from_dictionary(dictionary['iban'])
        if 'length' in dictionary:
            if not isinstance(dictionary['length'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['length']))
            value = LengthValidator()
            self.length = value.from_dictionary(dictionary['length'])
        if 'luhn' in dictionary:
            if not isinstance(dictionary['luhn'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['luhn']))
            value = EmptyValidator()
            self.luhn = value.from_dictionary(dictionary['luhn'])
        if 'range' in dictionary:
            if not isinstance(dictionary['range'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['range']))
            value = RangeValidator()
            self.range = value.from_dictionary(dictionary['range'])
        if 'regularExpression' in dictionary:
            if not isinstance(dictionary['regularExpression'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['regularExpression']))
            value = RegularExpressionValidator()
            self.regular_expression = value.from_dictionary(dictionary['regularExpression'])
        if 'termsAndConditions' in dictionary:
            if not isinstance(dictionary['termsAndConditions'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['termsAndConditions']))
            value = EmptyValidator()
            self.terms_and_conditions = value.from_dictionary(dictionary['termsAndConditions'])
        return self

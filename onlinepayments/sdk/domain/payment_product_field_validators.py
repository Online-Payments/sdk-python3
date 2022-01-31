# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.empty_validator import EmptyValidator
from onlinepayments.sdk.domain.fixed_list_validator import FixedListValidator
from onlinepayments.sdk.domain.length_validator import LengthValidator
from onlinepayments.sdk.domain.range_validator import RangeValidator
from onlinepayments.sdk.domain.regular_expression_validator import RegularExpressionValidator


class PaymentProductFieldValidators(DataObject):
    """
    | Object containing the details of the validations on the field
    """

    __email_address = None
    __expiration_date = None
    __fixed_list = None
    __iban = None
    __length = None
    __luhn = None
    __range = None
    __regular_expression = None
    __terms_and_conditions = None

    @property
    def email_address(self) -> EmptyValidator:
        """
        Type: :class:`onlinepayments.sdk.domain.empty_validator.EmptyValidator`
        """
        return self.__email_address

    @email_address.setter
    def email_address(self, value: EmptyValidator):
        self.__email_address = value

    @property
    def expiration_date(self) -> EmptyValidator:
        """
        Type: :class:`onlinepayments.sdk.domain.empty_validator.EmptyValidator`
        """
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value: EmptyValidator):
        self.__expiration_date = value

    @property
    def fixed_list(self) -> FixedListValidator:
        """
        Type: :class:`onlinepayments.sdk.domain.fixed_list_validator.FixedListValidator`
        """
        return self.__fixed_list

    @fixed_list.setter
    def fixed_list(self, value: FixedListValidator):
        self.__fixed_list = value

    @property
    def iban(self) -> EmptyValidator:
        """
        Type: :class:`onlinepayments.sdk.domain.empty_validator.EmptyValidator`
        """
        return self.__iban

    @iban.setter
    def iban(self, value: EmptyValidator):
        self.__iban = value

    @property
    def length(self) -> LengthValidator:
        """
        Type: :class:`onlinepayments.sdk.domain.length_validator.LengthValidator`
        """
        return self.__length

    @length.setter
    def length(self, value: LengthValidator):
        self.__length = value

    @property
    def luhn(self) -> EmptyValidator:
        """
        Type: :class:`onlinepayments.sdk.domain.empty_validator.EmptyValidator`
        """
        return self.__luhn

    @luhn.setter
    def luhn(self, value: EmptyValidator):
        self.__luhn = value

    @property
    def range(self) -> RangeValidator:
        """
        Type: :class:`onlinepayments.sdk.domain.range_validator.RangeValidator`
        """
        return self.__range

    @range.setter
    def range(self, value: RangeValidator):
        self.__range = value

    @property
    def regular_expression(self) -> RegularExpressionValidator:
        """
        Type: :class:`onlinepayments.sdk.domain.regular_expression_validator.RegularExpressionValidator`
        """
        return self.__regular_expression

    @regular_expression.setter
    def regular_expression(self, value: RegularExpressionValidator):
        self.__regular_expression = value

    @property
    def terms_and_conditions(self) -> EmptyValidator:
        """
        Type: :class:`onlinepayments.sdk.domain.empty_validator.EmptyValidator`
        """
        return self.__terms_and_conditions

    @terms_and_conditions.setter
    def terms_and_conditions(self, value: EmptyValidator):
        self.__terms_and_conditions = value

    def to_dictionary(self):
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

    def from_dictionary(self, dictionary):
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

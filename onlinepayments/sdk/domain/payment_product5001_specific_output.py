# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct5001SpecificOutput(DataObject):

    __account_number: Optional[str] = None
    __authorisation_code: Optional[str] = None
    __liability: Optional[str] = None
    __mobile_phone_number: Optional[str] = None
    __operation_code: Optional[str] = None

    @property
    def account_number(self) -> Optional[str]:
        """
        | The account number used for this transaction

        Type: str
        """
        return self.__account_number

    @account_number.setter
    def account_number(self, value: Optional[str]) -> None:
        self.__account_number = value

    @property
    def authorisation_code(self) -> Optional[str]:
        """
        | The reference returned by redsys to identify the transaction

        Type: str
        """
        return self.__authorisation_code

    @authorisation_code.setter
    def authorisation_code(self, value: Optional[str]) -> None:
        self.__authorisation_code = value

    @property
    def liability(self) -> Optional[str]:
        """
        | Determines the Fraud liability. Possible values are:
        
        * issuer - Fraud liability shifts to the issuer (eq. exemption accepted)
        * merchant - Fraud liability with the merchant Note: When not filled in, Fraud liability is not applicable for the current transaction.

        Type: str
        """
        return self.__liability

    @liability.setter
    def liability(self, value: Optional[str]) -> None:
        self.__liability = value

    @property
    def mobile_phone_number(self) -> Optional[str]:
        """
        | The mobile phone number used for this transaction

        Type: str
        """
        return self.__mobile_phone_number

    @mobile_phone_number.setter
    def mobile_phone_number(self, value: Optional[str]) -> None:
        self.__mobile_phone_number = value

    @property
    def operation_code(self) -> Optional[str]:
        """
        | The reference returned by redsys to identify the operation

        Type: str
        """
        return self.__operation_code

    @operation_code.setter
    def operation_code(self, value: Optional[str]) -> None:
        self.__operation_code = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct5001SpecificOutput, self).to_dictionary()
        if self.account_number is not None:
            dictionary['accountNumber'] = self.account_number
        if self.authorisation_code is not None:
            dictionary['authorisationCode'] = self.authorisation_code
        if self.liability is not None:
            dictionary['liability'] = self.liability
        if self.mobile_phone_number is not None:
            dictionary['mobilePhoneNumber'] = self.mobile_phone_number
        if self.operation_code is not None:
            dictionary['operationCode'] = self.operation_code
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct5001SpecificOutput':
        super(PaymentProduct5001SpecificOutput, self).from_dictionary(dictionary)
        if 'accountNumber' in dictionary:
            self.account_number = dictionary['accountNumber']
        if 'authorisationCode' in dictionary:
            self.authorisation_code = dictionary['authorisationCode']
        if 'liability' in dictionary:
            self.liability = dictionary['liability']
        if 'mobilePhoneNumber' in dictionary:
            self.mobile_phone_number = dictionary['mobilePhoneNumber']
        if 'operationCode' in dictionary:
            self.operation_code = dictionary['operationCode']
        return self

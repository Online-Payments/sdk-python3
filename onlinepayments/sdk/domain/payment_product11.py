# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct11(DataObject):

    __payment_bic: Optional[str] = None
    __payment_beneficiary: Optional[str] = None
    __payment_iban: Optional[str] = None
    __payment_reference: Optional[str] = None
    __qr_code: Optional[str] = None

    @property
    def payment_bic(self) -> Optional[str]:
        """
        | The BIC is the Bank Identifier Code, also known as SWIFT code, used to identify banks internationally.

        Type: str
        """
        return self.__payment_bic

    @payment_bic.setter
    def payment_bic(self, value: Optional[str]) -> None:
        self.__payment_bic = value

    @property
    def payment_beneficiary(self) -> Optional[str]:
        """
        | The beneficiary of the payment

        Type: str
        """
        return self.__payment_beneficiary

    @payment_beneficiary.setter
    def payment_beneficiary(self, value: Optional[str]) -> None:
        self.__payment_beneficiary = value

    @property
    def payment_iban(self) -> Optional[str]:
        """
        | The IBAN is the International Bank Account Number. It is an internationally agreed format for the BBAN and includes the ISO country code and two check digits.

        Type: str
        """
        return self.__payment_iban

    @payment_iban.setter
    def payment_iban(self, value: Optional[str]) -> None:
        self.__payment_iban = value

    @property
    def payment_reference(self) -> Optional[str]:
        """
        | The reference for the payment

        Type: str
        """
        return self.__payment_reference

    @payment_reference.setter
    def payment_reference(self, value: Optional[str]) -> None:
        self.__payment_reference = value

    @property
    def qr_code(self) -> Optional[str]:
        """
        | This field provides a Base64-encoded string representing a standardized payment QR code. The payload contains the complete transaction initiation data, including Service Tag, Version, Character Set, Identification, BIC, Beneficiary Name, IBAN, Amount, and Communication reference.

        Type: str
        """
        return self.__qr_code

    @qr_code.setter
    def qr_code(self, value: Optional[str]) -> None:
        self.__qr_code = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct11, self).to_dictionary()
        if self.payment_bic is not None:
            dictionary['paymentBIC'] = self.payment_bic
        if self.payment_beneficiary is not None:
            dictionary['paymentBeneficiary'] = self.payment_beneficiary
        if self.payment_iban is not None:
            dictionary['paymentIBAN'] = self.payment_iban
        if self.payment_reference is not None:
            dictionary['paymentReference'] = self.payment_reference
        if self.qr_code is not None:
            dictionary['qrCode'] = self.qr_code
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct11':
        super(PaymentProduct11, self).from_dictionary(dictionary)
        if 'paymentBIC' in dictionary:
            self.payment_bic = dictionary['paymentBIC']
        if 'paymentBeneficiary' in dictionary:
            self.payment_beneficiary = dictionary['paymentBeneficiary']
        if 'paymentIBAN' in dictionary:
            self.payment_iban = dictionary['paymentIBAN']
        if 'paymentReference' in dictionary:
            self.payment_reference = dictionary['paymentReference']
        if 'qrCode' in dictionary:
            self.qr_code = dictionary['qrCode']
        return self

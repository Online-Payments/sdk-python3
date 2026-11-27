#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentProduct11(DataObject):

    __slots__ = (
        "__payment_bic",
        "__payment_beneficiary",
        "__payment_iban",
        "__payment_reference",
        "__qr_code",
    )

    __payment_bic: str | None
    __payment_beneficiary: str | None
    __payment_iban: str | None
    __payment_reference: str | None
    __qr_code: str | None

    def __init__(
        self,
        *,
        payment_bic: str | None = None,
        payment_beneficiary: str | None = None,
        payment_iban: str | None = None,
        payment_reference: str | None = None,
        qr_code: str | None = None,
    ) -> None:
        self.payment_bic = payment_bic
        self.payment_beneficiary = payment_beneficiary
        self.payment_iban = payment_iban
        self.payment_reference = payment_reference
        self.qr_code = qr_code

    @property
    def payment_bic(self) -> str | None:
        """
        | The BIC is the Bank Identifier Code, also known as SWIFT code, used to identify banks internationally.

        Type: str
        """
        return self.__payment_bic

    @payment_bic.setter
    def payment_bic(self, value: str | None) -> None:
        self.__payment_bic = value

    @property
    def payment_beneficiary(self) -> str | None:
        """
        | The beneficiary of the payment

        Type: str
        """
        return self.__payment_beneficiary

    @payment_beneficiary.setter
    def payment_beneficiary(self, value: str | None) -> None:
        self.__payment_beneficiary = value

    @property
    def payment_iban(self) -> str | None:
        """
        | The IBAN is the International Bank Account Number. It is an internationally agreed format for the BBAN and includes the ISO country code and two check digits.

        Type: str
        """
        return self.__payment_iban

    @payment_iban.setter
    def payment_iban(self, value: str | None) -> None:
        self.__payment_iban = value

    @property
    def payment_reference(self) -> str | None:
        """
        | The reference for the payment

        Type: str
        """
        return self.__payment_reference

    @payment_reference.setter
    def payment_reference(self, value: str | None) -> None:
        self.__payment_reference = value

    @property
    def qr_code(self) -> str | None:
        """
        | This field provides a Base64-encoded string representing a standardized payment QR code. The payload contains the complete transaction initiation data, including Service Tag, Version, Character Set, Identification, BIC, Beneficiary Name, IBAN, Amount, and Communication reference.

        Type: str
        """
        return self.__qr_code

    @qr_code.setter
    def qr_code(self, value: str | None) -> None:
        self.__qr_code = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
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
        super().from_dictionary(dictionary)
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

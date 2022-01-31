# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class DecryptedPaymentData(DataObject):
    """
    | The payment data if you do the decryption of the encrypted payment data yourself.
    """

    __cardholder_name = None
    __cryptogram = None
    __dpan = None
    __eci = None
    __expiry_date = None

    @property
    def cardholder_name(self) -> str:
        """
        | Card holder's name on the card. 
        |  * For Apple Pay, maps to the cardholderName property in the encrypted payment data.

        Type: str
        """
        return self.__cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, value: str):
        self.__cardholder_name = value

    @property
    def cryptogram(self) -> str:
        """
        | The 3D secure online payment cryptogram.
        | * For Apple Pay, maps to the paymentData.onlinePaymentCryptogram property in the encrypted payment data.
        | * For Google Pay, maps to the paymentMethodDetails.3dsCryptogram property in the encrypted payment data.
        | Not allowed for Google Pay if the paymentMethod is CARD.

        Type: str
        """
        return self.__cryptogram

    @cryptogram.setter
    def cryptogram(self, value: str):
        self.__cryptogram = value

    @property
    def dpan(self) -> str:
        """
        | The device specific PAN. 
        |  * For Apple Pay, maps to the applicationPrimaryAccountNumber property in the encrypted payment.

        Type: str
        """
        return self.__dpan

    @dpan.setter
    def dpan(self, value: str):
        self.__dpan = value

    @property
    def eci(self) -> int:
        """
        | Electronic Commerce Indicator. 
        |  * For Apple Pay, maps to the paymentData.eciIndicator property in the encrypted payment data.

        Type: int
        """
        return self.__eci

    @eci.setter
    def eci(self, value: int):
        self.__eci = value

    @property
    def expiry_date(self) -> str:
        """
        | Expiry date of the card Format: MMYY. 
        |  * For Apple Pay, maps to the applicationExpirationDate property in the encrypted payment data. This property is formatted as YYMMDD, so this needs to be converted to get a correctly formatted expiry date

        Type: str
        """
        return self.__expiry_date

    @expiry_date.setter
    def expiry_date(self, value: str):
        self.__expiry_date = value

    def to_dictionary(self):
        dictionary = super(DecryptedPaymentData, self).to_dictionary()
        if self.cardholder_name is not None:
            dictionary['cardholderName'] = self.cardholder_name
        if self.cryptogram is not None:
            dictionary['cryptogram'] = self.cryptogram
        if self.dpan is not None:
            dictionary['dpan'] = self.dpan
        if self.eci is not None:
            dictionary['eci'] = self.eci
        if self.expiry_date is not None:
            dictionary['expiryDate'] = self.expiry_date
        return dictionary

    def from_dictionary(self, dictionary):
        super(DecryptedPaymentData, self).from_dictionary(dictionary)
        if 'cardholderName' in dictionary:
            self.cardholder_name = dictionary['cardholderName']
        if 'cryptogram' in dictionary:
            self.cryptogram = dictionary['cryptogram']
        if 'dpan' in dictionary:
            self.dpan = dictionary['dpan']
        if 'eci' in dictionary:
            self.eci = dictionary['eci']
        if 'expiryDate' in dictionary:
            self.expiry_date = dictionary['expiryDate']
        return self

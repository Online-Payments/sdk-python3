# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class CardFraudResults(DataObject):
    """
    | Fraud results contained in the CardFraudResults object
    """

    __avs_result = None
    __cvv_result = None
    __fraud_service_result = None

    @property
    def avs_result(self) -> str:
        """
        |  Result of the Address Verification Service checks. Possible values are: 
        |  * A - Address (Street) matches, Zip does not 
        |  * B - Street address match for international transactions—Postal code not verified due to incompatible formats 
        |  * C - Street address and postal code not verified for international transaction due to incompatible formats 
        |  * D - Street address and postal code match for international transaction, cardholder name is incorrect 
        |  * E - AVS error 
        |  * F - Address does match and five digit ZIP code does match (UK only) 
        |  * G - Address information is unavailable; international transaction; non-AVS participant 
        |  * H - Billing address and postal code match, cardholder name is incorrect (Amex) 
        |  * I - Address information not verified for international transaction 
        |  * K - Cardholder name matches (Amex) 
        |  * L - Cardholder name and postal code match (Amex) 
        |  * M - Cardholder name, street address, and postal code match for international transaction 
        |  * N - No Match on Address (Street) or Zip 
        |  * O - Cardholder name and address match (Amex) 
        |  * P - Postal codes match for international transaction—Street address not verified due to incompatible formats 
        |  * Q - Billing address matches, cardholder is incorrect (Amex) 
        |  * R - Retry, System unavailable or Timed out 
        |  * S - Service not supported by issuer 
        |  * U - Address information is unavailable 
        |  * W - 9 digit Zip matches, Address (Street) does not 
        |  * X - Exact AVS Match 
        |  * Y - Address (Street) and 5 digit Zip match 
        |  * Z - 5 digit Zip matches, Address (Street) does not 
        |  * 0 - No service available

        Type: str
        """
        return self.__avs_result

    @avs_result.setter
    def avs_result(self, value: str):
        self.__avs_result = value

    @property
    def cvv_result(self) -> str:
        """
        |  Result of the Card Verification Value checks. Possible values are: 
        |  * M - CVV check performed and valid value 
        |  * N - CVV checked and no match 
        |  * P - CVV check not performed, not requested 
        |  * S - Cardholder claims no CVV code on card, issuer states CVV-code should be on card 
        |  * U - Issuer not certified for CVV2 
        |  * Y - Server provider did not respond 
        |  * 0 - No service available

        Type: str
        """
        return self.__cvv_result

    @cvv_result.setter
    def cvv_result(self, value: str):
        self.__cvv_result = value

    @property
    def fraud_service_result(self) -> str:
        """
        | Resulting advice of the fraud prevention checks. Possible values are:
        | * accepted - Based on the checks performed the transaction can be accepted
        | * challenged - Based on the checks performed the transaction should be manually reviewed
        | * denied - Based on the checks performed the transaction should be rejected
        | * no-advice - No fraud check was requested/performed
        | * error - The fraud check resulted an error. Note that the fraud check was thus not performed.

        Type: str
        """
        return self.__fraud_service_result

    @fraud_service_result.setter
    def fraud_service_result(self, value: str):
        self.__fraud_service_result = value

    def to_dictionary(self):
        dictionary = super(CardFraudResults, self).to_dictionary()
        if self.avs_result is not None:
            dictionary['avsResult'] = self.avs_result
        if self.cvv_result is not None:
            dictionary['cvvResult'] = self.cvv_result
        if self.fraud_service_result is not None:
            dictionary['fraudServiceResult'] = self.fraud_service_result
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardFraudResults, self).from_dictionary(dictionary)
        if 'avsResult' in dictionary:
            self.avs_result = dictionary['avsResult']
        if 'cvvResult' in dictionary:
            self.cvv_result = dictionary['cvvResult']
        if 'fraudServiceResult' in dictionary:
            self.fraud_service_result = dictionary['fraudServiceResult']
        return self

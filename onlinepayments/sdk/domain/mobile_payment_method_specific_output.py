# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .card_fraud_results import CardFraudResults
from .data_object import DataObject
from .mobile_payment_data import MobilePaymentData
from .three_d_secure_results import ThreeDSecureResults


class MobilePaymentMethodSpecificOutput(DataObject):

    __authorisation_code: Optional[str] = None
    __fraud_results: Optional[CardFraudResults] = None
    __network: Optional[str] = None
    __payment_data: Optional[MobilePaymentData] = None
    __payment_product_id: Optional[int] = None
    __three_d_secure_results: Optional[ThreeDSecureResults] = None

    @property
    def authorisation_code(self) -> Optional[str]:
        """
        | Card Authorization code as returned by the acquirer

        Type: str
        """
        return self.__authorisation_code

    @authorisation_code.setter
    def authorisation_code(self, value: Optional[str]) -> None:
        self.__authorisation_code = value

    @property
    def fraud_results(self) -> Optional[CardFraudResults]:
        """
        | Fraud results contained in the CardFraudResults object

        Type: :class:`onlinepayments.sdk.domain.card_fraud_results.CardFraudResults`
        """
        return self.__fraud_results

    @fraud_results.setter
    def fraud_results(self, value: Optional[CardFraudResults]) -> None:
        self.__fraud_results = value

    @property
    def network(self) -> Optional[str]:
        """
        | The card network that was used for a mobile payment method operation

        Type: str
        """
        return self.__network

    @network.setter
    def network(self, value: Optional[str]) -> None:
        self.__network = value

    @property
    def payment_data(self) -> Optional[MobilePaymentData]:
        """
        | Object containing payment details

        Type: :class:`onlinepayments.sdk.domain.mobile_payment_data.MobilePaymentData`
        """
        return self.__payment_data

    @payment_data.setter
    def payment_data(self, value: Optional[MobilePaymentData]) -> None:
        self.__payment_data = value

    @property
    def payment_product_id(self) -> Optional[int]:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: Optional[int]) -> None:
        self.__payment_product_id = value

    @property
    def three_d_secure_results(self) -> Optional[ThreeDSecureResults]:
        """
        | 3D Secure results object

        Type: :class:`onlinepayments.sdk.domain.three_d_secure_results.ThreeDSecureResults`
        """
        return self.__three_d_secure_results

    @three_d_secure_results.setter
    def three_d_secure_results(self, value: Optional[ThreeDSecureResults]) -> None:
        self.__three_d_secure_results = value

    def to_dictionary(self) -> dict:
        dictionary = super(MobilePaymentMethodSpecificOutput, self).to_dictionary()
        if self.authorisation_code is not None:
            dictionary['authorisationCode'] = self.authorisation_code
        if self.fraud_results is not None:
            dictionary['fraudResults'] = self.fraud_results.to_dictionary()
        if self.network is not None:
            dictionary['network'] = self.network
        if self.payment_data is not None:
            dictionary['paymentData'] = self.payment_data.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        if self.three_d_secure_results is not None:
            dictionary['threeDSecureResults'] = self.three_d_secure_results.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MobilePaymentMethodSpecificOutput':
        super(MobilePaymentMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'authorisationCode' in dictionary:
            self.authorisation_code = dictionary['authorisationCode']
        if 'fraudResults' in dictionary:
            if not isinstance(dictionary['fraudResults'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraudResults']))
            value = CardFraudResults()
            self.fraud_results = value.from_dictionary(dictionary['fraudResults'])
        if 'network' in dictionary:
            self.network = dictionary['network']
        if 'paymentData' in dictionary:
            if not isinstance(dictionary['paymentData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentData']))
            value = MobilePaymentData()
            self.payment_data = value.from_dictionary(dictionary['paymentData'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'threeDSecureResults' in dictionary:
            if not isinstance(dictionary['threeDSecureResults'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecureResults']))
            value = ThreeDSecureResults()
            self.three_d_secure_results = value.from_dictionary(dictionary['threeDSecureResults'])
        return self

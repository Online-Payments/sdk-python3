# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .decrypted_payment_data import DecryptedPaymentData
from .mobile_payment_product320_specific_input import MobilePaymentProduct320SpecificInput


class MobilePaymentMethodSpecificInput(DataObject):

    __authorization_mode: Optional[str] = None
    __decrypted_payment_data: Optional[DecryptedPaymentData] = None
    __encrypted_payment_data: Optional[str] = None
    __ephemeral_key: Optional[str] = None
    __payment_product320_specific_input: Optional[MobilePaymentProduct320SpecificInput] = None
    __payment_product_id: Optional[int] = None
    __public_key_hash: Optional[str] = None
    __requires_approval: Optional[bool] = None

    @property
    def authorization_mode(self) -> Optional[str]:
        """
        | Determines the type of the authorization that will be used. Allowed values:
        
        * FINAL_AUTHORIZATION - The payment creation results in an authorization that is ready for capture. Final authorizations can't be reversed and need to be captured for the full amount within 7 days.
        * PRE_AUTHORIZATION - The payment creation results in a pre-authorization that is ready for capture. Pre-authortizations can be reversed and can be captured within 30 days. The capture amount can be lower than the authorized amount.
        * SALE - The payment creation results in an authorization that is already captured at the moment of approval.
        
        | Only used with some acquirers, ignored for acquirers that do not support this. In case the acquirer does not allow this to be specified the authorizationMode is 'unspecified', which behaves similar to a final authorization.

        Type: str
        """
        return self.__authorization_mode

    @authorization_mode.setter
    def authorization_mode(self, value: Optional[str]) -> None:
        self.__authorization_mode = value

    @property
    def decrypted_payment_data(self) -> Optional[DecryptedPaymentData]:
        """
        | The payment data if you do the decryption of the encrypted payment data yourself.

        Type: :class:`onlinepayments.sdk.domain.decrypted_payment_data.DecryptedPaymentData`
        """
        return self.__decrypted_payment_data

    @decrypted_payment_data.setter
    def decrypted_payment_data(self, value: Optional[DecryptedPaymentData]) -> None:
        self.__decrypted_payment_data = value

    @property
    def encrypted_payment_data(self) -> Optional[str]:
        """
        | The payment data if we will do the decryption of the encrypted payment data. Typically you'd use encryptedCustomerInput in the root of the create payment request to provide the encrypted payment data instead.
        
        * For Apple Pay, the encrypted payment data can be found in property data of the PKPayment.token.paymentData property.

        Type: str
        """
        return self.__encrypted_payment_data

    @encrypted_payment_data.setter
    def encrypted_payment_data(self, value: Optional[str]) -> None:
        self.__encrypted_payment_data = value

    @property
    def ephemeral_key(self) -> Optional[str]:
        """
        | Ephemeral Key A unique generated key used by Apple to encrypt data.

        Type: str
        """
        return self.__ephemeral_key

    @ephemeral_key.setter
    def ephemeral_key(self, value: Optional[str]) -> None:
        self.__ephemeral_key = value

    @property
    def payment_product320_specific_input(self) -> Optional[MobilePaymentProduct320SpecificInput]:
        """
        | Object containing information specific to Google Pay. Required for payments with product 320.

        Type: :class:`onlinepayments.sdk.domain.mobile_payment_product320_specific_input.MobilePaymentProduct320SpecificInput`
        """
        return self.__payment_product320_specific_input

    @payment_product320_specific_input.setter
    def payment_product320_specific_input(self, value: Optional[MobilePaymentProduct320SpecificInput]) -> None:
        self.__payment_product320_specific_input = value

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
    def public_key_hash(self) -> Optional[str]:
        """
        | Public Key Hash A unique identifier to retrieve key used by Apple to encrypt information.

        Type: str
        """
        return self.__public_key_hash

    @public_key_hash.setter
    def public_key_hash(self, value: Optional[str]) -> None:
        self.__public_key_hash = value

    @property
    def requires_approval(self) -> Optional[bool]:
        """
        * true = the payment requires approval before the funds will be captured using the Approve payment or Capture payment API
        * false = the payment does not require approval, and the funds will be captured automatically

        Type: bool
        """
        return self.__requires_approval

    @requires_approval.setter
    def requires_approval(self, value: Optional[bool]) -> None:
        self.__requires_approval = value

    def to_dictionary(self) -> dict:
        dictionary = super(MobilePaymentMethodSpecificInput, self).to_dictionary()
        if self.authorization_mode is not None:
            dictionary['authorizationMode'] = self.authorization_mode
        if self.decrypted_payment_data is not None:
            dictionary['decryptedPaymentData'] = self.decrypted_payment_data.to_dictionary()
        if self.encrypted_payment_data is not None:
            dictionary['encryptedPaymentData'] = self.encrypted_payment_data
        if self.ephemeral_key is not None:
            dictionary['ephemeralKey'] = self.ephemeral_key
        if self.payment_product320_specific_input is not None:
            dictionary['paymentProduct320SpecificInput'] = self.payment_product320_specific_input.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        if self.public_key_hash is not None:
            dictionary['publicKeyHash'] = self.public_key_hash
        if self.requires_approval is not None:
            dictionary['requiresApproval'] = self.requires_approval
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MobilePaymentMethodSpecificInput':
        super(MobilePaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'authorizationMode' in dictionary:
            self.authorization_mode = dictionary['authorizationMode']
        if 'decryptedPaymentData' in dictionary:
            if not isinstance(dictionary['decryptedPaymentData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['decryptedPaymentData']))
            value = DecryptedPaymentData()
            self.decrypted_payment_data = value.from_dictionary(dictionary['decryptedPaymentData'])
        if 'encryptedPaymentData' in dictionary:
            self.encrypted_payment_data = dictionary['encryptedPaymentData']
        if 'ephemeralKey' in dictionary:
            self.ephemeral_key = dictionary['ephemeralKey']
        if 'paymentProduct320SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct320SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct320SpecificInput']))
            value = MobilePaymentProduct320SpecificInput()
            self.payment_product320_specific_input = value.from_dictionary(dictionary['paymentProduct320SpecificInput'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'publicKeyHash' in dictionary:
            self.public_key_hash = dictionary['publicKeyHash']
        if 'requiresApproval' in dictionary:
            self.requires_approval = dictionary['requiresApproval']
        return self

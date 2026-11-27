#
# This file was automatically generated.
#
from .auto_capture import AutoCapture
from .data_object import DataObject
from .decrypted_payment_data import DecryptedPaymentData
from .mobile_payment_product302_specific_input import MobilePaymentProduct302SpecificInput
from .mobile_payment_product320_specific_input import MobilePaymentProduct320SpecificInput


class MobilePaymentMethodSpecificInput(DataObject):

    __slots__ = (
        "__authorization_mode",
        "__auto_capture",
        "__decrypted_payment_data",
        "__encrypted_payment_data",
        "__ephemeral_key",
        "__payment_product302_specific_input",
        "__payment_product320_specific_input",
        "__payment_product_id",
        "__public_key_hash",
        "__requires_approval",
    )

    __authorization_mode: str | None
    __auto_capture: AutoCapture | None
    __decrypted_payment_data: DecryptedPaymentData | None
    __encrypted_payment_data: str | None
    __ephemeral_key: str | None
    __payment_product302_specific_input: MobilePaymentProduct302SpecificInput | None
    __payment_product320_specific_input: MobilePaymentProduct320SpecificInput | None
    __payment_product_id: int | None
    __public_key_hash: str | None
    __requires_approval: bool | None

    def __init__(
        self,
        *,
        authorization_mode: str | None = None,
        auto_capture: AutoCapture | None = None,
        decrypted_payment_data: DecryptedPaymentData | None = None,
        encrypted_payment_data: str | None = None,
        ephemeral_key: str | None = None,
        payment_product302_specific_input: MobilePaymentProduct302SpecificInput | None = None,
        payment_product320_specific_input: MobilePaymentProduct320SpecificInput | None = None,
        payment_product_id: int | None = None,
        public_key_hash: str | None = None,
        requires_approval: bool | None = None,
    ) -> None:
        self.authorization_mode = authorization_mode
        self.auto_capture = auto_capture
        self.decrypted_payment_data = decrypted_payment_data
        self.encrypted_payment_data = encrypted_payment_data
        self.ephemeral_key = ephemeral_key
        self.payment_product302_specific_input = payment_product302_specific_input
        self.payment_product320_specific_input = payment_product320_specific_input
        self.payment_product_id = payment_product_id
        self.public_key_hash = public_key_hash
        self.requires_approval = requires_approval

    @property
    def authorization_mode(self) -> str | None:
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
    def authorization_mode(self, value: str | None) -> None:
        self.__authorization_mode = value

    @property
    def auto_capture(self) -> AutoCapture | None:
        """
        | Container for all auto capture-related settings.

        Type: :class:`onlinepayments.sdk.domain.auto_capture.AutoCapture`
        """
        return self.__auto_capture

    @auto_capture.setter
    def auto_capture(self, value: AutoCapture | None) -> None:
        self.__auto_capture = value

    @property
    def decrypted_payment_data(self) -> DecryptedPaymentData | None:
        """
        | The payment data if you do the decryption of the encrypted payment data yourself.

        Type: :class:`onlinepayments.sdk.domain.decrypted_payment_data.DecryptedPaymentData`
        """
        return self.__decrypted_payment_data

    @decrypted_payment_data.setter
    def decrypted_payment_data(self, value: DecryptedPaymentData | None) -> None:
        self.__decrypted_payment_data = value

    @property
    def encrypted_payment_data(self) -> str | None:
        """
        | The payment data if we will do the decryption of the encrypted payment data. Typically you'd use encryptedCustomerInput in the root of the create payment request to provide the encrypted payment data instead.
        
        * For Apple Pay, the encrypted payment data can be found in property data of the PKPayment.token.paymentData property.

        Type: str
        """
        return self.__encrypted_payment_data

    @encrypted_payment_data.setter
    def encrypted_payment_data(self, value: str | None) -> None:
        self.__encrypted_payment_data = value

    @property
    def ephemeral_key(self) -> str | None:
        """
        | Ephemeral Key A unique generated key used by Apple to encrypt data.

        Type: str
        """
        return self.__ephemeral_key

    @ephemeral_key.setter
    def ephemeral_key(self, value: str | None) -> None:
        self.__ephemeral_key = value

    @property
    def payment_product302_specific_input(self) -> MobilePaymentProduct302SpecificInput | None:
        """
        | Object containing information specific to Apple Pay.

        Type: :class:`onlinepayments.sdk.domain.mobile_payment_product302_specific_input.MobilePaymentProduct302SpecificInput`
        """
        return self.__payment_product302_specific_input

    @payment_product302_specific_input.setter
    def payment_product302_specific_input(self, value: MobilePaymentProduct302SpecificInput | None) -> None:
        self.__payment_product302_specific_input = value

    @property
    def payment_product320_specific_input(self) -> MobilePaymentProduct320SpecificInput | None:
        """
        | Object containing information specific to Google Pay. Required for payments with product 320.

        Type: :class:`onlinepayments.sdk.domain.mobile_payment_product320_specific_input.MobilePaymentProduct320SpecificInput`
        """
        return self.__payment_product320_specific_input

    @payment_product320_specific_input.setter
    def payment_product320_specific_input(self, value: MobilePaymentProduct320SpecificInput | None) -> None:
        self.__payment_product320_specific_input = value

    @property
    def payment_product_id(self) -> int | None:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: int | None) -> None:
        self.__payment_product_id = value

    @property
    def public_key_hash(self) -> str | None:
        """
        | Public Key Hash A unique identifier to retrieve key used by Apple to encrypt information.

        Type: str
        """
        return self.__public_key_hash

    @public_key_hash.setter
    def public_key_hash(self, value: str | None) -> None:
        self.__public_key_hash = value

    @property
    def requires_approval(self) -> bool | None:
        """
        * true = the payment requires approval before the funds will be captured using the Approve payment or Capture payment API
        * false = the payment does not require approval, and the funds will be captured automatically

        Type: bool
        """
        return self.__requires_approval

    @requires_approval.setter
    def requires_approval(self, value: bool | None) -> None:
        self.__requires_approval = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.authorization_mode is not None:
            dictionary['authorizationMode'] = self.authorization_mode
        if self.auto_capture is not None:
            dictionary['autoCapture'] = self.auto_capture.to_dictionary()
        if self.decrypted_payment_data is not None:
            dictionary['decryptedPaymentData'] = self.decrypted_payment_data.to_dictionary()
        if self.encrypted_payment_data is not None:
            dictionary['encryptedPaymentData'] = self.encrypted_payment_data
        if self.ephemeral_key is not None:
            dictionary['ephemeralKey'] = self.ephemeral_key
        if self.payment_product302_specific_input is not None:
            dictionary['paymentProduct302SpecificInput'] = self.payment_product302_specific_input.to_dictionary()
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
        super().from_dictionary(dictionary)
        if 'authorizationMode' in dictionary:
            self.authorization_mode = dictionary['authorizationMode']
        if 'autoCapture' in dictionary:
            if not isinstance(dictionary['autoCapture'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['autoCapture']))
            value = AutoCapture()
            self.auto_capture = value.from_dictionary(dictionary['autoCapture'])
        if 'decryptedPaymentData' in dictionary:
            if not isinstance(dictionary['decryptedPaymentData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['decryptedPaymentData']))
            value = DecryptedPaymentData()
            self.decrypted_payment_data = value.from_dictionary(dictionary['decryptedPaymentData'])
        if 'encryptedPaymentData' in dictionary:
            self.encrypted_payment_data = dictionary['encryptedPaymentData']
        if 'ephemeralKey' in dictionary:
            self.ephemeral_key = dictionary['ephemeralKey']
        if 'paymentProduct302SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct302SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct302SpecificInput']))
            value = MobilePaymentProduct302SpecificInput()
            self.payment_product302_specific_input = value.from_dictionary(dictionary['paymentProduct302SpecificInput'])
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

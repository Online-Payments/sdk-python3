#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentProduct3012SpecificInput(DataObject):

    __slots__ = (
        "__force_authentication",
        "__is_deferred_payment",
        "__is_wip_transaction",
        "__wip_merchant_authentication_method",
    )

    __force_authentication: bool | None
    __is_deferred_payment: bool | None
    __is_wip_transaction: bool | None
    __wip_merchant_authentication_method: str | None

    def __init__(
        self,
        *,
        force_authentication: bool | None = None,
        is_deferred_payment: bool | None = None,
        is_wip_transaction: bool | None = None,
        wip_merchant_authentication_method: str | None = None,
    ) -> None:
        self.force_authentication = force_authentication
        self.is_deferred_payment = is_deferred_payment
        self.is_wip_transaction = is_wip_transaction
        self.wip_merchant_authentication_method = wip_merchant_authentication_method

    @property
    def force_authentication(self) -> bool | None:
        """
        | Indicate whether 3D Secure authentication should be forced.

        Type: bool
        """
        return self.__force_authentication

    @force_authentication.setter
    def force_authentication(self, value: bool | None) -> None:
        self.__force_authentication = value

    @property
    def is_deferred_payment(self) -> bool | None:
        """
        | Indicate whether its a deferred payment.

        Type: bool
        """
        return self.__is_deferred_payment

    @is_deferred_payment.setter
    def is_deferred_payment(self, value: bool | None) -> None:
        self.__is_deferred_payment = value

    @property
    def is_wip_transaction(self) -> bool | None:
        """
        | Indicate whether its wallet initiated payment.

        Type: bool
        """
        return self.__is_wip_transaction

    @is_wip_transaction.setter
    def is_wip_transaction(self, value: bool | None) -> None:
        self.__is_wip_transaction = value

    @property
    def wip_merchant_authentication_method(self) -> str | None:
        """
        | Indicates how the cardholder was authenticated to the Merchant Wallet in the context of the transaction to which the BEPAF is attached
        
        * 01 = Username/password or PIN login successfully performed by cardholder.
        * 02 = Authentication through Secret/Private Key in Secure Hardware Solution was successfully performed.
        * 04 = Authentication through Secret/Private Key in Secure Software Solution (for example, mobile App) was successfully performed.
        * 08 = Location-based Authentication was successfully performed.
        * 10 = Environmental Authentication in Secure Software Solution (mobile App) was successfully performed.
        * 20 = Behavioral Analysis was successfully performed.
        * 40 = Biometrics Authentication was successfully performed.
        * 80 = Out of band user authentication was successfully performed.

        Type: str
        """
        return self.__wip_merchant_authentication_method

    @wip_merchant_authentication_method.setter
    def wip_merchant_authentication_method(self, value: str | None) -> None:
        self.__wip_merchant_authentication_method = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.force_authentication is not None:
            dictionary['forceAuthentication'] = self.force_authentication
        if self.is_deferred_payment is not None:
            dictionary['isDeferredPayment'] = self.is_deferred_payment
        if self.is_wip_transaction is not None:
            dictionary['isWipTransaction'] = self.is_wip_transaction
        if self.wip_merchant_authentication_method is not None:
            dictionary['wipMerchantAuthenticationMethod'] = self.wip_merchant_authentication_method
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct3012SpecificInput':
        super().from_dictionary(dictionary)
        if 'forceAuthentication' in dictionary:
            self.force_authentication = dictionary['forceAuthentication']
        if 'isDeferredPayment' in dictionary:
            self.is_deferred_payment = dictionary['isDeferredPayment']
        if 'isWipTransaction' in dictionary:
            self.is_wip_transaction = dictionary['isWipTransaction']
        if 'wipMerchantAuthenticationMethod' in dictionary:
            self.wip_merchant_authentication_method = dictionary['wipMerchantAuthenticationMethod']
        return self

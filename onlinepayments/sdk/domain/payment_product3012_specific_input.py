# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class PaymentProduct3012SpecificInput(DataObject):

    __force_authentication: Optional[bool] = None
    __is_deferred_payment: Optional[bool] = None
    __is_wip_transaction: Optional[bool] = None
    __wip_merchant_authentication_method: Optional[str] = None

    @property
    def force_authentication(self) -> Optional[bool]:
        """
        | Indicate whether 3D Secure authentication should be forced.

        Type: bool
        """
        return self.__force_authentication

    @force_authentication.setter
    def force_authentication(self, value: Optional[bool]) -> None:
        self.__force_authentication = value

    @property
    def is_deferred_payment(self) -> Optional[bool]:
        """
        | Indicate whether its a deferred payment.

        Type: bool
        """
        return self.__is_deferred_payment

    @is_deferred_payment.setter
    def is_deferred_payment(self, value: Optional[bool]) -> None:
        self.__is_deferred_payment = value

    @property
    def is_wip_transaction(self) -> Optional[bool]:
        """
        | Indicate whether its wallet initiated payment.

        Type: bool
        """
        return self.__is_wip_transaction

    @is_wip_transaction.setter
    def is_wip_transaction(self, value: Optional[bool]) -> None:
        self.__is_wip_transaction = value

    @property
    def wip_merchant_authentication_method(self) -> Optional[str]:
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
    def wip_merchant_authentication_method(self, value: Optional[str]) -> None:
        self.__wip_merchant_authentication_method = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentProduct3012SpecificInput, self).to_dictionary()
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
        super(PaymentProduct3012SpecificInput, self).from_dictionary(dictionary)
        if 'forceAuthentication' in dictionary:
            self.force_authentication = dictionary['forceAuthentication']
        if 'isDeferredPayment' in dictionary:
            self.is_deferred_payment = dictionary['isDeferredPayment']
        if 'isWipTransaction' in dictionary:
            self.is_wip_transaction = dictionary['isWipTransaction']
        if 'wipMerchantAuthenticationMethod' in dictionary:
            self.wip_merchant_authentication_method = dictionary['wipMerchantAuthenticationMethod']
        return self

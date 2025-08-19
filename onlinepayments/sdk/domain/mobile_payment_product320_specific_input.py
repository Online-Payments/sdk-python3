# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .g_pay_three_d_secure import GPayThreeDSecure
from .product320_recurring import Product320Recurring


class MobilePaymentProduct320SpecificInput(DataObject):

    __is_recurring: Optional[bool] = None
    __recurring: Optional[Product320Recurring] = None
    __three_d_secure: Optional[GPayThreeDSecure] = None
    __tokenize: Optional[bool] = None

    @property
    def is_recurring(self) -> Optional[bool]:
        """
        * true - Indicates that the transactions is part of a scheduled recurring sequence. In addition, recurringPaymentSequenceIndicator indicates if the transaction is the first or subsequent in a recurring sequence.
        * false - Indicates that the transaction is not part of a scheduled recurring sequence. The default value for this property is false. For HostedCheckout use the hostedCheckoutSpecificInput.isRecurring property instead.

        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value: Optional[bool]) -> None:
        self.__is_recurring = value

    @property
    def recurring(self) -> Optional[Product320Recurring]:
        """
        | Object containing information specific to Google Pay and recurring.

        Type: :class:`onlinepayments.sdk.domain.product320_recurring.Product320Recurring`
        """
        return self.__recurring

    @recurring.setter
    def recurring(self, value: Optional[Product320Recurring]) -> None:
        self.__recurring = value

    @property
    def three_d_secure(self) -> Optional[GPayThreeDSecure]:
        """
        | Object containing specific data regarding 3-D Secure

        Type: :class:`onlinepayments.sdk.domain.g_pay_three_d_secure.GPayThreeDSecure`
        """
        return self.__three_d_secure

    @three_d_secure.setter
    def three_d_secure(self, value: Optional[GPayThreeDSecure]) -> None:
        self.__three_d_secure = value

    @property
    def tokenize(self) -> Optional[bool]:
        """
        | Indicates if this transaction should be tokenized
        
        * true - Tokenize the transaction. Note that a payment on the payment platform that results in a status REDIRECTED cannot be tokenized in this way.
        * false - Do not tokenize the transaction, unless it would be tokenized by other means such as auto-tokenization of recurring payments.

        Type: bool
        """
        return self.__tokenize

    @tokenize.setter
    def tokenize(self, value: Optional[bool]) -> None:
        self.__tokenize = value

    def to_dictionary(self) -> dict:
        dictionary = super(MobilePaymentProduct320SpecificInput, self).to_dictionary()
        if self.is_recurring is not None:
            dictionary['isRecurring'] = self.is_recurring
        if self.recurring is not None:
            dictionary['recurring'] = self.recurring.to_dictionary()
        if self.three_d_secure is not None:
            dictionary['threeDSecure'] = self.three_d_secure.to_dictionary()
        if self.tokenize is not None:
            dictionary['tokenize'] = self.tokenize
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MobilePaymentProduct320SpecificInput':
        super(MobilePaymentProduct320SpecificInput, self).from_dictionary(dictionary)
        if 'isRecurring' in dictionary:
            self.is_recurring = dictionary['isRecurring']
        if 'recurring' in dictionary:
            if not isinstance(dictionary['recurring'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['recurring']))
            value = Product320Recurring()
            self.recurring = value.from_dictionary(dictionary['recurring'])
        if 'threeDSecure' in dictionary:
            if not isinstance(dictionary['threeDSecure'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecure']))
            value = GPayThreeDSecure()
            self.three_d_secure = value.from_dictionary(dictionary['threeDSecure'])
        if 'tokenize' in dictionary:
            self.tokenize = dictionary['tokenize']
        return self

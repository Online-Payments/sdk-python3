#
# This file was automatically generated.
#
from .apple_pay_recurring_payment_request import ApplePayRecurringPaymentRequest
from .data_object import DataObject
from .product302_recurring import Product302Recurring


class MobilePaymentProduct302SpecificInput(DataObject):

    __slots__ = (
        "__apple_pay_recurring_payment_request",
        "__is_recurring",
        "__recurring",
        "__tokenize",
    )

    __apple_pay_recurring_payment_request: ApplePayRecurringPaymentRequest | None
    __is_recurring: bool | None
    __recurring: Product302Recurring | None
    __tokenize: bool | None

    def __init__(
        self,
        *,
        apple_pay_recurring_payment_request: ApplePayRecurringPaymentRequest | None = None,
        is_recurring: bool | None = None,
        recurring: Product302Recurring | None = None,
        tokenize: bool | None = None,
    ) -> None:
        self.apple_pay_recurring_payment_request = apple_pay_recurring_payment_request
        self.is_recurring = is_recurring
        self.recurring = recurring
        self.tokenize = tokenize

    @property
    def apple_pay_recurring_payment_request(self) -> ApplePayRecurringPaymentRequest | None:
        """
        | Object containing information specific to Apple Pay recurring request. Only used for HostedCheckout.

        Type: :class:`onlinepayments.sdk.domain.apple_pay_recurring_payment_request.ApplePayRecurringPaymentRequest`
        """
        return self.__apple_pay_recurring_payment_request

    @apple_pay_recurring_payment_request.setter
    def apple_pay_recurring_payment_request(self, value: ApplePayRecurringPaymentRequest | None) -> None:
        self.__apple_pay_recurring_payment_request = value

    @property
    def is_recurring(self) -> bool | None:
        """
        * true - Indicates that the transaction is part of a scheduled recurring sequence. In addition, recurringPaymentSequenceIndicator indicates if the transaction is the first or subsequent in a recurring sequence.
        * false - Indicates that the transaction is not part of a scheduled recurring sequence. The default value for this property is false. For HostedCheckout use the hostedCheckoutSpecificInput.isRecurring property instead.

        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value: bool | None) -> None:
        self.__is_recurring = value

    @property
    def recurring(self) -> Product302Recurring | None:
        """
        | Object containing information specific to Apple Pay and recurring.

        Type: :class:`onlinepayments.sdk.domain.product302_recurring.Product302Recurring`
        """
        return self.__recurring

    @recurring.setter
    def recurring(self, value: Product302Recurring | None) -> None:
        self.__recurring = value

    @property
    def tokenize(self) -> bool | None:
        """
        | Indicates if this transaction should be tokenized
        
        * true - Tokenize the transaction.
        * false - Do not tokenize the transaction, unless it would be tokenized by other means such as auto-tokenization of recurring payments.

        Type: bool
        """
        return self.__tokenize

    @tokenize.setter
    def tokenize(self, value: bool | None) -> None:
        self.__tokenize = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.apple_pay_recurring_payment_request is not None:
            dictionary['applePayRecurringPaymentRequest'] = self.apple_pay_recurring_payment_request.to_dictionary()
        if self.is_recurring is not None:
            dictionary['isRecurring'] = self.is_recurring
        if self.recurring is not None:
            dictionary['recurring'] = self.recurring.to_dictionary()
        if self.tokenize is not None:
            dictionary['tokenize'] = self.tokenize
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MobilePaymentProduct302SpecificInput':
        super().from_dictionary(dictionary)
        if 'applePayRecurringPaymentRequest' in dictionary:
            if not isinstance(dictionary['applePayRecurringPaymentRequest'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['applePayRecurringPaymentRequest']))
            value = ApplePayRecurringPaymentRequest()
            self.apple_pay_recurring_payment_request = value.from_dictionary(dictionary['applePayRecurringPaymentRequest'])
        if 'isRecurring' in dictionary:
            self.is_recurring = dictionary['isRecurring']
        if 'recurring' in dictionary:
            if not isinstance(dictionary['recurring'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['recurring']))
            value = Product302Recurring()
            self.recurring = value.from_dictionary(dictionary['recurring'])
        if 'tokenize' in dictionary:
            self.tokenize = dictionary['tokenize']
        return self

# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .card_payment_method_specific_input_for_hosted_checkout import CardPaymentMethodSpecificInputForHostedCheckout
from .data_object import DataObject
from .payment_product_filters_hosted_checkout import PaymentProductFiltersHostedCheckout


class HostedCheckoutSpecificInput(DataObject):

    __allowed_number_of_payment_attempts: Optional[int] = None
    __card_payment_method_specific_input: Optional[CardPaymentMethodSpecificInputForHostedCheckout] = None
    __is_recurring: Optional[bool] = None
    __locale: Optional[str] = None
    __payment_product_filters: Optional[PaymentProductFiltersHostedCheckout] = None
    __return_url: Optional[str] = None
    __session_timeout: Optional[int] = None
    __show_result_page: Optional[bool] = None
    __tokens: Optional[str] = None
    __variant: Optional[str] = None

    @property
    def allowed_number_of_payment_attempts(self) -> Optional[int]:
        """
        | The maximum number of times a customer can try to pay before the payment is definitely declined. The value must be between 1 and 10. By default, the value is set to 10 attempts.

        Type: int
        """
        return self.__allowed_number_of_payment_attempts

    @allowed_number_of_payment_attempts.setter
    def allowed_number_of_payment_attempts(self, value: Optional[int]) -> None:
        self.__allowed_number_of_payment_attempts = value

    @property
    def card_payment_method_specific_input(self) -> Optional[CardPaymentMethodSpecificInputForHostedCheckout]:
        """
        | Object containing card payment specific data for hosted checkout

        Type: :class:`onlinepayments.sdk.domain.card_payment_method_specific_input_for_hosted_checkout.CardPaymentMethodSpecificInputForHostedCheckout`
        """
        return self.__card_payment_method_specific_input

    @card_payment_method_specific_input.setter
    def card_payment_method_specific_input(self, value: Optional[CardPaymentMethodSpecificInputForHostedCheckout]) -> None:
        self.__card_payment_method_specific_input = value

    @property
    def is_recurring(self) -> Optional[bool]:
        """
        * true - Only payment products that support recurring payments will be shown. Any transactions created will also be tagged as being a first of a recurring sequence.
        * false - Only payment products that support one-off payments will be shown. The default value for this property is false.

        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value: Optional[bool]) -> None:
        self.__is_recurring = value

    @property
    def locale(self) -> Optional[str]:
        """
        | Locale used in the GUI towards the consumer.

        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value: Optional[str]) -> None:
        self.__locale = value

    @property
    def payment_product_filters(self) -> Optional[PaymentProductFiltersHostedCheckout]:
        """
        | Contains the payment product ids and payment product groups that will be used for manipulating the payment products available for the payment to the customer.

        Type: :class:`onlinepayments.sdk.domain.payment_product_filters_hosted_checkout.PaymentProductFiltersHostedCheckout`
        """
        return self.__payment_product_filters

    @payment_product_filters.setter
    def payment_product_filters(self, value: Optional[PaymentProductFiltersHostedCheckout]) -> None:
        self.__payment_product_filters = value

    @property
    def return_url(self) -> Optional[str]:
        """
        | The URL that the customer is redirect to after the payment flow has finished. You can add any number of key value pairs in the query string that, for instance help you to identify the customer when they return to your site. Please note that we will also append some additional key value pairs that will also help you with this identification process. Note: The provided URL should be absolute and contain the protocol to use, e.g. http:// or https://. For use on mobile devices a custom protocol can be used in the form of protocol://. This protocol must be registered on the device first. URLs without a protocol will be rejected.

        Type: str
        """
        return self.__return_url

    @return_url.setter
    def return_url(self, value: Optional[str]) -> None:
        self.__return_url = value

    @property
    def session_timeout(self) -> Optional[int]:
        """
        | The number of minutes after which the session will expire. By default, the value is set to 180 minutes.

        Type: int
        """
        return self.__session_timeout

    @session_timeout.setter
    def session_timeout(self, value: Optional[int]) -> None:
        self.__session_timeout = value

    @property
    def show_result_page(self) -> Optional[bool]:
        """
        * true - Default - Hosted Checkout will show a result page to the customer when applicable.
        * false - Hosted Checkout will redirect the customer back to the provided returnUrl when this is possible.

        Type: bool
        """
        return self.__show_result_page

    @show_result_page.setter
    def show_result_page(self, value: Optional[bool]) -> None:
        self.__show_result_page = value

    @property
    def tokens(self) -> Optional[str]:
        """
        | String containing comma separated tokens (no spaces) associated with the customer of this hosted session. Valid tokens will be used to present the customer the option to re-use previously used payment details. This means the customer for instance does not have to re-enter their card details again, which a big plus when the customer is using their mobile phone to complete the operation.

        Type: str
        """
        return self.__tokens

    @tokens.setter
    def tokens(self, value: Optional[str]) -> None:
        self.__tokens = value

    @property
    def variant(self) -> Optional[str]:
        """
        | It is possible to upload multiple templates of your payment pages using the Merchant Portal. You can force the use of a custom template by specifying it in the variant field. This allows you to test out the effect of certain changes to your payment pages in a controlled manner. Please note that you need to specify the filename of the template or customization.

        Type: str
        """
        return self.__variant

    @variant.setter
    def variant(self, value: Optional[str]) -> None:
        self.__variant = value

    def to_dictionary(self) -> dict:
        dictionary = super(HostedCheckoutSpecificInput, self).to_dictionary()
        if self.allowed_number_of_payment_attempts is not None:
            dictionary['allowedNumberOfPaymentAttempts'] = self.allowed_number_of_payment_attempts
        if self.card_payment_method_specific_input is not None:
            dictionary['cardPaymentMethodSpecificInput'] = self.card_payment_method_specific_input.to_dictionary()
        if self.is_recurring is not None:
            dictionary['isRecurring'] = self.is_recurring
        if self.locale is not None:
            dictionary['locale'] = self.locale
        if self.payment_product_filters is not None:
            dictionary['paymentProductFilters'] = self.payment_product_filters.to_dictionary()
        if self.return_url is not None:
            dictionary['returnUrl'] = self.return_url
        if self.session_timeout is not None:
            dictionary['sessionTimeout'] = self.session_timeout
        if self.show_result_page is not None:
            dictionary['showResultPage'] = self.show_result_page
        if self.tokens is not None:
            dictionary['tokens'] = self.tokens
        if self.variant is not None:
            dictionary['variant'] = self.variant
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'HostedCheckoutSpecificInput':
        super(HostedCheckoutSpecificInput, self).from_dictionary(dictionary)
        if 'allowedNumberOfPaymentAttempts' in dictionary:
            self.allowed_number_of_payment_attempts = dictionary['allowedNumberOfPaymentAttempts']
        if 'cardPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificInput']))
            value = CardPaymentMethodSpecificInputForHostedCheckout()
            self.card_payment_method_specific_input = value.from_dictionary(dictionary['cardPaymentMethodSpecificInput'])
        if 'isRecurring' in dictionary:
            self.is_recurring = dictionary['isRecurring']
        if 'locale' in dictionary:
            self.locale = dictionary['locale']
        if 'paymentProductFilters' in dictionary:
            if not isinstance(dictionary['paymentProductFilters'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProductFilters']))
            value = PaymentProductFiltersHostedCheckout()
            self.payment_product_filters = value.from_dictionary(dictionary['paymentProductFilters'])
        if 'returnUrl' in dictionary:
            self.return_url = dictionary['returnUrl']
        if 'sessionTimeout' in dictionary:
            self.session_timeout = dictionary['sessionTimeout']
        if 'showResultPage' in dictionary:
            self.show_result_page = dictionary['showResultPage']
        if 'tokens' in dictionary:
            self.tokens = dictionary['tokens']
        if 'variant' in dictionary:
            self.variant = dictionary['variant']
        return self

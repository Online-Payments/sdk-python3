#
# This file was automatically generated.
#
from .card_payment_method_specific_input_for_hosted_checkout import CardPaymentMethodSpecificInputForHostedCheckout
from .data_object import DataObject
from .payment_product_filters_hosted_checkout import PaymentProductFiltersHostedCheckout
from .split_payment_product_filters_hosted_checkout import SplitPaymentProductFiltersHostedCheckout


class HostedCheckoutSpecificInput(DataObject):

    __slots__ = (
        "__allowed_number_of_payment_attempts",
        "__auto_refund_split_payments",
        "__card_payment_method_specific_input",
        "__is_new_unscheduled_card_on_file_series",
        "__is_recurring",
        "__locale",
        "__payment_product_filters",
        "__return_url",
        "__session_timeout",
        "__show_result_page",
        "__split_payment_product_filters",
        "__tokens",
        "__variant",
    )

    __allowed_number_of_payment_attempts: int | None
    __auto_refund_split_payments: bool | None
    __card_payment_method_specific_input: CardPaymentMethodSpecificInputForHostedCheckout | None
    __is_new_unscheduled_card_on_file_series: bool | None
    __is_recurring: bool | None
    __locale: str | None
    __payment_product_filters: PaymentProductFiltersHostedCheckout | None
    __return_url: str | None
    __session_timeout: int | None
    __show_result_page: bool | None
    __split_payment_product_filters: SplitPaymentProductFiltersHostedCheckout | None
    __tokens: str | None
    __variant: str | None

    def __init__(
        self,
        *,
        allowed_number_of_payment_attempts: int | None = None,
        auto_refund_split_payments: bool | None = None,
        card_payment_method_specific_input: CardPaymentMethodSpecificInputForHostedCheckout | None = None,
        is_new_unscheduled_card_on_file_series: bool | None = None,
        is_recurring: bool | None = None,
        locale: str | None = None,
        payment_product_filters: PaymentProductFiltersHostedCheckout | None = None,
        return_url: str | None = None,
        session_timeout: int | None = None,
        show_result_page: bool | None = None,
        split_payment_product_filters: SplitPaymentProductFiltersHostedCheckout | None = None,
        tokens: str | None = None,
        variant: str | None = None,
    ) -> None:
        self.allowed_number_of_payment_attempts = allowed_number_of_payment_attempts
        self.auto_refund_split_payments = auto_refund_split_payments
        self.card_payment_method_specific_input = card_payment_method_specific_input
        self.is_new_unscheduled_card_on_file_series = is_new_unscheduled_card_on_file_series
        self.is_recurring = is_recurring
        self.locale = locale
        self.payment_product_filters = payment_product_filters
        self.return_url = return_url
        self.session_timeout = session_timeout
        self.show_result_page = show_result_page
        self.split_payment_product_filters = split_payment_product_filters
        self.tokens = tokens
        self.variant = variant

    @property
    def allowed_number_of_payment_attempts(self) -> int | None:
        """
        | The maximum number of times a customer can try to pay before the payment is definitely declined. The value must be between 1 and 10. By default, the value is set to 10 attempts.

        Type: int
        """
        return self.__allowed_number_of_payment_attempts

    @allowed_number_of_payment_attempts.setter
    def allowed_number_of_payment_attempts(self, value: int | None) -> None:
        self.__allowed_number_of_payment_attempts = value

    @property
    def auto_refund_split_payments(self) -> bool | None:
        """
        * true - If the customer cancels the order or if the order validity period expires, any payments in a final status related to that order will automatically be subject to a refund attempt to the customer.
        * false - Default - If the customer cancels the order or if the order's validity period expires, payments in a final status related to this order won't automatically be subject to a refund attempt to the customer.

        Type: bool
        """
        return self.__auto_refund_split_payments

    @auto_refund_split_payments.setter
    def auto_refund_split_payments(self, value: bool | None) -> None:
        self.__auto_refund_split_payments = value

    @property
    def card_payment_method_specific_input(self) -> CardPaymentMethodSpecificInputForHostedCheckout | None:
        """
        | Object containing card payment specific data for hosted checkout

        Type: :class:`onlinepayments.sdk.domain.card_payment_method_specific_input_for_hosted_checkout.CardPaymentMethodSpecificInputForHostedCheckout`
        """
        return self.__card_payment_method_specific_input

    @card_payment_method_specific_input.setter
    def card_payment_method_specific_input(self, value: CardPaymentMethodSpecificInputForHostedCheckout | None) -> None:
        self.__card_payment_method_specific_input = value

    @property
    def is_new_unscheduled_card_on_file_series(self) -> bool | None:
        """
        * true - A new unscheduled credentials on file series will be started. You will be able to use the paymentID of this transaction to initiate subsequent merchant initiated transactions. In the EU, the current transaction should be authenticated.
        * false - Default. No new card on file series created.

        Type: bool
        """
        return self.__is_new_unscheduled_card_on_file_series

    @is_new_unscheduled_card_on_file_series.setter
    def is_new_unscheduled_card_on_file_series(self, value: bool | None) -> None:
        self.__is_new_unscheduled_card_on_file_series = value

    @property
    def is_recurring(self) -> bool | None:
        """
        * true - Only payment products that support recurring payments will be shown. Any transactions created will also be tagged as being a first of a recurring sequence.
        * false - Only payment products that support one-off payments will be shown. The default value for this property is false.

        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value: bool | None) -> None:
        self.__is_recurring = value

    @property
    def locale(self) -> str | None:
        """
        | Locale used in the GUI towards the consumer.

        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value: str | None) -> None:
        self.__locale = value

    @property
    def payment_product_filters(self) -> PaymentProductFiltersHostedCheckout | None:
        """
        | Contains the payment product ids and payment product groups that will be used for manipulating the payment products available for the payment to the customer.

        Type: :class:`onlinepayments.sdk.domain.payment_product_filters_hosted_checkout.PaymentProductFiltersHostedCheckout`
        """
        return self.__payment_product_filters

    @payment_product_filters.setter
    def payment_product_filters(self, value: PaymentProductFiltersHostedCheckout | None) -> None:
        self.__payment_product_filters = value

    @property
    def return_url(self) -> str | None:
        """
        | The URL that the customer is redirected to after the payment flow has finished. You can add any number of key value pairs in the query string that, for instance help you to identify the customer when they return to your site. Please note that we will also append some additional key value pairs that will also help you with this identification process.
        |
        | Note: The provided URL should be absolute and contain the protocol to use, e.g. http:// or https://. For use on mobile devices a custom protocol can be used in the form of protocol://. This protocol must be registered on the device first.
        |
        | URLs without a protocol will be rejected. The RETURNMAC parameter is a random string that allows to authenticate calls to the returnUrl. Here is an example with ```json "hostedCheckoutSpecificInput": { "returnUrl":"https://www.google.com" }
        |
        | ``` result is that user is redirected to https://www.google.com/?RETURNMAC=37159fa4-773e-4ea7-a067-83b681107c62&hostedCheckoutId=4501638561

        Type: str
        """
        return self.__return_url

    @return_url.setter
    def return_url(self, value: str | None) -> None:
        self.__return_url = value

    @property
    def session_timeout(self) -> int | None:
        """
        | The number of minutes after which the session will expire. By default, the value is set to 180 minutes.

        Type: int
        """
        return self.__session_timeout

    @session_timeout.setter
    def session_timeout(self, value: int | None) -> None:
        self.__session_timeout = value

    @property
    def show_result_page(self) -> bool | None:
        """
        * true - Default - Hosted Checkout will show a result page to the customer when applicable.
        * false - Hosted Checkout will redirect the customer back to the provided returnUrl when this is possible.

        Type: bool
        """
        return self.__show_result_page

    @show_result_page.setter
    def show_result_page(self, value: bool | None) -> None:
        self.__show_result_page = value

    @property
    def split_payment_product_filters(self) -> SplitPaymentProductFiltersHostedCheckout | None:
        """
        | Contains the payment product IDs and payment product groups that will be used to manage the payment products available for the following payments in a split payment. Note that this filter is applied after the paymentProductFilter has been applied. It cannot be used to enable split payments with payment products that were not already allowed by paymentProductFilter.

        Type: :class:`onlinepayments.sdk.domain.split_payment_product_filters_hosted_checkout.SplitPaymentProductFiltersHostedCheckout`
        """
        return self.__split_payment_product_filters

    @split_payment_product_filters.setter
    def split_payment_product_filters(self, value: SplitPaymentProductFiltersHostedCheckout | None) -> None:
        self.__split_payment_product_filters = value

    @property
    def tokens(self) -> str | None:
        """
        | String containing comma separated tokens (no spaces) associated with the customer of this hosted session. Valid tokens will be used to present the customer the option to re-use previously used payment details. This means the customer for instance does not have to re-enter their card details again, which a big plus when the customer is using their mobile phone to complete the operation.

        Type: str
        """
        return self.__tokens

    @tokens.setter
    def tokens(self, value: str | None) -> None:
        self.__tokens = value

    @property
    def variant(self) -> str | None:
        """
        | You can force the use of a custom template by specifying it in the variant field. This allows you to test out the effect of certain changes to your payment pages in a controlled manner. Please note that you need to specify the filename of the template or customization.

        Type: str
        """
        return self.__variant

    @variant.setter
    def variant(self, value: str | None) -> None:
        self.__variant = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.allowed_number_of_payment_attempts is not None:
            dictionary['allowedNumberOfPaymentAttempts'] = self.allowed_number_of_payment_attempts
        if self.auto_refund_split_payments is not None:
            dictionary['autoRefundSplitPayments'] = self.auto_refund_split_payments
        if self.card_payment_method_specific_input is not None:
            dictionary['cardPaymentMethodSpecificInput'] = self.card_payment_method_specific_input.to_dictionary()
        if self.is_new_unscheduled_card_on_file_series is not None:
            dictionary['isNewUnscheduledCardOnFileSeries'] = self.is_new_unscheduled_card_on_file_series
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
        if self.split_payment_product_filters is not None:
            dictionary['splitPaymentProductFilters'] = self.split_payment_product_filters.to_dictionary()
        if self.tokens is not None:
            dictionary['tokens'] = self.tokens
        if self.variant is not None:
            dictionary['variant'] = self.variant
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'HostedCheckoutSpecificInput':
        super().from_dictionary(dictionary)
        if 'allowedNumberOfPaymentAttempts' in dictionary:
            self.allowed_number_of_payment_attempts = dictionary['allowedNumberOfPaymentAttempts']
        if 'autoRefundSplitPayments' in dictionary:
            self.auto_refund_split_payments = dictionary['autoRefundSplitPayments']
        if 'cardPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificInput']))
            value = CardPaymentMethodSpecificInputForHostedCheckout()
            self.card_payment_method_specific_input = value.from_dictionary(dictionary['cardPaymentMethodSpecificInput'])
        if 'isNewUnscheduledCardOnFileSeries' in dictionary:
            self.is_new_unscheduled_card_on_file_series = dictionary['isNewUnscheduledCardOnFileSeries']
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
        if 'splitPaymentProductFilters' in dictionary:
            if not isinstance(dictionary['splitPaymentProductFilters'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['splitPaymentProductFilters']))
            value = SplitPaymentProductFiltersHostedCheckout()
            self.split_payment_product_filters = value.from_dictionary(dictionary['splitPaymentProductFilters'])
        if 'tokens' in dictionary:
            self.tokens = dictionary['tokens']
        if 'variant' in dictionary:
            self.variant = dictionary['variant']
        return self

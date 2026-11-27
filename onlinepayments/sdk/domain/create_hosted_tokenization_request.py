#
# This file was automatically generated.
#
from .credit_card_specific_input_hosted_tokenization import CreditCardSpecificInputHostedTokenization
from .data_object import DataObject
from .payment_product_filters_hosted_tokenization import PaymentProductFiltersHostedTokenization


class CreateHostedTokenizationRequest(DataObject):

    __slots__ = (
        "__ask_consumer_consent",
        "__credit_card_specific_input",
        "__locale",
        "__origin",
        "__payment_product_filters",
        "__tokens",
        "__variant",
    )

    __ask_consumer_consent: bool | None
    __credit_card_specific_input: CreditCardSpecificInputHostedTokenization | None
    __locale: str | None
    __origin: str | None
    __payment_product_filters: PaymentProductFiltersHostedTokenization | None
    __tokens: str | None
    __variant: str | None

    def __init__(
        self,
        *,
        ask_consumer_consent: bool | None = None,
        credit_card_specific_input: CreditCardSpecificInputHostedTokenization | None = None,
        locale: str | None = None,
        origin: str | None = None,
        payment_product_filters: PaymentProductFiltersHostedTokenization | None = None,
        tokens: str | None = None,
        variant: str | None = None,
    ) -> None:
        self.ask_consumer_consent = ask_consumer_consent
        self.credit_card_specific_input = credit_card_specific_input
        self.locale = locale
        self.origin = origin
        self.payment_product_filters = payment_product_filters
        self.tokens = tokens
        self.variant = variant

    @property
    def ask_consumer_consent(self) -> bool | None:
        """
        | Indicate if the tokenization form should contain a checkbox asking the user to give consent for storing their information for future payments. If this parameter is false or missing, you should ask the user yourself and provide their answer when submitting the Tokenizer in your JavaScript code. To pass this choice set the submitTokenization function's parameter storePermanently to false, if you choose not to store the token for subsequent payments, or to true otherwise.

        Type: bool
        """
        return self.__ask_consumer_consent

    @ask_consumer_consent.setter
    def ask_consumer_consent(self, value: bool | None) -> None:
        self.__ask_consumer_consent = value

    @property
    def credit_card_specific_input(self) -> CreditCardSpecificInputHostedTokenization | None:
        """
        Type: :class:`onlinepayments.sdk.domain.credit_card_specific_input_hosted_tokenization.CreditCardSpecificInputHostedTokenization`
        """
        return self.__credit_card_specific_input

    @credit_card_specific_input.setter
    def credit_card_specific_input(self, value: CreditCardSpecificInputHostedTokenization | None) -> None:
        self.__credit_card_specific_input = value

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
    def origin(self) -> str | None:
        """
        | The origin of the merchant site. This is used to prevent the HTP iframe from being embedded by other origins.

        Type: str
        """
        return self.__origin

    @origin.setter
    def origin(self, value: str | None) -> None:
        self.__origin = value

    @property
    def payment_product_filters(self) -> PaymentProductFiltersHostedTokenization | None:
        """
        | Contains the payment product ids that will be used for manipulating the payment products available for the payment to the customer.

        Type: :class:`onlinepayments.sdk.domain.payment_product_filters_hosted_tokenization.PaymentProductFiltersHostedTokenization`
        """
        return self.__payment_product_filters

    @payment_product_filters.setter
    def payment_product_filters(self, value: PaymentProductFiltersHostedTokenization | None) -> None:
        self.__payment_product_filters = value

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
        if self.ask_consumer_consent is not None:
            dictionary['askConsumerConsent'] = self.ask_consumer_consent
        if self.credit_card_specific_input is not None:
            dictionary['creditCardSpecificInput'] = self.credit_card_specific_input.to_dictionary()
        if self.locale is not None:
            dictionary['locale'] = self.locale
        if self.origin is not None:
            dictionary['origin'] = self.origin
        if self.payment_product_filters is not None:
            dictionary['paymentProductFilters'] = self.payment_product_filters.to_dictionary()
        if self.tokens is not None:
            dictionary['tokens'] = self.tokens
        if self.variant is not None:
            dictionary['variant'] = self.variant
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreateHostedTokenizationRequest':
        super().from_dictionary(dictionary)
        if 'askConsumerConsent' in dictionary:
            self.ask_consumer_consent = dictionary['askConsumerConsent']
        if 'creditCardSpecificInput' in dictionary:
            if not isinstance(dictionary['creditCardSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['creditCardSpecificInput']))
            value = CreditCardSpecificInputHostedTokenization()
            self.credit_card_specific_input = value.from_dictionary(dictionary['creditCardSpecificInput'])
        if 'locale' in dictionary:
            self.locale = dictionary['locale']
        if 'origin' in dictionary:
            self.origin = dictionary['origin']
        if 'paymentProductFilters' in dictionary:
            if not isinstance(dictionary['paymentProductFilters'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProductFilters']))
            value = PaymentProductFiltersHostedTokenization()
            self.payment_product_filters = value.from_dictionary(dictionary['paymentProductFilters'])
        if 'tokens' in dictionary:
            self.tokens = dictionary['tokens']
        if 'variant' in dictionary:
            self.variant = dictionary['variant']
        return self

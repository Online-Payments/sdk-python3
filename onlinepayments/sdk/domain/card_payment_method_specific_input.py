# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.card import Card
from onlinepayments.sdk.domain.card_recurrence_details import CardRecurrenceDetails
from onlinepayments.sdk.domain.currency_conversion_input import CurrencyConversionInput
from onlinepayments.sdk.domain.multiple_payment_information import MultiplePaymentInformation
from onlinepayments.sdk.domain.payment_product130_specific_input import PaymentProduct130SpecificInput
from onlinepayments.sdk.domain.payment_product3208_specific_input import PaymentProduct3208SpecificInput
from onlinepayments.sdk.domain.payment_product3209_specific_input import PaymentProduct3209SpecificInput
from onlinepayments.sdk.domain.three_d_secure import ThreeDSecure


class CardPaymentMethodSpecificInput(DataObject):
    """
    | Object containing the specific input details for card payments
    """

    __allow_dynamic_linking = None
    __authorization_mode = None
    __card = None
    __card_on_file_recurring_expiration = None
    __card_on_file_recurring_frequency = None
    __currency_conversion = None
    __initial_scheme_transaction_id = None
    __is_recurring = None
    __multiple_payment_information = None
    __payment_product130_specific_input = None
    __payment_product3208_specific_input = None
    __payment_product3209_specific_input = None
    __payment_product_id = None
    __recurring = None
    __return_url = None
    __scheme_reference_data = None
    __skip_authentication = None
    __three_d_secure = None
    __token = None
    __tokenize = None
    __transaction_channel = None
    __unscheduled_card_on_file_requestor = None
    __unscheduled_card_on_file_sequence_indicator = None

    @property
    def allow_dynamic_linking(self) -> bool:
        """
        | * true - Default - Allows subsequent payments to use PSD2 dynamic linking from this payment (including Card On File).
        | * false - Indicates that the dynamic linking (including Card On File data) will be ignored.

        Type: bool
        """
        return self.__allow_dynamic_linking

    @allow_dynamic_linking.setter
    def allow_dynamic_linking(self, value: bool):
        self.__allow_dynamic_linking = value

    @property
    def authorization_mode(self) -> str:
        """
        | Determines the type of the authorization that will be used. Allowed values: 
        |   * FINAL_AUTHORIZATION - The payment creation results in an authorization that is ready for capture. Final authorizations can't be reversed and need to be captured for the full amount within 7 days. 
        |   * PRE_AUTHORIZATION - The payment creation results in a pre-authorization that is ready for capture. Pre-authortizations can be reversed and can be captured within 30 days. The capture amount can be lower than the authorized amount. 
        |   * SALE - The payment creation results in an authorization that is already captured at the moment of approval. 
        
        |   Only used with some acquirers, ignored for acquirers that do not support this. In case the acquirer does not allow this to be specified the authorizationMode is 'unspecified', which behaves similar to a final authorization.

        Type: str
        """
        return self.__authorization_mode

    @authorization_mode.setter
    def authorization_mode(self, value: str):
        self.__authorization_mode = value

    @property
    def card(self) -> Card:
        """
        | Object containing card details

        Type: :class:`onlinepayments.sdk.domain.card.Card`
        """
        return self.__card

    @card.setter
    def card(self, value: Card):
        self.__card = value

    @property
    def card_on_file_recurring_expiration(self) -> str:
        """
        | The end date of the last scheduled payment in a series of transactions.
        | Format YYYYMMDD

        Type: str
        """
        return self.__card_on_file_recurring_expiration

    @card_on_file_recurring_expiration.setter
    def card_on_file_recurring_expiration(self, value: str):
        self.__card_on_file_recurring_expiration = value

    @property
    def card_on_file_recurring_frequency(self) -> str:
        """
        | Period of payment occurrence for recurring and installment payments. Allowed values:
        |   * Yearly
        |   * Quarterly
        |   * Monthly
        |   * Weekly
        |   * Daily

        Type: str
        """
        return self.__card_on_file_recurring_frequency

    @card_on_file_recurring_frequency.setter
    def card_on_file_recurring_frequency(self, value: str):
        self.__card_on_file_recurring_frequency = value

    @property
    def currency_conversion(self) -> CurrencyConversionInput:
        """
        Type: :class:`onlinepayments.sdk.domain.currency_conversion_input.CurrencyConversionInput`
        """
        return self.__currency_conversion

    @currency_conversion.setter
    def currency_conversion(self, value: CurrencyConversionInput):
        self.__currency_conversion = value

    @property
    def initial_scheme_transaction_id(self) -> str:
        """
        | The unique scheme transactionId of the initial transaction that was performed with SCA. In case this is unknown a scheme transactionId of an earlier transaction part of the same sequence can be used as a fall-back. Strongly advised to be submitted for any MerchantInitiated or recurring transaction (a subsequent one).

        Type: str
        """
        return self.__initial_scheme_transaction_id

    @initial_scheme_transaction_id.setter
    def initial_scheme_transaction_id(self, value: str):
        self.__initial_scheme_transaction_id = value

    @property
    def is_recurring(self) -> bool:
        """
        | * true - Indicates that the transactions is part of a scheduled recurring sequence. In addition, recurringPaymentSequenceIndicator indicates if the transaction is the first or subsequent in a recurring sequence. 
        | * false - Indicates that the transaction is not part of a scheduled recurring sequence.
        | The default value for this property is false.

        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value: bool):
        self.__is_recurring = value

    @property
    def multiple_payment_information(self) -> MultiplePaymentInformation:
        """
        | Container announcing forecoming subsequent payments. Holds modalities of these subsequent payments.

        Type: :class:`onlinepayments.sdk.domain.multiple_payment_information.MultiplePaymentInformation`
        """
        return self.__multiple_payment_information

    @multiple_payment_information.setter
    def multiple_payment_information(self, value: MultiplePaymentInformation):
        self.__multiple_payment_information = value

    @property
    def payment_product130_specific_input(self) -> PaymentProduct130SpecificInput:
        """
        | Object containing specific input required for CB payments

        Type: :class:`onlinepayments.sdk.domain.payment_product130_specific_input.PaymentProduct130SpecificInput`
        """
        return self.__payment_product130_specific_input

    @payment_product130_specific_input.setter
    def payment_product130_specific_input(self, value: PaymentProduct130SpecificInput):
        self.__payment_product130_specific_input = value

    @property
    def payment_product3208_specific_input(self) -> PaymentProduct3208SpecificInput:
        """
        | Object containing specific input required for OneyDuplo Leroy Merlin payments.

        Type: :class:`onlinepayments.sdk.domain.payment_product3208_specific_input.PaymentProduct3208SpecificInput`
        """
        return self.__payment_product3208_specific_input

    @payment_product3208_specific_input.setter
    def payment_product3208_specific_input(self, value: PaymentProduct3208SpecificInput):
        self.__payment_product3208_specific_input = value

    @property
    def payment_product3209_specific_input(self) -> PaymentProduct3209SpecificInput:
        """
        | Object containing specific input required for OneyDuplo Alcampo payments.

        Type: :class:`onlinepayments.sdk.domain.payment_product3209_specific_input.PaymentProduct3209SpecificInput`
        """
        return self.__payment_product3209_specific_input

    @payment_product3209_specific_input.setter
    def payment_product3209_specific_input(self, value: PaymentProduct3209SpecificInput):
        self.__payment_product3209_specific_input = value

    @property
    def payment_product_id(self) -> int:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: int):
        self.__payment_product_id = value

    @property
    def recurring(self) -> CardRecurrenceDetails:
        """
        | Object containing data related to recurring

        Type: :class:`onlinepayments.sdk.domain.card_recurrence_details.CardRecurrenceDetails`
        """
        return self.__recurring

    @recurring.setter
    def recurring(self, value: CardRecurrenceDetails):
        self.__recurring = value

    @property
    def return_url(self) -> str:
        """
        | The URL that the customer is redirect to after the payment flow has finished. You can add any number of key value pairs in the query string that, for instance help you to identify the customer when they return to your site. Please note that we will also append some additional key value pairs that will also help you with this identification process.
        | Note: The provided URL should be absolute and contain the protocol to use, e.g. http:// or https://. For use on mobile devices a custom protocol can be used in the form of protocol://. This protocol must be registered on the device first.
        | URLs without a protocol will be rejected.

        Type: str
        """
        return self.__return_url

    @return_url.setter
    def return_url(self, value: str):
        self.__return_url = value

    @property
    def scheme_reference_data(self) -> str:
        """
        | This is the unique Scheme Reference Data from the initial transaction that was performed with a Strong Customer Authentication. In case this value is unknown, a Scheme Reference of an earlier transaction that was part of the same sequence can be used as a fall-back. Still, it is strongly advised to submit this value for any Merchant Initiated Transaction or any recurring transaction (hereby defined as "Subsequent").

        Type: str
        """
        return self.__scheme_reference_data

    @scheme_reference_data.setter
    def scheme_reference_data(self, value: str):
        self.__scheme_reference_data = value

    @property
    def skip_authentication(self) -> bool:
        """
        | Deprecated: Use threeDSecure.skipAuthentication instead.
        |  * true = 3D Secure authentication will be skipped for this transaction. This setting should be used when isRecurring is set to true and recurringPaymentSequenceIndicator is set to recurring.
        |  * false = 3D Secure authentication will not be skipped for this transaction.
        
        |   Note: This is only possible if your account in our system is setup for 3D Secure authentication and if your configuration in our system allows you to override it per transaction.

        Type: bool
        """
        return self.__skip_authentication

    @skip_authentication.setter
    def skip_authentication(self, value: bool):
        self.__skip_authentication = value

    @property
    def three_d_secure(self) -> ThreeDSecure:
        """
        | Object containing specific data regarding 3-D Secure

        Type: :class:`onlinepayments.sdk.domain.three_d_secure.ThreeDSecure`
        """
        return self.__three_d_secure

    @three_d_secure.setter
    def three_d_secure(self, value: ThreeDSecure):
        self.__three_d_secure = value

    @property
    def token(self) -> str:
        """
        | ID of the token to use to create the payment.

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: str):
        self.__token = value

    @property
    def tokenize(self) -> bool:
        """
        | Indicates if this transaction should be tokenized
        |  * true - Tokenize the transaction. Note that a payment on the payment platform that results in a status REDIRECTED cannot be tokenized in this way.
        |  * false - Do not tokenize the transaction, unless it would be tokenized by other means such as auto-tokenization of recurring payments.

        Type: bool
        """
        return self.__tokenize

    @tokenize.setter
    def tokenize(self, value: bool):
        self.__tokenize = value

    @property
    def transaction_channel(self) -> str:
        """
        | Indicates the channel via which the payment is created. Allowed values:
        |   * ECOMMERCE - The transaction is a regular E-Commerce transaction.
        |   * MOTO - The transaction is a Mail Order/Telephone Order.
        
        |   Defaults to ECOMMERCE.

        Type: str
        """
        return self.__transaction_channel

    @transaction_channel.setter
    def transaction_channel(self, value: str):
        self.__transaction_channel = value

    @property
    def unscheduled_card_on_file_requestor(self) -> str:
        """
        | Indicates which party initiated the unscheduled recurring transaction. Allowed values:
        |   * merchantInitiated - Merchant Initiated Transaction.
        |   * cardholderInitiated - Cardholder Initiated Transaction.
        | Note:
        |   * This property is not allowed if isRecurring is true.
        |   * When a customer has chosen to use a token on a hosted checkout this property is set to "cardholderInitiated".

        Type: str
        """
        return self.__unscheduled_card_on_file_requestor

    @unscheduled_card_on_file_requestor.setter
    def unscheduled_card_on_file_requestor(self, value: str):
        self.__unscheduled_card_on_file_requestor = value

    @property
    def unscheduled_card_on_file_sequence_indicator(self) -> str:
        """
        | * first = This transaction is the first of a series of unscheduled recurring transactions
        | * subsequent = This transaction is a subsequent transaction in a series of unscheduled recurring transactions
        | Note: this property is not allowed if isRecurring is true.

        Type: str
        """
        return self.__unscheduled_card_on_file_sequence_indicator

    @unscheduled_card_on_file_sequence_indicator.setter
    def unscheduled_card_on_file_sequence_indicator(self, value: str):
        self.__unscheduled_card_on_file_sequence_indicator = value

    def to_dictionary(self):
        dictionary = super(CardPaymentMethodSpecificInput, self).to_dictionary()
        if self.allow_dynamic_linking is not None:
            dictionary['allowDynamicLinking'] = self.allow_dynamic_linking
        if self.authorization_mode is not None:
            dictionary['authorizationMode'] = self.authorization_mode
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.card_on_file_recurring_expiration is not None:
            dictionary['cardOnFileRecurringExpiration'] = self.card_on_file_recurring_expiration
        if self.card_on_file_recurring_frequency is not None:
            dictionary['cardOnFileRecurringFrequency'] = self.card_on_file_recurring_frequency
        if self.currency_conversion is not None:
            dictionary['currencyConversion'] = self.currency_conversion.to_dictionary()
        if self.initial_scheme_transaction_id is not None:
            dictionary['initialSchemeTransactionId'] = self.initial_scheme_transaction_id
        if self.is_recurring is not None:
            dictionary['isRecurring'] = self.is_recurring
        if self.multiple_payment_information is not None:
            dictionary['multiplePaymentInformation'] = self.multiple_payment_information.to_dictionary()
        if self.payment_product130_specific_input is not None:
            dictionary['paymentProduct130SpecificInput'] = self.payment_product130_specific_input.to_dictionary()
        if self.payment_product3208_specific_input is not None:
            dictionary['paymentProduct3208SpecificInput'] = self.payment_product3208_specific_input.to_dictionary()
        if self.payment_product3209_specific_input is not None:
            dictionary['paymentProduct3209SpecificInput'] = self.payment_product3209_specific_input.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        if self.recurring is not None:
            dictionary['recurring'] = self.recurring.to_dictionary()
        if self.return_url is not None:
            dictionary['returnUrl'] = self.return_url
        if self.scheme_reference_data is not None:
            dictionary['schemeReferenceData'] = self.scheme_reference_data
        if self.skip_authentication is not None:
            dictionary['skipAuthentication'] = self.skip_authentication
        if self.three_d_secure is not None:
            dictionary['threeDSecure'] = self.three_d_secure.to_dictionary()
        if self.token is not None:
            dictionary['token'] = self.token
        if self.tokenize is not None:
            dictionary['tokenize'] = self.tokenize
        if self.transaction_channel is not None:
            dictionary['transactionChannel'] = self.transaction_channel
        if self.unscheduled_card_on_file_requestor is not None:
            dictionary['unscheduledCardOnFileRequestor'] = self.unscheduled_card_on_file_requestor
        if self.unscheduled_card_on_file_sequence_indicator is not None:
            dictionary['unscheduledCardOnFileSequenceIndicator'] = self.unscheduled_card_on_file_sequence_indicator
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'allowDynamicLinking' in dictionary:
            self.allow_dynamic_linking = dictionary['allowDynamicLinking']
        if 'authorizationMode' in dictionary:
            self.authorization_mode = dictionary['authorizationMode']
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = Card()
            self.card = value.from_dictionary(dictionary['card'])
        if 'cardOnFileRecurringExpiration' in dictionary:
            self.card_on_file_recurring_expiration = dictionary['cardOnFileRecurringExpiration']
        if 'cardOnFileRecurringFrequency' in dictionary:
            self.card_on_file_recurring_frequency = dictionary['cardOnFileRecurringFrequency']
        if 'currencyConversion' in dictionary:
            if not isinstance(dictionary['currencyConversion'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['currencyConversion']))
            value = CurrencyConversionInput()
            self.currency_conversion = value.from_dictionary(dictionary['currencyConversion'])
        if 'initialSchemeTransactionId' in dictionary:
            self.initial_scheme_transaction_id = dictionary['initialSchemeTransactionId']
        if 'isRecurring' in dictionary:
            self.is_recurring = dictionary['isRecurring']
        if 'multiplePaymentInformation' in dictionary:
            if not isinstance(dictionary['multiplePaymentInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['multiplePaymentInformation']))
            value = MultiplePaymentInformation()
            self.multiple_payment_information = value.from_dictionary(dictionary['multiplePaymentInformation'])
        if 'paymentProduct130SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct130SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct130SpecificInput']))
            value = PaymentProduct130SpecificInput()
            self.payment_product130_specific_input = value.from_dictionary(dictionary['paymentProduct130SpecificInput'])
        if 'paymentProduct3208SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct3208SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct3208SpecificInput']))
            value = PaymentProduct3208SpecificInput()
            self.payment_product3208_specific_input = value.from_dictionary(dictionary['paymentProduct3208SpecificInput'])
        if 'paymentProduct3209SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct3209SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct3209SpecificInput']))
            value = PaymentProduct3209SpecificInput()
            self.payment_product3209_specific_input = value.from_dictionary(dictionary['paymentProduct3209SpecificInput'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'recurring' in dictionary:
            if not isinstance(dictionary['recurring'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['recurring']))
            value = CardRecurrenceDetails()
            self.recurring = value.from_dictionary(dictionary['recurring'])
        if 'returnUrl' in dictionary:
            self.return_url = dictionary['returnUrl']
        if 'schemeReferenceData' in dictionary:
            self.scheme_reference_data = dictionary['schemeReferenceData']
        if 'skipAuthentication' in dictionary:
            self.skip_authentication = dictionary['skipAuthentication']
        if 'threeDSecure' in dictionary:
            if not isinstance(dictionary['threeDSecure'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecure']))
            value = ThreeDSecure()
            self.three_d_secure = value.from_dictionary(dictionary['threeDSecure'])
        if 'token' in dictionary:
            self.token = dictionary['token']
        if 'tokenize' in dictionary:
            self.tokenize = dictionary['tokenize']
        if 'transactionChannel' in dictionary:
            self.transaction_channel = dictionary['transactionChannel']
        if 'unscheduledCardOnFileRequestor' in dictionary:
            self.unscheduled_card_on_file_requestor = dictionary['unscheduledCardOnFileRequestor']
        if 'unscheduledCardOnFileSequenceIndicator' in dictionary:
            self.unscheduled_card_on_file_sequence_indicator = dictionary['unscheduledCardOnFileSequenceIndicator']
        return self

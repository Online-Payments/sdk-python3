# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.card_recurrence_details import CardRecurrenceDetails
from onlinepayments.sdk.domain.currency_conversion_specific_input import CurrencyConversionSpecificInput
from onlinepayments.sdk.domain.multiple_payment_information import MultiplePaymentInformation
from onlinepayments.sdk.domain.payment_product130_specific_input import PaymentProduct130SpecificInput
from onlinepayments.sdk.domain.payment_product3208_specific_input import PaymentProduct3208SpecificInput
from onlinepayments.sdk.domain.payment_product3209_specific_input import PaymentProduct3209SpecificInput
from onlinepayments.sdk.domain.payment_product5100_specific_input import PaymentProduct5100SpecificInput
from onlinepayments.sdk.domain.three_d_secure_base import ThreeDSecureBase


class CardPaymentMethodSpecificInputBase(DataObject):
    """
    | Object containing the specific input details for card payments
    """

    __allow_dynamic_linking = None
    __authorization_mode = None
    __currency_conversion_specific_input = None
    __initial_scheme_transaction_id = None
    __multiple_payment_information = None
    __payment_product130_specific_input = None
    __payment_product3208_specific_input = None
    __payment_product3209_specific_input = None
    __payment_product5100_specific_input = None
    __payment_product_id = None
    __recurring = None
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
    def currency_conversion_specific_input(self) -> CurrencyConversionSpecificInput:
        """
        | Object containing specific input required for Dynamic Currency Conversion.

        Type: :class:`onlinepayments.sdk.domain.currency_conversion_specific_input.CurrencyConversionSpecificInput`
        """
        return self.__currency_conversion_specific_input

    @currency_conversion_specific_input.setter
    def currency_conversion_specific_input(self, value: CurrencyConversionSpecificInput):
        self.__currency_conversion_specific_input = value

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
    def payment_product5100_specific_input(self) -> PaymentProduct5100SpecificInput:
        """
        | Object containing specific input required for Cpay payments.

        Type: :class:`onlinepayments.sdk.domain.payment_product5100_specific_input.PaymentProduct5100SpecificInput`
        """
        return self.__payment_product5100_specific_input

    @payment_product5100_specific_input.setter
    def payment_product5100_specific_input(self, value: PaymentProduct5100SpecificInput):
        self.__payment_product5100_specific_input = value

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
    def three_d_secure(self) -> ThreeDSecureBase:
        """
        | Object containing specific data regarding 3-D Secure

        Type: :class:`onlinepayments.sdk.domain.three_d_secure_base.ThreeDSecureBase`
        """
        return self.__three_d_secure

    @three_d_secure.setter
    def three_d_secure(self, value: ThreeDSecureBase):
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
        dictionary = super(CardPaymentMethodSpecificInputBase, self).to_dictionary()
        if self.allow_dynamic_linking is not None:
            dictionary['allowDynamicLinking'] = self.allow_dynamic_linking
        if self.authorization_mode is not None:
            dictionary['authorizationMode'] = self.authorization_mode
        if self.currency_conversion_specific_input is not None:
            dictionary['currencyConversionSpecificInput'] = self.currency_conversion_specific_input.to_dictionary()
        if self.initial_scheme_transaction_id is not None:
            dictionary['initialSchemeTransactionId'] = self.initial_scheme_transaction_id
        if self.multiple_payment_information is not None:
            dictionary['multiplePaymentInformation'] = self.multiple_payment_information.to_dictionary()
        if self.payment_product130_specific_input is not None:
            dictionary['paymentProduct130SpecificInput'] = self.payment_product130_specific_input.to_dictionary()
        if self.payment_product3208_specific_input is not None:
            dictionary['paymentProduct3208SpecificInput'] = self.payment_product3208_specific_input.to_dictionary()
        if self.payment_product3209_specific_input is not None:
            dictionary['paymentProduct3209SpecificInput'] = self.payment_product3209_specific_input.to_dictionary()
        if self.payment_product5100_specific_input is not None:
            dictionary['paymentProduct5100SpecificInput'] = self.payment_product5100_specific_input.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        if self.recurring is not None:
            dictionary['recurring'] = self.recurring.to_dictionary()
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
        super(CardPaymentMethodSpecificInputBase, self).from_dictionary(dictionary)
        if 'allowDynamicLinking' in dictionary:
            self.allow_dynamic_linking = dictionary['allowDynamicLinking']
        if 'authorizationMode' in dictionary:
            self.authorization_mode = dictionary['authorizationMode']
        if 'currencyConversionSpecificInput' in dictionary:
            if not isinstance(dictionary['currencyConversionSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['currencyConversionSpecificInput']))
            value = CurrencyConversionSpecificInput()
            self.currency_conversion_specific_input = value.from_dictionary(dictionary['currencyConversionSpecificInput'])
        if 'initialSchemeTransactionId' in dictionary:
            self.initial_scheme_transaction_id = dictionary['initialSchemeTransactionId']
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
        if 'paymentProduct5100SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct5100SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct5100SpecificInput']))
            value = PaymentProduct5100SpecificInput()
            self.payment_product5100_specific_input = value.from_dictionary(dictionary['paymentProduct5100SpecificInput'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'recurring' in dictionary:
            if not isinstance(dictionary['recurring'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['recurring']))
            value = CardRecurrenceDetails()
            self.recurring = value.from_dictionary(dictionary['recurring'])
        if 'threeDSecure' in dictionary:
            if not isinstance(dictionary['threeDSecure'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecure']))
            value = ThreeDSecureBase()
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

# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .acquirer_information import AcquirerInformation
from .card_essentials import CardEssentials
from .card_fraud_results import CardFraudResults
from .click_to_pay import ClickToPay
from .currency_conversion import CurrencyConversion
from .data_object import DataObject
from .external_token_linked import ExternalTokenLinked
from .payment_product3208_specific_output import PaymentProduct3208SpecificOutput
from .payment_product3209_specific_output import PaymentProduct3209SpecificOutput
from .reattempt_instructions import ReattemptInstructions
from .three_d_secure_results import ThreeDSecureResults


class CardPaymentMethodSpecificOutput(DataObject):

    __acquirer_information: Optional[AcquirerInformation] = None
    __authenticated_amount: Optional[int] = None
    __authorisation_code: Optional[str] = None
    __card: Optional[CardEssentials] = None
    __click_to_pay: Optional[ClickToPay] = None
    __currency_conversion: Optional[CurrencyConversion] = None
    __external_token_linked: Optional[ExternalTokenLinked] = None
    __fraud_results: Optional[CardFraudResults] = None
    __initial_scheme_transaction_id: Optional[str] = None
    __payment_account_reference: Optional[str] = None
    __payment_option: Optional[str] = None
    __payment_product3208_specific_output: Optional[PaymentProduct3208SpecificOutput] = None
    __payment_product3209_specific_output: Optional[PaymentProduct3209SpecificOutput] = None
    __payment_product_id: Optional[int] = None
    __reattempt_instructions: Optional[ReattemptInstructions] = None
    __scheme_reference_data: Optional[str] = None
    __three_d_secure_results: Optional[ThreeDSecureResults] = None
    __token: Optional[str] = None

    @property
    def acquirer_information(self) -> Optional[AcquirerInformation]:
        """
        | Information about the acquirer used to process the transaction

        Type: :class:`onlinepayments.sdk.domain.acquirer_information.AcquirerInformation`
        """
        return self.__acquirer_information

    @acquirer_information.setter
    def acquirer_information(self, value: Optional[AcquirerInformation]) -> None:
        self.__acquirer_information = value

    @property
    def authenticated_amount(self) -> Optional[int]:
        """
        | The amount to be authenticated. This field should be populated if the amount to be authenticated differs from the amount to be authorized (by default they are considered equal). Amount in cents and always having 2 decimals.

        Type: int
        """
        return self.__authenticated_amount

    @authenticated_amount.setter
    def authenticated_amount(self, value: Optional[int]) -> None:
        self.__authenticated_amount = value

    @property
    def authorisation_code(self) -> Optional[str]:
        """
        | Card Authorization code as returned by the acquirer

        Type: str
        """
        return self.__authorisation_code

    @authorisation_code.setter
    def authorisation_code(self, value: Optional[str]) -> None:
        self.__authorisation_code = value

    @property
    def card(self) -> Optional[CardEssentials]:
        """
        | Object containing card details

        Type: :class:`onlinepayments.sdk.domain.card_essentials.CardEssentials`
        """
        return self.__card

    @card.setter
    def card(self, value: Optional[CardEssentials]) -> None:
        self.__card = value

    @property
    def click_to_pay(self) -> Optional[ClickToPay]:
        """
        | Information about whether the payment is made using Click to Pay

        Type: :class:`onlinepayments.sdk.domain.click_to_pay.ClickToPay`
        """
        return self.__click_to_pay

    @click_to_pay.setter
    def click_to_pay(self, value: Optional[ClickToPay]) -> None:
        self.__click_to_pay = value

    @property
    def currency_conversion(self) -> Optional[CurrencyConversion]:
        """
        Type: :class:`onlinepayments.sdk.domain.currency_conversion.CurrencyConversion`
        """
        return self.__currency_conversion

    @currency_conversion.setter
    def currency_conversion(self, value: Optional[CurrencyConversion]) -> None:
        self.__currency_conversion = value

    @property
    def external_token_linked(self) -> Optional[ExternalTokenLinked]:
        """
        Type: :class:`onlinepayments.sdk.domain.external_token_linked.ExternalTokenLinked`
        """
        return self.__external_token_linked

    @external_token_linked.setter
    def external_token_linked(self, value: Optional[ExternalTokenLinked]) -> None:
        self.__external_token_linked = value

    @property
    def fraud_results(self) -> Optional[CardFraudResults]:
        """
        | Fraud results contained in the CardFraudResults object

        Type: :class:`onlinepayments.sdk.domain.card_fraud_results.CardFraudResults`
        """
        return self.__fraud_results

    @fraud_results.setter
    def fraud_results(self, value: Optional[CardFraudResults]) -> None:
        self.__fraud_results = value

    @property
    def initial_scheme_transaction_id(self) -> Optional[str]:
        """
        | The unique scheme transactionId of the initial transaction that was performed with SCA. In case this is unknown a scheme transactionId of an earlier transaction part of the same sequence can be used as a fall-back. Strongly advised to be submitted for any MerchantInitiated or recurring transaction (a subsequent one).

        Type: str
        """
        return self.__initial_scheme_transaction_id

    @initial_scheme_transaction_id.setter
    def initial_scheme_transaction_id(self, value: Optional[str]) -> None:
        self.__initial_scheme_transaction_id = value

    @property
    def payment_account_reference(self) -> Optional[str]:
        """
        | The Payment Account Reference is a unique alphanumeric identifier that links a PAN with all subsequent PANs for the same payment account (e.g., following card replacement) and all EMV payment tokens associated with that account. On its own Payment Account Reference cannot be used to start financial transactions, but it does allow for complying with regulatory requirements, performing risk analysis & supporting loyalty programs. Please note that the Payment Account Reference is a value returned after an authorization & only if provided by the acquirer and/or the issuer.

        Type: str
        """
        return self.__payment_account_reference

    @payment_account_reference.setter
    def payment_account_reference(self, value: Optional[str]) -> None:
        self.__payment_account_reference = value

    @property
    def payment_option(self) -> Optional[str]:
        """
        | The specific payment option for the payment. To be used as a complement of the more generic paymentProductId (oney, banquecasino, cofidis), which allows to define a variation of the selected paymentProductId (ex: facilypay3x, banquecasino4x, cofidis3x-sansfrais, ...). List of modalities included in the payment product page.

        Type: str
        """
        return self.__payment_option

    @payment_option.setter
    def payment_option(self, value: Optional[str]) -> None:
        self.__payment_option = value

    @property
    def payment_product3208_specific_output(self) -> Optional[PaymentProduct3208SpecificOutput]:
        """
        | OneyDuplo Leroy Merlin specific details

        Type: :class:`onlinepayments.sdk.domain.payment_product3208_specific_output.PaymentProduct3208SpecificOutput`
        """
        return self.__payment_product3208_specific_output

    @payment_product3208_specific_output.setter
    def payment_product3208_specific_output(self, value: Optional[PaymentProduct3208SpecificOutput]) -> None:
        self.__payment_product3208_specific_output = value

    @property
    def payment_product3209_specific_output(self) -> Optional[PaymentProduct3209SpecificOutput]:
        """
        | OneyDuplo Alcampo specific details

        Type: :class:`onlinepayments.sdk.domain.payment_product3209_specific_output.PaymentProduct3209SpecificOutput`
        """
        return self.__payment_product3209_specific_output

    @payment_product3209_specific_output.setter
    def payment_product3209_specific_output(self, value: Optional[PaymentProduct3209SpecificOutput]) -> None:
        self.__payment_product3209_specific_output = value

    @property
    def payment_product_id(self) -> Optional[int]:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: Optional[int]) -> None:
        self.__payment_product_id = value

    @property
    def reattempt_instructions(self) -> Optional[ReattemptInstructions]:
        """
        | Instructions for reattempting a declined authorization. Provided only in case of declined authorization, for those acquirers that may respond with explicit instructions regarding potential reattempt processing.

        Type: :class:`onlinepayments.sdk.domain.reattempt_instructions.ReattemptInstructions`
        """
        return self.__reattempt_instructions

    @reattempt_instructions.setter
    def reattempt_instructions(self, value: Optional[ReattemptInstructions]) -> None:
        self.__reattempt_instructions = value

    @property
    def scheme_reference_data(self) -> Optional[str]:
        """
        | This is the unique Scheme Reference Data from the initial transaction that was performed with a Strong Customer Authentication. In case this value is unknown, a Scheme Reference of an earlier transaction that was part of the same sequence can be used as a fall-back. Still, it is strongly advised to submit this value for any Merchant Initiated Transaction or any recurring transaction (hereby defined as "Subsequent").

        Type: str
        """
        return self.__scheme_reference_data

    @scheme_reference_data.setter
    def scheme_reference_data(self, value: Optional[str]) -> None:
        self.__scheme_reference_data = value

    @property
    def three_d_secure_results(self) -> Optional[ThreeDSecureResults]:
        """
        | 3D Secure results object

        Type: :class:`onlinepayments.sdk.domain.three_d_secure_results.ThreeDSecureResults`
        """
        return self.__three_d_secure_results

    @three_d_secure_results.setter
    def three_d_secure_results(self, value: Optional[ThreeDSecureResults]) -> None:
        self.__three_d_secure_results = value

    @property
    def token(self) -> Optional[str]:
        """
        | ID of the token. This property is populated when the payment was done with a token or when the payment was tokenized.

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: Optional[str]) -> None:
        self.__token = value

    def to_dictionary(self) -> dict:
        dictionary = super(CardPaymentMethodSpecificOutput, self).to_dictionary()
        if self.acquirer_information is not None:
            dictionary['acquirerInformation'] = self.acquirer_information.to_dictionary()
        if self.authenticated_amount is not None:
            dictionary['authenticatedAmount'] = self.authenticated_amount
        if self.authorisation_code is not None:
            dictionary['authorisationCode'] = self.authorisation_code
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        if self.click_to_pay is not None:
            dictionary['clickToPay'] = self.click_to_pay.to_dictionary()
        if self.currency_conversion is not None:
            dictionary['currencyConversion'] = self.currency_conversion.to_dictionary()
        if self.external_token_linked is not None:
            dictionary['externalTokenLinked'] = self.external_token_linked.to_dictionary()
        if self.fraud_results is not None:
            dictionary['fraudResults'] = self.fraud_results.to_dictionary()
        if self.initial_scheme_transaction_id is not None:
            dictionary['initialSchemeTransactionId'] = self.initial_scheme_transaction_id
        if self.payment_account_reference is not None:
            dictionary['paymentAccountReference'] = self.payment_account_reference
        if self.payment_option is not None:
            dictionary['paymentOption'] = self.payment_option
        if self.payment_product3208_specific_output is not None:
            dictionary['paymentProduct3208SpecificOutput'] = self.payment_product3208_specific_output.to_dictionary()
        if self.payment_product3209_specific_output is not None:
            dictionary['paymentProduct3209SpecificOutput'] = self.payment_product3209_specific_output.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        if self.reattempt_instructions is not None:
            dictionary['reattemptInstructions'] = self.reattempt_instructions.to_dictionary()
        if self.scheme_reference_data is not None:
            dictionary['schemeReferenceData'] = self.scheme_reference_data
        if self.three_d_secure_results is not None:
            dictionary['threeDSecureResults'] = self.three_d_secure_results.to_dictionary()
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardPaymentMethodSpecificOutput':
        super(CardPaymentMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'acquirerInformation' in dictionary:
            if not isinstance(dictionary['acquirerInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['acquirerInformation']))
            value = AcquirerInformation()
            self.acquirer_information = value.from_dictionary(dictionary['acquirerInformation'])
        if 'authenticatedAmount' in dictionary:
            self.authenticated_amount = dictionary['authenticatedAmount']
        if 'authorisationCode' in dictionary:
            self.authorisation_code = dictionary['authorisationCode']
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = CardEssentials()
            self.card = value.from_dictionary(dictionary['card'])
        if 'clickToPay' in dictionary:
            if not isinstance(dictionary['clickToPay'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['clickToPay']))
            value = ClickToPay()
            self.click_to_pay = value.from_dictionary(dictionary['clickToPay'])
        if 'currencyConversion' in dictionary:
            if not isinstance(dictionary['currencyConversion'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['currencyConversion']))
            value = CurrencyConversion()
            self.currency_conversion = value.from_dictionary(dictionary['currencyConversion'])
        if 'externalTokenLinked' in dictionary:
            if not isinstance(dictionary['externalTokenLinked'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['externalTokenLinked']))
            value = ExternalTokenLinked()
            self.external_token_linked = value.from_dictionary(dictionary['externalTokenLinked'])
        if 'fraudResults' in dictionary:
            if not isinstance(dictionary['fraudResults'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraudResults']))
            value = CardFraudResults()
            self.fraud_results = value.from_dictionary(dictionary['fraudResults'])
        if 'initialSchemeTransactionId' in dictionary:
            self.initial_scheme_transaction_id = dictionary['initialSchemeTransactionId']
        if 'paymentAccountReference' in dictionary:
            self.payment_account_reference = dictionary['paymentAccountReference']
        if 'paymentOption' in dictionary:
            self.payment_option = dictionary['paymentOption']
        if 'paymentProduct3208SpecificOutput' in dictionary:
            if not isinstance(dictionary['paymentProduct3208SpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct3208SpecificOutput']))
            value = PaymentProduct3208SpecificOutput()
            self.payment_product3208_specific_output = value.from_dictionary(dictionary['paymentProduct3208SpecificOutput'])
        if 'paymentProduct3209SpecificOutput' in dictionary:
            if not isinstance(dictionary['paymentProduct3209SpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct3209SpecificOutput']))
            value = PaymentProduct3209SpecificOutput()
            self.payment_product3209_specific_output = value.from_dictionary(dictionary['paymentProduct3209SpecificOutput'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'reattemptInstructions' in dictionary:
            if not isinstance(dictionary['reattemptInstructions'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['reattemptInstructions']))
            value = ReattemptInstructions()
            self.reattempt_instructions = value.from_dictionary(dictionary['reattemptInstructions'])
        if 'schemeReferenceData' in dictionary:
            self.scheme_reference_data = dictionary['schemeReferenceData']
        if 'threeDSecureResults' in dictionary:
            if not isinstance(dictionary['threeDSecureResults'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecureResults']))
            value = ThreeDSecureResults()
            self.three_d_secure_results = value.from_dictionary(dictionary['threeDSecureResults'])
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self

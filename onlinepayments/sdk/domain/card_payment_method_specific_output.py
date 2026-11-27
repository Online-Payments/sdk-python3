#
# This file was automatically generated.
#
from .acceptance import Acceptance
from .acquirer_information import AcquirerInformation
from .card_essentials import CardEssentials
from .card_fraud_results import CardFraudResults
from .click_to_pay import ClickToPay
from .crm_token import CrmToken
from .currency_conversion import CurrencyConversion
from .data_object import DataObject
from .external_token_linked import ExternalTokenLinked
from .network_token_essentials import NetworkTokenEssentials
from .payment_product3208_specific_output import PaymentProduct3208SpecificOutput
from .payment_product3209_specific_output import PaymentProduct3209SpecificOutput
from .reattempt_instructions import ReattemptInstructions
from .three_d_secure_results import ThreeDSecureResults


class CardPaymentMethodSpecificOutput(DataObject):

    __slots__ = (
        "__acceptance",
        "__acquirer_information",
        "__authenticated_amount",
        "__authorisation_code",
        "__card",
        "__click_to_pay",
        "__cobrand_selection_indicator",
        "__crm_token",
        "__currency_conversion",
        "__external_token_linked",
        "__fraud_results",
        "__initial_scheme_transaction_id",
        "__network_token_data",
        "__payment_account_reference",
        "__payment_option",
        "__payment_product3208_specific_output",
        "__payment_product3209_specific_output",
        "__payment_product_id",
        "__reattempt_instructions",
        "__scheme_reference_data",
        "__scheme_transaction_id",
        "__three_d_secure_results",
        "__token",
    )

    __acceptance: Acceptance | None
    __acquirer_information: AcquirerInformation | None
    __authenticated_amount: int | None
    __authorisation_code: str | None
    __card: CardEssentials | None
    __click_to_pay: ClickToPay | None
    __cobrand_selection_indicator: str | None
    __crm_token: CrmToken | None
    __currency_conversion: CurrencyConversion | None
    __external_token_linked: ExternalTokenLinked | None
    __fraud_results: CardFraudResults | None
    __initial_scheme_transaction_id: str | None
    __network_token_data: NetworkTokenEssentials | None
    __payment_account_reference: str | None
    __payment_option: str | None
    __payment_product3208_specific_output: PaymentProduct3208SpecificOutput | None
    __payment_product3209_specific_output: PaymentProduct3209SpecificOutput | None
    __payment_product_id: int | None
    __reattempt_instructions: ReattemptInstructions | None
    __scheme_reference_data: str | None
    __scheme_transaction_id: str | None
    __three_d_secure_results: ThreeDSecureResults | None
    __token: str | None

    def __init__(
        self,
        *,
        acceptance: Acceptance | None = None,
        acquirer_information: AcquirerInformation | None = None,
        authenticated_amount: int | None = None,
        authorisation_code: str | None = None,
        card: CardEssentials | None = None,
        click_to_pay: ClickToPay | None = None,
        cobrand_selection_indicator: str | None = None,
        crm_token: CrmToken | None = None,
        currency_conversion: CurrencyConversion | None = None,
        external_token_linked: ExternalTokenLinked | None = None,
        fraud_results: CardFraudResults | None = None,
        initial_scheme_transaction_id: str | None = None,
        network_token_data: NetworkTokenEssentials | None = None,
        payment_account_reference: str | None = None,
        payment_option: str | None = None,
        payment_product3208_specific_output: PaymentProduct3208SpecificOutput | None = None,
        payment_product3209_specific_output: PaymentProduct3209SpecificOutput | None = None,
        payment_product_id: int | None = None,
        reattempt_instructions: ReattemptInstructions | None = None,
        scheme_reference_data: str | None = None,
        scheme_transaction_id: str | None = None,
        three_d_secure_results: ThreeDSecureResults | None = None,
        token: str | None = None,
    ) -> None:
        self.acceptance = acceptance
        self.acquirer_information = acquirer_information
        self.authenticated_amount = authenticated_amount
        self.authorisation_code = authorisation_code
        self.card = card
        self.click_to_pay = click_to_pay
        self.cobrand_selection_indicator = cobrand_selection_indicator
        self.crm_token = crm_token
        self.currency_conversion = currency_conversion
        self.external_token_linked = external_token_linked
        self.fraud_results = fraud_results
        self.initial_scheme_transaction_id = initial_scheme_transaction_id
        self.network_token_data = network_token_data
        self.payment_account_reference = payment_account_reference
        self.payment_option = payment_option
        self.payment_product3208_specific_output = payment_product3208_specific_output
        self.payment_product3209_specific_output = payment_product3209_specific_output
        self.payment_product_id = payment_product_id
        self.reattempt_instructions = reattempt_instructions
        self.scheme_reference_data = scheme_reference_data
        self.scheme_transaction_id = scheme_transaction_id
        self.three_d_secure_results = three_d_secure_results
        self.token = token

    @property
    def acceptance(self) -> Acceptance | None:
        """
        | This object contains the acceptance information for the card payment authorization.

        Type: :class:`onlinepayments.sdk.domain.acceptance.Acceptance`
        """
        return self.__acceptance

    @acceptance.setter
    def acceptance(self, value: Acceptance | None) -> None:
        self.__acceptance = value

    @property
    def acquirer_information(self) -> AcquirerInformation | None:
        """
        | Information about the acquirer used to process the transaction

        Type: :class:`onlinepayments.sdk.domain.acquirer_information.AcquirerInformation`
        """
        return self.__acquirer_information

    @acquirer_information.setter
    def acquirer_information(self, value: AcquirerInformation | None) -> None:
        self.__acquirer_information = value

    @property
    def authenticated_amount(self) -> int | None:
        """
        | The amount to be authenticated. This field should be populated if the amount to be authenticated differs from the amount to be authorized (by default they are considered equal). Amount in cents and always having 2 decimals.

        Type: int
        """
        return self.__authenticated_amount

    @authenticated_amount.setter
    def authenticated_amount(self, value: int | None) -> None:
        self.__authenticated_amount = value

    @property
    def authorisation_code(self) -> str | None:
        """
        | Card Authorization code as returned by the acquirer

        Type: str
        """
        return self.__authorisation_code

    @authorisation_code.setter
    def authorisation_code(self, value: str | None) -> None:
        self.__authorisation_code = value

    @property
    def card(self) -> CardEssentials | None:
        """
        | Object containing card details

        Type: :class:`onlinepayments.sdk.domain.card_essentials.CardEssentials`
        """
        return self.__card

    @card.setter
    def card(self, value: CardEssentials | None) -> None:
        self.__card = value

    @property
    def click_to_pay(self) -> ClickToPay | None:
        """
        | Information about whether the payment is made using Click to Pay

        Type: :class:`onlinepayments.sdk.domain.click_to_pay.ClickToPay`
        """
        return self.__click_to_pay

    @click_to_pay.setter
    def click_to_pay(self, value: ClickToPay | None) -> None:
        self.__click_to_pay = value

    @property
    def cobrand_selection_indicator(self) -> str | None:
        """
        | For cobranded cards, this field indicates the brand selection method:
        
        * default - The holder implicitly accepted the default brand.
        * alternative - The holder explicitly selected an alternative brand.
        * notApplicable - The card is not cobranded.

        Type: str
        """
        return self.__cobrand_selection_indicator

    @cobrand_selection_indicator.setter
    def cobrand_selection_indicator(self, value: str | None) -> None:
        self.__cobrand_selection_indicator = value

    @property
    def crm_token(self) -> CrmToken | None:
        """
        | The CRM (Customer Relationship Management) token group. CRM tokens are available to enhance knowledge of a merchant's customers by attempting to identify the customer.

        Type: :class:`onlinepayments.sdk.domain.crm_token.CrmToken`
        """
        return self.__crm_token

    @crm_token.setter
    def crm_token(self, value: CrmToken | None) -> None:
        self.__crm_token = value

    @property
    def currency_conversion(self) -> CurrencyConversion | None:
        """
        Type: :class:`onlinepayments.sdk.domain.currency_conversion.CurrencyConversion`
        """
        return self.__currency_conversion

    @currency_conversion.setter
    def currency_conversion(self, value: CurrencyConversion | None) -> None:
        self.__currency_conversion = value

    @property
    def external_token_linked(self) -> ExternalTokenLinked | None:
        """
        Type: :class:`onlinepayments.sdk.domain.external_token_linked.ExternalTokenLinked`
        """
        return self.__external_token_linked

    @external_token_linked.setter
    def external_token_linked(self, value: ExternalTokenLinked | None) -> None:
        self.__external_token_linked = value

    @property
    def fraud_results(self) -> CardFraudResults | None:
        """
        | Fraud results contained in the CardFraudResults object

        Type: :class:`onlinepayments.sdk.domain.card_fraud_results.CardFraudResults`
        """
        return self.__fraud_results

    @fraud_results.setter
    def fraud_results(self, value: CardFraudResults | None) -> None:
        self.__fraud_results = value

    @property
    def initial_scheme_transaction_id(self) -> str | None:
        """
        | The unique scheme transactionId of the initial transaction that was performed with SCA. In case this is unknown a scheme transactionId of an earlier transaction part of the same sequence can be used as a fall-back. Strongly advised to be submitted for any MerchantInitiated or recurring transaction (a subsequent one).

        Type: str
        """
        return self.__initial_scheme_transaction_id

    @initial_scheme_transaction_id.setter
    def initial_scheme_transaction_id(self, value: str | None) -> None:
        self.__initial_scheme_transaction_id = value

    @property
    def network_token_data(self) -> NetworkTokenEssentials | None:
        """
        | Object containing network token details

        Type: :class:`onlinepayments.sdk.domain.network_token_essentials.NetworkTokenEssentials`
        """
        return self.__network_token_data

    @network_token_data.setter
    def network_token_data(self, value: NetworkTokenEssentials | None) -> None:
        self.__network_token_data = value

    @property
    def payment_account_reference(self) -> str | None:
        """
        | The Payment Account Reference is a unique alphanumeric identifier that links a PAN with all subsequent PANs for the same payment account (e.g., following card replacement) and all EMV payment tokens associated with that account. On its own Payment Account Reference cannot be used to start financial transactions, but it does allow for complying with regulatory requirements, performing risk analysis & supporting loyalty programs. Please note that the Payment Account Reference is a value returned after an authorization & only if provided by the acquirer and/or the issuer.

        Type: str
        """
        return self.__payment_account_reference

    @payment_account_reference.setter
    def payment_account_reference(self, value: str | None) -> None:
        self.__payment_account_reference = value

    @property
    def payment_option(self) -> str | None:
        """
        | The specific payment option for the payment. To be used as a complement of the more generic paymentProductId (oney, banquecasino, cofidis), which allows to define a variation of the selected paymentProductId (ex: facilypay3x, banquecasino4x, cofidis3x-sansfrais, ...). List of modalities included in the payment product page.

        Type: str
        """
        return self.__payment_option

    @payment_option.setter
    def payment_option(self, value: str | None) -> None:
        self.__payment_option = value

    @property
    def payment_product3208_specific_output(self) -> PaymentProduct3208SpecificOutput | None:
        """
        | OneyDuplo Leroy Merlin specific details

        Type: :class:`onlinepayments.sdk.domain.payment_product3208_specific_output.PaymentProduct3208SpecificOutput`
        """
        return self.__payment_product3208_specific_output

    @payment_product3208_specific_output.setter
    def payment_product3208_specific_output(self, value: PaymentProduct3208SpecificOutput | None) -> None:
        self.__payment_product3208_specific_output = value

    @property
    def payment_product3209_specific_output(self) -> PaymentProduct3209SpecificOutput | None:
        """
        | OneyDuplo Alcampo specific details

        Type: :class:`onlinepayments.sdk.domain.payment_product3209_specific_output.PaymentProduct3209SpecificOutput`
        """
        return self.__payment_product3209_specific_output

    @payment_product3209_specific_output.setter
    def payment_product3209_specific_output(self, value: PaymentProduct3209SpecificOutput | None) -> None:
        self.__payment_product3209_specific_output = value

    @property
    def payment_product_id(self) -> int | None:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: int | None) -> None:
        self.__payment_product_id = value

    @property
    def reattempt_instructions(self) -> ReattemptInstructions | None:
        """
        | Provided only in case of declined authorization, for those acquirers that may respond with explicit instructions regarding potential reattempt processing.

        Type: :class:`onlinepayments.sdk.domain.reattempt_instructions.ReattemptInstructions`
        """
        return self.__reattempt_instructions

    @reattempt_instructions.setter
    def reattempt_instructions(self, value: ReattemptInstructions | None) -> None:
        self.__reattempt_instructions = value

    @property
    def scheme_reference_data(self) -> str | None:
        """
        | This is the unique Scheme Reference Data from the initial transaction that was performed with a Strong Customer Authentication. In case this value is unknown, a Scheme Reference of an earlier transaction that was part of the same sequence can be used as a fall-back. Still, it is strongly advised to submit this value for any Merchant Initiated Transaction or any recurring transaction (hereby defined as "Subsequent").

        Type: str
        """
        return self.__scheme_reference_data

    @scheme_reference_data.setter
    def scheme_reference_data(self, value: str | None) -> None:
        self.__scheme_reference_data = value

    @property
    def scheme_transaction_id(self) -> str | None:
        """
        | This is populated in case of a Mastercard payment, with the Mastercard TLID (Transaction Life Cycle ID) field.

        Type: str
        """
        return self.__scheme_transaction_id

    @scheme_transaction_id.setter
    def scheme_transaction_id(self, value: str | None) -> None:
        self.__scheme_transaction_id = value

    @property
    def three_d_secure_results(self) -> ThreeDSecureResults | None:
        """
        | 3D Secure results object

        Type: :class:`onlinepayments.sdk.domain.three_d_secure_results.ThreeDSecureResults`
        """
        return self.__three_d_secure_results

    @three_d_secure_results.setter
    def three_d_secure_results(self, value: ThreeDSecureResults | None) -> None:
        self.__three_d_secure_results = value

    @property
    def token(self) -> str | None:
        """
        | ID of the token. This property is populated when the payment was done with a token or when the payment was tokenized.

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: str | None) -> None:
        self.__token = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.acceptance is not None:
            dictionary['acceptance'] = self.acceptance.to_dictionary()
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
        if self.cobrand_selection_indicator is not None:
            dictionary['cobrandSelectionIndicator'] = self.cobrand_selection_indicator
        if self.crm_token is not None:
            dictionary['crmToken'] = self.crm_token.to_dictionary()
        if self.currency_conversion is not None:
            dictionary['currencyConversion'] = self.currency_conversion.to_dictionary()
        if self.external_token_linked is not None:
            dictionary['externalTokenLinked'] = self.external_token_linked.to_dictionary()
        if self.fraud_results is not None:
            dictionary['fraudResults'] = self.fraud_results.to_dictionary()
        if self.initial_scheme_transaction_id is not None:
            dictionary['initialSchemeTransactionId'] = self.initial_scheme_transaction_id
        if self.network_token_data is not None:
            dictionary['networkTokenData'] = self.network_token_data.to_dictionary()
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
        if self.scheme_transaction_id is not None:
            dictionary['schemeTransactionId'] = self.scheme_transaction_id
        if self.three_d_secure_results is not None:
            dictionary['threeDSecureResults'] = self.three_d_secure_results.to_dictionary()
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardPaymentMethodSpecificOutput':
        super().from_dictionary(dictionary)
        if 'acceptance' in dictionary:
            if not isinstance(dictionary['acceptance'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['acceptance']))
            value = Acceptance()
            self.acceptance = value.from_dictionary(dictionary['acceptance'])
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
        if 'cobrandSelectionIndicator' in dictionary:
            self.cobrand_selection_indicator = dictionary['cobrandSelectionIndicator']
        if 'crmToken' in dictionary:
            if not isinstance(dictionary['crmToken'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['crmToken']))
            value = CrmToken()
            self.crm_token = value.from_dictionary(dictionary['crmToken'])
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
        if 'networkTokenData' in dictionary:
            if not isinstance(dictionary['networkTokenData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['networkTokenData']))
            value = NetworkTokenEssentials()
            self.network_token_data = value.from_dictionary(dictionary['networkTokenData'])
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
        if 'schemeTransactionId' in dictionary:
            self.scheme_transaction_id = dictionary['schemeTransactionId']
        if 'threeDSecureResults' in dictionary:
            if not isinstance(dictionary['threeDSecureResults'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecureResults']))
            value = ThreeDSecureResults()
            self.three_d_secure_results = value.from_dictionary(dictionary['threeDSecureResults'])
        if 'token' in dictionary:
            self.token = dictionary['token']
        return self

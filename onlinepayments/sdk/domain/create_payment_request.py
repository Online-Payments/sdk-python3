#
# This file was automatically generated.
#
from .card_payment_method_specific_input import CardPaymentMethodSpecificInput
from .data_object import DataObject
from .feedbacks import Feedbacks
from .fraud_fields import FraudFields
from .mobile_payment_method_specific_input import MobilePaymentMethodSpecificInput
from .omnichannel_payment_specific_input import OmnichannelPaymentSpecificInput
from .order import Order
from .redirect_payment_method_specific_input import RedirectPaymentMethodSpecificInput
from .sepa_direct_debit_payment_method_specific_input import SepaDirectDebitPaymentMethodSpecificInput


class CreatePaymentRequest(DataObject):

    __slots__ = (
        "__card_payment_method_specific_input",
        "__encrypted_customer_input",
        "__feedbacks",
        "__fraud_fields",
        "__hosted_fields_session_id",
        "__hosted_tokenization_id",
        "__mobile_payment_method_specific_input",
        "__omnichannel_payment_specific_input",
        "__order",
        "__redirect_payment_method_specific_input",
        "__sepa_direct_debit_payment_method_specific_input",
    )

    __card_payment_method_specific_input: CardPaymentMethodSpecificInput | None
    __encrypted_customer_input: str | None
    __feedbacks: Feedbacks | None
    __fraud_fields: FraudFields | None
    __hosted_fields_session_id: str | None
    __hosted_tokenization_id: str | None
    __mobile_payment_method_specific_input: MobilePaymentMethodSpecificInput | None
    __omnichannel_payment_specific_input: OmnichannelPaymentSpecificInput | None
    __order: Order | None
    __redirect_payment_method_specific_input: RedirectPaymentMethodSpecificInput | None
    __sepa_direct_debit_payment_method_specific_input: SepaDirectDebitPaymentMethodSpecificInput | None

    def __init__(
        self,
        *,
        card_payment_method_specific_input: CardPaymentMethodSpecificInput | None = None,
        encrypted_customer_input: str | None = None,
        feedbacks: Feedbacks | None = None,
        fraud_fields: FraudFields | None = None,
        hosted_fields_session_id: str | None = None,
        hosted_tokenization_id: str | None = None,
        mobile_payment_method_specific_input: MobilePaymentMethodSpecificInput | None = None,
        omnichannel_payment_specific_input: OmnichannelPaymentSpecificInput | None = None,
        order: Order | None = None,
        redirect_payment_method_specific_input: RedirectPaymentMethodSpecificInput | None = None,
        sepa_direct_debit_payment_method_specific_input: SepaDirectDebitPaymentMethodSpecificInput | None = None,
    ) -> None:
        self.card_payment_method_specific_input = card_payment_method_specific_input
        self.encrypted_customer_input = encrypted_customer_input
        self.feedbacks = feedbacks
        self.fraud_fields = fraud_fields
        self.hosted_fields_session_id = hosted_fields_session_id
        self.hosted_tokenization_id = hosted_tokenization_id
        self.mobile_payment_method_specific_input = mobile_payment_method_specific_input
        self.omnichannel_payment_specific_input = omnichannel_payment_specific_input
        self.order = order
        self.redirect_payment_method_specific_input = redirect_payment_method_specific_input
        self.sepa_direct_debit_payment_method_specific_input = sepa_direct_debit_payment_method_specific_input

    @property
    def card_payment_method_specific_input(self) -> CardPaymentMethodSpecificInput | None:
        """
        | Object containing the specific input details for card payments

        Type: :class:`onlinepayments.sdk.domain.card_payment_method_specific_input.CardPaymentMethodSpecificInput`
        """
        return self.__card_payment_method_specific_input

    @card_payment_method_specific_input.setter
    def card_payment_method_specific_input(self, value: CardPaymentMethodSpecificInput | None) -> None:
        self.__card_payment_method_specific_input = value

    @property
    def encrypted_customer_input(self) -> str | None:
        """
        | Data that was encrypted client side containing all customer entered data elements like card data. Note: Because this data can only be submitted once to our system and contains encrypted card data you should not store it. As the data was captured within the context of a client session you also need to submit it to us before the session has expired.

        Type: str
        """
        return self.__encrypted_customer_input

    @encrypted_customer_input.setter
    def encrypted_customer_input(self, value: str | None) -> None:
        self.__encrypted_customer_input = value

    @property
    def feedbacks(self) -> Feedbacks | None:
        """
        | This section will contain feedback Urls to provide feedback on the payment.

        Type: :class:`onlinepayments.sdk.domain.feedbacks.Feedbacks`
        """
        return self.__feedbacks

    @feedbacks.setter
    def feedbacks(self, value: Feedbacks | None) -> None:
        self.__feedbacks = value

    @property
    def fraud_fields(self) -> FraudFields | None:
        """
        | Object containing additional data that will be used to assess the risk of fraud

        Type: :class:`onlinepayments.sdk.domain.fraud_fields.FraudFields`
        """
        return self.__fraud_fields

    @fraud_fields.setter
    def fraud_fields(self, value: FraudFields | None) -> None:
        self.__fraud_fields = value

    @property
    def hosted_fields_session_id(self) -> str | None:
        """
        | A unique identifier that references a previously created hosted fields session. Use this field to reuse the payment method details securely captured in the referenced hosted fields session.

        Type: str
        """
        return self.__hosted_fields_session_id

    @hosted_fields_session_id.setter
    def hosted_fields_session_id(self, value: str | None) -> None:
        self.__hosted_fields_session_id = value

    @property
    def hosted_tokenization_id(self) -> str | None:
        """
        | Use this field after a successful Hosted Tokenization session to create a payment with the tokenized payment method details.

        Type: str
        """
        return self.__hosted_tokenization_id

    @hosted_tokenization_id.setter
    def hosted_tokenization_id(self, value: str | None) -> None:
        self.__hosted_tokenization_id = value

    @property
    def mobile_payment_method_specific_input(self) -> MobilePaymentMethodSpecificInput | None:
        """
        | Object containing the specific input details for mobile payments

        Type: :class:`onlinepayments.sdk.domain.mobile_payment_method_specific_input.MobilePaymentMethodSpecificInput`
        """
        return self.__mobile_payment_method_specific_input

    @mobile_payment_method_specific_input.setter
    def mobile_payment_method_specific_input(self, value: MobilePaymentMethodSpecificInput | None) -> None:
        self.__mobile_payment_method_specific_input = value

    @property
    def omnichannel_payment_specific_input(self) -> OmnichannelPaymentSpecificInput | None:
        """
        | This object contains additional payment details for omnichannel merchants.

        Type: :class:`onlinepayments.sdk.domain.omnichannel_payment_specific_input.OmnichannelPaymentSpecificInput`
        """
        return self.__omnichannel_payment_specific_input

    @omnichannel_payment_specific_input.setter
    def omnichannel_payment_specific_input(self, value: OmnichannelPaymentSpecificInput | None) -> None:
        self.__omnichannel_payment_specific_input = value

    @property
    def order(self) -> Order | None:
        """
        | The order object contains order-related data; Please note that this object is required to submit the amount.

        Type: :class:`onlinepayments.sdk.domain.order.Order`
        """
        return self.__order

    @order.setter
    def order(self, value: Order | None) -> None:
        self.__order = value

    @property
    def redirect_payment_method_specific_input(self) -> RedirectPaymentMethodSpecificInput | None:
        """
        | Object containing the specific input details for payments that involve redirects to 3rd parties to complete, like iDeal and PayPal

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_method_specific_input.RedirectPaymentMethodSpecificInput`
        """
        return self.__redirect_payment_method_specific_input

    @redirect_payment_method_specific_input.setter
    def redirect_payment_method_specific_input(self, value: RedirectPaymentMethodSpecificInput | None) -> None:
        self.__redirect_payment_method_specific_input = value

    @property
    def sepa_direct_debit_payment_method_specific_input(self) -> SepaDirectDebitPaymentMethodSpecificInput | None:
        """
        | Object containing the specific input details for SEPA direct debit payments

        Type: :class:`onlinepayments.sdk.domain.sepa_direct_debit_payment_method_specific_input.SepaDirectDebitPaymentMethodSpecificInput`
        """
        return self.__sepa_direct_debit_payment_method_specific_input

    @sepa_direct_debit_payment_method_specific_input.setter
    def sepa_direct_debit_payment_method_specific_input(self, value: SepaDirectDebitPaymentMethodSpecificInput | None) -> None:
        self.__sepa_direct_debit_payment_method_specific_input = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.card_payment_method_specific_input is not None:
            dictionary['cardPaymentMethodSpecificInput'] = self.card_payment_method_specific_input.to_dictionary()
        if self.encrypted_customer_input is not None:
            dictionary['encryptedCustomerInput'] = self.encrypted_customer_input
        if self.feedbacks is not None:
            dictionary['feedbacks'] = self.feedbacks.to_dictionary()
        if self.fraud_fields is not None:
            dictionary['fraudFields'] = self.fraud_fields.to_dictionary()
        if self.hosted_fields_session_id is not None:
            dictionary['hostedFieldsSessionId'] = self.hosted_fields_session_id
        if self.hosted_tokenization_id is not None:
            dictionary['hostedTokenizationId'] = self.hosted_tokenization_id
        if self.mobile_payment_method_specific_input is not None:
            dictionary['mobilePaymentMethodSpecificInput'] = self.mobile_payment_method_specific_input.to_dictionary()
        if self.omnichannel_payment_specific_input is not None:
            dictionary['omnichannelPaymentSpecificInput'] = self.omnichannel_payment_specific_input.to_dictionary()
        if self.order is not None:
            dictionary['order'] = self.order.to_dictionary()
        if self.redirect_payment_method_specific_input is not None:
            dictionary['redirectPaymentMethodSpecificInput'] = self.redirect_payment_method_specific_input.to_dictionary()
        if self.sepa_direct_debit_payment_method_specific_input is not None:
            dictionary['sepaDirectDebitPaymentMethodSpecificInput'] = self.sepa_direct_debit_payment_method_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreatePaymentRequest':
        super().from_dictionary(dictionary)
        if 'cardPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificInput']))
            value = CardPaymentMethodSpecificInput()
            self.card_payment_method_specific_input = value.from_dictionary(dictionary['cardPaymentMethodSpecificInput'])
        if 'encryptedCustomerInput' in dictionary:
            self.encrypted_customer_input = dictionary['encryptedCustomerInput']
        if 'feedbacks' in dictionary:
            if not isinstance(dictionary['feedbacks'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['feedbacks']))
            value = Feedbacks()
            self.feedbacks = value.from_dictionary(dictionary['feedbacks'])
        if 'fraudFields' in dictionary:
            if not isinstance(dictionary['fraudFields'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraudFields']))
            value = FraudFields()
            self.fraud_fields = value.from_dictionary(dictionary['fraudFields'])
        if 'hostedFieldsSessionId' in dictionary:
            self.hosted_fields_session_id = dictionary['hostedFieldsSessionId']
        if 'hostedTokenizationId' in dictionary:
            self.hosted_tokenization_id = dictionary['hostedTokenizationId']
        if 'mobilePaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['mobilePaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mobilePaymentMethodSpecificInput']))
            value = MobilePaymentMethodSpecificInput()
            self.mobile_payment_method_specific_input = value.from_dictionary(dictionary['mobilePaymentMethodSpecificInput'])
        if 'omnichannelPaymentSpecificInput' in dictionary:
            if not isinstance(dictionary['omnichannelPaymentSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['omnichannelPaymentSpecificInput']))
            value = OmnichannelPaymentSpecificInput()
            self.omnichannel_payment_specific_input = value.from_dictionary(dictionary['omnichannelPaymentSpecificInput'])
        if 'order' in dictionary:
            if not isinstance(dictionary['order'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['order']))
            value = Order()
            self.order = value.from_dictionary(dictionary['order'])
        if 'redirectPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['redirectPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectPaymentMethodSpecificInput']))
            value = RedirectPaymentMethodSpecificInput()
            self.redirect_payment_method_specific_input = value.from_dictionary(dictionary['redirectPaymentMethodSpecificInput'])
        if 'sepaDirectDebitPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['sepaDirectDebitPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['sepaDirectDebitPaymentMethodSpecificInput']))
            value = SepaDirectDebitPaymentMethodSpecificInput()
            self.sepa_direct_debit_payment_method_specific_input = value.from_dictionary(dictionary['sepaDirectDebitPaymentMethodSpecificInput'])
        return self

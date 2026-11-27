#
# This file was automatically generated.
#
from .card_payment_method_specific_input_base import CardPaymentMethodSpecificInputBase
from .data_object import DataObject
from .feedbacks import Feedbacks
from .fraud_fields import FraudFields
from .hosted_checkout_specific_input import HostedCheckoutSpecificInput
from .mobile_payment_method_hosted_checkout_specific_input import MobilePaymentMethodHostedCheckoutSpecificInput
from .order import Order
from .redirect_payment_method_specific_input import RedirectPaymentMethodSpecificInput
from .sepa_direct_debit_payment_method_specific_input_base import SepaDirectDebitPaymentMethodSpecificInputBase


class CreateHostedCheckoutRequest(DataObject):

    __slots__ = (
        "__card_payment_method_specific_input",
        "__feedbacks",
        "__fraud_fields",
        "__hosted_checkout_specific_input",
        "__mobile_payment_method_specific_input",
        "__order",
        "__redirect_payment_method_specific_input",
        "__sepa_direct_debit_payment_method_specific_input",
    )

    __card_payment_method_specific_input: CardPaymentMethodSpecificInputBase | None
    __feedbacks: Feedbacks | None
    __fraud_fields: FraudFields | None
    __hosted_checkout_specific_input: HostedCheckoutSpecificInput | None
    __mobile_payment_method_specific_input: MobilePaymentMethodHostedCheckoutSpecificInput | None
    __order: Order | None
    __redirect_payment_method_specific_input: RedirectPaymentMethodSpecificInput | None
    __sepa_direct_debit_payment_method_specific_input: SepaDirectDebitPaymentMethodSpecificInputBase | None

    def __init__(
        self,
        *,
        card_payment_method_specific_input: CardPaymentMethodSpecificInputBase | None = None,
        feedbacks: Feedbacks | None = None,
        fraud_fields: FraudFields | None = None,
        hosted_checkout_specific_input: HostedCheckoutSpecificInput | None = None,
        mobile_payment_method_specific_input: MobilePaymentMethodHostedCheckoutSpecificInput | None = None,
        order: Order | None = None,
        redirect_payment_method_specific_input: RedirectPaymentMethodSpecificInput | None = None,
        sepa_direct_debit_payment_method_specific_input: SepaDirectDebitPaymentMethodSpecificInputBase | None = None,
    ) -> None:
        self.card_payment_method_specific_input = card_payment_method_specific_input
        self.feedbacks = feedbacks
        self.fraud_fields = fraud_fields
        self.hosted_checkout_specific_input = hosted_checkout_specific_input
        self.mobile_payment_method_specific_input = mobile_payment_method_specific_input
        self.order = order
        self.redirect_payment_method_specific_input = redirect_payment_method_specific_input
        self.sepa_direct_debit_payment_method_specific_input = sepa_direct_debit_payment_method_specific_input

    @property
    def card_payment_method_specific_input(self) -> CardPaymentMethodSpecificInputBase | None:
        """
        | Object containing the specific input details for card payments

        Type: :class:`onlinepayments.sdk.domain.card_payment_method_specific_input_base.CardPaymentMethodSpecificInputBase`
        """
        return self.__card_payment_method_specific_input

    @card_payment_method_specific_input.setter
    def card_payment_method_specific_input(self, value: CardPaymentMethodSpecificInputBase | None) -> None:
        self.__card_payment_method_specific_input = value

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
    def hosted_checkout_specific_input(self) -> HostedCheckoutSpecificInput | None:
        """
        | Object containing hosted checkout specific data

        Type: :class:`onlinepayments.sdk.domain.hosted_checkout_specific_input.HostedCheckoutSpecificInput`
        """
        return self.__hosted_checkout_specific_input

    @hosted_checkout_specific_input.setter
    def hosted_checkout_specific_input(self, value: HostedCheckoutSpecificInput | None) -> None:
        self.__hosted_checkout_specific_input = value

    @property
    def mobile_payment_method_specific_input(self) -> MobilePaymentMethodHostedCheckoutSpecificInput | None:
        """
        | Object containing the specific input details for mobile payments

        Type: :class:`onlinepayments.sdk.domain.mobile_payment_method_hosted_checkout_specific_input.MobilePaymentMethodHostedCheckoutSpecificInput`
        """
        return self.__mobile_payment_method_specific_input

    @mobile_payment_method_specific_input.setter
    def mobile_payment_method_specific_input(self, value: MobilePaymentMethodHostedCheckoutSpecificInput | None) -> None:
        self.__mobile_payment_method_specific_input = value

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
    def sepa_direct_debit_payment_method_specific_input(self) -> SepaDirectDebitPaymentMethodSpecificInputBase | None:
        """
        | Object containing the specific input details for SEPA direct debit payments

        Type: :class:`onlinepayments.sdk.domain.sepa_direct_debit_payment_method_specific_input_base.SepaDirectDebitPaymentMethodSpecificInputBase`
        """
        return self.__sepa_direct_debit_payment_method_specific_input

    @sepa_direct_debit_payment_method_specific_input.setter
    def sepa_direct_debit_payment_method_specific_input(self, value: SepaDirectDebitPaymentMethodSpecificInputBase | None) -> None:
        self.__sepa_direct_debit_payment_method_specific_input = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.card_payment_method_specific_input is not None:
            dictionary['cardPaymentMethodSpecificInput'] = self.card_payment_method_specific_input.to_dictionary()
        if self.feedbacks is not None:
            dictionary['feedbacks'] = self.feedbacks.to_dictionary()
        if self.fraud_fields is not None:
            dictionary['fraudFields'] = self.fraud_fields.to_dictionary()
        if self.hosted_checkout_specific_input is not None:
            dictionary['hostedCheckoutSpecificInput'] = self.hosted_checkout_specific_input.to_dictionary()
        if self.mobile_payment_method_specific_input is not None:
            dictionary['mobilePaymentMethodSpecificInput'] = self.mobile_payment_method_specific_input.to_dictionary()
        if self.order is not None:
            dictionary['order'] = self.order.to_dictionary()
        if self.redirect_payment_method_specific_input is not None:
            dictionary['redirectPaymentMethodSpecificInput'] = self.redirect_payment_method_specific_input.to_dictionary()
        if self.sepa_direct_debit_payment_method_specific_input is not None:
            dictionary['sepaDirectDebitPaymentMethodSpecificInput'] = self.sepa_direct_debit_payment_method_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreateHostedCheckoutRequest':
        super().from_dictionary(dictionary)
        if 'cardPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificInput']))
            value = CardPaymentMethodSpecificInputBase()
            self.card_payment_method_specific_input = value.from_dictionary(dictionary['cardPaymentMethodSpecificInput'])
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
        if 'hostedCheckoutSpecificInput' in dictionary:
            if not isinstance(dictionary['hostedCheckoutSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['hostedCheckoutSpecificInput']))
            value = HostedCheckoutSpecificInput()
            self.hosted_checkout_specific_input = value.from_dictionary(dictionary['hostedCheckoutSpecificInput'])
        if 'mobilePaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['mobilePaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mobilePaymentMethodSpecificInput']))
            value = MobilePaymentMethodHostedCheckoutSpecificInput()
            self.mobile_payment_method_specific_input = value.from_dictionary(dictionary['mobilePaymentMethodSpecificInput'])
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
            value = SepaDirectDebitPaymentMethodSpecificInputBase()
            self.sepa_direct_debit_payment_method_specific_input = value.from_dictionary(dictionary['sepaDirectDebitPaymentMethodSpecificInput'])
        return self

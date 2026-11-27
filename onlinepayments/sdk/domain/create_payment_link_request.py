#
# This file was automatically generated.
#
from datetime import datetime

from .card_payment_method_specific_input_base import CardPaymentMethodSpecificInputBase
from .data_object import DataObject
from .feedbacks import Feedbacks
from .fraud_fields import FraudFields
from .hosted_checkout_specific_input import HostedCheckoutSpecificInput
from .mobile_payment_method_hosted_checkout_specific_input import MobilePaymentMethodHostedCheckoutSpecificInput
from .order import Order
from .payment_link_order_input import PaymentLinkOrderInput
from .payment_link_specific_input import PaymentLinkSpecificInput
from .redirect_payment_method_specific_input import RedirectPaymentMethodSpecificInput
from .sepa_direct_debit_payment_method_specific_input_base import SepaDirectDebitPaymentMethodSpecificInputBase


class CreatePaymentLinkRequest(DataObject):

    __slots__ = (
        "__card_payment_method_specific_input",
        "__description",
        "__display_qr_code",
        "__expiration_date",
        "__feedbacks",
        "__fraud_fields",
        "__hosted_checkout_specific_input",
        "__is_reusable_link",
        "__mobile_payment_method_specific_input",
        "__order",
        "__payment_link_order",
        "__payment_link_specific_input",
        "__recipient_name",
        "__redirect_payment_method_specific_input",
        "__sepa_direct_debit_payment_method_specific_input",
    )

    __card_payment_method_specific_input: CardPaymentMethodSpecificInputBase | None
    __description: str | None
    __display_qr_code: bool | None
    __expiration_date: datetime | None
    __feedbacks: Feedbacks | None
    __fraud_fields: FraudFields | None
    __hosted_checkout_specific_input: HostedCheckoutSpecificInput | None
    __is_reusable_link: bool | None
    __mobile_payment_method_specific_input: MobilePaymentMethodHostedCheckoutSpecificInput | None
    __order: Order | None
    __payment_link_order: PaymentLinkOrderInput | None
    __payment_link_specific_input: PaymentLinkSpecificInput | None
    __recipient_name: str | None
    __redirect_payment_method_specific_input: RedirectPaymentMethodSpecificInput | None
    __sepa_direct_debit_payment_method_specific_input: SepaDirectDebitPaymentMethodSpecificInputBase | None

    def __init__(
        self,
        *,
        card_payment_method_specific_input: CardPaymentMethodSpecificInputBase | None = None,
        description: str | None = None,
        display_qr_code: bool | None = None,
        expiration_date: datetime | None = None,
        feedbacks: Feedbacks | None = None,
        fraud_fields: FraudFields | None = None,
        hosted_checkout_specific_input: HostedCheckoutSpecificInput | None = None,
        is_reusable_link: bool | None = None,
        mobile_payment_method_specific_input: MobilePaymentMethodHostedCheckoutSpecificInput | None = None,
        order: Order | None = None,
        payment_link_order: PaymentLinkOrderInput | None = None,
        payment_link_specific_input: PaymentLinkSpecificInput | None = None,
        recipient_name: str | None = None,
        redirect_payment_method_specific_input: RedirectPaymentMethodSpecificInput | None = None,
        sepa_direct_debit_payment_method_specific_input: SepaDirectDebitPaymentMethodSpecificInputBase | None = None,
    ) -> None:
        self.card_payment_method_specific_input = card_payment_method_specific_input
        self.description = description
        self.display_qr_code = display_qr_code
        self.expiration_date = expiration_date
        self.feedbacks = feedbacks
        self.fraud_fields = fraud_fields
        self.hosted_checkout_specific_input = hosted_checkout_specific_input
        self.is_reusable_link = is_reusable_link
        self.mobile_payment_method_specific_input = mobile_payment_method_specific_input
        self.order = order
        self.payment_link_order = payment_link_order
        self.payment_link_specific_input = payment_link_specific_input
        self.recipient_name = recipient_name
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
    def description(self) -> str | None:
        """
        | A note related to the created payment link.
        |
        | Deprecated: Use ``paymentLinkSpecificInput/description`` instead.

        Type: str

        Deprecated; A note related to the created payment link.  Use paymentLinkSpecificInput/description instead.
        """
        return self.__description

    @description.setter
    def description(self, value: str | None) -> None:
        self.__description = value

    @property
    def display_qr_code(self) -> bool | None:
        """
        | Indicates whether to include a QR code in the response. When set to true, the response will contain a Base64 encoded QR code image containing the payment link URL.

        Type: bool
        """
        return self.__display_qr_code

    @display_qr_code.setter
    def display_qr_code(self, value: bool | None) -> None:
        self.__display_qr_code = value

    @property
    def expiration_date(self) -> datetime | None:
        """
        | The date after which the payment link will not be usable to complete the payment. The date sent cannot be more than 6 months in the future or a past date. It must also contain the UTC offset.
        |
        | Deprecated: Use ``paymentLinkSpecificInput/expirationDate`` instead.

        Type: datetime

        Deprecated; The date after which the payment link will not be usable to complete the payment. The date sent cannot be more than 6 months in the future or a past date. It must also contain the UTC offset.  Use paymentLinkSpecificInput/expirationDate instead.
        """
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value: datetime | None) -> None:
        self.__expiration_date = value

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
    def is_reusable_link(self) -> bool | None:
        """
        | Indicates if the payment link can be used multiple times. The default value for this property is false

        Type: bool
        """
        return self.__is_reusable_link

    @is_reusable_link.setter
    def is_reusable_link(self, value: bool | None) -> None:
        self.__is_reusable_link = value

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
    def payment_link_order(self) -> PaymentLinkOrderInput | None:
        """
        | An object containing the details of the related payment input.
        |
        | Deprecated: All properties in ``paymentLinkOrder`` are deprecated. Use corresponding values as noted below: | Property | Replacement | | - | - | | merchantReference | ``references/merchantReference`` | | amount | ``order/amountOfMoney`` | | surchargeSpecificInput | ``order/surchargeSpecificInput`` |

        Type: :class:`onlinepayments.sdk.domain.payment_link_order_input.PaymentLinkOrderInput`
        """
        return self.__payment_link_order

    @payment_link_order.setter
    def payment_link_order(self, value: PaymentLinkOrderInput | None) -> None:
        self.__payment_link_order = value

    @property
    def payment_link_specific_input(self) -> PaymentLinkSpecificInput | None:
        """
        | An object containing details specific to payment link creation

        Type: :class:`onlinepayments.sdk.domain.payment_link_specific_input.PaymentLinkSpecificInput`
        """
        return self.__payment_link_specific_input

    @payment_link_specific_input.setter
    def payment_link_specific_input(self, value: PaymentLinkSpecificInput | None) -> None:
        self.__payment_link_specific_input = value

    @property
    def recipient_name(self) -> str | None:
        """
        | The payment link recipient name.
        |
        | Deprecated: Use ``paymentLinkSpecificInput/recipientName`` instead.

        Type: str

        Deprecated; The payment link recipient name.  Use paymentLinkSpecificInput/recipientName instead.
        """
        return self.__recipient_name

    @recipient_name.setter
    def recipient_name(self, value: str | None) -> None:
        self.__recipient_name = value

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
        if self.description is not None:
            dictionary['description'] = self.description
        if self.display_qr_code is not None:
            dictionary['displayQRCode'] = self.display_qr_code
        if self.expiration_date is not None:
            dictionary['expirationDate'] = DataObject.format_datetime(self.expiration_date)
        if self.feedbacks is not None:
            dictionary['feedbacks'] = self.feedbacks.to_dictionary()
        if self.fraud_fields is not None:
            dictionary['fraudFields'] = self.fraud_fields.to_dictionary()
        if self.hosted_checkout_specific_input is not None:
            dictionary['hostedCheckoutSpecificInput'] = self.hosted_checkout_specific_input.to_dictionary()
        if self.is_reusable_link is not None:
            dictionary['isReusableLink'] = self.is_reusable_link
        if self.mobile_payment_method_specific_input is not None:
            dictionary['mobilePaymentMethodSpecificInput'] = self.mobile_payment_method_specific_input.to_dictionary()
        if self.order is not None:
            dictionary['order'] = self.order.to_dictionary()
        if self.payment_link_order is not None:
            dictionary['paymentLinkOrder'] = self.payment_link_order.to_dictionary()
        if self.payment_link_specific_input is not None:
            dictionary['paymentLinkSpecificInput'] = self.payment_link_specific_input.to_dictionary()
        if self.recipient_name is not None:
            dictionary['recipientName'] = self.recipient_name
        if self.redirect_payment_method_specific_input is not None:
            dictionary['redirectPaymentMethodSpecificInput'] = self.redirect_payment_method_specific_input.to_dictionary()
        if self.sepa_direct_debit_payment_method_specific_input is not None:
            dictionary['sepaDirectDebitPaymentMethodSpecificInput'] = self.sepa_direct_debit_payment_method_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreatePaymentLinkRequest':
        super().from_dictionary(dictionary)
        if 'cardPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificInput']))
            value = CardPaymentMethodSpecificInputBase()
            self.card_payment_method_specific_input = value.from_dictionary(dictionary['cardPaymentMethodSpecificInput'])
        if 'description' in dictionary:
            self.description = dictionary['description']
        if 'displayQRCode' in dictionary:
            self.display_qr_code = dictionary['displayQRCode']
        if 'expirationDate' in dictionary:
            self.expiration_date = DataObject.parse_datetime(dictionary['expirationDate'])
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
        if 'isReusableLink' in dictionary:
            self.is_reusable_link = dictionary['isReusableLink']
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
        if 'paymentLinkOrder' in dictionary:
            if not isinstance(dictionary['paymentLinkOrder'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentLinkOrder']))
            value = PaymentLinkOrderInput()
            self.payment_link_order = value.from_dictionary(dictionary['paymentLinkOrder'])
        if 'paymentLinkSpecificInput' in dictionary:
            if not isinstance(dictionary['paymentLinkSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentLinkSpecificInput']))
            value = PaymentLinkSpecificInput()
            self.payment_link_specific_input = value.from_dictionary(dictionary['paymentLinkSpecificInput'])
        if 'recipientName' in dictionary:
            self.recipient_name = dictionary['recipientName']
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

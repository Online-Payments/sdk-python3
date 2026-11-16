from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.card_payment_method_specific_input import CardPaymentMethodSpecificInput
from onlinepayments.sdk.domain.create_hosted_tokenization_request import CreateHostedTokenizationRequest
from onlinepayments.sdk.domain.create_hosted_tokenization_response import CreateHostedTokenizationResponse
from onlinepayments.sdk.domain.create_payment_request import CreatePaymentRequest
from onlinepayments.sdk.domain.customer import Customer
from onlinepayments.sdk.domain.customer_device import CustomerDevice
from onlinepayments.sdk.domain.order import Order
from onlinepayments.sdk.domain.order_references import OrderReferences
from onlinepayments.sdk.domain.redirection_data import RedirectionData
from onlinepayments.sdk.domain.three_d_secure import ThreeDSecure
from onlinepayments.sdk.merchant.i_merchant_client import IMerchantClient

from app_types import OrderStore, PaymentStep
from create_payment_response_handler import handle_create_payment_response
from payment_attempt import payment_attempt_key


class HostedTokenizationExample:

    def __init__(self, merchant: IMerchantClient, orders: OrderStore):
        self.__merchant = merchant
        self.__orders = orders

    # [START hosted-tokenization-create]
    # Creates the session for the card form iframe on your checkout page.
    def create_session(self) -> CreateHostedTokenizationResponse:
        request = CreateHostedTokenizationRequest()
        request.locale = "en-GB"
        # Optional: request.variant = "MyTemplate.html", the file name of a custom template.

        response = self.__merchant.hosted_tokenization().create_hosted_tokenization(request)

        # Send hosted_tokenization_url (iframe URL) and sri (script integrity) to the page.
        return response
    # [END hosted-tokenization-create]

    # [START hosted-tokenization-payment]
    # The page calls tokenizer.submitTokenization() and posts result.hostedTokenizationId to your server.
    def pay(self, order_id: str, hosted_tokenization_id: str, amount_in_cents: int, currency_code: str,
            device: CustomerDevice, return_url: str) -> PaymentStep:
        amount_of_money = AmountOfMoney()
        amount_of_money.amount = amount_in_cents
        amount_of_money.currency_code = currency_code

        references = OrderReferences()
        references.merchant_reference = order_id

        customer = Customer()
        customer.device = device

        order = Order()
        order.amount_of_money = amount_of_money
        order.references = references
        order.customer = customer

        redirection_data = RedirectionData()
        redirection_data.return_url = return_url

        three_d_secure = ThreeDSecure()
        three_d_secure.redirection_data = redirection_data

        card_input = CardPaymentMethodSpecificInput()
        card_input.authorization_mode = "SALE"
        card_input.three_d_secure = three_d_secure

        request = CreatePaymentRequest()
        request.hosted_tokenization_id = hosted_tokenization_id
        request.order = order
        request.card_payment_method_specific_input = card_input

        context = CallContext(idempotence_key=payment_attempt_key(order_id, self.__orders))
        response = self.__merchant.payments().create_payment(request, context)
        return handle_create_payment_response(response, order_id, self.__orders)
    # [END hosted-tokenization-payment]

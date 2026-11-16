from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.card import Card
from onlinepayments.sdk.domain.card_payment_method_specific_input import CardPaymentMethodSpecificInput
from onlinepayments.sdk.domain.create_payment_request import CreatePaymentRequest
from onlinepayments.sdk.domain.customer import Customer
from onlinepayments.sdk.domain.customer_device import CustomerDevice
from onlinepayments.sdk.domain.order import Order
from onlinepayments.sdk.domain.order_references import OrderReferences
from onlinepayments.sdk.domain.redirection_data import RedirectionData
from onlinepayments.sdk.domain.three_d_secure import ThreeDSecure
from onlinepayments.sdk.merchant.i_merchant_client import IMerchantClient

from app_types import CardInput, OrderStore, PaymentStep
from create_payment_response_handler import handle_create_payment_response
from payment_attempt import payment_attempt_key


class ServerToServerExample:

    def __init__(self, merchant: IMerchantClient, orders: OrderStore):
        self.__merchant = merchant
        self.__orders = orders

    # [START server-to-server-create]
    # Card data on your server puts you in scope of PCI DSS SAQ D.
    # Use Hosted Tokenization or Hosted Fields unless you are certified for it.
    def pay_with_card(self, order_id: str, amount_in_cents: int, currency_code: str, payment_product_id: int,
                      card: CardInput, device: CustomerDevice, return_url: str) -> PaymentStep:
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

        card_data = Card()
        card_data.card_number = card.number
        card_data.cardholder_name = card.holder_name
        card_data.expiry_date = card.expiry_date
        card_data.cvv = card.cvv

        redirection_data = RedirectionData()
        redirection_data.return_url = return_url

        three_d_secure = ThreeDSecure()
        three_d_secure.redirection_data = redirection_data

        card_input = CardPaymentMethodSpecificInput()
        # e.g. 1 = Visa, 3 = Mastercard.
        card_input.payment_product_id = payment_product_id
        card_input.card = card_data
        # SALE: authorised and captured at once. Acquirers that do not support it ignore it.
        # FINAL_AUTHORIZATION: capture the full amount within 7 days.
        # PRE_AUTHORIZATION: can be reversed; capture the authorised amount or less within 30 days.
        card_input.authorization_mode = "SALE"
        card_input.three_d_secure = three_d_secure

        request = CreatePaymentRequest()
        request.order = order
        request.card_payment_method_specific_input = card_input

        context = CallContext(idempotence_key=payment_attempt_key(order_id, self.__orders))
        # Raises DeclinedPaymentException if the payment is declined, and other ApiException subclasses for errors;
        # see ErrorHandlingExample for handling each case.
        response = self.__merchant.payments().create_payment(request, context)
        return handle_create_payment_response(response, order_id, self.__orders)
    # [END server-to-server-create]

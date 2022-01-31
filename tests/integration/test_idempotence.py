import unittest
import uuid

import tests.integration.init_utils as init_utils
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.domain.address import Address
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.card import Card
from onlinepayments.sdk.domain.card_payment_method_specific_input import CardPaymentMethodSpecificInput
from onlinepayments.sdk.domain.create_payment_request import CreatePaymentRequest
from onlinepayments.sdk.domain.customer import Customer
from onlinepayments.sdk.domain.order import Order
from tests.integration.init_utils import MERCHANT_ID


class IdempotenceTest(unittest.TestCase):
    """Test that the client can successfully detect that an idempotent request is sent twice"""

    def test_idempotence(self):
        """Test that the client can successfully detect that an idempotent request is sent twice"""

        amount_of_money = AmountOfMoney()
        amount_of_money.currency_code = "EUR"
        amount_of_money.amount = 100

        billing_address = Address()
        billing_address.country_code = "BE"

        customer = Customer()
        customer.locale = "en"
        customer.billing_address = billing_address

        order = Order()
        order.amount_of_money = amount_of_money
        order.customer = customer

        card = Card()
        card.card_number = "4567350000427977"
        card.cardholder_name = "Wile E. Coyote"
        card.cvv = "123"
        card.expiry_date = "1234"

        payment_method_input = CardPaymentMethodSpecificInput()
        payment_method_input.return_url = "http://example.com"
        payment_method_input.payment_product_id = 1
        payment_method_input.card = card

        body = CreatePaymentRequest()
        body.order = order
        body.card_payment_method_specific_input = payment_method_input
        idempotence_key = str(uuid.uuid4())
        context = CallContext(idempotence_key)

        with init_utils.create_client() as client:
            response = client.merchant(MERCHANT_ID).payments().create_payment(body, context)

            payment_id = response.payment.id
            self.assertEqual(idempotence_key, context.idempotence_key)
            self.assertIsNone(context.idempotence_request_timestamp)

            response_2 = client.merchant(MERCHANT_ID).payments().create_payment(body, context)

            payment_id_2 = response_2.payment.id
            self.assertEqual(payment_id, payment_id_2)
            self.assertEqual(idempotence_key, context.idempotence_key)
            self.assertIsNotNone(context.idempotence_request_timestamp)


if __name__ == '__main__':
    unittest.main()

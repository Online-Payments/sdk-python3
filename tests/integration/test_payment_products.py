import unittest

from onlinepayments.sdk.merchant.products.get_payment_products_params import GetPaymentProductsParams
from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID


class PaymentProductTest(unittest.TestCase):
    """Test if products functions"""

    def test_payment_products(self):
        """Test if get_payment_products functions"""
        params = GetPaymentProductsParams()
        params.country_code = "BE"
        params.currency_code = "EUR"

        with init_utils.create_client() as client:
            response = client.merchant(MERCHANT_ID).products().get_payment_products(params)
        self.assertGreater(len(response.payment_products), 0)


if __name__ == '__main__':
    unittest.main()

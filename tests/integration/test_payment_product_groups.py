import unittest

from onlinepayments.sdk.merchant.productgroups.get_product_groups_params import GetProductGroupsParams
from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID


class PaymentProductGroupsTest(unittest.TestCase):
    """Test if product groups function"""

    def test_payment_product_groups(self):
        """Test if product groups function"""
        params = GetProductGroupsParams()
        params.country_code = "BE"
        params.currency_code = "EUR"

        with init_utils.create_client() as client:
            response = client.merchant(MERCHANT_ID).product_groups().get_product_groups(params)
        self.assertIsNotNone(response.payment_product_groups)
        self.assertGreater(len(response.payment_product_groups), 0)


if __name__ == '__main__':
    unittest.main()

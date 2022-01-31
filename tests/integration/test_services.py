import unittest

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID


class ServicesTest(unittest.TestCase):
    def test_services(self):
        with init_utils.create_client() as client:
            response = client.merchant(MERCHANT_ID).services().test_connection()

            self.assertIsNotNone(response.result)


if __name__ == '__main__':
    unittest.main()

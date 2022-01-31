import unittest

from onlinepayments.sdk.merchant.productgroups.get_product_group_params import GetProductGroupParams
from onlinepayments.sdk.merchant.productgroups.get_product_groups_params import GetProductGroupsParams
from onlinepayments.sdk.merchant.products.get_payment_product_params import GetPaymentProductParams
from onlinepayments.sdk.merchant.products.get_payment_products_params import GetPaymentProductsParams
from tests.unit.comparable_param import ComparableParam


class GetPaymentProductParamsTest(unittest.TestCase):
    """Tests if instances of the GetPaymentProductParams class for products can be correctly converted to RequestParameter objects"""

    def test_empty_request_parameters(self):
        """Tests that the GetPaymentProductParams object correctly functions when values are not set"""
        params = GetPaymentProductParams()
        expected = []
        self.assertCountEqual(expected, params.to_request_parameters())

    def test_filled_request_parameters(self):
        """Tests that the GetPaymentProductParams object can correctly store and convert its data to RequestParameters"""
        params = GetPaymentProductParams()
        expected = []
        params.amount = 1000
        expected.append(ComparableParam("amount", "1000"))
        params.country_code = "NL"
        expected.append(ComparableParam("countryCode", "NL"))
        params.currency_code = "EUR"
        expected.append(ComparableParam("currencyCode", "EUR"))
        params.is_recurring = True
        expected.append(ComparableParam("isRecurring", "True"))
        params.locale = "nl_NL"
        expected.append(ComparableParam("locale", "nl_NL"))
        params.add_hide("fields")
        expected.append(ComparableParam("hide", "fields"))
        params.add_hide("accounts_on_file")
        expected.append(ComparableParam("hide", "accounts_on_file"))

        request_params = params.to_request_parameters()

        self.maxDiff = None
        self.assertCountEqual(expected, request_params)

    def test_delete_request_parameters(self):
        """Test if removing parameter correctly removes them from the GetPaymentProductParams object"""
        params = GetPaymentProductParams()
        expected = []
        params.amount = 1000
        params.country_code = "NL"
        params.currency_code = "EUR"
        params.amount = None
        params.currency_code = None
        params.country_code = None

        request_params = params.to_request_parameters()

        self.assertCountEqual(expected, request_params)


class GetPaymentProductsParamsTest(unittest.TestCase):
    """Tests if instances of the GetPaymentProductsParams class for products can be correctly converted to RequestParameter objects"""

    def test_empty_request_parameters(self):
        """Tests that the GetPaymentProductsParams object correctly functions when values are not set"""
        params = GetPaymentProductsParams()
        expected = []
        self.assertCountEqual(expected, params.to_request_parameters())

    def test_filled_request_parameters(self):
        """Tests that the GetPaymentProductsParams object can correctly store and convert its data to RequestParameters"""
        params = GetPaymentProductsParams()
        expected = []
        params.amount = 1000
        expected.append(ComparableParam("amount", "1000"))
        params.country_code = "NL"
        expected.append(ComparableParam("countryCode", "NL"))
        params.currency_code = "EUR"
        expected.append(ComparableParam("currencyCode", "EUR"))
        params.is_recurring = True
        expected.append(ComparableParam("isRecurring", "True"))
        params.locale = "nl_NL"
        expected.append(ComparableParam("locale", "nl_NL"))
        params.add_hide("fields")
        expected.append(ComparableParam("hide", "fields"))
        params.add_hide("accounts_on_file")
        expected.append(ComparableParam("hide", "accounts_on_file"))

        request_params = params.to_request_parameters()

        self.maxDiff = None
        self.assertCountEqual(expected, request_params)

    def test_delete_request_parameters(self):
        """Test if removing parameter correctly removes them from the GetPaymentProductsParams object"""
        params = GetPaymentProductsParams()
        expected = []
        params.amount = 1000
        params.country_code = "NL"
        params.currency_code = "EUR"
        params.amount = None
        params.currency_code = None
        params.country_code = None

        request_params = params.to_request_parameters()

        self.assertCountEqual(expected, request_params)


class GetProductGroupParamsTest(unittest.TestCase):
    """Tests if instances of the GetProductGroupParams class for product groups can be correctly converted to RequestParameter objects"""

    def test_empty_request_parameters(self):
        """Tests that the GetProductGroupParams object correctly functions when values are not set"""
        params = GetProductGroupParams()
        expected = []
        self.assertCountEqual(expected, params.to_request_parameters())

    def test_filled_request_parameters(self):
        """Tests that the GetProductGroupParams object can correctly store and convert its data to RequestParameters"""
        params = GetProductGroupParams()
        expected = []
        params.amount = 1000
        expected.append(ComparableParam("amount", "1000"))
        params.country_code = "NL"
        expected.append(ComparableParam("countryCode", "NL"))
        params.currency_code = "EUR"
        expected.append(ComparableParam("currencyCode", "EUR"))
        params.is_recurring = True
        expected.append(ComparableParam("isRecurring", "True"))
        params.locale = "nl_NL"
        expected.append(ComparableParam("locale", "nl_NL"))
        params.add_hide("fields")
        expected.append(ComparableParam("hide", "fields"))
        params.add_hide("accounts_on_file")
        expected.append(ComparableParam("hide", "accounts_on_file"))

        request_params = params.to_request_parameters()

        self.maxDiff = None
        self.assertCountEqual(expected, request_params)

    def test_delete_request_parameters(self):
        """Test if removing parameter correctly removes them from the GetProductGroupParams object"""
        params = GetProductGroupParams()
        expected = []
        params.amount = 1000
        params.country_code = "NL"
        params.currency_code = "EUR"
        params.amount = None
        params.currency_code = None
        params.country_code = None

        request_params = params.to_request_parameters()

        self.assertCountEqual(expected, request_params)


class GetProductGroupsParamsTest(unittest.TestCase):
    """Tests if instances of the GetProductGroupsParams class for product groups can be correctly converted to RequestParameter objects"""

    def test_empty_request_parameters(self):
        """Tests that the GetProductGroupsParams object correctly functions when values are not set"""
        params = GetProductGroupsParams()
        expected = []
        self.assertCountEqual(expected, params.to_request_parameters())

    def test_filled_request_parameters(self):
        """Tests that the GetProductGroupsParams object can correctly store and convert its data to RequestParameters
        """
        params = GetProductGroupsParams()
        expected = []
        params.amount = 1000
        expected.append(ComparableParam("amount", "1000"))
        params.country_code = "NL"
        expected.append(ComparableParam("countryCode", "NL"))
        params.currency_code = "EUR"
        expected.append(ComparableParam("currencyCode", "EUR"))
        params.is_recurring = True
        expected.append(ComparableParam("isRecurring", "True"))
        params.locale = "nl_NL"
        expected.append(ComparableParam("locale", "nl_NL"))
        params.add_hide("fields")
        expected.append(ComparableParam("hide", "fields"))
        params.add_hide("accounts_on_file")
        expected.append(ComparableParam("hide", "accounts_on_file"))

        request_params = params.to_request_parameters()

        self.maxDiff = None
        self.assertCountEqual(expected, request_params)

    def test_delete_request_parameters(self):
        """Test if removing parameter correctly removes them from the GetProductGroupsParams object"""
        params = GetProductGroupsParams()
        expected = []
        params.amount = 1000
        params.country_code = "NL"
        params.currency_code = "EUR"
        params.amount = None
        params.currency_code = None
        params.country_code = None

        request_params = params.to_request_parameters()

        self.maxDiff = None
        self.assertCountEqual(expected, request_params)


if __name__ == '__main__':
    unittest.main()

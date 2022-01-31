# -*-coding: UTF-8 -*-
import unittest
from urllib.parse import urlparse

from onlinepayments.sdk.communicator import Communicator
from onlinepayments.sdk.defaultimpl.default_authenticator import DefaultAuthenticator
from onlinepayments.sdk.meta_data_provider import MetaDataProvider
from onlinepayments.sdk.request_param import RequestParam


class CommunicatorTest(unittest.TestCase):
    """Contains tests that test if the communicator can construct proper urls if given the base url, a relative url and possibly a list of request parameters"""

    def test_to_uri_without_request_parameters(self):
        """Tests if the communicator can correctly construct an url using a known base url and a relative url"""
        communicator = Communicator(
            api_endpoint=urlparse("https://example.com"),
            authenticator=DefaultAuthenticator("a_key", "a_secret"),
            meta_data_provider=MetaDataProvider("OnlinePayments"))

        uri1 = communicator._to_absolute_uri("v2/merchant/1/testconnection", [])
        uri2 = communicator._to_absolute_uri("/v2/merchant/1/testconnection", [])

        self.assertEqual("https://example.com/v2/merchant/1/testconnection", uri1.geturl())
        self.assertEqual("https://example.com/v2/merchant/1/testconnection", uri2.geturl())

    def test_to_uri_with_request_parameters(self):
        """Tests if the communicator can correctly construct an url using a known base url, a relative url and a list of request parameters"""
        requestParams = [RequestParam("amount", "123"), RequestParam("source", "USD"), RequestParam("target", "EUR"),
                         RequestParam("dummy", "é&%=")]
        communicator = Communicator(
            api_endpoint=urlparse("https://example.com"),
            authenticator=DefaultAuthenticator("a_key", "a_secret"),
            meta_data_provider=MetaDataProvider("OnlinePayments"))

        uri1 = communicator._to_absolute_uri("v2/1/testconnection", requestParams)
        uri2 = communicator._to_absolute_uri("/v2/1/testconnection", requestParams)

        self.assertEqual("https://example.com/v2/1/testconnection"
                         "?amount=123&source=USD&target=EUR&dummy=%C3%A9%26%25%3D", uri1.geturl())
        self.assertEqual("https://example.com/v2/1/testconnection"
                         "?amount=123&source=USD&target=EUR&dummy=%C3%A9%26%25%3D", uri2.geturl())


if __name__ == '__main__':
    unittest.main()

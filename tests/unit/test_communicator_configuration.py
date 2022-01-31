import configparser
import unittest

from onlinepayments.sdk.communicator_configuration import CommunicatorConfiguration
from onlinepayments.sdk.defaultimpl.authorization_type import AuthorizationType


class CommunicatorConfigurationTest(unittest.TestCase):
    """Contains tests testing that the correct communicator configuration can be made from a properties file"""

    def setUp(self):
        """Initialize a set of commonly used configurations"""
        self.config = configparser.ConfigParser()

        self.config.add_section("OnlinePaymentsSDK")
        self.config.set('OnlinePaymentsSDK', "onlinePayments.api.endpoint.host", "example.com")

    def tearDown(self):
        self.config = None

    def assertDefaults(self, communicator_config):
        """Tests commonly used settings for testing url, authorization type, timeouts and max_connections"""
        self.assertEqual("https://example.com", communicator_config.api_endpoint.geturl())
        self.assertEqual(AuthorizationType.V1HMAC, communicator_config.authorization_type)
        self.assertEqual(CommunicatorConfiguration().DEFAULT_CONNECT_TIMEOUT, communicator_config.connect_timeout)
        self.assertEqual(CommunicatorConfiguration().DEFAULT_SOCKET_TIMEOUT, communicator_config.socket_timeout)
        self.assertEqual(CommunicatorConfiguration().DEFAULT_MAX_CONNECTIONS, communicator_config.max_connections)

    def test_construct_from_properties_without_proxy(self):
        """Test if a CommunicatorConfiguration can be constructed correctly from a list of properties"""

        communicator_config = CommunicatorConfiguration(self.config)

        self.assertDefaults(communicator_config)
        self.assertIsNone(communicator_config.api_key_id)
        self.assertIsNone(communicator_config.secret_api_key)
        self.assertIsNone(communicator_config.proxy_configuration)
        self.assertIsNone(communicator_config.integrator)
        self.assertIsNone(communicator_config.shopping_cart_extension)

    def test_construct_from_properties_with_proxy_without_authentication(self):
        """Tests if a CommunicatorConfiguration can be constructed correctly from settings including a proxy"""
        self.config.set('OnlinePaymentsSDK', "onlinePayments.api.proxy.uri", "http://proxy.example.org:3128")

        communicator_config = CommunicatorConfiguration(self.config)

        self.assertDefaults(communicator_config)
        self.assertIsNone(communicator_config.api_key_id)
        self.assertIsNone(communicator_config.secret_api_key)
        proxy_config = communicator_config.proxy_configuration
        self.assertIsNotNone(proxy_config)
        self.assertEqual("http", proxy_config.scheme)
        self.assertEqual("proxy.example.org", proxy_config.host)
        self.assertEqual(3128, proxy_config.port)
        self.assertIsNone(proxy_config.username)
        self.assertIsNone(proxy_config.password)

    def test_construct_from_properties_with_proxy_authentication(self):
        """Tests if a CommunicatorConfiguration can be constructed correctly from settings with a proxy and authentication"""
        self.config.set('OnlinePaymentsSDK', "onlinePayments.api.proxy.uri", "http://proxy.example.org:3128")
        self.config.set('OnlinePaymentsSDK', "onlinePayments.api.proxy.username", "username")
        self.config.set('OnlinePaymentsSDK', "onlinePayments.api.proxy.password", "password")

        communicator_config = CommunicatorConfiguration(self.config)

        self.assertDefaults(communicator_config)
        self.assertIsNone(communicator_config.api_key_id)
        self.assertIsNone(communicator_config.secret_api_key)
        proxy_config = communicator_config.proxy_configuration
        self.assertIsNotNone(proxy_config)
        self.assertEqual("http", proxy_config.scheme)
        self.assertEqual("proxy.example.org", proxy_config.host)
        self.assertEqual(3128, proxy_config.port)
        self.assertEqual("username", proxy_config.username)
        self.assertEqual("password", proxy_config.password)

    def test_construct_from_properties_with_defaults_overridden(self):
        """Tests if a CommunicatorConfiguration can be constructed correctly from settings that contain a different number for defaults"""
        self.config.set('OnlinePaymentsSDK', 'onlinePayments.api.connectTimeout', '100')
        self.config.set('OnlinePaymentsSDK', 'onlinePayments.api.socketTimeout', '200')
        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.maxConnections", "300")

        communicator_config = CommunicatorConfiguration(self.config)
        self.assertEqual("https://example.com", communicator_config.api_endpoint.geturl())
        self.assertEqual(AuthorizationType.V1HMAC, communicator_config.authorization_type)
        self.assertEqual(100, communicator_config.connect_timeout)
        self.assertEqual(200, communicator_config.socket_timeout)
        self.assertEqual(300, communicator_config.max_connections)
        self.assertIsNone(communicator_config.api_key_id)
        self.assertIsNone(communicator_config.secret_api_key)
        self.assertIsNone(communicator_config.proxy_configuration)

    def test_construct_from_properties_with_host_and_scheme(self):
        """Tests that constructing a communicator configuration from a host and port correctly processes this info"""
        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.endpoint.scheme", "http")

        communicator_config = CommunicatorConfiguration(self.config)

        self.assertEqual("http://example.com", communicator_config.api_endpoint.geturl())

    def test_construct_from_properties_with_host_and_port(self):
        """Tests that constructing a communicator configuration from a host and port correctly processes this info"""

        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.endpoint.port", "8443")

        communicator_config = CommunicatorConfiguration(self.config)

        self.assertEqual("https://example.com:8443", communicator_config.api_endpoint.geturl())

    def test_construct_from_properties_with_host_scheme_port(self):
        """Tests that constructing a communicator configuration from host, scheme and port correctly processes this info"""
        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.endpoint.scheme", "http")
        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.endpoint.port", "8080")

        communicator_config = CommunicatorConfiguration(self.config)

        self.assertEqual("http://example.com:8080", communicator_config.api_endpoint.geturl())

    def test_construct_from_properties_with_metadata(self):
        """Tests that constructing a communicator configuration using integrator and shopping cart data constructs properly"""
        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.integrator", "OnlinePayments.Integrator")
        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.shoppingCartExtension.creator",
                        "OnlinePayments.Creator")
        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.shoppingCartExtension.name",
                        "OnlinePayments.ShoppingCarts")
        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.shoppingCartExtension.version", "1.0")
        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.shoppingCartExtension.extensionId", "ExtensionId")

        communicator_config = CommunicatorConfiguration(self.config)

        self.assertDefaults(communicator_config)
        self.assertIsNone(communicator_config.api_key_id)
        self.assertIsNone(communicator_config.secret_api_key)
        self.assertIsNone(communicator_config.proxy_configuration)
        self.assertEqual("OnlinePayments.Integrator", communicator_config.integrator)
        self.assertIsNotNone(communicator_config.shopping_cart_extension)
        self.assertEqual("OnlinePayments.Creator", communicator_config.shopping_cart_extension.creator)
        self.assertEqual("OnlinePayments.ShoppingCarts", communicator_config.shopping_cart_extension.name)
        self.assertEqual("1.0", communicator_config.shopping_cart_extension.version)
        self.assertEqual("ExtensionId", communicator_config.shopping_cart_extension.extension_id)

    def test_accept_lowercased_authorization_type_in_config(self):
        """Tests if the default authenticator accepts authorization types with different casing in config."""
        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.authorizationType", "v1hmac")
        communicator_config = CommunicatorConfiguration(self.config)
        self.assertEqual(AuthorizationType.V1HMAC, communicator_config.authorization_type)

    def test_accept_uppercased_authorization_type_in_param(self):
        """Tests if the default authenticator accepts authorization types with different casing as parameter."""
        communicator_config = CommunicatorConfiguration(self.config, authorization_type="V1HMAC")
        self.assertEqual(AuthorizationType.V1HMAC, communicator_config.authorization_type)

    def test_reject_unknown_authorization_type_in_config(self):
        """Tests if the default authenticator throws an exception if an invalid authorization type is provided."""
        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.authorizationType", "invalidAuthorizationType")
        self.assertRaises(RuntimeError, CommunicatorConfiguration, self.config)

    def test_reject_unknown_authorization_type_in_param(self):
        """Tests if the default authenticator throws an exception if an invalid authorization type is provided."""
        self.assertRaises(RuntimeError, CommunicatorConfiguration, self.config,
                          authorization_type="invalidAuthorizationType")


if __name__ == '__main__':
    unittest.main()

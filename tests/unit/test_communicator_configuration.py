import configparser
import unittest

from onlinepayments.sdk.authentication.authorization_type import AuthorizationType
from onlinepayments.sdk.communicator_configuration import CommunicatorConfiguration
from onlinepayments.sdk.proxy_configuration import ProxyConfiguration
from onlinepayments.sdk.domain.shopping_cart_extension import ShoppingCartExtension


class CommunicatorConfigurationTest(unittest.TestCase):

    def setUp(self):
        self.config = configparser.ConfigParser()

        self.config.add_section("OnlinePaymentsSDK")
        self.config.set('OnlinePaymentsSDK', 'onlinePayments.api.endpoint.host', "payment.preprod.online-payments.com")
        self.config.set('OnlinePaymentsSDK', 'onlinePayments.api.authorizationType', 'v1HMAC')
        self.config.set('OnlinePaymentsSDK', 'onlinePayments.api.connectTimeout', '20')
        self.config.set('OnlinePaymentsSDK', 'onlinePayments.api.socketTimeout', '10')

    def tearDown(self):
        self.config = None

    def assertDefaults(self, communicator_config):
        self.assertEqual("https://payment.preprod.online-payments.com", communicator_config.api_endpoint.geturl())
        self.assertEqual(AuthorizationType.get_authorization("v1HMAC"), communicator_config.authorization_type)
        self.assertEqual(20, communicator_config.connect_timeout)
        self.assertEqual(10, communicator_config.socket_timeout)

        self.assertEqual(CommunicatorConfiguration().DEFAULT_MAX_CONNECTIONS, communicator_config.max_connections)

    def test_ConstructedFromProperties_DefaultScenario_SetExpectedConfigurationWithoutProxy(self):
        communicator_config = CommunicatorConfiguration(self.config)

        self.assertDefaults(communicator_config)
        self.assertIsNone(communicator_config.api_key_id)
        self.assertIsNone(communicator_config.secret_api_key)
        self.assertIsNone(communicator_config.proxy_configuration)
        self.assertIsNone(communicator_config.integrator)
        self.assertIsNone(communicator_config.shopping_cart_extension)

    def test_ConstructedWithProxyWithoutAuthentication_DefaultScenario_SetExpectedProxyConfiguration(self):
        self.config.set('OnlinePaymentsSDK', "onlinePayments.api.proxy.uri",
                        "http://proxy.example.org:3128")

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

    def test_ConstructedWithProxyWithAuthentication_DefaultScenario_SetExpectedProxyConfiguration(self):
        self.config.set('OnlinePaymentsSDK', "onlinePayments.api.proxy.uri", "http://proxy.example.org:3128")
        self.config.set('OnlinePaymentsSDK', "onlinePayments.api.proxy.username", "proxy-username")
        self.config.set('OnlinePaymentsSDK', "onlinePayments.api.proxy.password", "proxy-password")

        communicator_config = CommunicatorConfiguration(self.config)

        self.assertDefaults(communicator_config)
        self.assertIsNone(communicator_config.api_key_id)
        self.assertIsNone(communicator_config.secret_api_key)
        proxy_config = communicator_config.proxy_configuration
        self.assertIsNotNone(proxy_config)
        self.assertEqual("http", proxy_config.scheme)
        self.assertEqual("proxy.example.org", proxy_config.host)
        self.assertEqual(3128, proxy_config.port)
        self.assertEqual("proxy-username", proxy_config.username)
        self.assertEqual("proxy-password", proxy_config.password)

    def test_ConstructedWithMaxConnections_DefaultScenario_SetConfiguredMaxConnections(self):
        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.maxConnections", "100")

        communicator_config = CommunicatorConfiguration(self.config)
        self.assertEqual("https://payment.preprod.online-payments.com", communicator_config.api_endpoint.geturl())
        self.assertEqual(AuthorizationType.get_authorization("v1HMAC"), communicator_config.authorization_type)
        self.assertEqual(20, communicator_config.connect_timeout)
        self.assertEqual(10, communicator_config.socket_timeout)
        self.assertEqual(100, communicator_config.max_connections)
        self.assertIsNone(communicator_config.api_key_id)
        self.assertIsNone(communicator_config.secret_api_key)
        self.assertIsNone(communicator_config.proxy_configuration)

    def test_ConstructedWithHostAndScheme_DefaultScenario_SetEndpointWithConfiguredScheme(self):
        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.endpoint.scheme", "http")

        communicator_config = CommunicatorConfiguration(self.config)

        self.assertEqual("http://payment.preprod.online-payments.com", communicator_config.api_endpoint.geturl())

    def test_ConstructedWithHostAndPort_DefaultScenario_SetEndpointWithConfiguredPort(self):
        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.endpoint.port", "8443")

        communicator_config = CommunicatorConfiguration(self.config)

        self.assertEqual("https://payment.preprod.online-payments.com:8443", communicator_config.api_endpoint.geturl())

    def test_ConstructedWithHostSchemeAndPort_DefaultScenario_SetEndpointWithConfiguredSchemeAndPort(self):
        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.endpoint.scheme", "http")
        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.endpoint.port", "8080")

        communicator_config = CommunicatorConfiguration(self.config)

        self.assertEqual("http://payment.preprod.online-payments.com:8080", communicator_config.api_endpoint.geturl())

    def test_ConstructedWithHostOnly_DefaultScenario_SetHttpsEndpoint(self):
        self.config.remove_option("OnlinePaymentsSDK", "onlinePayments.api.endpoint.scheme")
        communicator_config = CommunicatorConfiguration(self.config)
        self.assertTrue(communicator_config.api_endpoint.geturl().startswith("https://"))

    def test_ConstructedWithMetadata_DefaultScenario_SetIntegratorAndShoppingCartExtension(self):
        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.integrator", "OnlinePayments.Integrator")
        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.shoppingCartExtension.creator", "OnlinePayments.Creator")
        self.config.set("OnlinePaymentsSDK", "onlinePayments.api.shoppingCartExtension.name", "OnlinePayments.ShoppingCarts")
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

    def test_ConstructingFromKwargs_DefaultScenario_SetProvidedValues(self):
        proxy = ProxyConfiguration("proxy.example.com", 3128)
        config = CommunicatorConfiguration(
            api_endpoint="https://api.example.com",
            api_key_id="my-key-id",
            secret_api_key="my-secret",
            connect_timeout=15,
            socket_timeout=25,
            max_connections=42,
            proxy_configuration=proxy,
            integrator="MyIntegrator",
        )
        self.assertEqual("https://api.example.com", config.api_endpoint.geturl())
        self.assertEqual("my-key-id", config.api_key_id)
        self.assertEqual("my-secret", config.secret_api_key)
        self.assertEqual(15, config.connect_timeout)
        self.assertEqual(25, config.socket_timeout)
        self.assertEqual(42, config.max_connections)
        self.assertIs(proxy, config.proxy_configuration)
        self.assertEqual("MyIntegrator", config.integrator)

    def test_ConstructingDefaultConfiguration_DefaultScenario_CreateValidInstance(self):
        config = CommunicatorConfiguration()
        self.assertIsNotNone(config)

    def test_ConstructingDefaultConfiguration_DefaultScenario_HaveDefaultValues(self):
        config = CommunicatorConfiguration()
        self.assertIsNone(config.api_endpoint)
        self.assertIsNone(config.api_key_id)
        self.assertIsNone(config.secret_api_key)
        self.assertIsNone(config.authorization_type)
        self.assertIsNone(config.connect_timeout)
        self.assertIsNone(config.socket_timeout)
        self.assertIsNone(config.max_connections)
        self.assertIsNone(config.proxy_configuration)
        self.assertIsNone(config.integrator)
        self.assertIsNone(config.shopping_cart_extension)

    def test_SettingAndGettingApiKeyId_DefaultScenario_SetAndGetApiKeyId(self):
        config = CommunicatorConfiguration()
        config.api_key_id = "my-api-key-id"
        self.assertEqual("my-api-key-id", config.api_key_id)

    def test_SettingAndGettingApiKeyId_DefaultScenario_SetNullApiKeyId(self):
        config = CommunicatorConfiguration()
        config.api_key_id = "initial-key"
        config.api_key_id = None
        self.assertIsNone(config.api_key_id)

    def test_SettingAndGettingSecretApiKey_DefaultScenario_SetAndGetSecretApiKey(self):
        config = CommunicatorConfiguration()
        config.secret_api_key = "my-secret-key"
        self.assertEqual("my-secret-key", config.secret_api_key)

    def test_SettingAndGettingSecretApiKey_DefaultScenario_SetNullSecretApiKey(self):
        config = CommunicatorConfiguration()
        config.secret_api_key = "initial-secret"
        config.secret_api_key = None
        self.assertIsNone(config.secret_api_key)

    def test_SettingAndGettingAuthorizationType_DefaultScenario_SetAndGetAuthorizationType(self):
        config = CommunicatorConfiguration()
        config.authorization_type = AuthorizationType.V1HMAC
        self.assertEqual(AuthorizationType.V1HMAC, config.authorization_type)

    def test_SettingAndGettingAuthorizationType_DefaultScenario_SetNullAuthorizationType(self):
        config = CommunicatorConfiguration()
        config.authorization_type = None
        self.assertIsNone(config.authorization_type)

    def test_SettingAndGettingConnectTimeout_DefaultScenario_SetAndGetConnectTimeout(self):
        config = CommunicatorConfiguration()
        config.connect_timeout = 20
        self.assertEqual(20, config.connect_timeout)

    def test_SettingAndGettingConnectTimeout_DefaultScenario_SetZeroConnectTimeout(self):
        config = CommunicatorConfiguration()
        config.connect_timeout = 0
        self.assertEqual(0, config.connect_timeout)

    def test_SettingAndGettingSocketTimeout_DefaultScenario_SetAndGetSocketTimeout(self):
        config = CommunicatorConfiguration()
        config.socket_timeout = 60
        self.assertEqual(60, config.socket_timeout)

    def test_SettingAndGettingSocketTimeout_DefaultScenario_SetZeroSocketTimeout(self):
        config = CommunicatorConfiguration()
        config.socket_timeout = 0
        self.assertEqual(0, config.socket_timeout)

    def test_SettingAndGettingMaxConnections_DefaultScenario_SetAndGetMaxConnections(self):
        config = CommunicatorConfiguration()
        config.max_connections = CommunicatorConfiguration.DEFAULT_MAX_CONNECTIONS
        self.assertEqual(CommunicatorConfiguration.DEFAULT_MAX_CONNECTIONS, config.max_connections)

    def test_SettingAndGettingMaxConnections_DefaultScenario_SetCustomMaxConnections(self):
        config = CommunicatorConfiguration()
        config.max_connections = 50
        self.assertEqual(50, config.max_connections)

    def test_SettingAndGettingProxyConfiguration_DefaultScenario_SetAndGetProxyConfiguration(self):
        config = CommunicatorConfiguration()
        proxy = ProxyConfiguration("proxy.example.com", 3128)
        config.proxy_configuration = proxy
        self.assertIs(proxy, config.proxy_configuration)

    def test_SettingAndGettingProxyConfiguration_DefaultScenario_SetNullProxyConfiguration(self):
        config = CommunicatorConfiguration()
        config.proxy_configuration = None
        self.assertIsNone(config.proxy_configuration)

    def test_SettingAndGettingIntegrator_DefaultScenario_SetAndGetIntegrator(self):
        config = CommunicatorConfiguration()
        config.integrator = "MyIntegrator/1.0"
        self.assertEqual("MyIntegrator/1.0", config.integrator)

    def test_SettingAndGettingIntegrator_DefaultScenario_SetNullIntegrator(self):
        config = CommunicatorConfiguration()
        config.integrator = None
        self.assertIsNone(config.integrator)

    def test_SettingAndGettingShoppingCartExtension_DefaultScenario_SetAndGetShoppingCartExtension(self):
        config = CommunicatorConfiguration()
        sce = ShoppingCartExtension("Creator", "Name", "1.0")
        config.shopping_cart_extension = sce
        self.assertIs(sce, config.shopping_cart_extension)

    def test_SettingAndGettingShoppingCartExtension_DefaultScenario_SetNullShoppingCartExtension(self):
        config = CommunicatorConfiguration()
        config.shopping_cart_extension = None
        self.assertIsNone(config.shopping_cart_extension)

    def test_SettingInvalidApiEndpoint_DefaultScenario_ThrowIllegalArgumentExceptionWhenApiEndpointContainsPath(self):
        config = CommunicatorConfiguration()
        with self.assertRaises(ValueError):
            config.api_endpoint = "https://api.example.com/some/path"

    def test_SettingInvalidApiEndpoint_DefaultScenario_ThrowIllegalArgumentExceptionWhenApiEndpointContainsQuery(self):
        config = CommunicatorConfiguration()
        with self.assertRaises(ValueError):
            config.api_endpoint = "https://api.example.com?key=value"

    def test_SettingInvalidApiEndpoint_DefaultScenario_ThrowIllegalArgumentExceptionWhenApiEndpointContainsUserInfo(self):
        config = CommunicatorConfiguration()
        with self.assertRaises(ValueError):
            config.api_endpoint = "https://user:pass@api.example.com"

    def test_SettingInvalidApiEndpoint_DefaultScenario_ThrowIllegalArgumentExceptionWhenApiEndpointContainsFragment(self):
        config = CommunicatorConfiguration()
        with self.assertRaises(ValueError):
            config.api_endpoint = "https://api.example.com#section"


if __name__ == '__main__':
    unittest.main()

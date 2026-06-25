import unittest

from onlinepayments.sdk.proxy_configuration import ProxyConfiguration


class ProxyConfigurationTest(unittest.TestCase):

    def test_ConstructingWith2Parameters_DefaultScenario_CreateInstanceWithHostAndPort(self):
        config = ProxyConfiguration("proxy.example.com", 3128)
        self.assertEqual("http", config.scheme)
        self.assertEqual("proxy.example.com", config.host)
        self.assertEqual(3128, config.port)
        self.assertIsNone(config.username)
        self.assertIsNone(config.password)

    def test_ConstructingWith2Parameters_DefaultScenario_DefaultToHttpScheme(self):
        config = ProxyConfiguration("localhost", 8080)
        self.assertEqual("http", config.scheme)

    def test_ConstructingWith2Parameters_DefaultScenario_DelegateToFullConstructor(self):
        config = ProxyConfiguration("proxy.example.com", 3128)
        self.assertEqual("http", config.scheme)
        self.assertEqual("proxy.example.com", config.host)
        self.assertEqual(3128, config.port)

    def test_ConstructingWith4Parameters_DefaultScenario_CreateInstanceWithCredentials(self):
        config = ProxyConfiguration("proxy.example.com", 3128, username="user", password="pass")
        self.assertEqual("http", config.scheme)
        self.assertEqual("proxy.example.com", config.host)
        self.assertEqual(3128, config.port)
        self.assertEqual("user", config.username)
        self.assertEqual("pass", config.password)

    def test_ConstructingWith4Parameters_DefaultScenario_HandleNullCredentials(self):
        config = ProxyConfiguration("proxy.example.com", 3128, username=None, password=None)
        self.assertIsNone(config.username)
        self.assertIsNone(config.password)

    def test_ConstructingWith4Parameters_DefaultScenario_DelegateToFullConstructor(self):
        config = ProxyConfiguration("proxy.example.com", 3128, username="user", password="pass")
        self.assertEqual("http", config.scheme)
        self.assertEqual("proxy.example.com", config.host)
        self.assertEqual(3128, config.port)
        self.assertEqual("user", config.username)
        self.assertEqual("pass", config.password)

    def test_ConstructingWith3Parameters_DefaultScenario_CreateInstanceWithCustomScheme(self):
        config = ProxyConfiguration("proxy.example.com", 1080, "socks5")
        self.assertEqual("socks5", config.scheme)
        self.assertEqual("proxy.example.com", config.host)
        self.assertEqual(1080, config.port)
        self.assertIsNone(config.username)
        self.assertIsNone(config.password)

    def test_ConstructingWith3Parameters_DefaultScenario_AcceptHttpScheme(self):
        config = ProxyConfiguration("proxy.example.com", 80, "http")
        self.assertEqual("http", config.scheme)
        self.assertEqual("proxy.example.com", config.host)
        self.assertEqual(80, config.port)

    def test_ConstructingWith3Parameters_DefaultScenario_AcceptHttpsScheme(self):
        config = ProxyConfiguration("proxy.example.com", 443, "https")
        self.assertEqual("https", config.scheme)
        self.assertEqual("proxy.example.com", config.host)
        self.assertEqual(443, config.port)

    def test_ConstructingWith3Parameters_DefaultScenario_DelegateToFullConstructor(self):
        config = ProxyConfiguration("proxy.example.com", 443, "https")
        self.assertEqual("https", config.scheme)
        self.assertEqual("proxy.example.com", config.host)
        self.assertEqual(443, config.port)
        self.assertIsNone(config.username)
        self.assertIsNone(config.password)

    def test_ConstructingWith5Parameters_DefaultScenario_CreateFullConfigurationInstance(self):
        config = ProxyConfiguration("proxy.example.com", 3128, "http", "user", "pass")
        self.assertEqual("http", config.scheme)
        self.assertEqual("proxy.example.com", config.host)
        self.assertEqual(3128, config.port)
        self.assertEqual("user", config.username)
        self.assertEqual("pass", config.password)

    def test_ConstructingWith5Parameters_DefaultScenario_ThrowExceptionWhenHostIsNull(self):
        with self.assertRaises(ValueError):
            ProxyConfiguration(None, 3128, "http", "user", "pass")

    def test_ConstructingWith5Parameters_DefaultScenario_ThrowExceptionWhenHostIsEmpty(self):
        with self.assertRaises(ValueError):
            ProxyConfiguration("", 3128, "http", "user", "pass")

    def test_ConstructingWith5Parameters_DefaultScenario_ThrowExceptionWhenPortIsZero(self):
        with self.assertRaises(ValueError):
            ProxyConfiguration("proxy.example.com", 0, "http", "user", "pass")

    def test_ConstructingWith5Parameters_DefaultScenario_ThrowExceptionWhenPortIsNegative(self):
        with self.assertRaises(ValueError):
            ProxyConfiguration("proxy.example.com", -1, "http", "user", "pass")

    def test_ConstructingWith5Parameters_DefaultScenario_ThrowExceptionWhenPortIsGreaterThan65535(self):
        with self.assertRaises(ValueError):
            ProxyConfiguration("proxy.example.com", 65536, "http", "user", "pass")

    def test_ConstructingWith5Parameters_DefaultScenario_AcceptValidPort1(self):
        config = ProxyConfiguration("proxy.example.com", 1, "http", None, None)
        self.assertEqual(1, config.port)

    def test_ConstructingWith5Parameters_DefaultScenario_AcceptValidPort65535(self):
        config = ProxyConfiguration("proxy.example.com", 65535, "http", None, None)
        self.assertEqual(65535, config.port)

    def test_ConstructingWith5Parameters_DefaultScenario_AcceptNullCredentials(self):
        config = ProxyConfiguration("proxy.example.com", 3128, "http", None, None)
        self.assertIsNone(config.username)
        self.assertIsNone(config.password)

    def test_ConstructingFromURI_DefaultScenario_CreateFromHttpURI(self):
        config = ProxyConfiguration.from_uri("http://proxy.example.com:3128")
        self.assertEqual("http", config.scheme)
        self.assertEqual("proxy.example.com", config.host)
        self.assertEqual(3128, config.port)
        self.assertIsNone(config.username)
        self.assertIsNone(config.password)

    def test_ConstructingFromURI_DefaultScenario_CreateFromHttpsURI(self):
        config = ProxyConfiguration.from_uri("https://proxy.example.com:443")
        self.assertEqual("https", config.scheme)
        self.assertEqual("proxy.example.com", config.host)
        self.assertEqual(443, config.port)

    def test_ConstructingFromURI_DefaultScenario_DelegateToURIWithCredentialsConstructor(self):
        config = ProxyConfiguration.from_uri("http://proxy.example.com:3128")
        self.assertEqual("http", config.scheme)
        self.assertEqual("proxy.example.com", config.host)
        self.assertEqual(3128, config.port)

    def test_ConstructingFromURIWithCredentials_DefaultScenario_CreateFromURIWithCredentials(self):
        config = ProxyConfiguration.from_uri("http://proxy.example.com:3128", "user", "pass")
        self.assertEqual("http", config.scheme)
        self.assertEqual("proxy.example.com", config.host)
        self.assertEqual(3128, config.port)
        self.assertEqual("user", config.username)
        self.assertEqual("pass", config.password)

    def test_ConstructingFromURIWithCredentials_DefaultScenario_CreateFromURIWithNullCredentials(self):
        config = ProxyConfiguration.from_uri("https://proxy.example.com:443", None, None)
        self.assertIsNone(config.username)
        self.assertIsNone(config.password)

    def test_ConstructingFromURIWithCredentials_DefaultScenario_HandleURIWithoutExplicitPort(self):
        config = ProxyConfiguration.from_uri("http://proxy.example.com")
        self.assertEqual("http", config.scheme)
        self.assertEqual("proxy.example.com", config.host)
        self.assertEqual(80, config.port)

    def test_ResolvingDefaultPorts_DefaultScenario_DefaultHttpPortTo80(self):
        config = ProxyConfiguration.from_uri("http://proxy.example.com")
        self.assertEqual(80, config.port)

    def test_ResolvingDefaultPorts_DefaultScenario_DefaultHttpsPortTo443(self):
        config = ProxyConfiguration.from_uri("https://proxy.example.com")
        self.assertEqual(443, config.port)

    def test_ResolvingDefaultPorts_DefaultScenario_OverrideDefaultWithExplicitPort(self):
        config = ProxyConfiguration.from_uri("http://proxy.example.com:8080")
        self.assertEqual(8080, config.port)

    def test_HandlingInvalidURISchemes_DefaultScenario_ThrowExceptionForUnsupportedScheme(self):
        with self.assertRaises(ValueError):
            ProxyConfiguration.from_uri("ftp://proxy.example.com")

    def test_SettingAndGettingScheme_DefaultScenario_SetAndGetScheme(self):
        config = ProxyConfiguration("proxy.example.com", 3128)
        config.scheme = "https"
        self.assertEqual("https", config.scheme)

    def test_SettingAndGettingScheme_DefaultScenario_HandleNullSchemeInSetter(self):
        config = ProxyConfiguration("proxy.example.com", 3128)
        config.scheme = None
        self.assertIsNone(config.scheme)

    def test_SettingAndGettingHost_DefaultScenario_SetAndGetHost(self):
        config = ProxyConfiguration("proxy.example.com", 3128)
        config.host = "newproxy.example.com"
        self.assertEqual("newproxy.example.com", config.host)

    def test_SettingAndGettingHost_DefaultScenario_HandleNullHostInSetter(self):
        config = ProxyConfiguration("proxy.example.com", 3128)
        config.host = None
        self.assertIsNone(config.host)

    def test_SettingAndGettingPort_DefaultScenario_SetAndGetPort(self):
        config = ProxyConfiguration("proxy.example.com", 3128)
        config.port = 8080
        self.assertEqual(8080, config.port)

    def test_SettingAndGettingPort_DefaultScenario_SetMinimumValidPort(self):
        config = ProxyConfiguration("proxy.example.com", 3128)
        config.port = 1
        self.assertEqual(1, config.port)

    def test_SettingAndGettingPort_DefaultScenario_SetMaximumValidPort(self):
        config = ProxyConfiguration("proxy.example.com", 3128)
        config.port = 65535
        self.assertEqual(65535, config.port)

    def test_SettingAndGettingUsername_DefaultScenario_SetAndGetUsername(self):
        config = ProxyConfiguration("proxy.example.com", 3128)
        config.username = "proxyuser"
        self.assertEqual("proxyuser", config.username)

    def test_SettingAndGettingUsername_DefaultScenario_HandleNullUsername(self):
        config = ProxyConfiguration("proxy.example.com", 3128, "http", "user", "pass")
        config.username = None
        self.assertIsNone(config.username)

    def test_SettingAndGettingPassword_DefaultScenario_SetAndGetPassword(self):
        config = ProxyConfiguration("proxy.example.com", 3128)
        config.password = "secret"
        self.assertEqual("secret", config.password)

    def test_SettingAndGettingPassword_DefaultScenario_HandleNullPassword(self):
        config = ProxyConfiguration("proxy.example.com", 3128, "http", "user", "pass")
        config.password = None
        self.assertIsNone(config.password)

    def test_StringRepresentation_DefaultScenario_OmitCredentialsWhenPasswordIsNone(self):
        config = ProxyConfiguration("proxy.example.com", 3128, "http", "user", None)
        self.assertEqual("http://proxy.example.com:3128", str(config))

    def test_ConstructingFromURI_DefaultScenario_ExtractCredentialsFromUri(self):
        config = ProxyConfiguration.from_uri("http://uri-user:uri-pass@proxy.example.com:3128")
        self.assertEqual("uri-user", config.username)
        self.assertEqual("uri-pass", config.password)

    def test_ConstructingFromURIWithCredentials_DefaultScenario_ExplicitCredentialsOverrideUri(self):
        config = ProxyConfiguration.from_uri("http://uri-user:uri-pass@proxy.example.com:3128", "arg-user", "arg-pass")
        self.assertEqual("arg-user", config.username)
        self.assertEqual("arg-pass", config.password)


if __name__ == '__main__':
    unittest.main()

import os
from collections.abc import Mapping
from configparser import ConfigParser, NoOptionError
from typing import Any
from urllib.parse import urlparse, ParseResult

from .proxy_configuration import ProxyConfiguration

from onlinepayments.sdk.authentication.authorization_type import AuthorizationType
from onlinepayments.sdk.domain.shopping_cart_extension import ShoppingCartExtension
from onlinepayments.sdk.log.obfuscation_rule import obfuscate_with_fixed_length


_SECTION = "OnlinePaymentsSDK"


# pylint: disable=too-many-instance-attributes
# Necessary to load information from config
class CommunicatorConfiguration:
    """
    Configuration for the communicator.
    """
    # The default number of maximum connections.
    DEFAULT_MAX_CONNECTIONS = 10

    __api_endpoint: ParseResult | None = None
    __connect_timeout: int | None = None
    __socket_timeout: int | None = None
    __max_connections: int | None = DEFAULT_MAX_CONNECTIONS
    __authorization_type: str | None = AuthorizationType.V1HMAC
    __api_key_id: str | None = None
    __secret_api_key: str | None = None
    __proxy_configuration: ProxyConfiguration | None = None
    __integrator: str | None = None
    __shopping_cart_extension: ShoppingCartExtension | None = None

    def __init__(self, properties: ConfigParser | None = None,
                 api_endpoint: str | ParseResult | None = None,
                 api_key_id: str | None = None, secret_api_key: str | None = None,
                 authorization_type: str | None = None,
                 connect_timeout: int | None = None, socket_timeout: int | None = None,
                 max_connections: int | None = None, proxy_configuration: ProxyConfiguration | None = None,
                 integrator: str | None = None, shopping_cart_extension: ShoppingCartExtension | None = None):
        """
        :param properties: a ConfigParser.ConfigParser object containing configuration data
        :param connect_timeout: connection timeout for the network communication in seconds
        :param socket_timeout: socket timeout for the network communication in seconds
        :param max_connections: The maximum number of connections in the connection pool
        """
        if properties is not None:
            if not properties.has_section(_SECTION):
                raise ValueError(f"configuration section '{_SECTION}' is missing")
            self.__api_endpoint = self.__get_endpoint(properties)
            try:
                authorization = properties.get(_SECTION, "onlinePayments.api.authorizationType")
            except NoOptionError:
                authorization = AuthorizationType.V1HMAC
            self.__authorization_type = AuthorizationType.get_authorization(authorization)
            self.__connect_timeout = self.__get_required_int(properties, "onlinePayments.api.connectTimeout")
            self.__socket_timeout = self.__get_required_int(properties, "onlinePayments.api.socketTimeout")
            self.__max_connections = self.__get_property(properties, "onlinePayments.api.maxConnections",
                                                         self.DEFAULT_MAX_CONNECTIONS)
            try:
                proxy_uri = properties.get(_SECTION, "onlinePayments.api.proxy.uri")
            except NoOptionError:
                proxy_uri = None
            try:
                proxy_user = properties.get(_SECTION, "onlinePayments.api.proxy.username")
            except NoOptionError:
                proxy_user = None
            try:
                proxy_pass = properties.get(_SECTION, "onlinePayments.api.proxy.password")
            except NoOptionError:
                proxy_pass = None
            if proxy_uri is not None:
                self.__proxy_configuration = ProxyConfiguration.from_uri(proxy_uri, proxy_user, proxy_pass)
            else:
                self.__proxy_configuration = None
            try:
                self.__integrator = properties.get(_SECTION, "onlinePayments.api.integrator")
            except NoOptionError:
                self.__integrator = None
            try:
                self.__shopping_cart_extension = self.__get_shopping_cart_extension(properties)
            except NoOptionError:
                self.__shopping_cart_extension = None

        if api_endpoint is not None:
            self.api_endpoint = api_endpoint
        if api_key_id is not None:
            self.api_key_id = api_key_id
        if secret_api_key is not None:
            self.secret_api_key = secret_api_key
        if authorization_type is not None:
            self.authorization_type = authorization_type
        if connect_timeout is not None:
            self.connect_timeout = connect_timeout
        if socket_timeout is not None:
            self.socket_timeout = socket_timeout
        if max_connections is not None:
            self.max_connections = max_connections
        if proxy_configuration is not None:
            self.proxy_configuration = proxy_configuration
        if integrator is not None:
            self.integrator = integrator
        if shopping_cart_extension is not None:
            self.shopping_cart_extension = shopping_cart_extension

    @classmethod
    def from_file(cls, configuration_file_name: str | bytes, api_key_id: str | None = None,
                  secret_api_key: str | None = None) -> 'CommunicatorConfiguration':
        """
        Creates a CommunicatorConfiguration from the [OnlinePaymentsSDK] section of the given .ini file.
        Values are read as-is; a % sign does not need to be escaped.

        :raise OSError: if the file cannot be read
        :raise ValueError: if the section or a required option is missing
        """
        properties = ConfigParser(interpolation=None)
        with open(configuration_file_name, encoding="utf-8") as f:
            properties.read_file(f)
        return cls(properties=properties, api_key_id=api_key_id, secret_api_key=secret_api_key)

    @classmethod
    def from_mapping(cls, mapping: Mapping[str, Any], api_key_id: str | None = None,
                     secret_api_key: str | None = None) -> 'CommunicatorConfiguration':
        """
        Creates a CommunicatorConfiguration from a mapping that uses the same property names as the .ini file,
        for example {"onlinePayments.api.endpoint.host": "...", "onlinePayments.api.connectTimeout": 10}.

        :raise ValueError: if a required property is missing
        """
        properties = ConfigParser(interpolation=None)
        properties.read_dict({_SECTION: {key: str(value) for key, value in mapping.items() if value is not None}})
        return cls(properties=properties, api_key_id=api_key_id, secret_api_key=secret_api_key)

    @classmethod
    def from_env(cls, environ: Mapping[str, str] | None = None) -> 'CommunicatorConfiguration':
        """
        Creates a CommunicatorConfiguration from the following environment variables:

        * ONLINEPAYMENTS_API_ENDPOINT (required), for example https://payment.direct.ecom.preprod.worldline-solutions.com
        * ONLINEPAYMENTS_API_KEY_ID (required)
        * ONLINEPAYMENTS_SECRET_API_KEY (required)
        * ONLINEPAYMENTS_INTEGRATOR (required)
        * ONLINEPAYMENTS_CONNECT_TIMEOUT (required, in seconds)
        * ONLINEPAYMENTS_SOCKET_TIMEOUT (required, in seconds)

        :param environ: the environment to read from; defaults to os.environ
        :raise ValueError: if a variable is missing or has an invalid value
        """
        if environ is None:
            environ = os.environ

        def required(name: str) -> str:
            value = environ.get(name)
            if value is None or not value.strip():
                raise ValueError(f"environment variable {name} is required")
            return value.strip()

        def required_int(name: str) -> int:
            value = required(name)
            try:
                return int(value)
            except ValueError:
                raise ValueError(f"environment variable {name} must be an integer, got '{value}'") from None

        return cls(api_endpoint=required("ONLINEPAYMENTS_API_ENDPOINT"),
                   api_key_id=required("ONLINEPAYMENTS_API_KEY_ID"),
                   secret_api_key=required("ONLINEPAYMENTS_SECRET_API_KEY"),
                   integrator=required("ONLINEPAYMENTS_INTEGRATOR"),
                   connect_timeout=required_int("ONLINEPAYMENTS_CONNECT_TIMEOUT"),
                   socket_timeout=required_int("ONLINEPAYMENTS_SOCKET_TIMEOUT"))

    @classmethod
    def __get_required(cls, properties: ConfigParser, key: str) -> str:
        try:
            return properties.get(_SECTION, key)
        except NoOptionError:
            raise ValueError(f"configuration option '{key}' is missing in section '{_SECTION}'") from None

    @classmethod
    def __get_required_int(cls, properties: ConfigParser, key: str) -> int:
        value = cls.__get_required(properties, key)
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"configuration option '{key}' must be an integer, got '{value}'") from None

    @classmethod
    def __get_property(cls, properties: ConfigParser, key: str, default_value: int) -> int:
        try:
            property_value = properties.get(_SECTION, key)
        except NoOptionError:
            property_value = None
        if property_value is not None:
            return int(property_value)
        else:
            return default_value

    def __get_endpoint(self, properties: ConfigParser) -> ParseResult:
        host = self.__get_required(properties, "onlinePayments.api.endpoint.host")
        try:
            scheme = properties.get(_SECTION, "onlinePayments.api.endpoint.scheme")
        except NoOptionError:
            scheme = None
        try:
            port = properties.get(_SECTION, "onlinePayments.api.endpoint.port")
        except NoOptionError:
            port = None
        if scheme:
            if port:
                return self.__create_uri(scheme, host, int(port))
            else:
                return self.__create_uri(scheme, host, -1)
        elif port:
            return self.__create_uri("https", host, int(port))
        else:
            return self.__create_uri("https", host, -1)

    @staticmethod
    def __create_uri(scheme: str, host: str, port: int) -> ParseResult:
        if port != -1:
            uri = scheme + "://" + host + ":" + str(port)
        else:
            uri = scheme + "://" + host
        url = urlparse(uri)
        if url.scheme.lower() not in ["http", "https"] or not url.netloc:
            raise ValueError("Unable to construct endpoint URI")
        return url

    @staticmethod
    def __get_shopping_cart_extension(properties: ConfigParser) -> ShoppingCartExtension | None:
        try:
            creator = properties.get(_SECTION, "onlinePayments.api.shoppingCartExtension.creator")
        except NoOptionError:
            creator = None
        try:
            name = properties.get(_SECTION, "onlinePayments.api.shoppingCartExtension.name")
        except NoOptionError:
            name = None
        try:
            version = properties.get(_SECTION, "onlinePayments.api.shoppingCartExtension.version")
        except NoOptionError:
            version = None
        try:
            extension_id = properties.get(_SECTION, "onlinePayments.api.shoppingCartExtension.extensionId")
        except NoOptionError:
            extension_id = None
        if creator is None and name is None and version is None and extension_id is None:
            return None
        if creator is None:
            raise ValueError("creator is required")
        if name is None:
            raise ValueError("name is required")
        if version is None:
            raise ValueError("version is required")
        return ShoppingCartExtension(creator, name, version, extension_id)

    @property
    def api_endpoint(self) -> ParseResult | None:
        """
        The Online Payments platform API endpoint URI.
        """
        return self.__api_endpoint

    @api_endpoint.setter
    def api_endpoint(self, api_endpoint: str | ParseResult | None) -> None:
        if isinstance(api_endpoint, str):
            api_endpoint = urlparse(str(api_endpoint))
        if api_endpoint is not None and \
                (api_endpoint.scheme.lower() not in ["http", "https"] or not api_endpoint.netloc):
            raise ValueError("api_endpoint must be an absolute http or https URL")
        if api_endpoint is not None and api_endpoint.path:
            raise ValueError("apiEndpoint should not contain a path")
        if api_endpoint is not None and \
                (api_endpoint.username is not None or api_endpoint.query or api_endpoint.fragment):
            raise ValueError("apiEndpoint should not contain user info, query or fragment")
        self.__api_endpoint = api_endpoint

    @property
    def api_key_id(self) -> str | None:
        """
        An identifier for the secret API key. The api_key_id can be
        retrieved from the Configuration Center. This identifier is visible in
        the HTTP request and is also used to identify the correct account.
        """
        return self.__api_key_id

    @api_key_id.setter
    def api_key_id(self, api_key_id: str | None) -> None:
        self.__api_key_id = api_key_id

    @property
    def secret_api_key(self) -> str | None:
        """
        A shared secret. The shared secret can be retrieved from the
        Configuration Center. An api_key_id and secret_api_key always go
        hand-in-hand, the difference is that secret_api_key is never visible in
        the HTTP request. This secret is used as input for the HMAC algorithm.
        """
        return self.__secret_api_key

    @secret_api_key.setter
    def secret_api_key(self, secret_api_key: str | None) -> None:
        self.__secret_api_key = secret_api_key

    @property
    def authorization_type(self) -> str | None:
        return self.__authorization_type

    @authorization_type.setter
    def authorization_type(self, authorization_type: str | None) -> None:
        self.__authorization_type = authorization_type

    @property
    def connect_timeout(self) -> int | None:
        """Connection timeout for the underlying network communication in seconds"""
        return self.__connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout: int | None) -> None:
        self.__connect_timeout = connect_timeout

    @property
    def socket_timeout(self) -> int | None:
        """Socket timeout for the underlying network communication in seconds"""
        return self.__socket_timeout

    @socket_timeout.setter
    def socket_timeout(self, socket_timeout: int | None) -> None:
        self.__socket_timeout = socket_timeout

    @property
    def max_connections(self) -> int | None:
        return self.__max_connections

    @max_connections.setter
    def max_connections(self, max_connections: int | None) -> None:
        self.__max_connections = max_connections

    @property
    def proxy_configuration(self) -> ProxyConfiguration | None:
        return self.__proxy_configuration

    @proxy_configuration.setter
    def proxy_configuration(self, proxy_configuration: ProxyConfiguration | None) -> None:
        self.__proxy_configuration = proxy_configuration

    @property
    def integrator(self) -> str | None:
        return self.__integrator

    @integrator.setter
    def integrator(self, integrator: str | None) -> None:
        self.__integrator = integrator

    @property
    def shopping_cart_extension(self) -> ShoppingCartExtension | None:
        return self.__shopping_cart_extension

    @shopping_cart_extension.setter
    def shopping_cart_extension(self, shopping_cart_extension: ShoppingCartExtension | None) -> None:
        self.__shopping_cart_extension = shopping_cart_extension

    def __repr__(self):
        obfuscate = obfuscate_with_fixed_length(8)
        api_endpoint = self.api_endpoint.geturl() if self.api_endpoint is not None else None
        api_key_id = obfuscate(self.api_key_id) if self.api_key_id is not None else None
        secret_api_key = obfuscate(self.secret_api_key) if self.secret_api_key is not None else None
        return (f"CommunicatorConfiguration(api_endpoint={api_endpoint!r}, api_key_id={api_key_id!r}, "
                f"secret_api_key={secret_api_key!r}, authorization_type={self.authorization_type!r}, "
                f"connect_timeout={self.connect_timeout!r}, socket_timeout={self.socket_timeout!r}, "
                f"max_connections={self.max_connections!r}, proxy_configuration={self.proxy_configuration!r}, "
                f"integrator={self.integrator!r}, shopping_cart_extension={self.shopping_cart_extension!r})")

from typing import Union
from urllib.parse import ParseResult, ParseResultBytes, urlparse

from onlinepayments.sdk.domain.shopping_cart_extension import ShoppingCartExtension
from onlinepayments.sdk.proxy_configuration import ProxyConfiguration


class EndpointConfiguration:
    """
    Base class for endpoint configurations.
    """
    # The default number of maximum connections.
    DEFAULT_CONNECT_TIMEOUT = 5
    DEFAULT_SOCKET_TIMEOUT = 300
    DEFAULT_MAX_CONNECTIONS = 10

    def __init__(self, properties=None, prefix=None):
        if properties and properties.sections() and properties.options("OnlinePaymentsSDK"):
            self.__endpoint = self.__get_endpoint(properties, prefix)
            self.__connect_timeout = int(properties.get("OnlinePaymentsSDK", prefix + ".connectTimeout", fallback=self.DEFAULT_CONNECT_TIMEOUT))
            self.__socket_timeout = int(properties.get("OnlinePaymentsSDK", prefix + ".socketTimeout", fallback=self.DEFAULT_SOCKET_TIMEOUT))
            self.__max_connections = int(properties.get("OnlinePaymentsSDK", prefix + ".maxConnections", fallback=self.DEFAULT_MAX_CONNECTIONS))
            proxy_uri = properties.get("OnlinePaymentsSDK", prefix + ".proxy.uri", fallback=None)
            if proxy_uri is None:
                self.__proxy_configuration = None
            else:
                self.__proxy_configuration = ProxyConfiguration.from_uri(
                    proxy_uri,
                    properties.get("OnlinePaymentsSDK", prefix + ".proxy.username", fallback=None),
                    properties.get("OnlinePaymentsSDK", prefix + ".proxy.password", fallback=None))
            self.__integrator = properties.get("OnlinePaymentsSDK", prefix + ".integrator", fallback=None)
            self.__shopping_cart_extension = self.__get_shopping_cart_extension(properties, prefix)

    def __get_endpoint(self, properties, prefix):
        host = properties.get("OnlinePaymentsSDK", prefix + ".endpoint.host")
        scheme = properties.get("OnlinePaymentsSDK", prefix + ".endpoint.scheme", fallback="https")
        port = int(properties.get("OnlinePaymentsSDK", prefix + ".endpoint.port", fallback=-1))
        return self.__create_uri(scheme, host, port)

    @staticmethod
    def __create_uri(scheme, host, port):
        if port != -1:
            uri = scheme + "://" + host + ":" + str(port)
        else:
            uri = scheme + "://" + host
        url = urlparse(uri)
        if not url.scheme.lower() in ["http", "https"] or not url.netloc:
            raise ValueError("Unable to construct endpoint URI")
        return url

    @staticmethod
    def __get_shopping_cart_extension(properties, prefix):
        creator = properties.get("OnlinePaymentsSDK", prefix + ".shoppingCartExtension.creator", fallback=None)
        name = properties.get("OnlinePaymentsSDK", prefix + ".shoppingCartExtension.name", fallback=None)
        version = properties.get("OnlinePaymentsSDK", prefix + ".shoppingCartExtension.version", fallback=None)
        extension_id = properties.get("OnlinePaymentsSDK", prefix + ".shoppingCartExtension.extensionId", fallback=None)
        if creator is None and name is None and version is None and extension_id is None:
            return None
        else:
            return ShoppingCartExtension(creator, name, version, extension_id)

    @property
    def _endpoint(self) -> Union[ParseResult, ParseResultBytes]:
        return self.__endpoint

    def _set_endpoint(self, endpoint: Union[str, ParseResult, ParseResultBytes]):
        if isinstance(endpoint, str):
            endpoint = urlparse(str(endpoint))
        if endpoint is not None and endpoint.path:
            raise ValueError("apiEndpoint should not contain a path")
        if endpoint is not None and (
                endpoint.username is not None or
                endpoint.query or endpoint.fragment):
            raise ValueError(
                "apiEndpoint should not contain user info, query or fragment")
        self.__endpoint = endpoint

    @property
    def connect_timeout(self) -> int:
        """Connection timeout for the underlying network communication in seconds"""
        return self.__connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout: int):
        self.__connect_timeout = connect_timeout

    @property
    def socket_timeout(self) -> int:
        """Socket timeout for the underlying network communication in seconds"""
        return self.__socket_timeout

    @socket_timeout.setter
    def socket_timeout(self, socket_timeout: int):
        self.__socket_timeout = socket_timeout

    @property
    def max_connections(self) -> int:
        return self.__max_connections

    @max_connections.setter
    def max_connections(self, max_connections: int):
        self.__max_connections = max_connections

    @property
    def proxy_configuration(self) -> ProxyConfiguration:
        return self.__proxy_configuration

    @proxy_configuration.setter
    def proxy_configuration(self, proxy_configuration: ProxyConfiguration):
        self.__proxy_configuration = proxy_configuration

    @property
    def integrator(self) -> str:
        return self.__integrator

    @integrator.setter
    def integrator(self, integrator: str):
        self.__integrator = integrator

    @property
    def shopping_cart_extension(self) -> ShoppingCartExtension:
        return self.__shopping_cart_extension

    @shopping_cart_extension.setter
    def shopping_cart_extension(self, shopping_cart_extension: ShoppingCartExtension):
        self.__shopping_cart_extension = shopping_cart_extension

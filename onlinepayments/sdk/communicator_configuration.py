from typing import Union
from urllib.parse import ParseResult, ParseResultBytes

from onlinepayments.sdk.defaultimpl.authorization_type import AuthorizationType
from onlinepayments.sdk.domain.shopping_cart_extension import ShoppingCartExtension
from onlinepayments.sdk.endpoint_configuration import EndpointConfiguration
# pylint: disable=too-many-instance-attributes
# Necessary to load information from config
from onlinepayments.sdk.proxy_configuration import ProxyConfiguration


class CommunicatorConfiguration(EndpointConfiguration):
    """
    Configuration for the communicator.

    :param properties: a ConfigParser.ConfigParser object containing configuration data
    :param connect_timeout: connection timeout for the network communication in seconds
    :param socket_timeout: socket timeout for the network communication in seconds
    :param max_connections: The maximum number of connections in the connection pool
    """
    __api_key_id = None
    __secret_api_key = None

    def __init__(self,
                 properties=None,
                 api_endpoint: Union[str, ParseResult, ParseResultBytes] = None,
                 api_key_id: str = None,
                 secret_api_key: str = None,
                 authorization_type: str = None,
                 connect_timeout: int = None,
                 socket_timeout: int = None,
                 max_connections: int = None,
                 proxy_configuration: ProxyConfiguration = None,
                 integrator: str = None,
                 shopping_cart_extension: ShoppingCartExtension = None):
        if properties:
            super(CommunicatorConfiguration, self).__init__(properties, "onlinePayments.api")
            if properties.sections() and properties.options("OnlinePaymentsSDK"):
                authorization = properties.get("OnlinePaymentsSDK", "onlinePayments.api.authorizationType", fallback=AuthorizationType.V1HMAC)
                self.__authorization_type = AuthorizationType.get_authorization(authorization)
        if api_endpoint is not None:
            self.api_endpoint = api_endpoint
        if api_key_id is not None:
            self.api_key_id = api_key_id
        if secret_api_key is not None:
            self.secret_api_key = secret_api_key
        if authorization_type is not None:
            self.__authorization_type = AuthorizationType.get_authorization(authorization_type)
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

    @property
    def api_endpoint(self) -> Union[ParseResult, ParseResultBytes]:
        """
        The Online Payments platform API endpoint URI.
        """
        return super(CommunicatorConfiguration, self)._endpoint

    @api_endpoint.setter
    def api_endpoint(self, api_endpoint: Union[str, ParseResult, ParseResultBytes]):
        super(CommunicatorConfiguration, self)._set_endpoint(api_endpoint)

    @property
    def api_key_id(self) -> str:
        """
        An identifier for the secret API key. The api_key_id can be
        retrieved from the Configuration Center. This identifier is visible in
        the HTTP request and is also used to identify the correct account.
        """
        return self.__api_key_id

    @api_key_id.setter
    def api_key_id(self, api_key_id: str):
        self.__api_key_id = api_key_id

    @property
    def secret_api_key(self) -> str:
        """
        A shared secret. The shared secret can be retrieved from the
        Configuration Center. An api_key_id and secret_api_key always go
        hand-in-hand, the difference is that secret_api_key is never visible in
        the HTTP request. This secret is used as input for the HMAC algorithm.
        """
        return self.__secret_api_key

    @secret_api_key.setter
    def secret_api_key(self, secret_api_key: str):
        self.__secret_api_key = secret_api_key

    @property
    def authorization_type(self) -> str:
        return self.__authorization_type

    @authorization_type.setter
    def authorization_type(self, authorization_type: str):
        self.__authorization_type = AuthorizationType.get_authorization(authorization_type)

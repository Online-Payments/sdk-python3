from urllib.parse import ParseResult

from .client import Client
from .i_client import IClient
from .communicator import Communicator
from .i_communicator import ICommunicator
from .communicator_configuration import CommunicatorConfiguration
from .proxy_configuration import ProxyConfiguration

from onlinepayments.sdk.authentication.authorization_type import AuthorizationType
from onlinepayments.sdk.authentication.authenticator import Authenticator
from onlinepayments.sdk.authentication.v1hmac_authenticator import V1HmacAuthenticator
from onlinepayments.sdk.communication.connection import Connection
from onlinepayments.sdk.communication.default_connection import DefaultConnection
from onlinepayments.sdk.communication.metadata_provider import MetadataProvider
from onlinepayments.sdk.communication.i_metadata_provider import IMetadataProvider
from onlinepayments.sdk.domain.shopping_cart_extension import ShoppingCartExtension
from onlinepayments.sdk.json.default_marshaller import DefaultMarshaller
from onlinepayments.sdk.json.marshaller import Marshaller


class Factory:
    """
    Online Payments platform factory for several SDK components.

    Create the client once with create_client_from_configuration and reuse it.

    AI coding agents: read the agent skill for this SDK version before writing integration code:
    https://raw.githubusercontent.com/Online-Payments/sdk-python3/12.0.0/onlinepayments/sdk/skills/online-payments/SKILL.md
    The same skill is included in this package, in the onlinepayments/sdk/skills/online-payments/ folder.
    """

    @staticmethod
    def create_configuration(configuration_file_name: str | bytes, api_key_id: str, secret_api_key: str) -> CommunicatorConfiguration:
        """
        Creates a CommunicatorConfiguration based on the configuration values in configuration_file_name, api_key_id and secret_api_key.
        """
        try:
            return CommunicatorConfiguration.from_file(configuration_file_name,
                                                       api_key_id=api_key_id,
                                                       secret_api_key=secret_api_key)
        except OSError as e:
            raise RuntimeError(f"Unable to read configuration located at {e.filename}", e) from e

    @staticmethod
    def create_communicator_from_configuration(communicator_configuration: CommunicatorConfiguration,
                                               metadata_provider: IMetadataProvider | None = None,
                                               connection: Connection | None = None,
                                               authenticator: Authenticator | None = None,
                                               marshaller: Marshaller | None = None) -> ICommunicator:
        """
        Creates a Communicator based on the configuration stored in the CommunicatorConfiguration argument
        """
        if metadata_provider is None:
            metadata_provider = MetadataProvider(integrator=communicator_configuration.integrator,
                                                 shopping_cart_extension=communicator_configuration.shopping_cart_extension)
        if connection is None:
            if communicator_configuration.connect_timeout is None:
                raise ValueError("connect_timeout is required")
            if communicator_configuration.socket_timeout is None:
                raise ValueError("socket_timeout is required")
            if communicator_configuration.max_connections is None:
                raise ValueError("max_connections is required")
            connection = DefaultConnection(communicator_configuration.connect_timeout,
                                           communicator_configuration.socket_timeout,
                                           communicator_configuration.max_connections,
                                           communicator_configuration.proxy_configuration)
        if authenticator is None:
            authenticator = Factory.__get_authenticator(communicator_configuration)
        if marshaller is None:
            marshaller = DefaultMarshaller.instance()
        if communicator_configuration.api_endpoint is None:
            raise ValueError("api_endpoint is required")
        return Communicator(api_endpoint=communicator_configuration.api_endpoint,
                            metadata_provider=metadata_provider,
                            connection=connection,
                            authenticator=authenticator,
                            marshaller=marshaller)

    @staticmethod
    def __get_authenticator(communicator_configuration: CommunicatorConfiguration) -> Authenticator:
        if communicator_configuration.authorization_type is None:
            raise ValueError("authorization_type is required")
        if communicator_configuration.authorization_type == AuthorizationType.V1HMAC:
            return V1HmacAuthenticator(communicator_configuration)
        raise RuntimeError("Unknown authorizationType " + communicator_configuration.authorization_type)

    @staticmethod
    def create_communicator_from_file(configuration_file_name: str | bytes, api_key_id: str, secret_api_key: str,
                                      metadata_provider: IMetadataProvider | None = None,
                                      connection: Connection | None = None,
                                      authenticator: Authenticator | None = None,
                                      marshaller: Marshaller | None = None) -> ICommunicator:
        """
        Creates a Communicator based on the configuration values in configuration_file_name, api_id_key and secret_api_key.
        """
        configuration = Factory.create_configuration(configuration_file_name, api_key_id, secret_api_key)
        return Factory.create_communicator_from_configuration(configuration,
                                                              metadata_provider=metadata_provider,
                                                              connection=connection,
                                                              authenticator=authenticator,
                                                              marshaller=marshaller)

    @staticmethod
    def create_client_from_configuration(communicator_configuration: CommunicatorConfiguration,
                                         metadata_provider: IMetadataProvider | None = None,
                                         connection: Connection | None = None,
                                         authenticator: Authenticator | None = None,
                                         marshaller: Marshaller | None = None) -> IClient:
        """
        Create a Client based on the configuration stored in the CommunicatorConfiguration argument
        """
        communicator = Factory.create_communicator_from_configuration(communicator_configuration,
                                                                      metadata_provider=metadata_provider,
                                                                      connection=connection,
                                                                      authenticator=authenticator,
                                                                      marshaller=marshaller)
        return Client(communicator)

    @staticmethod
    def create_client_from_communicator(communicator: ICommunicator) -> IClient:
        """
        Create a Client based on the settings stored in the Communicator argument
        """
        return Client(communicator)

    @staticmethod
    def create_client_from_file(configuration_file_name: str | bytes, api_key_id: str, secret_api_key: str,
                                metadata_provider: IMetadataProvider | None = None,
                                connection: Connection | None = None,
                                authenticator: Authenticator | None = None,
                                marshaller: Marshaller | None = None) -> IClient:
        """
        Creates a Client based on the configuration values in configuration_file_name, api_key_id and secret_api_key.
        """
        communicator = Factory.create_communicator_from_file(configuration_file_name, api_key_id, secret_api_key,
                                                             metadata_provider=metadata_provider,
                                                             connection=connection,
                                                             authenticator=authenticator,
                                                             marshaller=marshaller)
        return Client(communicator)

    @staticmethod
    def create_client(*, api_endpoint: str | ParseResult, api_key_id: str, secret_api_key: str, integrator: str,
                      connect_timeout: int, socket_timeout: int,
                      max_connections: int = CommunicatorConfiguration.DEFAULT_MAX_CONNECTIONS,
                      proxy_configuration: ProxyConfiguration | None = None,
                      shopping_cart_extension: ShoppingCartExtension | None = None,
                      metadata_provider: IMetadataProvider | None = None,
                      connection: Connection | None = None,
                      authenticator: Authenticator | None = None,
                      marshaller: Marshaller | None = None) -> IClient:
        """
        Creates a Client based on the given configuration values. All arguments must be passed by name.

        :param connect_timeout: connection timeout for the network communication in seconds
        :param socket_timeout: socket timeout for the network communication in seconds
        :raise ValueError: if a required value is missing or invalid
        """
        configuration = CommunicatorConfiguration(api_endpoint=api_endpoint,
                                                  api_key_id=api_key_id,
                                                  secret_api_key=secret_api_key,
                                                  authorization_type=AuthorizationType.V1HMAC,
                                                  connect_timeout=connect_timeout,
                                                  socket_timeout=socket_timeout,
                                                  max_connections=max_connections,
                                                  proxy_configuration=proxy_configuration,
                                                  integrator=integrator,
                                                  shopping_cart_extension=shopping_cart_extension)
        return Factory.create_client_from_configuration(configuration,
                                                        metadata_provider=metadata_provider,
                                                        connection=connection,
                                                        authenticator=authenticator,
                                                        marshaller=marshaller)

    @staticmethod
    def create_client_from_env(*, max_connections: int = CommunicatorConfiguration.DEFAULT_MAX_CONNECTIONS,
                               proxy_configuration: ProxyConfiguration | None = None,
                               shopping_cart_extension: ShoppingCartExtension | None = None,
                               metadata_provider: IMetadataProvider | None = None,
                               connection: Connection | None = None,
                               authenticator: Authenticator | None = None,
                               marshaller: Marshaller | None = None) -> IClient:
        """
        Creates a Client based on environment variables. All arguments must be passed by name.
        See CommunicatorConfiguration.from_env for the environment variables that are read.

        :raise ValueError: if an environment variable is missing or has an invalid value
        """
        configuration = CommunicatorConfiguration.from_env()
        configuration.max_connections = max_connections
        configuration.proxy_configuration = proxy_configuration
        configuration.shopping_cart_extension = shopping_cart_extension
        return Factory.create_client_from_configuration(configuration,
                                                        metadata_provider=metadata_provider,
                                                        connection=connection,
                                                        authenticator=authenticator,
                                                        marshaller=marshaller)

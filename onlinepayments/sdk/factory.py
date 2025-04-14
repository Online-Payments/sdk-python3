from configparser import ConfigParser
from typing import Optional, Union

from .client import Client
from .i_client import IClient
from .communicator import Communicator
from .i_communicator import ICommunicator
from .communicator_configuration import CommunicatorConfiguration

from onlinepayments.sdk.authentication.authorization_type import AuthorizationType
from onlinepayments.sdk.authentication.authenticator import Authenticator
from onlinepayments.sdk.authentication.v1hmac_authenticator import V1HmacAuthenticator
from onlinepayments.sdk.communication.connection import Connection
from onlinepayments.sdk.communication.default_connection import DefaultConnection
from onlinepayments.sdk.communication.metadata_provider import MetadataProvider
from onlinepayments.sdk.communication.i_metadata_provider import IMetadataProvider
from onlinepayments.sdk.json.default_marshaller import DefaultMarshaller
from onlinepayments.sdk.json.marshaller import Marshaller


class Factory(object):
    """
    Online Payments platform factory for several SDK components.
    """

    @staticmethod
    def create_configuration(configuration_file_name: Union[str, bytes], api_key_id: str, secret_api_key: str) -> CommunicatorConfiguration:
        """
        Creates a CommunicatorConfiguration based on the configuration values in configuration_file_name, api_key_id and secret_api_key.
        """
        try:
            parser = ConfigParser()
            with open(configuration_file_name) as f:
                parser.read_file(f)
            return CommunicatorConfiguration(properties=parser,
                                             api_key_id=api_key_id,
                                             secret_api_key=secret_api_key)
        except IOError as e:
            raise RuntimeError("Unable to read configuration located at {}".format(e.filename), e) from e

    @staticmethod
    def create_communicator_from_configuration(communicator_configuration: CommunicatorConfiguration,
                                               metadata_provider: Optional[IMetadataProvider] = None,
                                               connection: Optional[Connection] = None,
                                               authenticator: Optional[Authenticator] = None,
                                               marshaller: Optional[Marshaller] = None) -> ICommunicator:
        """
        Creates a Communicator based on the configuration stored in the CommunicatorConfiguration argument
        """
        if metadata_provider is None:
            metadata_provider = MetadataProvider(integrator=communicator_configuration.integrator,
                                                 shopping_cart_extension=communicator_configuration.shopping_cart_extension)
        if connection is None:
            connection = DefaultConnection(communicator_configuration.connect_timeout,
                                           communicator_configuration.socket_timeout,
                                           communicator_configuration.max_connections,
                                           communicator_configuration.proxy_configuration)
        if authenticator is None:
            authenticator = Factory.__get_authenticator(communicator_configuration)
        if marshaller is None:
            marshaller = DefaultMarshaller.instance()
        return Communicator(api_endpoint=communicator_configuration.api_endpoint,
                            metadata_provider=metadata_provider,
                            connection=connection,
                            authenticator=authenticator,
                            marshaller=marshaller)

    @staticmethod
    def __get_authenticator(communicator_configuration: CommunicatorConfiguration) -> Authenticator:
        if communicator_configuration.authorization_type == AuthorizationType.V1HMAC:
            return V1HmacAuthenticator(communicator_configuration)
        raise RuntimeError("Unknown authorizationType " + communicator_configuration.authorization_type)

    @staticmethod
    def create_communicator_from_file(configuration_file_name: Union[str, bytes], api_key_id: str, secret_api_key: str,
                                      metadata_provider: Optional[IMetadataProvider] = None,
                                      connection: Optional[Connection] = None,
                                      authenticator: Optional[Authenticator] = None,
                                      marshaller: Optional[Marshaller] = None) -> ICommunicator:
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
                                         metadata_provider: Optional[IMetadataProvider] = None,
                                         connection: Optional[Connection] = None,
                                         authenticator: Optional[Authenticator] = None,
                                         marshaller: Optional[Marshaller] = None) -> IClient:
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
    def create_client_from_file(configuration_file_name: Union[str, bytes], api_key_id: str, secret_api_key: str,
                                metadata_provider: Optional[IMetadataProvider] = None,
                                connection: Optional[Connection] = None,
                                authenticator: Optional[Authenticator] = None,
                                marshaller: Optional[Marshaller] = None) -> IClient:
        """
        Creates a Client based on the configuration values in configuration_file_name, api_key_id and secret_api_key.
        """
        communicator = Factory.create_communicator_from_file(configuration_file_name, api_key_id, secret_api_key,
                                                             metadata_provider=metadata_provider,
                                                             connection=connection,
                                                             authenticator=authenticator,
                                                             marshaller=marshaller)
        return Client(communicator)

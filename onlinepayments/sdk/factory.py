from configparser import ConfigParser

from onlinepayments.sdk.client import Client
from onlinepayments.sdk.communicator import Communicator
from onlinepayments.sdk.communicator_configuration import CommunicatorConfiguration
from onlinepayments.sdk.defaultimpl.default_authenticator import DefaultAuthenticator
from onlinepayments.sdk.defaultimpl.default_connection import DefaultConnection
from onlinepayments.sdk.defaultimpl.default_marshaller import DefaultMarshaller
from onlinepayments.sdk.i_client import IClient
from onlinepayments.sdk.meta_data_provider import MetaDataProvider


class Factory:
    """
    Online Payments platform factory for several SDK components.
    """

    @staticmethod
    def create_configuration(configuration_file_name, api_key_id, secret_api_key) -> CommunicatorConfiguration:
        """
        Creates a CommunicatorConfiguration based on the configuration
        values in configuration_file_name, api_key_id and secret_api_key.
        """
        parser = ConfigParser()
        try:
            parser.read(configuration_file_name)
            with open(configuration_file_name) as f:
                parser.read_file(f)
            return CommunicatorConfiguration(
                properties=parser,
                api_key_id=api_key_id,
                secret_api_key=secret_api_key)
        except IOError as e:
            raise RuntimeError("Unable to read configuration located at {}".format(e.filename), e)

    @staticmethod
    def create_communicator_from_configuration(communicator_configuration,
                                               meta_data_provider=None,
                                               connection=None,
                                               authenticator=None,
                                               marshaller=DefaultMarshaller.INSTANCE()) -> Communicator:
        """
        Creates a Communicator based on the configuration stored in the CommunicatorConfiguration argument
        """
        # If an authenticator is not given, api_key_id and secret_api_key are
        # used to create a DefaultAuthenticator used to create the communicator.
        if connection is None:
            connection = DefaultConnection(
                connect_timeout=communicator_configuration.connect_timeout,
                socket_timeout=communicator_configuration.socket_timeout,
                max_connections=communicator_configuration.max_connections,
                proxy_configuration=communicator_configuration.proxy_configuration)
        if authenticator is None:
            authenticator = DefaultAuthenticator(
                api_key_id=communicator_configuration.api_key_id,
                secret_api_key=communicator_configuration.secret_api_key,
                authorization_type=communicator_configuration.authorization_type)
        if meta_data_provider is None:
            meta_data_provider = MetaDataProvider(
                integrator=communicator_configuration.integrator,
                shopping_cart_extension=communicator_configuration.shopping_cart_extension)
        return Communicator(
            api_endpoint=communicator_configuration.api_endpoint,
            authenticator=authenticator,
            connection=connection,
            meta_data_provider=meta_data_provider,
            marshaller=marshaller)

    @staticmethod
    def create_communicator_from_file(configuration_file_name,
                                      api_key_id,
                                      secret_api_key,
                                      meta_data_provider=None,
                                      connection=None,
                                      authenticator=None,
                                      marshaller=DefaultMarshaller.INSTANCE()) -> Communicator:
        """
        Creates a Communicator based on the configuration values in configuration_file_name, api_id_key and secret_api_key.
        """
        configuration = Factory.create_configuration(configuration_file_name, api_key_id, secret_api_key)
        return Factory.create_communicator_from_configuration(configuration, meta_data_provider, connection, authenticator, marshaller)

    @staticmethod
    def create_client_from_configuration(communicator_configuration) -> IClient:
        """
        Create a Client based on the configuration stored in the CommunicatorConfiguration argument
        """
        communicator = Factory.create_communicator_from_configuration(communicator_configuration)
        return Client(communicator)

    @staticmethod
    def create_client_from_communicator(communicator) -> IClient:
        """
        Create a Client based on the settings stored in the Communicator argument
        """
        return Client(communicator)

    @staticmethod
    def create_client_from_file(configuration_file_name,
                                api_key_id,
                                secret_api_key,
                                meta_data_provider=None,
                                connection=None,
                                authenticator=None,
                                marshaller=DefaultMarshaller.INSTANCE()) -> IClient:
        """
        Creates a Client based on the configuration values in configuration_file_name, api_key_id and secret_api_key.
        """
        communicator = Factory.create_communicator_from_file(
            configuration_file_name,
            api_key_id,
            secret_api_key,
            meta_data_provider,
            connection,
            authenticator,
            marshaller)
        return Client(communicator)

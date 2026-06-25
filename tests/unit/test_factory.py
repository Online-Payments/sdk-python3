import os
import unittest
import warnings
from unittest.mock import MagicMock

from onlinepayments.sdk.factory import Factory
from onlinepayments.sdk.authentication.authorization_type import AuthorizationType
from onlinepayments.sdk.authentication.v1hmac_authenticator import V1HmacAuthenticator
from onlinepayments.sdk.client import Client
from onlinepayments.sdk.communication.connection import Connection
from onlinepayments.sdk.communication.default_connection import DefaultConnection
from onlinepayments.sdk.communication.metadata_provider import MetadataProvider
from onlinepayments.sdk.json.default_marshaller import DefaultMarshaller
from onlinepayments.sdk.json.marshaller import Marshaller

PROPERTIES_URI = os.path.abspath(os.path.join(__file__, os.pardir, "../resources/configuration.v1hmac.ini"))
INVALID_PROPERTIES_URI = "/nonexistent/path/configuration.ini"
API_KEY_ID = "someKey"
SECRET_API_KEY = "someSecret"


class FactoryTest(unittest.TestCase):

    def test_CreateConfigurationIsCalled_ValidPropertiesUri_ReturnExpectedConfiguration(self):
        configuration = Factory.create_configuration(PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY)
        self.assertIsNotNone(configuration.api_endpoint)
        self.assertEqual("https", configuration.api_endpoint.scheme)
        self.assertIn("worldline", configuration.api_endpoint.netloc)
        self.assertEqual(AuthorizationType.get_authorization("v1HMAC"), configuration.authorization_type)
        self.assertEqual(1000, configuration.connect_timeout)
        self.assertEqual(1000, configuration.socket_timeout)
        self.assertEqual(100, configuration.max_connections)
        self.assertEqual(API_KEY_ID, configuration.api_key_id)
        self.assertEqual(SECRET_API_KEY, configuration.secret_api_key)
        self.assertIsNone(configuration.proxy_configuration)

    def test_CreateConfigurationIsCalled_InvalidPropertiesUri_ThrowRuntimeException(self):
        with self.assertRaises(RuntimeError):
            Factory.create_configuration(INVALID_PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY)

    def test_CreateCommunicatorBuilderIsCalled_ValidPropertiesUri_ReturnBuilderWithExpectedConfiguration(self):
        communicator = Factory.create_communicator_from_file(PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY)

        self.assertIs(communicator.marshaller, DefaultMarshaller.instance())

        connection = communicator._Communicator__connection
        self.assertIsInstance(connection, DefaultConnection)
        self.assertEqual(1000, connection.connect_timeout)
        self.assertEqual(1000, connection.socket_timeout)
        session = connection._DefaultConnection__requests_session
        self.assertEqual(100, session.get_adapter("http://")._pool_maxsize)
        self.assertEqual(100, session.get_adapter("https://")._pool_maxsize)
        self.assertFalse(session.proxies)

        authenticator = communicator._Communicator__authenticator
        self.assertIsInstance(authenticator, V1HmacAuthenticator)

        metadata_provider = communicator._Communicator__metadata_provider
        self.assertIsInstance(metadata_provider, MetadataProvider)
        request_headers = metadata_provider.metadata_headers
        self.assertEqual(1, len(request_headers))
        self.assertEqual("X-GCS-ServerMetaInfo", request_headers[0].name)

    def test_CreateCommunicatorFromFileIsCalled_ValidPropertiesUri_ReturnCommunicatorWithV1HmacAuthenticator(self):
        communicator = Factory.create_communicator_from_file(PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY)

        authenticator = communicator._Communicator__authenticator
        self.assertIsInstance(authenticator, V1HmacAuthenticator)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.assertEqual(API_KEY_ID, authenticator._V1HmacAuthenticator__api_id_key)
            self.assertEqual(SECRET_API_KEY, authenticator._V1HmacAuthenticator__secret_api_key)

    def test_CreateCommunicatorBuilderIsCalled_InvalidPropertiesUri_ThrowRuntimeException(self):
        with self.assertRaises(RuntimeError):
            Factory.create_communicator_from_file(INVALID_PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY)

    def test_CreateCommunicatorIsCalled_InvalidPropertiesUri_ThrowRuntimeException(self):
        with self.assertRaises(RuntimeError):
            Factory.create_communicator_from_file(INVALID_PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY)

    def test_CreateCommunicatorFromFileIsCalled_CustomConnection_UseProvidedConnection(self):
        custom_connection = MagicMock(spec=Connection)
        communicator = Factory.create_communicator_from_file(
            PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY,
            connection=custom_connection
        )
        self.assertIs(custom_connection, communicator._Communicator__connection)

    def test_CreateCommunicatorFromFileIsCalled_CustomMarshaller_UseProvidedMarshaller(self):
        custom_marshaller = MagicMock(spec=Marshaller)
        communicator = Factory.create_communicator_from_file(
            PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY,
            marshaller=custom_marshaller
        )
        self.assertIs(custom_marshaller, communicator.marshaller)

    def test_CreateCommunicatorFromFileIsCalled_CustomMetadataProvider_UseProvidedMetadataProvider(self):
        custom_metadata_provider = MagicMock(spec=MetadataProvider)
        communicator = Factory.create_communicator_from_file(
            PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY,
            metadata_provider=custom_metadata_provider
        )
        self.assertIs(custom_metadata_provider, communicator._Communicator__metadata_provider)

    def test_CreateCommunicatorFromConfigurationIsCalled_DefaultScenario_ReturnCommunicator(self):
        configuration = Factory.create_configuration(PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY)
        communicator = Factory.create_communicator_from_configuration(configuration)
        self.assertIsNotNone(communicator)
        self.assertIs(communicator.marshaller, DefaultMarshaller.instance())

    def test_CreateCommunicatorFromConfigurationIsCalled_CustomConnection_UseProvidedConnection(self):
        configuration = Factory.create_configuration(PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY)
        custom_connection = MagicMock(spec=Connection)
        communicator = Factory.create_communicator_from_configuration(configuration, connection=custom_connection)
        self.assertIs(custom_connection, communicator._Communicator__connection)

    def test_CreateCommunicatorFromConfigurationIsCalled_UnsupportedAuthorizationType_RaiseRuntimeError(self):
        config = Factory.create_configuration(PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY)
        config.authorization_type = "UNSUPPORTED_TYPE"
        with self.assertRaises(RuntimeError) as ctx:
            Factory.create_communicator_from_configuration(config)
        self.assertIn("UNSUPPORTED_TYPE", str(ctx.exception))

    def test_CreateClientIsCalled_ValidPropertiesUri_ReturnNonNullClient(self):
        client = Factory.create_client_from_file(PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY)
        self.assertIsNotNone(client)
        self.assertIsInstance(client, Client)

    def test_CreateClientIsCalled_InvalidPropertiesUri_ThrowRuntimeException(self):
        with self.assertRaises(RuntimeError):
            Factory.create_client_from_file(INVALID_PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY)

    def test_CreateClientIsCalled_CommunicatorConfiguration_ReturnClientFromConfiguration(self):
        configuration = Factory.create_configuration(PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY)
        client = Factory.create_client_from_configuration(configuration)
        self.assertIsNotNone(client)
        self.assertIsInstance(client, Client)

    def test_CreateClientFromCommunicatorIsCalled_DefaultScenario_ReturnClient(self):
        communicator = Factory.create_communicator_from_file(PROPERTIES_URI, API_KEY_ID, SECRET_API_KEY)
        client = Factory.create_client_from_communicator(communicator)
        self.assertIsNotNone(client)
        self.assertIsInstance(client, Client)


if __name__ == '__main__':
    unittest.main()

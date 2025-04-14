import os
from configparser import ConfigParser

from onlinepayments.sdk.authentication.v1hmac_authenticator import V1HmacAuthenticator
from onlinepayments.sdk.communicator import Communicator
from onlinepayments.sdk.communicator_configuration import CommunicatorConfiguration
from onlinepayments.sdk.factory import Factory
from onlinepayments.sdk.communication.default_connection import DefaultConnection
from onlinepayments.sdk.communication.metadata_provider import MetadataProvider
from onlinepayments.sdk.json.default_marshaller import DefaultMarshaller

"""File containing a number of creation methods for integration tests"""

PROPERTIES_URL = os.path.abspath(os.path.join(__file__, os.pardir, "../resources/configuration.v1hmac.ini"))
PROPERTIES_URL_PROXY = os.path.abspath(os.path.join(__file__, os.pardir, "../resources/configuration.proxy.ini"))
# API_KEY_ID, SECRET_API_KEY, and MERCHANT_ID are stored in OS and should be retrieved
API_KEY_ID = os.getenv("onlinePayments.api.v1hmac.apiKeyId")
SECRET_API_KEY = os.getenv("onlinePayments.api.v1hmac.secretApiKey")
MERCHANT_ID = str(os.getenv("onlinePayments.api.merchantId"))
if API_KEY_ID is None:
    raise EnvironmentError("could not access environment variable onlinePayments.api.v1hmac.apiKeyId required for testing")
if SECRET_API_KEY is None:
    raise EnvironmentError("could not access environment variable onlinePayments.api.v1hmac.secretApiKey required for testing")
if MERCHANT_ID == 'None':
    raise EnvironmentError("could not access environment variable onlinePayments.api.merchantId required for testing")


def create_communicator_configuration(properties_url=PROPERTIES_URL, max_connections=None):
    """Convenience method to create a communicator configuration that connects to a host stored in system variables"""
    try:
        parser = ConfigParser()
        parser.read(properties_url)
        with open(properties_url) as f:
            parser.read_file(f)
        configuration = CommunicatorConfiguration(parser,
                                                  api_key_id=API_KEY_ID,
                                                  secret_api_key=SECRET_API_KEY,
                                                  max_connections=max_connections)
    except IOError as e:
        raise RuntimeError("Unable to read configuration", e)
    host = os.getenv("onlinePayments.api.endpoint.host")
    if host is not None:
        scheme = os.getenv("onlinePayments.api.endpoint.scheme", "https")
        port = int(os.getenv("onlinePayments.api.endpoint.port", -1))
        configuration.api_endpoint = "{2}://{0}:{1}".format(host, port, scheme)
    return configuration


def create_communicator():
    configuration = create_communicator_configuration()
    authenticator = V1HmacAuthenticator(configuration)
    return Communicator(api_endpoint=configuration.api_endpoint, authenticator=authenticator,
                        connection=DefaultConnection(3, 3), metadata_provider=MetadataProvider("OnlinePayments"),
                        marshaller=DefaultMarshaller.instance())


def create_client(max_connections=None):
    configuration = create_communicator_configuration(max_connections=max_connections)
    return Factory.create_client_from_configuration(configuration).with_client_meta_info('{"test":"test"}')


def create_client_with_proxy(max_connections=None):
    configuration = create_communicator_configuration(PROPERTIES_URL_PROXY, max_connections=max_connections)
    return Factory.create_client_from_configuration(configuration).with_client_meta_info('{"test":"test"}')

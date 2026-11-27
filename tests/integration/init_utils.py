import os

from onlinepayments.sdk.authentication.v1hmac_authenticator import V1HmacAuthenticator
from onlinepayments.sdk.communicator import Communicator
from onlinepayments.sdk.communicator_configuration import CommunicatorConfiguration
from onlinepayments.sdk.factory import Factory
from onlinepayments.sdk.communication.default_connection import DefaultConnection
from onlinepayments.sdk.communication.metadata_provider import MetadataProvider
from onlinepayments.sdk.json.default_marshaller import DefaultMarshaller

"""File containing a number of creation methods for integration tests"""

try:
    from dotenv import load_dotenv
except ImportError:  # python-dotenv is part of the [test] extra; without it only real environment variables are used
    load_dotenv = None

ENV_FILE = os.path.abspath(os.path.join(__file__, os.pardir, "../../.env"))
if load_dotenv is not None:
    # override=False (the default): variables that are already set in the environment take precedence over .env
    load_dotenv(ENV_FILE)

PROPERTIES_URL = os.path.abspath(os.path.join(__file__, os.pardir, "../resources/configuration.v1hmac.ini"))
PROPERTIES_URL_PROXY = os.path.abspath(os.path.join(__file__, os.pardir, "../resources/configuration.proxy.ini"))
# The credentials and merchant ID are read from the environment; tests/conftest.py skips the integration tests
# when any of the required variables is missing.
REQUIRED_ENVIRONMENT_VARIABLES = ("ONLINEPAYMENTS_API_KEY_ID", "ONLINEPAYMENTS_SECRET_API_KEY", "ONLINEPAYMENTS_MERCHANT_ID")
API_KEY_ID = os.getenv("ONLINEPAYMENTS_API_KEY_ID")
SECRET_API_KEY = os.getenv("ONLINEPAYMENTS_SECRET_API_KEY")
MERCHANT_ID = os.getenv("ONLINEPAYMENTS_MERCHANT_ID")


def missing_environment_variables():
    """Returns the names of the required environment variables that are not set"""
    return [name for name in REQUIRED_ENVIRONMENT_VARIABLES if not os.getenv(name)]


def create_communicator_configuration(properties_url=PROPERTIES_URL, max_connections=None):
    """Convenience method to create a communicator configuration that connects to a host stored in system variables"""
    try:
        configuration = CommunicatorConfiguration.from_file(properties_url,
                                                            api_key_id=API_KEY_ID,
                                                            secret_api_key=SECRET_API_KEY)
    except OSError as e:
        raise RuntimeError("Unable to read configuration", e) from e
    if max_connections is not None:
        configuration.max_connections = max_connections
    # optionally override the endpoint from the .ini file, for example https://payment.direct.ecom.preprod.worldline-solutions.com
    api_endpoint = os.getenv("ONLINEPAYMENTS_API_ENDPOINT")
    if api_endpoint:
        configuration.api_endpoint = api_endpoint
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

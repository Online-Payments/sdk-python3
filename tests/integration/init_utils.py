import os
from configparser import ConfigParser

from onlinepayments.sdk.communicator_configuration import CommunicatorConfiguration
from onlinepayments.sdk.factory import Factory

"""File containing a number of creation methods for integration tests"""

PROPERTIES_URL = os.path.abspath(os.path.join(__file__, os.pardir, "../resources/configuration.ini"))
# API_KEY_ID, SECRET_API_KEY and MERCHANT_ID are stored in OS and should be retrieved
API_KEY_ID = os.getenv("onlinePayments.api.apiKeyId")
SECRET_API_KEY = os.getenv("onlinePayments.api.secretApiKey")
MERCHANT_ID = str(os.getenv("onlinePayments.api.merchantId"))
if API_KEY_ID is None:
    raise EnvironmentError("could not access environment variable onlinePayments.api.apiKeyId required for testing")
if SECRET_API_KEY is None:
    raise EnvironmentError("could not access environment variable onlinePayments.api.secretApiKey required for testing")
if MERCHANT_ID == 'None':
    raise EnvironmentError("could not access environment variable onlinePayments.api.merchantId required for testing")


def create_communicator_configuration(properties_url=PROPERTIES_URL, max_connections=False):
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
        port = int(os.getenv("onlinePayments.api.endpoint.port", 443))
        configuration.api_endpoint = "{2}://{0}:{1}".format(host, port, scheme)
    return configuration


def create_client(max_connections=False):
    configuration = create_communicator_configuration(max_connections=max_connections)
    return Factory.create_client_from_configuration(configuration).with_client_meta_info('{"test":"test"}')

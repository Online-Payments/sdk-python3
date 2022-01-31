import _thread
import contextlib
import socketserver
import time
from http.server import BaseHTTPRequestHandler

from onlinepayments.sdk.communicator import Communicator
from onlinepayments.sdk.defaultimpl.default_authenticator import DefaultAuthenticator
from onlinepayments.sdk.defaultimpl.default_connection import DefaultConnection
from onlinepayments.sdk.endpoint_configuration import EndpointConfiguration
from onlinepayments.sdk.factory import Factory
from onlinepayments.sdk.meta_data_provider import MetaDataProvider


def create_handler(call_able):
    """Creates a handler that serves requests by calling the callable object
    with this handler as argument
    """

    class RequestHandler(BaseHTTPRequestHandler):

        def do_GET(self):
            call_able(self)
            time.sleep(0.1)  # sleep to avoid dropping the client before it can read the response

        def do_POST(self):
            call_able(self)
            time.sleep(0.1)  # sleep to avoid dropping the client before it can read the response

        def do_HEAD(self):
            pass

        def do_DELETE(self):
            call_able(self)
            time.sleep(0.1)  # sleep to avoid dropping the client before it can read the response

    return RequestHandler


@contextlib.contextmanager
def create_server_listening(call_able):
    """Context manager that creates a thread with a server at localhost which listens for requests
    and responds by calling the *call_able* function.

    :param call_able: a callable function to handle incoming requests, when a request comes in
    the function will be called with a SimpleHTTPRequestHandler to handle the request
    :return the url where the server is listening (http://localhost:port)
    """
    server = socketserver.TCPServer(('localhost', 0), create_handler(call_able), bind_and_activate=True)
    try:
        # frequent polling server for a faster server shutdown and faster tests
        _thread.start_new(server.serve_forever, (0.1,))
        yield 'http://localhost:' + str(server.server_address[1])
    finally:
        server.shutdown()
        server.server_close()


def create_client(http_host, connect_timeout=0.500, socket_timeout=0.500,
                  max_connections=EndpointConfiguration.DEFAULT_MAX_CONNECTIONS):
    connection = DefaultConnection(connect_timeout, socket_timeout, max_connections)
    authenticator = DefaultAuthenticator("apiKey", "secret")
    meta_data_provider = MetaDataProvider("OnlinePayments")
    communicator = Communicator(
        api_endpoint=http_host,
        authenticator=authenticator,
        meta_data_provider=meta_data_provider,
        connection=connection)
    return Factory.create_client_from_communicator(communicator)

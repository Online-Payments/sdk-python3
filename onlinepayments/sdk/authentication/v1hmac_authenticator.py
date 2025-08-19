import hashlib
import hmac
from base64 import b64encode
from operator import attrgetter
from re import sub
from typing import Optional, Sequence
from urllib.parse import ParseResult

from .authenticator import Authenticator

from onlinepayments.sdk.authentication.authorization_type import AuthorizationType
from onlinepayments.sdk.communicator_configuration import CommunicatorConfiguration
from onlinepayments.sdk.communication.request_header import RequestHeader


class V1HmacAuthenticator(Authenticator):
    """
    V1Hmac Authenticator implementation.
    """

    def __init__(self, communicator_configuration: CommunicatorConfiguration):
        """
        Constructs a new V1HmacAuthenticator instance using the provided CommunicatorConfiguration.

        :param communicator_configuration: The configuration object containing the v1Hmac api key and api key secret
         , connection timeout, and socket timeout. None of these can be None or empty,
         and the timeout values must be positive.
        """
        Authenticator.__init__(self)

        if not communicator_configuration.api_key_id:
            raise ValueError("api_key_id is required")
        if not communicator_configuration.secret_api_key:
            raise ValueError("secret_api_key is required")
        if communicator_configuration.authorization_type is None:
            raise ValueError("authorization_type is required")
        if communicator_configuration.connect_timeout <= 0:
            raise ValueError("connect_timeout must be positive")
        if communicator_configuration.socket_timeout <= 0:
            raise ValueError("socket_timeout must be positive")

        self.__api_id_key = communicator_configuration.api_key_id
        self.__secret_api_key = communicator_configuration.secret_api_key
        self.__authorization_type = AuthorizationType.get_authorization(communicator_configuration.authorization_type)
        self.__connect_timeout = communicator_configuration.connect_timeout
        self.__socket_timeout = communicator_configuration.socket_timeout
        self.__proxy_configuration = communicator_configuration.proxy_configuration

    def get_authorization(self, http_method: Optional[str], resource_uri: Optional[ParseResult],
                          request_headers: Optional[Sequence[RequestHeader]]) -> str:
        """Returns a v1HMAC authentication signature header"""
        if http_method is None or not http_method.strip():
            raise ValueError("http_method is required")
        if resource_uri is None:
            raise ValueError("resource_uri is required")
        data_to_sign = self.to_data_to_sign(http_method, resource_uri, request_headers)
        return "GCS " + self.__authorization_type + ":" + self.__api_id_key + \
               ":" + self.create_authentication_signature(data_to_sign)

    def to_data_to_sign(self, http_method, resource_uri, http_headers):
        content_type = None
        date = None
        canonicalized_headers = ""
        canonicalized_resource = self.__to_canonicalized_resource(resource_uri)
        xgcs_http_headers = []
        if http_headers is not None:
            for http_header in http_headers:
                if "Content-Type".lower() == http_header.name.lower():
                    content_type = http_header.value
                elif "Date".lower() == http_header.name.lower():
                    date = http_header.value
                else:
                    name = self.__to_canonicalize_header_name(http_header.name)
                    if name.startswith("x-gcs"):
                        value = self.to_canonicalize_header_value(
                            http_header.value)
                        xgcs_http_header = RequestHeader(name, value)
                        xgcs_http_headers.append(xgcs_http_header)
        xgcs_http_headers.sort(key=attrgetter('name'))
        for xgcs_http_header in xgcs_http_headers:
            canonicalized_headers += xgcs_http_header.name + ":" + xgcs_http_header.value + "\n"
        string = http_method.upper() + "\n"
        if content_type is not None:
            string += content_type + "\n"
        else:
            string += "\n"
        string += date + "\n"
        string += str(canonicalized_headers)
        string += canonicalized_resource + "\n"
        return str(string)

    @staticmethod
    def __to_canonicalized_resource(resource_uri):
        """
        Returns the encoded URI path without the HTTP method and including all
        decoded query parameters.
        """
        string = ""
        string += resource_uri.path
        if resource_uri.query:
            string += "?" + resource_uri.query
        return str(string)

    @staticmethod
    def __to_canonicalize_header_name(original_name):
        if original_name is None:
            return None
        else:
            return original_name.lower()

    @staticmethod
    def to_canonicalize_header_value(original_value):
        # For now V1HMAC is the only supported AuthorizationType so always use
        # the same logic.
        if original_value is None:
            return ""
        return sub(r"\r?\n(?:(?![\r\n])\s)*", " ", original_value).strip()

    def create_authentication_signature(self, data_to_sign):
        sig = hmac.new(self.__secret_api_key.encode("utf-8"), data_to_sign.encode("utf-8"),
                       hashlib.sha256)
        return b64encode(sig.digest()).decode("utf-8").rstrip('\n')

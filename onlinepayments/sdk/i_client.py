# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from abc import abstractmethod
from datetime import timedelta
from typing import Optional

from onlinepayments.sdk.log.body_obfuscator import BodyObfuscator
from onlinepayments.sdk.log.communicator_logger import CommunicatorLogger
from onlinepayments.sdk.log.header_obfuscator import HeaderObfuscator
from onlinepayments.sdk.log.logging_capable import LoggingCapable
from onlinepayments.sdk.log.obfuscation_capable import ObfuscationCapable
from onlinepayments.sdk.merchant.i_merchant_client import IMerchantClient


class IClient(LoggingCapable, ObfuscationCapable):
    """
    Payment platform client interface.

    This client and all its child clients are bound to one specific value for the X-GCS-ClientMetaInfo header.
    To get a new client with a different header value, use with_client_meta_info.

    Thread-safe.
    """

    @abstractmethod
    def with_client_meta_info(self, client_meta_info: Optional[str]) -> 'Client':
        """
        :param client_meta_info: JSON string containing the metadata for the client
        :return: a new Client which uses the passed metadata for the X-GCS-ClientMetaInfo header.
        :raise MarshallerSyntaxException: if the given clientMetaInfo is not a valid JSON string
        """

    @abstractmethod
    def close_idle_connections(self, idle_time: timedelta) -> None:
        """
        Utility method that delegates the call to this client's communicator.

        :param idle_time: a datetime.timedelta object indicating the idle time
        """

    @abstractmethod
    def close_expired_connections(self) -> None:
        """
        Utility method that delegates the call to this client's communicator.
        """

    @abstractmethod
    def set_body_obfuscator(self, body_obfuscator: BodyObfuscator) -> None:
        """"""

    @abstractmethod
    def set_header_obfuscator(self, header_obfuscator: HeaderObfuscator) -> None:
        """"""

    @abstractmethod
    def enable_logging(self, communicator_logger: CommunicatorLogger) -> None:
        """"""

    @abstractmethod
    def disable_logging(self) -> None:
        """"""

    @abstractmethod
    def close(self) -> None:
        """
        Releases any system resources associated with this object.
        """

    @abstractmethod
    def merchant(self, merchant_id: str) -> IMerchantClient:
        """
        Resource /v2/{merchantId}

        :param merchant_id:  str
        :return: :class:`onlinepayments.sdk.merchant.i_merchant_client.IMerchantClient`
        """

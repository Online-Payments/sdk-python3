#
# This class was auto-generated.
#
from abc import abstractmethod

from onlinepayments.sdk.log.logging_capable import LoggingCapable
from onlinepayments.sdk.merchant.merchant_client import MerchantClient


class IClient(LoggingCapable):
    """
    Payment platform client interface.

    This client interface and all its child client interfaces are bound to one specific value for the X-GCS-ClientMetaInfo header.
    To get a new client with a different header value, use with_client_meta_info.

    Thread-safe.
    """

    @staticmethod
    def API_VERSION():
        return "v2"

    @abstractmethod
    def with_client_meta_info(self, client_meta_info):
        """
        :param client_meta_info: JSON string containing the meta data for the client
        :return: a new Client which uses the passed meta data for the X-GCS-ClientMetaInfo header.
        :raise: MarshallerSyntaxException if the given clientMetaInfo is not a valid JSON string
        """

    @abstractmethod
    def close_idle_connections(self, idle_time):
        """
        Utility method that delegates the call to this client's communicator.

        :param idle_time: a datetime.timedelta object indicating the idle time
        """

    @abstractmethod
    def close_expired_connections(self):
        """
        Utility method that delegates the call to this client's communicator.
        """

    @abstractmethod
    def enable_logging(self, communicator_logger):
        """"""

    @abstractmethod
    def disable_logging(self):
        """"""

    @abstractmethod
    def close(self):
        """
        Releases any system resources associated with this object.
        """

    @abstractmethod
    def merchant(self, merchant_id: str) -> MerchantClient:
        """
        Resource /v2/{merchantId}

        :param merchant_id: str
        :return: :class:`onlinepayments.sdk.merchant.i_merchant_client.IMerchantClient`
        """

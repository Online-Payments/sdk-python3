from typing import Mapping, Sequence, Optional

from .i_communicator import ICommunicator

from onlinepayments.sdk.communication.request_header import RequestHeader


class ApiResource(object):
    """
    Base class of all Online Payments platform API resources.
    """

    def __init__(self, parent: Optional['ApiResource'] = None, communicator: Optional[ICommunicator] = None,
                 path_context: Optional[Mapping[str, str]] = None, client_meta_info: Optional[str] = None):
        """
        The parent and/or communicator must be given.
        """
        if not parent and not communicator:
            raise ValueError("parent and/or communicator is required")
        self.__parent = parent
        self.__communicator = communicator if communicator else parent._communicator
        self.__path_context = path_context
        self.__client_meta_info = client_meta_info if client_meta_info or not parent else parent._client_meta_info

    @property
    def _communicator(self) -> ICommunicator:
        return self.__communicator

    @property
    def _client_meta_info(self) -> str:
        return self.__client_meta_info

    @property
    def _client_headers(self) -> Optional[Sequence[RequestHeader]]:
        if self._client_meta_info is not None:
            client_headers = [RequestHeader("X-GCS-ClientMetaInfo", self._client_meta_info)]
            return client_headers
        else:
            return None

    def _instantiate_uri(self, uri: str, path_context: Optional[Mapping[str, str]]) -> str:
        uri = self.__replace_all(uri, path_context)
        uri = self.__instantiate_uri(uri)
        return uri

    def __instantiate_uri(self, uri: str) -> str:
        uri = self.__replace_all(uri, self.__path_context)
        if self.__parent is not None:
            uri = self.__parent.__instantiate_uri(uri)
        return uri

    @staticmethod
    def __replace_all(uri: str, path_context: Optional[Mapping[str, str]]) -> str:
        if path_context:
            for key, value in path_context.items():
                uri = uri.replace("{" + key + "}", value)
        return uri

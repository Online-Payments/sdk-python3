import re
from collections.abc import Mapping, Sequence
from urllib.parse import quote

from .i_communicator import ICommunicator

from onlinepayments.sdk.communication.request_header import RequestHeader


class ApiResource:
    """
    Base class of all Online Payments platform API resources.
    """

    __PLACEHOLDER = re.compile(r"\{(\w+)\}")

    def __init__(self, parent: 'ApiResource | None' = None, communicator: ICommunicator | None = None,
                 path_context: Mapping[str, str] | None = None, client_meta_info: str | None = None):
        """
        The parent and/or communicator must be given.
        """
        if communicator is None:
            if parent is None:
                raise ValueError("parent and/or communicator is required")
            communicator = parent._communicator
        self.__parent = parent
        self.__communicator = communicator
        self.__path_context = path_context
        self.__client_meta_info = client_meta_info if client_meta_info or not parent else parent._client_meta_info

    @property
    def _communicator(self) -> ICommunicator:
        return self.__communicator

    @property
    def _client_meta_info(self) -> str | None:
        return self.__client_meta_info

    @property
    def _client_headers(self) -> Sequence[RequestHeader] | None:
        if self._client_meta_info is not None:
            client_headers = [RequestHeader("X-GCS-ClientMetaInfo", self._client_meta_info)]
            return client_headers
        else:
            return None

    def _instantiate_uri(self, uri: str, path_context: Mapping[str, str] | None) -> str:
        context = self.__collect_path_context()
        if path_context:
            context.update(path_context)

        def replace(match: re.Match) -> str:
            key = match.group(1)
            return ApiResource.__encode_path_value(context[key]) if key in context else match.group(0)

        return ApiResource.__PLACEHOLDER.sub(replace, uri)

    def __collect_path_context(self) -> dict[str, str]:
        context = self.__parent.__collect_path_context() if self.__parent is not None else {}
        if self.__path_context:
            context.update(self.__path_context)
        return context

    @staticmethod
    def __encode_path_value(value: object) -> str:
        if value is None:
            raise ValueError("path parameter value is required")
        value = str(value)
        if value in (".", ".."):
            raise ValueError(f"invalid path parameter value: '{value}'")
        return quote(value, safe="")

from abc import ABC, abstractmethod
from typing import Sequence

from onlinepayments.sdk.communication.request_header import RequestHeader


class IMetadataProvider(ABC):
    """
    Provides meta info about the server.
    """

    @property
    @abstractmethod
    def metadata_headers(self) -> Sequence[RequestHeader]:
        """
        :return: The server related headers containing the metadata to be
         associated with the request (if any). This will always contain at least
         an automatically generated header X-GCS-ServerMetaInfo.
        """

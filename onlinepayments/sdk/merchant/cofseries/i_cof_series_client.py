# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from abc import ABC, abstractmethod
from typing import Optional

from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.domain.import_cof_series_request import ImportCofSeriesRequest
from onlinepayments.sdk.domain.import_cof_series_response import ImportCofSeriesResponse


class ICofSeriesClient(ABC):
    """
    CofSeries client interface. Thread-safe.
    """

    @abstractmethod
    def import_cof_series(self, body: ImportCofSeriesRequest, context: Optional[CallContext] = None) -> ImportCofSeriesResponse:
        """
        Resource /v2/{merchantId}/tokens/importCofSeries - Imports the COF Series token.

        :param body:     :class:`onlinepayments.sdk.domain.import_cof_series_request.ImportCofSeriesRequest`
        :param context:  :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.import_cof_series_response.ImportCofSeriesResponse`
        :raise IdempotenceException: if an idempotent request caused a conflict (HTTP status code 409)
        :raise ValidationException: if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise AuthorizationException: if the request was not allowed (HTTP status code 403)
        :raise ReferenceException: if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise PlatformException: if something went wrong at the payment platform,
                   the payment platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise ApiException: if the payment platform returned any other error
        """

# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Mapping, Optional

from .i_cof_series_client import ICofSeriesClient

from onlinepayments.sdk.api_resource import ApiResource
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.communication.response_exception import ResponseException
from onlinepayments.sdk.domain.error_response import ErrorResponse
from onlinepayments.sdk.domain.import_cof_series_request import ImportCofSeriesRequest
from onlinepayments.sdk.domain.import_cof_series_response import ImportCofSeriesResponse
from onlinepayments.sdk.exception_factory import create_exception


class CofSeriesClient(ApiResource, ICofSeriesClient):
    """
    CofSeries client. Thread-safe.
    """

    def __init__(self, parent: ApiResource, path_context: Optional[Mapping[str, str]]):
        """
        :param parent:       :class:`onlinepayments.sdk.api_resource.ApiResource`
        :param path_context: Mapping[str, str]
        """
        super(CofSeriesClient, self).__init__(parent=parent, path_context=path_context)

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
        uri = self._instantiate_uri("/v2/{merchantId}/tokens/importCofSeries", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    ImportCofSeriesResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

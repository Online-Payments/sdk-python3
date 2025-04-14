# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Mapping, Optional

from .i_services_client import IServicesClient

from onlinepayments.sdk.api_resource import ApiResource
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.communication.response_exception import ResponseException
from onlinepayments.sdk.domain.calculate_surcharge_request import CalculateSurchargeRequest
from onlinepayments.sdk.domain.calculate_surcharge_response import CalculateSurchargeResponse
from onlinepayments.sdk.domain.currency_conversion_request import CurrencyConversionRequest
from onlinepayments.sdk.domain.currency_conversion_response import CurrencyConversionResponse
from onlinepayments.sdk.domain.error_response import ErrorResponse
from onlinepayments.sdk.domain.get_iin_details_request import GetIINDetailsRequest
from onlinepayments.sdk.domain.get_iin_details_response import GetIINDetailsResponse
from onlinepayments.sdk.domain.test_connection import TestConnection
from onlinepayments.sdk.exception_factory import create_exception


class ServicesClient(ApiResource, IServicesClient):
    """
    Services client. Thread-safe.
    """

    def __init__(self, parent: ApiResource, path_context: Optional[Mapping[str, str]]):
        """
        :param parent:       :class:`onlinepayments.sdk.api_resource.ApiResource`
        :param path_context: Mapping[str, str]
        """
        super(ServicesClient, self).__init__(parent=parent, path_context=path_context)

    def test_connection(self, context: Optional[CallContext] = None) -> TestConnection:
        """
        Resource /v2/{merchantId}/services/testconnection - Test connection

        :param context:  :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.test_connection.TestConnection`
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
        uri = self._instantiate_uri("/v2/{merchantId}/services/testconnection", None)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    TestConnection,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

    def get_iin_details(self, body: GetIINDetailsRequest, context: Optional[CallContext] = None) -> GetIINDetailsResponse:
        """
        Resource /v2/{merchantId}/services/getIINdetails - Get IIN details

        :param body:     :class:`onlinepayments.sdk.domain.get_iin_details_request.GetIINDetailsRequest`
        :param context:  :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.get_iin_details_response.GetIINDetailsResponse`
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
        uri = self._instantiate_uri("/v2/{merchantId}/services/getIINdetails", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    GetIINDetailsResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

    def get_dcc_rate_inquiry(self, body: CurrencyConversionRequest, context: Optional[CallContext] = None) -> CurrencyConversionResponse:
        """
        Resource /v2/{merchantId}/services/dccrate - Get currency conversion quote

        :param body:     :class:`onlinepayments.sdk.domain.currency_conversion_request.CurrencyConversionRequest`
        :param context:  :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.currency_conversion_response.CurrencyConversionResponse`
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
        uri = self._instantiate_uri("/v2/{merchantId}/services/dccrate", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    CurrencyConversionResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

    def surcharge_calculation(self, body: CalculateSurchargeRequest, context: Optional[CallContext] = None) -> CalculateSurchargeResponse:
        """
        Resource /v2/{merchantId}/services/surchargecalculation - Surcharge Calculation

        :param body:     :class:`onlinepayments.sdk.domain.calculate_surcharge_request.CalculateSurchargeRequest`
        :param context:  :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.calculate_surcharge_response.CalculateSurchargeResponse`
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
        uri = self._instantiate_uri("/v2/{merchantId}/services/surchargecalculation", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    CalculateSurchargeResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

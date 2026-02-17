# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Mapping, Optional

from .get_card_data_by_payments_params import GetCardDataByPaymentsParams
from .get_card_data_by_tokens_params import GetCardDataByTokensParams
from .i_tokenization_client import ITokenizationClient

from onlinepayments.sdk.api_resource import ApiResource
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.communication.response_exception import ResponseException
from onlinepayments.sdk.domain.create_certificate_response import CreateCertificateResponse
from onlinepayments.sdk.domain.csr_request import CsrRequest
from onlinepayments.sdk.domain.detokenization_response import DetokenizationResponse
from onlinepayments.sdk.domain.error_response import ErrorResponse
from onlinepayments.sdk.exception_factory import create_exception


class TokenizationClient(ApiResource, ITokenizationClient):
    """
    Tokenization client. Thread-safe.
    """

    def __init__(self, parent: ApiResource, path_context: Optional[Mapping[str, str]]):
        """
        :param parent:       :class:`onlinepayments.sdk.api_resource.ApiResource`
        :param path_context: Mapping[str, str]
        """
        super(TokenizationClient, self).__init__(parent=parent, path_context=path_context)

    def create_certificate(self, body: CsrRequest, context: Optional[CallContext] = None) -> CreateCertificateResponse:
        """
        Resource /v2/{merchantId}/detokenize/csr - Sign certificate

        :param body:     :class:`onlinepayments.sdk.domain.csr_request.CsrRequest`
        :param context:  :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.create_certificate_response.CreateCertificateResponse`
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
        uri = self._instantiate_uri("/v2/{merchantId}/detokenize/csr", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    CreateCertificateResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

    def get_card_data_by_tokens(self, query: GetCardDataByTokensParams, context: Optional[CallContext] = None) -> DetokenizationResponse:
        """
        Resource /v2/{merchantId}/detokenize/tokens - Get sensitive card details by card alias tokens

        :param query:    :class:`onlinepayments.sdk.merchant.tokenization.get_card_data_by_tokens_params.GetCardDataByTokensParams`
        :param context:  :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.detokenization_response.DetokenizationResponse`
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
        uri = self._instantiate_uri("/v2/{merchantId}/detokenize/tokens", None)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    DetokenizationResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

    def get_card_data_by_payments(self, query: GetCardDataByPaymentsParams, context: Optional[CallContext] = None) -> DetokenizationResponse:
        """
        Resource /v2/{merchantId}/detokenize/payments - Get sensitive card details by card payment identifiers

        :param query:    :class:`onlinepayments.sdk.merchant.tokenization.get_card_data_by_payments_params.GetCardDataByPaymentsParams`
        :param context:  :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.detokenization_response.DetokenizationResponse`
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
        uri = self._instantiate_uri("/v2/{merchantId}/detokenize/payments", None)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    DetokenizationResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

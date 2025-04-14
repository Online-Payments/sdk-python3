# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Mapping, Optional

from .i_payment_links_client import IPaymentLinksClient

from onlinepayments.sdk.api_resource import ApiResource
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.communication.response_exception import ResponseException
from onlinepayments.sdk.domain.create_payment_link_request import CreatePaymentLinkRequest
from onlinepayments.sdk.domain.error_response import ErrorResponse
from onlinepayments.sdk.domain.payment_link_response import PaymentLinkResponse
from onlinepayments.sdk.exception_factory import create_exception


class PaymentLinksClient(ApiResource, IPaymentLinksClient):
    """
    PaymentLinks client. Thread-safe.
    """

    def __init__(self, parent: ApiResource, path_context: Optional[Mapping[str, str]]):
        """
        :param parent:       :class:`onlinepayments.sdk.api_resource.ApiResource`
        :param path_context: Mapping[str, str]
        """
        super(PaymentLinksClient, self).__init__(parent=parent, path_context=path_context)

    def create_payment_link(self, body: CreatePaymentLinkRequest, context: Optional[CallContext] = None) -> PaymentLinkResponse:
        """
        Resource /v2/{merchantId}/paymentlinks - Create payment link

        :param body:     :class:`onlinepayments.sdk.domain.create_payment_link_request.CreatePaymentLinkRequest`
        :param context:  :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.payment_link_response.PaymentLinkResponse`
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
        uri = self._instantiate_uri("/v2/{merchantId}/paymentlinks", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    PaymentLinkResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

    def get_payment_link_by_id(self, payment_link_id: str, context: Optional[CallContext] = None) -> PaymentLinkResponse:
        """
        Resource /v2/{merchantId}/paymentlinks/{paymentLinkId} - Get payment link by ID

        :param payment_link_id:  str
        :param context:          :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.payment_link_response.PaymentLinkResponse`
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
        path_context = {
            "paymentLinkId": payment_link_id,
        }
        uri = self._instantiate_uri("/v2/{merchantId}/paymentlinks/{paymentLinkId}", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    PaymentLinkResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

    def cancel_payment_link_by_id(self, payment_link_id: str, context: Optional[CallContext] = None) -> None:
        """
        Resource /v2/{merchantId}/paymentlinks/{paymentLinkId}/cancel - Cancel PaymentLink by ID

        :param payment_link_id:  str
        :param context:          :class:`onlinepayments.sdk.call_context.CallContext`
        :return: None
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
        path_context = {
            "paymentLinkId": payment_link_id,
        }
        uri = self._instantiate_uri("/v2/{merchantId}/paymentlinks/{paymentLinkId}/cancel", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    None,
                    None,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

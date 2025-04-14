# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Mapping, Optional

from .i_complete_client import ICompleteClient

from onlinepayments.sdk.api_resource import ApiResource
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.communication.response_exception import ResponseException
from onlinepayments.sdk.domain.complete_payment_request import CompletePaymentRequest
from onlinepayments.sdk.domain.complete_payment_response import CompletePaymentResponse
from onlinepayments.sdk.domain.payment_error_response import PaymentErrorResponse
from onlinepayments.sdk.exception_factory import create_exception


class CompleteClient(ApiResource, ICompleteClient):
    """
    Complete client. Thread-safe.
    """

    def __init__(self, parent: ApiResource, path_context: Optional[Mapping[str, str]]):
        """
        :param parent:       :class:`onlinepayments.sdk.api_resource.ApiResource`
        :param path_context: Mapping[str, str]
        """
        super(CompleteClient, self).__init__(parent=parent, path_context=path_context)

    def complete_payment(self, payment_id: str, body: CompletePaymentRequest, context: Optional[CallContext] = None) -> CompletePaymentResponse:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/complete - Complete payment

        :param payment_id:  str
        :param body:        :class:`onlinepayments.sdk.domain.complete_payment_request.CompletePaymentRequest`
        :param context:     :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.complete_payment_response.CompletePaymentResponse`
        :raise DeclinedPaymentException: if the payment platform declined / rejected the payment. The payment result will be available from the exception.
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
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v2/{merchantId}/payments/{paymentId}/complete", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    CompletePaymentResponse,
                    context)

        except ResponseException as e:
            error_type = PaymentErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

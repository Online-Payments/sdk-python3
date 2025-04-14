# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Mapping, Optional

from .i_payments_client import IPaymentsClient

from onlinepayments.sdk.api_resource import ApiResource
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.communication.response_exception import ResponseException
from onlinepayments.sdk.domain.cancel_payment_request import CancelPaymentRequest
from onlinepayments.sdk.domain.cancel_payment_response import CancelPaymentResponse
from onlinepayments.sdk.domain.capture_payment_request import CapturePaymentRequest
from onlinepayments.sdk.domain.capture_response import CaptureResponse
from onlinepayments.sdk.domain.create_payment_request import CreatePaymentRequest
from onlinepayments.sdk.domain.create_payment_response import CreatePaymentResponse
from onlinepayments.sdk.domain.error_response import ErrorResponse
from onlinepayments.sdk.domain.payment_details_response import PaymentDetailsResponse
from onlinepayments.sdk.domain.payment_error_response import PaymentErrorResponse
from onlinepayments.sdk.domain.payment_response import PaymentResponse
from onlinepayments.sdk.domain.refund_error_response import RefundErrorResponse
from onlinepayments.sdk.domain.refund_request import RefundRequest
from onlinepayments.sdk.domain.refund_response import RefundResponse
from onlinepayments.sdk.domain.subsequent_payment_request import SubsequentPaymentRequest
from onlinepayments.sdk.domain.subsequent_payment_response import SubsequentPaymentResponse
from onlinepayments.sdk.exception_factory import create_exception


class PaymentsClient(ApiResource, IPaymentsClient):
    """
    Payments client. Thread-safe.
    """

    def __init__(self, parent: ApiResource, path_context: Optional[Mapping[str, str]]):
        """
        :param parent:       :class:`onlinepayments.sdk.api_resource.ApiResource`
        :param path_context: Mapping[str, str]
        """
        super(PaymentsClient, self).__init__(parent=parent, path_context=path_context)

    def create_payment(self, body: CreatePaymentRequest, context: Optional[CallContext] = None) -> CreatePaymentResponse:
        """
        Resource /v2/{merchantId}/payments - Create payment

        :param body:     :class:`onlinepayments.sdk.domain.create_payment_request.CreatePaymentRequest`
        :param context:  :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.create_payment_response.CreatePaymentResponse`
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
        uri = self._instantiate_uri("/v2/{merchantId}/payments", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    CreatePaymentResponse,
                    context)

        except ResponseException as e:
            error_type = PaymentErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

    def get_payment(self, payment_id: str, context: Optional[CallContext] = None) -> PaymentResponse:
        """
        Resource /v2/{merchantId}/payments/{paymentId} - Get payment

        :param payment_id:  str
        :param context:     :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.payment_response.PaymentResponse`
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
        uri = self._instantiate_uri("/v2/{merchantId}/payments/{paymentId}", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    PaymentResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

    def get_payment_details(self, payment_id: str, context: Optional[CallContext] = None) -> PaymentDetailsResponse:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/details - Get payment details

        :param payment_id:  str
        :param context:     :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.payment_details_response.PaymentDetailsResponse`
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
        uri = self._instantiate_uri("/v2/{merchantId}/payments/{paymentId}/details", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    PaymentDetailsResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

    def cancel_payment(self, payment_id: str, body: CancelPaymentRequest, context: Optional[CallContext] = None) -> CancelPaymentResponse:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/cancel - Cancel payment

        :param payment_id:  str
        :param body:        :class:`onlinepayments.sdk.domain.cancel_payment_request.CancelPaymentRequest`
        :param context:     :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.cancel_payment_response.CancelPaymentResponse`
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
        uri = self._instantiate_uri("/v2/{merchantId}/payments/{paymentId}/cancel", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    CancelPaymentResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

    def capture_payment(self, payment_id: str, body: CapturePaymentRequest, context: Optional[CallContext] = None) -> CaptureResponse:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/capture - Capture payment

        :param payment_id:  str
        :param body:        :class:`onlinepayments.sdk.domain.capture_payment_request.CapturePaymentRequest`
        :param context:     :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.capture_response.CaptureResponse`
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
        uri = self._instantiate_uri("/v2/{merchantId}/payments/{paymentId}/capture", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    CaptureResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

    def refund_payment(self, payment_id: str, body: RefundRequest, context: Optional[CallContext] = None) -> RefundResponse:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/refund - Refund payment

        :param payment_id:  str
        :param body:        :class:`onlinepayments.sdk.domain.refund_request.RefundRequest`
        :param context:     :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.refund_response.RefundResponse`
        :raise DeclinedRefundException: if the payment platform declined / rejected the refund. The refund result will be available from the exception.
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
        uri = self._instantiate_uri("/v2/{merchantId}/payments/{paymentId}/refund", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    RefundResponse,
                    context)

        except ResponseException as e:
            error_type = RefundErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

    def subsequent_payment(self, payment_id: str, body: SubsequentPaymentRequest, context: Optional[CallContext] = None) -> SubsequentPaymentResponse:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/subsequent - Subsequent payment

        :param payment_id:  str
        :param body:        :class:`onlinepayments.sdk.domain.subsequent_payment_request.SubsequentPaymentRequest`
        :param context:     :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.subsequent_payment_response.SubsequentPaymentResponse`
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
        uri = self._instantiate_uri("/v2/{merchantId}/payments/{paymentId}/subsequent", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    SubsequentPaymentResponse,
                    context)

        except ResponseException as e:
            error_type = PaymentErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from abc import ABC, abstractmethod
from typing import Optional

from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.domain.add_authorization_details_response import AddAuthorizationDetailsResponse
from onlinepayments.sdk.domain.increment_authorization_request import IncrementAuthorizationRequest
from onlinepayments.sdk.domain.increment_authorization_response import IncrementAuthorizationResponse
from onlinepayments.sdk.domain.update_authorization_additional_data_request import UpdateAuthorizationAdditionalDataRequest


class IPreAuthorizationClient(ABC):
    """
    PreAuthorization client interface. Thread-safe.
    """

    @abstractmethod
    def increment_authorization(self, payment_id: str, body: IncrementAuthorizationRequest, context: Optional[CallContext] = None) -> IncrementAuthorizationResponse:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/increment-authorization - Increment authorization

        :param payment_id:  str
        :param body:        :class:`onlinepayments.sdk.domain.increment_authorization_request.IncrementAuthorizationRequest`
        :param context:     :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.increment_authorization_response.IncrementAuthorizationResponse`
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

    @abstractmethod
    def add_authorization_details(self, payment_id: str, body: UpdateAuthorizationAdditionalDataRequest, context: Optional[CallContext] = None) -> AddAuthorizationDetailsResponse:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/authorization-additional-data - Add market specific additional data to a payment prior to capture.

        :param payment_id:  str
        :param body:        :class:`onlinepayments.sdk.domain.update_authorization_additional_data_request.UpdateAuthorizationAdditionalDataRequest`
        :param context:     :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.add_authorization_details_response.AddAuthorizationDetailsResponse`
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

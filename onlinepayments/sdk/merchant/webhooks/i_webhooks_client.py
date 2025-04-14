# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from abc import ABC, abstractmethod
from typing import Optional

from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.domain.send_test_request import SendTestRequest
from onlinepayments.sdk.domain.validate_credentials_request import ValidateCredentialsRequest
from onlinepayments.sdk.domain.validate_credentials_response import ValidateCredentialsResponse


class IWebhooksClient(ABC):
    """
    Webhooks client interface. Thread-safe.
    """

    @abstractmethod
    def validate_webhook_credentials(self, body: ValidateCredentialsRequest, context: Optional[CallContext] = None) -> ValidateCredentialsResponse:
        """
        Resource /v2/{merchantId}/webhooks/validateCredentials - Validate credentials

        :param body:     :class:`onlinepayments.sdk.domain.validate_credentials_request.ValidateCredentialsRequest`
        :param context:  :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.validate_credentials_response.ValidateCredentialsResponse`
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
    def send_test_webhook(self, body: SendTestRequest, context: Optional[CallContext] = None) -> None:
        """
        Resource /v2/{merchantId}/webhooks/sendtest - Send test

        :param body:     :class:`onlinepayments.sdk.domain.send_test_request.SendTestRequest`
        :param context:  :class:`onlinepayments.sdk.call_context.CallContext`
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

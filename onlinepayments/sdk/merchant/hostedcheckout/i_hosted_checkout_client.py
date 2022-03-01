#
# This class was auto-generated.
#
from abc import ABC, abstractmethod

from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.domain.create_hosted_checkout_request import CreateHostedCheckoutRequest
from onlinepayments.sdk.domain.create_hosted_checkout_response import CreateHostedCheckoutResponse
from onlinepayments.sdk.domain.get_hosted_checkout_response import GetHostedCheckoutResponse

class IHostedCheckoutClient(ABC):
    """
    HostedCheckout client interface. Thread-safe.
    """

    @abstractmethod
    def create_hosted_checkout(self, body: CreateHostedCheckoutRequest, context: CallContext = None) -> CreateHostedCheckoutResponse:
        """
        Resource /v2/{merchantId}/hostedcheckouts - Create hosted checkout


        :param body: :class:`onlinepayments.sdk.domain.create_hosted_checkout_request.CreateHostedCheckoutRequest`
        :param context: :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.create_hosted_checkout_response.CreateHostedCheckoutResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: PaymentPlatformException if something went wrong at the payment platform,
                   the payment platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the payment platform returned any other error
        """

    @abstractmethod
    def get_hosted_checkout(self, hosted_checkout_id: str, context: CallContext = None) -> GetHostedCheckoutResponse:
        """
        Resource /v2/{merchantId}/hostedcheckouts/{hostedCheckoutId} - Get hosted checkout status


        :param hosted_checkout_id: str
        :param context: :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.get_hosted_checkout_response.GetHostedCheckoutResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: PaymentPlatformException if something went wrong at the payment platform,
                   the payment platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the payment platform returned any other error
        """

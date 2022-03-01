#
# This class was auto-generated.
#
from abc import ABC, abstractmethod

from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.domain.create_token_request import CreateTokenRequest
from onlinepayments.sdk.domain.created_token_response import CreatedTokenResponse
from onlinepayments.sdk.domain.token_response import TokenResponse

class ITokensClient(ABC):
    """
    Tokens client interface. Thread-safe.
    """

    @abstractmethod
    def create_token(self, body: CreateTokenRequest, context: CallContext = None) -> CreatedTokenResponse:
        """
        Resource /v2/{merchantId}/tokens - Create token


        :param body: :class:`onlinepayments.sdk.domain.create_token_request.CreateTokenRequest`
        :param context: :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.created_token_response.CreatedTokenResponse`
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
    def get_token(self, token_id: str, context: CallContext = None) -> TokenResponse:
        """
        Resource /v2/{merchantId}/tokens/{tokenId} - Get token


        :param token_id: str
        :param context: :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.token_response.TokenResponse`
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
    def delete_token(self, token_id: str, context: CallContext = None) -> None:
        """
        Resource /v2/{merchantId}/tokens/{tokenId} - Delete token


        :param token_id: str
        :param context: :class:`onlinepayments.sdk.call_context.CallContext`
        :return: None
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: PaymentPlatformException if something went wrong at the payment platform,
                   the payment platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the payment platform returned any other error
        """

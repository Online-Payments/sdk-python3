#
# This class was auto-generated.
#
from onlinepayments.sdk.api_resource import ApiResource
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.response_exception import ResponseException
from onlinepayments.sdk.domain.create_payout_request import CreatePayoutRequest
from onlinepayments.sdk.domain.error_response import ErrorResponse
from onlinepayments.sdk.domain.payout_error_response import PayoutErrorResponse
from onlinepayments.sdk.domain.payout_response import PayoutResponse
from onlinepayments.sdk.merchant.payouts.i_payouts_client import IPayoutsClient


class PayoutsClient(ApiResource, IPayoutsClient):
    """
    Payouts client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`onlinepayments.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(PayoutsClient, self).__init__(parent, path_context)

    def create_payout(self, body: CreatePayoutRequest, context: CallContext = None) -> PayoutResponse:
        """
        Resource /v2/{merchantId}/payouts - Create payout


        :param body: :class:`onlinepayments.sdk.domain.create_payout_request.CreatePayoutRequest`
        :param context: :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.payout_response.PayoutResponse`
        :raise: DeclinedPayoutException if the payment platform declined / rejected the payout. The payout result will be available from the exception.
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: PaymentPlatformException if something went wrong at the payment platform,
                   the payment platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the payment platform returned any other error
        """
        uri = self._instantiate_uri("/v2/{merchantId}/payouts", None)
        try:
            return self._communicator.post(
                uri,
                self._client_headers,
                None,
                body,
                PayoutResponse,
                context)

        except ResponseException as e:
            error_type = PayoutErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get_payout(self, payout_id: str, context: CallContext = None) -> PayoutResponse:
        """
        Resource /v2/{merchantId}/payouts/{payoutId} - Get payout


        :param payout_id: str
        :param context: :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.payout_response.PayoutResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: PaymentPlatformException if something went wrong at the payment platform,
                   the payment platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the payment platform returned any other error
        """
        path_context = {
            "payoutId": payout_id,
        }
        uri = self._instantiate_uri("/v2/{merchantId}/payouts/{payoutId}", path_context)
        try:
            return self._communicator.get(
                uri,
                self._client_headers,
                None,
                PayoutResponse,
                context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

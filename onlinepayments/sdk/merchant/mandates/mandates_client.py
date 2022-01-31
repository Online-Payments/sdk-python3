#
# This class was auto-generated.
#
from onlinepayments.sdk.api_resource import ApiResource
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.response_exception import ResponseException
from onlinepayments.sdk.domain.create_mandate_request import CreateMandateRequest
from onlinepayments.sdk.domain.create_mandate_response import CreateMandateResponse
from onlinepayments.sdk.domain.error_response import ErrorResponse
from onlinepayments.sdk.domain.get_mandate_response import GetMandateResponse
from onlinepayments.sdk.merchant.mandates.i_mandates_client import IMandatesClient


class MandatesClient(ApiResource, IMandatesClient):
    """
    Mandates client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`onlinepayments.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(MandatesClient, self).__init__(parent, path_context)

    def create_mandate(self, body: CreateMandateRequest, context: CallContext = None) -> CreateMandateResponse:
        """
        Resource /v2/{merchantId}/mandates - Create mandate


        :param body: :class:`onlinepayments.sdk.domain.create_mandate_request.CreateMandateRequest`
        :param context: :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.create_mandate_response.CreateMandateResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: PaymentPlatformException if something went wrong at the payment platform,
                   the payment platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the payment platform returned any other error
        """
        uri = self._instantiate_uri("/v2/{merchantId}/mandates", None)
        try:
            return self._communicator.post(
                uri,
                self._client_headers,
                None,
                body,
                CreateMandateResponse,
                context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get_mandate(self, unique_mandate_reference: str, context: CallContext = None) -> GetMandateResponse:
        """
        Resource /v2/{merchantId}/mandates/{uniqueMandateReference} - Get mandate


        :param unique_mandate_reference: str
        :param context: :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.get_mandate_response.GetMandateResponse`
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
            "uniqueMandateReference": unique_mandate_reference,
        }
        uri = self._instantiate_uri("/v2/{merchantId}/mandates/{uniqueMandateReference}", path_context)
        try:
            return self._communicator.get(
                uri,
                self._client_headers,
                None,
                GetMandateResponse,
                context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def block_mandate(self, unique_mandate_reference: str, context: CallContext = None) -> GetMandateResponse:
        """
        Resource /v2/{merchantId}/mandates/{uniqueMandateReference}/block - Block mandate


        :param unique_mandate_reference: str
        :param context: :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.get_mandate_response.GetMandateResponse`
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
            "uniqueMandateReference": unique_mandate_reference,
        }
        uri = self._instantiate_uri("/v2/{merchantId}/mandates/{uniqueMandateReference}/block", path_context)
        try:
            return self._communicator.post(
                uri,
                self._client_headers,
                None,
                None,
                GetMandateResponse,
                context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def unblock_mandate(self, unique_mandate_reference: str, context: CallContext = None) -> GetMandateResponse:
        """
        Resource /v2/{merchantId}/mandates/{uniqueMandateReference}/unblock - Unblock mandate


        :param unique_mandate_reference: str
        :param context: :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.get_mandate_response.GetMandateResponse`
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
            "uniqueMandateReference": unique_mandate_reference,
        }
        uri = self._instantiate_uri("/v2/{merchantId}/mandates/{uniqueMandateReference}/unblock", path_context)
        try:
            return self._communicator.post(
                uri,
                self._client_headers,
                None,
                None,
                GetMandateResponse,
                context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def revoke_mandate(self, unique_mandate_reference: str, context: CallContext = None) -> GetMandateResponse:
        """
        Resource /v2/{merchantId}/mandates/{uniqueMandateReference}/revoke - Revoke mandate


        :param unique_mandate_reference: str
        :param context: :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.get_mandate_response.GetMandateResponse`
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
            "uniqueMandateReference": unique_mandate_reference,
        }
        uri = self._instantiate_uri("/v2/{merchantId}/mandates/{uniqueMandateReference}/revoke", path_context)
        try:
            return self._communicator.post(
                uri,
                self._client_headers,
                None,
                None,
                GetMandateResponse,
                context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

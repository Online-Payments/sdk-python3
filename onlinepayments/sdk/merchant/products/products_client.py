#
# This class was auto-generated.
#
from onlinepayments.sdk.api_resource import ApiResource
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.response_exception import ResponseException
from onlinepayments.sdk.domain.error_response import ErrorResponse
from onlinepayments.sdk.domain.get_payment_products_response import GetPaymentProductsResponse
from onlinepayments.sdk.domain.payment_product import PaymentProduct
from onlinepayments.sdk.domain.payment_product_networks_response import PaymentProductNetworksResponse
from onlinepayments.sdk.domain.product_directory import ProductDirectory
from onlinepayments.sdk.merchant.products.get_payment_product_networks_params import GetPaymentProductNetworksParams
from onlinepayments.sdk.merchant.products.get_payment_product_params import GetPaymentProductParams
from onlinepayments.sdk.merchant.products.get_payment_products_params import GetPaymentProductsParams
from onlinepayments.sdk.merchant.products.get_product_directory_params import GetProductDirectoryParams
from onlinepayments.sdk.merchant.products.i_products_client import IProductsClient


class ProductsClient(ApiResource, IProductsClient):
    """
    Products client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`onlinepayments.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(ProductsClient, self).__init__(parent, path_context)

    def get_payment_products(self, query: GetPaymentProductsParams, context: CallContext = None) -> GetPaymentProductsResponse:
        """
        Resource /v2/{merchantId}/products - Get payment products


        :param query: :class:`onlinepayments.sdk.merchant.products.get_payment_products_params.GetPaymentProductsParams`
        :param context: :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.get_payment_products_response.GetPaymentProductsResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: PaymentPlatformException if something went wrong at the payment platform,
                   the payment platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the payment platform returned any other error
        """
        uri = self._instantiate_uri("/v2/{merchantId}/products", None)
        try:
            return self._communicator.get(
                uri,
                self._client_headers,
                query,
                GetPaymentProductsResponse,
                context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get_payment_product(self, payment_product_id: int, query: GetPaymentProductParams, context: CallContext = None) -> PaymentProduct:
        """
        Resource /v2/{merchantId}/products/{paymentProductId} - Get payment product


        :param payment_product_id: int
        :param query: :class:`onlinepayments.sdk.merchant.products.get_payment_product_params.GetPaymentProductParams`
        :param context: :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.payment_product.PaymentProduct`
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
            "paymentProductId": str(payment_product_id),
        }
        uri = self._instantiate_uri("/v2/{merchantId}/products/{paymentProductId}", path_context)
        try:
            return self._communicator.get(
                uri,
                self._client_headers,
                query,
                PaymentProduct,
                context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get_product_directory(self, payment_product_id: int, query: GetProductDirectoryParams, context: CallContext = None) -> ProductDirectory:
        """
        Resource /v2/{merchantId}/products/{paymentProductId}/directory - Get payment product directory


        :param payment_product_id: int
        :param query: :class:`onlinepayments.sdk.merchant.products.get_product_directory_params.GetProductDirectoryParams`
        :param context: :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.product_directory.ProductDirectory`
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
            "paymentProductId": str(payment_product_id),
        }
        uri = self._instantiate_uri("/v2/{merchantId}/products/{paymentProductId}/directory", path_context)
        try:
            return self._communicator.get(
                uri,
                self._client_headers,
                query,
                ProductDirectory,
                context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get_payment_product_networks(self, payment_product_id: int, query: GetPaymentProductNetworksParams, context: CallContext = None) -> PaymentProductNetworksResponse:
        """
        Resource /v2/{merchantId}/products/{paymentProductId}/networks - Get payment product networks


        :param payment_product_id: int
        :param query: :class:`onlinepayments.sdk.merchant.products.get_payment_product_networks_params.GetPaymentProductNetworksParams`
        :param context: :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.payment_product_networks_response.PaymentProductNetworksResponse`
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
            "paymentProductId": str(payment_product_id),
        }
        uri = self._instantiate_uri("/v2/{merchantId}/products/{paymentProductId}/networks", path_context)
        try:
            return self._communicator.get(
                uri,
                self._client_headers,
                query,
                PaymentProductNetworksResponse,
                context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Mapping, Optional

from .get_product_group_params import GetProductGroupParams
from .get_product_groups_params import GetProductGroupsParams
from .i_product_groups_client import IProductGroupsClient

from onlinepayments.sdk.api_resource import ApiResource
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.communication.response_exception import ResponseException
from onlinepayments.sdk.domain.error_response import ErrorResponse
from onlinepayments.sdk.domain.get_payment_product_groups_response import GetPaymentProductGroupsResponse
from onlinepayments.sdk.domain.payment_product_group import PaymentProductGroup
from onlinepayments.sdk.exception_factory import create_exception


class ProductGroupsClient(ApiResource, IProductGroupsClient):
    """
    ProductGroups client. Thread-safe.
    """

    def __init__(self, parent: ApiResource, path_context: Optional[Mapping[str, str]]):
        """
        :param parent:       :class:`onlinepayments.sdk.api_resource.ApiResource`
        :param path_context: Mapping[str, str]
        """
        super(ProductGroupsClient, self).__init__(parent=parent, path_context=path_context)

    def get_product_groups(self, query: GetProductGroupsParams, context: Optional[CallContext] = None) -> GetPaymentProductGroupsResponse:
        """
        Resource /v2/{merchantId}/productgroups - Get product groups

        :param query:    :class:`onlinepayments.sdk.merchant.productgroups.get_product_groups_params.GetProductGroupsParams`
        :param context:  :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.get_payment_product_groups_response.GetPaymentProductGroupsResponse`
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
        uri = self._instantiate_uri("/v2/{merchantId}/productgroups", None)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    GetPaymentProductGroupsResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

    def get_product_group(self, payment_product_group_id: str, query: GetProductGroupParams, context: Optional[CallContext] = None) -> PaymentProductGroup:
        """
        Resource /v2/{merchantId}/productgroups/{paymentProductGroupId} - Get product group

        :param payment_product_group_id:  str
        :param query:                     :class:`onlinepayments.sdk.merchant.productgroups.get_product_group_params.GetProductGroupParams`
        :param context:                   :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.payment_product_group.PaymentProductGroup`
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
            "paymentProductGroupId": payment_product_group_id,
        }
        uri = self._instantiate_uri("/v2/{merchantId}/productgroups/{paymentProductGroupId}", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    PaymentProductGroup,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

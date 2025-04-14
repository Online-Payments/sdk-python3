# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from abc import ABC, abstractmethod
from typing import Optional

from .get_product_group_params import GetProductGroupParams
from .get_product_groups_params import GetProductGroupsParams

from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.domain.get_payment_product_groups_response import GetPaymentProductGroupsResponse
from onlinepayments.sdk.domain.payment_product_group import PaymentProductGroup


class IProductGroupsClient(ABC):
    """
    ProductGroups client interface. Thread-safe.
    """

    @abstractmethod
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

    @abstractmethod
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

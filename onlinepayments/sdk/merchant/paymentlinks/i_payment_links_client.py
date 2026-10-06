# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from abc import ABC, abstractmethod
from typing import Optional

from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.domain.create_payment_link_request import CreatePaymentLinkRequest
from onlinepayments.sdk.domain.get_payment_links_by_merchant_group_request import GetPaymentLinksByMerchantGroupRequest
from onlinepayments.sdk.domain.payment_link_overview_response import PaymentLinkOverviewResponse
from onlinepayments.sdk.domain.payment_link_response import PaymentLinkResponse
from onlinepayments.sdk.domain.share_payment_link_request import SharePaymentLinkRequest


class IPaymentLinksClient(ABC):
    """
    PaymentLinks client interface. Thread-safe.
    """

    @abstractmethod
    def share(self, payment_link_id: str, body: SharePaymentLinkRequest, context: Optional[CallContext] = None) -> None:
        """
        Resource /v2/{merchantId}/paymentlinks/{paymentLinkId}/share - Share the specified payment link to a customer.

        :param payment_link_id:  str
        :param body:             :class:`onlinepayments.sdk.domain.share_payment_link_request.SharePaymentLinkRequest`
        :param context:          :class:`onlinepayments.sdk.call_context.CallContext`
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

    @abstractmethod
    def create_payment_link(self, body: CreatePaymentLinkRequest, context: Optional[CallContext] = None) -> PaymentLinkResponse:
        """
        Resource /v2/{merchantId}/paymentlinks - Create payment link

        :param body:     :class:`onlinepayments.sdk.domain.create_payment_link_request.CreatePaymentLinkRequest`
        :param context:  :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.payment_link_response.PaymentLinkResponse`
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
    def get_payment_links_by_merchant_group_id(self, merchant_group_id: str, body: GetPaymentLinksByMerchantGroupRequest, context: Optional[CallContext] = None) -> PaymentLinkOverviewResponse:
        """
        Resource /v2/merchant-groups/{merchantGroupId}/paymentlinks/search - Retrieve payment links for a merchant group

        :param merchant_group_id:  str
        :param body:               :class:`onlinepayments.sdk.domain.get_payment_links_by_merchant_group_request.GetPaymentLinksByMerchantGroupRequest`
        :param context:            :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.payment_link_overview_response.PaymentLinkOverviewResponse`
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
    def get_payment_link_by_id(self, payment_link_id: str, context: Optional[CallContext] = None) -> PaymentLinkResponse:
        """
        Resource /v2/{merchantId}/paymentlinks/{paymentLinkId} - Get payment link by ID

        :param payment_link_id:  str
        :param context:          :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.payment_link_response.PaymentLinkResponse`
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
    def cancel_payment_link_by_id(self, payment_link_id: str, context: Optional[CallContext] = None) -> None:
        """
        Resource /v2/{merchantId}/paymentlinks/{paymentLinkId}/cancel - Cancel PaymentLink by ID

        :param payment_link_id:  str
        :param context:          :class:`onlinepayments.sdk.call_context.CallContext`
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

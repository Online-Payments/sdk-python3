# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Mapping, Optional

from .i_merchant_client import IMerchantClient

from onlinepayments.sdk.api_resource import ApiResource
from onlinepayments.sdk.merchant.captures.captures_client import CapturesClient
from onlinepayments.sdk.merchant.captures.i_captures_client import ICapturesClient
from onlinepayments.sdk.merchant.complete.complete_client import CompleteClient
from onlinepayments.sdk.merchant.complete.i_complete_client import ICompleteClient
from onlinepayments.sdk.merchant.hostedcheckout.hosted_checkout_client import HostedCheckoutClient
from onlinepayments.sdk.merchant.hostedcheckout.i_hosted_checkout_client import IHostedCheckoutClient
from onlinepayments.sdk.merchant.hostedtokenization.hosted_tokenization_client import HostedTokenizationClient
from onlinepayments.sdk.merchant.hostedtokenization.i_hosted_tokenization_client import IHostedTokenizationClient
from onlinepayments.sdk.merchant.mandates.i_mandates_client import IMandatesClient
from onlinepayments.sdk.merchant.mandates.mandates_client import MandatesClient
from onlinepayments.sdk.merchant.paymentlinks.i_payment_links_client import IPaymentLinksClient
from onlinepayments.sdk.merchant.paymentlinks.payment_links_client import PaymentLinksClient
from onlinepayments.sdk.merchant.payments.i_payments_client import IPaymentsClient
from onlinepayments.sdk.merchant.payments.payments_client import PaymentsClient
from onlinepayments.sdk.merchant.payouts.i_payouts_client import IPayoutsClient
from onlinepayments.sdk.merchant.payouts.payouts_client import PayoutsClient
from onlinepayments.sdk.merchant.privacypolicy.i_privacy_policy_client import IPrivacyPolicyClient
from onlinepayments.sdk.merchant.privacypolicy.privacy_policy_client import PrivacyPolicyClient
from onlinepayments.sdk.merchant.productgroups.i_product_groups_client import IProductGroupsClient
from onlinepayments.sdk.merchant.productgroups.product_groups_client import ProductGroupsClient
from onlinepayments.sdk.merchant.products.i_products_client import IProductsClient
from onlinepayments.sdk.merchant.products.products_client import ProductsClient
from onlinepayments.sdk.merchant.refunds.i_refunds_client import IRefundsClient
from onlinepayments.sdk.merchant.refunds.refunds_client import RefundsClient
from onlinepayments.sdk.merchant.services.i_services_client import IServicesClient
from onlinepayments.sdk.merchant.services.services_client import ServicesClient
from onlinepayments.sdk.merchant.sessions.i_sessions_client import ISessionsClient
from onlinepayments.sdk.merchant.sessions.sessions_client import SessionsClient
from onlinepayments.sdk.merchant.tokens.i_tokens_client import ITokensClient
from onlinepayments.sdk.merchant.tokens.tokens_client import TokensClient
from onlinepayments.sdk.merchant.webhooks.i_webhooks_client import IWebhooksClient
from onlinepayments.sdk.merchant.webhooks.webhooks_client import WebhooksClient


class MerchantClient(ApiResource, IMerchantClient):
    """
    Merchant client. Thread-safe.
    """

    def __init__(self, parent: ApiResource, path_context: Optional[Mapping[str, str]]):
        """
        :param parent:       :class:`onlinepayments.sdk.api_resource.ApiResource`
        :param path_context: Mapping[str, str]
        """
        super(MerchantClient, self).__init__(parent=parent, path_context=path_context)

    def hosted_checkout(self) -> IHostedCheckoutClient:
        """
        Resource /v2/{merchantId}/hostedcheckouts

        :return: :class:`onlinepayments.sdk.merchant.hostedcheckout.i_hosted_checkout_client.IHostedCheckoutClient`
        """
        return HostedCheckoutClient(self, None)

    def hosted_tokenization(self) -> IHostedTokenizationClient:
        """
        Resource /v2/{merchantId}/hostedtokenizations

        :return: :class:`onlinepayments.sdk.merchant.hostedtokenization.i_hosted_tokenization_client.IHostedTokenizationClient`
        """
        return HostedTokenizationClient(self, None)

    def payments(self) -> IPaymentsClient:
        """
        Resource /v2/{merchantId}/payments

        :return: :class:`onlinepayments.sdk.merchant.payments.i_payments_client.IPaymentsClient`
        """
        return PaymentsClient(self, None)

    def captures(self) -> ICapturesClient:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/captures

        :return: :class:`onlinepayments.sdk.merchant.captures.i_captures_client.ICapturesClient`
        """
        return CapturesClient(self, None)

    def refunds(self) -> IRefundsClient:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/refunds

        :return: :class:`onlinepayments.sdk.merchant.refunds.i_refunds_client.IRefundsClient`
        """
        return RefundsClient(self, None)

    def complete(self) -> ICompleteClient:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/complete

        :return: :class:`onlinepayments.sdk.merchant.complete.i_complete_client.ICompleteClient`
        """
        return CompleteClient(self, None)

    def product_groups(self) -> IProductGroupsClient:
        """
        Resource /v2/{merchantId}/productgroups

        :return: :class:`onlinepayments.sdk.merchant.productgroups.i_product_groups_client.IProductGroupsClient`
        """
        return ProductGroupsClient(self, None)

    def products(self) -> IProductsClient:
        """
        Resource /v2/{merchantId}/products

        :return: :class:`onlinepayments.sdk.merchant.products.i_products_client.IProductsClient`
        """
        return ProductsClient(self, None)

    def services(self) -> IServicesClient:
        """
        Resource /v2/{merchantId}/services/testconnection

        :return: :class:`onlinepayments.sdk.merchant.services.i_services_client.IServicesClient`
        """
        return ServicesClient(self, None)

    def webhooks(self) -> IWebhooksClient:
        """
        Resource /v2/{merchantId}/webhooks/validateCredentials

        :return: :class:`onlinepayments.sdk.merchant.webhooks.i_webhooks_client.IWebhooksClient`
        """
        return WebhooksClient(self, None)

    def sessions(self) -> ISessionsClient:
        """
        Resource /v2/{merchantId}/sessions

        :return: :class:`onlinepayments.sdk.merchant.sessions.i_sessions_client.ISessionsClient`
        """
        return SessionsClient(self, None)

    def tokens(self) -> ITokensClient:
        """
        Resource /v2/{merchantId}/tokens/{tokenId}

        :return: :class:`onlinepayments.sdk.merchant.tokens.i_tokens_client.ITokensClient`
        """
        return TokensClient(self, None)

    def payouts(self) -> IPayoutsClient:
        """
        Resource /v2/{merchantId}/payouts/{payoutId}

        :return: :class:`onlinepayments.sdk.merchant.payouts.i_payouts_client.IPayoutsClient`
        """
        return PayoutsClient(self, None)

    def mandates(self) -> IMandatesClient:
        """
        Resource /v2/{merchantId}/mandates

        :return: :class:`onlinepayments.sdk.merchant.mandates.i_mandates_client.IMandatesClient`
        """
        return MandatesClient(self, None)

    def privacy_policy(self) -> IPrivacyPolicyClient:
        """
        Resource /v2/{merchantId}/services/privacypolicy

        :return: :class:`onlinepayments.sdk.merchant.privacypolicy.i_privacy_policy_client.IPrivacyPolicyClient`
        """
        return PrivacyPolicyClient(self, None)

    def payment_links(self) -> IPaymentLinksClient:
        """
        Resource /v2/{merchantId}/paymentlinks

        :return: :class:`onlinepayments.sdk.merchant.paymentlinks.i_payment_links_client.IPaymentLinksClient`
        """
        return PaymentLinksClient(self, None)

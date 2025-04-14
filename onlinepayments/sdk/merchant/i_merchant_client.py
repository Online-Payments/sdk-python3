# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from abc import ABC, abstractmethod
from typing import Optional

from onlinepayments.sdk.merchant.captures.i_captures_client import ICapturesClient
from onlinepayments.sdk.merchant.complete.i_complete_client import ICompleteClient
from onlinepayments.sdk.merchant.hostedcheckout.i_hosted_checkout_client import IHostedCheckoutClient
from onlinepayments.sdk.merchant.hostedtokenization.i_hosted_tokenization_client import IHostedTokenizationClient
from onlinepayments.sdk.merchant.mandates.i_mandates_client import IMandatesClient
from onlinepayments.sdk.merchant.paymentlinks.i_payment_links_client import IPaymentLinksClient
from onlinepayments.sdk.merchant.payments.i_payments_client import IPaymentsClient
from onlinepayments.sdk.merchant.payouts.i_payouts_client import IPayoutsClient
from onlinepayments.sdk.merchant.privacypolicy.i_privacy_policy_client import IPrivacyPolicyClient
from onlinepayments.sdk.merchant.productgroups.i_product_groups_client import IProductGroupsClient
from onlinepayments.sdk.merchant.products.i_products_client import IProductsClient
from onlinepayments.sdk.merchant.refunds.i_refunds_client import IRefundsClient
from onlinepayments.sdk.merchant.services.i_services_client import IServicesClient
from onlinepayments.sdk.merchant.sessions.i_sessions_client import ISessionsClient
from onlinepayments.sdk.merchant.tokens.i_tokens_client import ITokensClient
from onlinepayments.sdk.merchant.webhooks.i_webhooks_client import IWebhooksClient


class IMerchantClient(ABC):
    """
    Merchant client interface. Thread-safe.
    """

    @abstractmethod
    def hosted_checkout(self) -> IHostedCheckoutClient:
        """
        Resource /v2/{merchantId}/hostedcheckouts

        :return: :class:`onlinepayments.sdk.merchant.hostedcheckout.i_hosted_checkout_client.IHostedCheckoutClient`
        """

    @abstractmethod
    def hosted_tokenization(self) -> IHostedTokenizationClient:
        """
        Resource /v2/{merchantId}/hostedtokenizations

        :return: :class:`onlinepayments.sdk.merchant.hostedtokenization.i_hosted_tokenization_client.IHostedTokenizationClient`
        """

    @abstractmethod
    def payments(self) -> IPaymentsClient:
        """
        Resource /v2/{merchantId}/payments

        :return: :class:`onlinepayments.sdk.merchant.payments.i_payments_client.IPaymentsClient`
        """

    @abstractmethod
    def captures(self) -> ICapturesClient:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/captures

        :return: :class:`onlinepayments.sdk.merchant.captures.i_captures_client.ICapturesClient`
        """

    @abstractmethod
    def refunds(self) -> IRefundsClient:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/refunds

        :return: :class:`onlinepayments.sdk.merchant.refunds.i_refunds_client.IRefundsClient`
        """

    @abstractmethod
    def complete(self) -> ICompleteClient:
        """
        Resource /v2/{merchantId}/payments/{paymentId}/complete

        :return: :class:`onlinepayments.sdk.merchant.complete.i_complete_client.ICompleteClient`
        """

    @abstractmethod
    def product_groups(self) -> IProductGroupsClient:
        """
        Resource /v2/{merchantId}/productgroups

        :return: :class:`onlinepayments.sdk.merchant.productgroups.i_product_groups_client.IProductGroupsClient`
        """

    @abstractmethod
    def products(self) -> IProductsClient:
        """
        Resource /v2/{merchantId}/products

        :return: :class:`onlinepayments.sdk.merchant.products.i_products_client.IProductsClient`
        """

    @abstractmethod
    def services(self) -> IServicesClient:
        """
        Resource /v2/{merchantId}/services/testconnection

        :return: :class:`onlinepayments.sdk.merchant.services.i_services_client.IServicesClient`
        """

    @abstractmethod
    def webhooks(self) -> IWebhooksClient:
        """
        Resource /v2/{merchantId}/webhooks/validateCredentials

        :return: :class:`onlinepayments.sdk.merchant.webhooks.i_webhooks_client.IWebhooksClient`
        """

    @abstractmethod
    def sessions(self) -> ISessionsClient:
        """
        Resource /v2/{merchantId}/sessions

        :return: :class:`onlinepayments.sdk.merchant.sessions.i_sessions_client.ISessionsClient`
        """

    @abstractmethod
    def tokens(self) -> ITokensClient:
        """
        Resource /v2/{merchantId}/tokens/{tokenId}

        :return: :class:`onlinepayments.sdk.merchant.tokens.i_tokens_client.ITokensClient`
        """

    @abstractmethod
    def payouts(self) -> IPayoutsClient:
        """
        Resource /v2/{merchantId}/payouts/{payoutId}

        :return: :class:`onlinepayments.sdk.merchant.payouts.i_payouts_client.IPayoutsClient`
        """

    @abstractmethod
    def mandates(self) -> IMandatesClient:
        """
        Resource /v2/{merchantId}/mandates

        :return: :class:`onlinepayments.sdk.merchant.mandates.i_mandates_client.IMandatesClient`
        """

    @abstractmethod
    def privacy_policy(self) -> IPrivacyPolicyClient:
        """
        Resource /v2/{merchantId}/services/privacypolicy

        :return: :class:`onlinepayments.sdk.merchant.privacypolicy.i_privacy_policy_client.IPrivacyPolicyClient`
        """

    @abstractmethod
    def payment_links(self) -> IPaymentLinksClient:
        """
        Resource /v2/{merchantId}/paymentlinks

        :return: :class:`onlinepayments.sdk.merchant.paymentlinks.i_payment_links_client.IPaymentLinksClient`
        """

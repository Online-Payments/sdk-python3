#
# This class was auto-generated.
#
from onlinepayments.sdk.api_resource import ApiResource
from onlinepayments.sdk.merchant.i_merchant_client import IMerchantClient
from onlinepayments.sdk.merchant.hostedcheckout.hosted_checkout_client import HostedCheckoutClient
from onlinepayments.sdk.merchant.hostedtokenization.hosted_tokenization_client import HostedTokenizationClient
from onlinepayments.sdk.merchant.mandates.mandates_client import MandatesClient
from onlinepayments.sdk.merchant.payments.payments_client import PaymentsClient
from onlinepayments.sdk.merchant.payouts.payouts_client import PayoutsClient
from onlinepayments.sdk.merchant.productgroups.product_groups_client import ProductGroupsClient
from onlinepayments.sdk.merchant.products.products_client import ProductsClient
from onlinepayments.sdk.merchant.services.services_client import ServicesClient
from onlinepayments.sdk.merchant.sessions.sessions_client import SessionsClient
from onlinepayments.sdk.merchant.tokens.tokens_client import TokensClient


class MerchantClient(ApiResource, IMerchantClient):
    """
    Merchant client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`onlinepayments.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(MerchantClient, self).__init__(parent, path_context)

    def hosted_checkout(self) -> HostedCheckoutClient:
        """
        Resource /v2/{merchantId}/hostedcheckouts

        :return: :class:`onlinepayments.sdk.merchant.hostedcheckout.i_hosted_checkout_client.IHostedCheckoutClient`
        """
        return HostedCheckoutClient(self, None)

    def hosted_tokenization(self) -> HostedTokenizationClient:
        """
        Resource /v2/{merchantId}/hostedtokenizations

        :return: :class:`onlinepayments.sdk.merchant.hostedtokenization.i_hosted_tokenization_client.IHostedTokenizationClient`
        """
        return HostedTokenizationClient(self, None)

    def mandates(self) -> MandatesClient:
        """
        Resource /v2/{merchantId}/mandates

        :return: :class:`onlinepayments.sdk.merchant.mandates.i_mandates_client.IMandatesClient`
        """
        return MandatesClient(self, None)

    def payments(self) -> PaymentsClient:
        """
        Resource /v2/{merchantId}/payments

        :return: :class:`onlinepayments.sdk.merchant.payments.i_payments_client.IPaymentsClient`
        """
        return PaymentsClient(self, None)

    def payouts(self) -> PayoutsClient:
        """
        Resource /v2/{merchantId}/payouts

        :return: :class:`onlinepayments.sdk.merchant.payouts.i_payouts_client.IPayoutsClient`
        """
        return PayoutsClient(self, None)

    def product_groups(self) -> ProductGroupsClient:
        """
        Resource /v2/{merchantId}/productgroups

        :return: :class:`onlinepayments.sdk.merchant.productgroups.i_product_groups_client.IProductGroupsClient`
        """
        return ProductGroupsClient(self, None)

    def products(self) -> ProductsClient:
        """
        Resource /v2/{merchantId}/products

        :return: :class:`onlinepayments.sdk.merchant.products.i_products_client.IProductsClient`
        """
        return ProductsClient(self, None)

    def services(self) -> ServicesClient:
        """
        Resource /v2/{merchantId}/services

        :return: :class:`onlinepayments.sdk.merchant.services.i_services_client.IServicesClient`
        """
        return ServicesClient(self, None)

    def sessions(self) -> SessionsClient:
        """
        Resource /v2/{merchantId}/sessions

        :return: :class:`onlinepayments.sdk.merchant.sessions.i_sessions_client.ISessionsClient`
        """
        return SessionsClient(self, None)

    def tokens(self) -> TokensClient:
        """
        Resource /v2/{merchantId}/tokens

        :return: :class:`onlinepayments.sdk.merchant.tokens.i_tokens_client.ITokensClient`
        """
        return TokensClient(self, None)

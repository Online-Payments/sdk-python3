import os
from urllib.parse import urlparse

from onlinepayments.sdk.authentication.authorization_type import AuthorizationType
from onlinepayments.sdk.communicator_configuration import CommunicatorConfiguration
from onlinepayments.sdk.factory import Factory
from onlinepayments.sdk.i_client import IClient
from onlinepayments.sdk.merchant.i_merchant_client import IMerchantClient


# [START client-setup]
# Create the client once when the application starts, reuse it for every request and close it on shutdown.
def create_client() -> IClient:
    configuration = CommunicatorConfiguration(
        # Test or live endpoint host, e.g. payment.direct.ecom.preprod.worldline-solutions.com (without a path).
        api_endpoint="https://" + required_env("onlinePayments_api_endpoint_host"),
        api_key_id=required_env("onlinePayments_api_v1hmac_apiKeyId"),
        secret_api_key=required_env("onlinePayments_api_v1hmac_secretApiKey"),
        # Required: without it, creating the client fails.
        authorization_type=AuthorizationType.V1HMAC,
        # Required: your company or application name; it identifies your requests in the platform logs.
        # The SDK raises ValueError("integrator is required") without it; reading it with required_env fails
        # at startup with a message that names the setting.
        integrator=required_env("onlinePayments_api_integrator"),
        # Required, in seconds.
        connect_timeout=5,
        socket_timeout=300,
        # Required: the size of the connection pool. Without it, the first API call fails.
        max_connections=CommunicatorConfiguration.DEFAULT_MAX_CONNECTIONS,
    )
    return Factory.create_client_from_configuration(configuration)


# The merchant ID is your PSPID. All API calls start from the merchant client.
def create_merchant_client(client: IClient) -> IMerchantClient:
    return client.merchant(required_env("onlinePayments_api_merchantId"))


# The absolute public base URL of your shop, e.g. https://shop.example. The return URL is built from it, never from
# the request's Host header, which the sender controls. Use https in production.
def required_public_base_url() -> str:
    value = required_env("shop_publicBaseUrl")
    parsed = urlparse(value)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise RuntimeError("shop_publicBaseUrl must be an absolute http(s) URL, e.g. https://shop.example")
    return value


# Read credentials from a secret store of your platform. For local development only, environment variables or a
# file outside the repository work too. Never hard-code them. Check every value once at startup and fail fast:
# a blank value is as wrong as a missing one.
def required_env(name: str) -> str:
    value = os.environ.get(name)
    if value is None or not value.strip():
        raise RuntimeError(f"Environment variable {name} is not set")
    return value.strip()
# [END client-setup]

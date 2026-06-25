import uuid

from tests.integration.init_utils import MERCHANT_ID
from tests.integration.builders.common.create_payment_request_builder import CreatePaymentRequestBuilder
from tests.integration.builders.common.create_token_request_builder import CreateTokenRequestBuilder
from tests.integration.builders.mandates.create_mandate_request_builder import CreateMandateRequestBuilder
from tests.integration.builders.merchant_batch.submit_batch_request_body_builder import SubmitBatchRequestBodyBuilder
from tests.integration.builders.payouts.create_payout_request_builder import CreatePayoutRequestBuilder
from tests.integration.builders.paymentlinks.create_payment_link_request_builder import CreatePaymentLinkRequestBuilder
from tests.integration.builders.hostedtokenization.create_hosted_tokenization_request_builder import CreateHostedTokenizationRequestBuilder

def create_payment_and_get_id(client, amount=1000, currency="EUR"):
    request = CreatePaymentRequestBuilder() \
        .with_amount(amount) \
        .with_currency(currency) \
        .build()

    response = client.merchant(MERCHANT_ID).payments().create_payment(request)

    return response.payment.id

def _create_paypal_payment_and_get_id(client):
    response = client.merchant(MERCHANT_ID).payments().create_payment(
        CreatePaymentRequestBuilder().with_pay_pal_redirect_payment_method().build()
    )

    return response.payment.id


def submit_batch_and_get_reference(client, operation_type, item_count, create_payment_requests):
    request = SubmitBatchRequestBodyBuilder() \
        .with_operation_type(operation_type) \
        .with_item_count(item_count) \
        .with_create_payment_requests(create_payment_requests) \
        .build()

    response = client.merchant(MERCHANT_ID).merchant_batch().submit_batch(request)

    return response.merchant_batch_reference


def create_payout_and_get_id(client):
    response = client.merchant(MERCHANT_ID).payouts().create_payout(
        CreatePayoutRequestBuilder().build()
    )

    return response.id


def create_mandate_and_get_reference(client):
    response = client.merchant(MERCHANT_ID).mandates().create_mandate(
        CreateMandateRequestBuilder()
        .with_unique_mandate_reference(uuid.uuid4().hex[:35])
        .build()
    )

    return response.mandate.unique_mandate_reference


def create_token_and_get_id(client):
    response = client.merchant(MERCHANT_ID).tokens().create_token(
        CreateTokenRequestBuilder().build()
    )

    return response.token

def create_payment_link_and_get_id(client):
    response = client.merchant(MERCHANT_ID).payment_links().create_payment_link(
        CreatePaymentLinkRequestBuilder().build()
    )

    return response.payment_link_id


def create_hosted_tokenization_and_get_id(client):
    response = client.merchant(MERCHANT_ID).hosted_tokenization().create_hosted_tokenization(
        CreateHostedTokenizationRequestBuilder().build()
    )

    return response.hosted_tokenization_id

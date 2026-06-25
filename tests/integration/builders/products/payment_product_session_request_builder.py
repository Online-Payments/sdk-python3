from onlinepayments.sdk.domain.payment_product_session302_specific_input import PaymentProductSession302SpecificInput
from onlinepayments.sdk.domain.payment_product_session_request import PaymentProductSessionRequest


class PaymentProductSessionRequestBuilder:

    def __init__(self):
        self._display_name = "Test Merchant"
        self._domain_name = "example.com"

    def with_display_name(self, display_name):
        self._display_name = display_name
        return self

    def with_domain_name(self, domain_name):
        self._domain_name = domain_name
        return self

    def build(self):
        specific_input = PaymentProductSession302SpecificInput()
        specific_input.display_name = self._display_name
        specific_input.domain_name = self._domain_name

        request = PaymentProductSessionRequest()
        request.payment_product_session302_specific_input = specific_input

        return request

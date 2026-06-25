from onlinepayments.sdk.domain.capture_payment_request import CapturePaymentRequest


class CapturePaymentRequestBuilder:

    def __init__(self):
        self._amount = None
        self._is_final = None

    def with_amount(self, amount):
        self._amount = amount
        return self

    def with_is_final(self, is_final):
        self._is_final = is_final
        return self

    def build(self):
        request = CapturePaymentRequest()

        if self._amount is not None:
            request.amount = self._amount

        if self._is_final is not None:
            request.is_final = self._is_final

        return request

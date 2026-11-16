from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.cancel_payment_request import CancelPaymentRequest
from onlinepayments.sdk.domain.cancel_payment_response import CancelPaymentResponse
from onlinepayments.sdk.domain.capture_payment_request import CapturePaymentRequest
from onlinepayments.sdk.domain.capture_response import CaptureResponse
from onlinepayments.sdk.domain.refund_request import RefundRequest
from onlinepayments.sdk.domain.refund_response import RefundResponse
from onlinepayments.sdk.merchant.i_merchant_client import IMerchantClient


# Each method takes an idempotence key. Create it once per operation (e.g. when someone clicks "Refund") and store it.
# Pass the same key again if the request got no answer; see ErrorHandlingExample.
class AfterPaymentOperationsExample:

    def __init__(self, merchant: IMerchantClient):
        self.__merchant = merchant

    # [START capture-payment]
    # Captures an authorized payment (status PENDING_CAPTURE). Without an amount, the full amount is captured.
    def capture(self, payment_id: str, amount_in_cents: int, is_final: bool, idempotence_key: str) -> CaptureResponse:
        details = self.__merchant.payments().get_payment_details(payment_id)
        if details.status != "PENDING_CAPTURE":
            raise RuntimeError(f"Payment {payment_id} cannot be captured in status {details.status}")

        request = CapturePaymentRequest()
        request.amount = amount_in_cents
        # is_final = True: this capture is final, no further capture is accepted.
        request.is_final = is_final

        context = CallContext(idempotence_key=idempotence_key)
        return self.__merchant.payments().capture_payment(payment_id, request, context)
    # [END capture-payment]

    # [START refund-payment]
    # Refunds a captured payment, fully or partly.
    def refund(self, payment_id: str, amount_in_cents: int, currency_code: str, idempotence_key: str) -> RefundResponse:
        details = self.__merchant.payments().get_payment_details(payment_id)
        if details.status_output is None or details.status_output.is_refundable is not True:
            raise RuntimeError(f"Payment {payment_id} is not refundable in status {details.status}")

        amount_of_money = AmountOfMoney()
        amount_of_money.amount = amount_in_cents
        amount_of_money.currency_code = currency_code

        request = RefundRequest()
        request.amount_of_money = amount_of_money

        context = CallContext(idempotence_key=idempotence_key)
        # REFUND_REQUESTED: the platform is processing the refund and waiting for the result. The status then
        # becomes REFUNDED or REJECTED; treat the refund as done only when it is REFUNDED.
        return self.__merchant.payments().refund_payment(payment_id, request, context)
    # [END refund-payment]

    # [START cancel-payment]
    # Cancels (voids) an authorization that is not captured yet. No amount cancels the full amount.
    def cancel(self, payment_id: str, idempotence_key: str) -> CancelPaymentResponse:
        details = self.__merchant.payments().get_payment_details(payment_id)
        if details.status_output is None or details.status_output.is_cancellable is not True:
            raise RuntimeError(f"Payment {payment_id} is not cancellable in status {details.status}")

        context = CallContext(idempotence_key=idempotence_key)
        return self.__merchant.payments().cancel_payment(payment_id, CancelPaymentRequest(), context)
    # [END cancel-payment]

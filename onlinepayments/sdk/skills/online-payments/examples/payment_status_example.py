
from onlinepayments.sdk.domain.payment_status_output import PaymentStatusOutput
from onlinepayments.sdk.merchant.i_merchant_client import IMerchantClient

from app_types import OrderPaymentState, OrderStore


class PaymentStatusExample:

    def __init__(self, merchant: IMerchantClient, orders: OrderStore):
        self.__merchant = merchant
        self.__orders = orders

    # [START payment-status]
    def refresh_payment_state(self, order_id: str) -> OrderPaymentState:
        payment_id = self.__orders.get_payment_id(order_id)
        if payment_id is None:
            # No payment yet is not a failure. A webhook or your reconciliation job settles the order.
            return OrderPaymentState.PENDING
        details = self.__merchant.payments().get_payment_details(payment_id)

        state = PaymentStatusExample.to_order_state(details.status, details.status_output)
        self.__orders.save_state(order_id, state)
        return state

    # Decide on status_category. status and status_code give more detail.
    # status_output or status_category can be missing in a response: that ends in PENDING below, never in PAID.
    @staticmethod
    def to_order_state(status: str | None, status_output: PaymentStatusOutput | None) -> OrderPaymentState:
        category = status_output.status_category if status_output is not None else None
        if category == "COMPLETED":
            return OrderPaymentState.PAID
        if category == "PENDING_MERCHANT":
            # PENDING_CAPTURE: authorized but not captured yet, capture or cancel it.
            # Any other status (CANCELLED, waiting for its final result) is not final.
            if status == "PENDING_CAPTURE":
                return OrderPaymentState.AUTHORIZED
            return OrderPaymentState.PENDING
        if category == "REFUNDED":
            return OrderPaymentState.REFUNDED
        if category == "REVERSED":
            # Not paid: do not treat the order as paid.
            return OrderPaymentState.REVERSED
        if category == "UNSUCCESSFUL":
            return OrderPaymentState.CANCELLED if status == "CANCELLED" else OrderPaymentState.FAILED
        # CREATED, PENDING_PAYMENT, PENDING_CONNECT_OR_3RD_PARTY: not final.
        # Wait for a webhook or check again later.
        return OrderPaymentState.PENDING
    # [END payment-status]

from onlinepayments.sdk.domain.create_payment_response import CreatePaymentResponse

from app_types import OrderStore, PaymentStep
from payment_status_example import PaymentStatusExample


# [START payment-response-handle]
# Use for every create_payment response: server-to-server, Hosted Tokenization, Hosted Fields and client integration.
def handle_create_payment_response(response: CreatePaymentResponse, order_id: str, orders: OrderStore) -> PaymentStep:
    payment = response.payment
    if payment is None or payment.id is None:
        raise RuntimeError(f"The create payment response for order {order_id} has no payment")
    orders.save_payment_id(order_id, payment.id)

    action = response.merchant_action
    if action is not None and action.action_type == "REDIRECT" and action.redirect_data is not None \
            and action.redirect_data.redirect_url:
        # 3-D Secure challenge or a third-party page. Redirect to the URL exactly as returned.
        # The customer comes back on your return URL; then read the status with get_payment_details.
        return PaymentStep(redirect_url=action.redirect_data.redirect_url)

    # No customer action needed: the result is already known.
    state = PaymentStatusExample.to_order_state(payment.status, payment.status_output)
    orders.save_state(order_id, state)
    return PaymentStep(state=state)
# [END payment-response-handle]

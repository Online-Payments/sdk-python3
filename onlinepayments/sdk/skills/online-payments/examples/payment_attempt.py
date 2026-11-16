import uuid

from app_types import OrderStore


# [START payment-attempt-key]
# One idempotence key per payment attempt, stored with the order.
# Call start_payment_attempt when the customer begins to pay, for example when you show the payment form, and again
# before a new attempt after a decline or a rejected request. It stores the key before any create_payment call.
def start_payment_attempt(order_id: str, orders: OrderStore) -> str:
    key = str(uuid.uuid4())
    orders.save_idempotence_key(order_id, key)
    return key


# The request that creates the payment reads the stored key. A double submit, a retry after a timeout and a restart
# then send the same key, so the platform does not create a second payment.
def payment_attempt_key(order_id: str, orders: OrderStore) -> str:
    key = orders.get_idempotence_key(order_id)
    if key is None:
        raise RuntimeError(f"No payment attempt was started for order {order_id}")
    return key
# [END payment-attempt-key]

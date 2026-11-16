from onlinepayments.sdk.domain.web_hooks_event import WebhooksEvent
from onlinepayments.sdk.merchant.i_merchant_client import IMerchantClient

from app_types import OrderStore
from payment_status_example import PaymentStatusExample


class WebhookEventProcessor:

    def __init__(self, merchant: IMerchantClient, orders: OrderStore):
        self.__merchant = merchant
        self.__orders = orders

    # [START webhooks-process]
    # Runs in a background job for events saved in the inbox; retry it when it fails. Events can arrive twice and
    # out of order, so read the current status instead of trusting the event; repeating this is harmless.
    def process(self, webhooks_event: WebhooksEvent) -> None:
        payment = webhooks_event.payment
        if payment is None or payment.id is None:
            # Refund, payment link, payout and token events carry other objects, e.g. webhooks_event.refund.
            return

        output = payment.payment_output
        references = output.references if output is not None else None
        order_id = references.merchant_reference if references is not None else None
        if not order_id:
            return

        details = self.__merchant.payments().get_payment_details(payment.id)
        self.__orders.save_payment_id(order_id, details.id or payment.id)
        self.__orders.save_state(order_id, PaymentStatusExample.to_order_state(details.status, details.status_output))
    # [END webhooks-process]

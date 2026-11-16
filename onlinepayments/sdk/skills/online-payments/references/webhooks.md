# Webhooks

The platform sends an HTTP POST to your endpoint when a payment, refund, payment link, payout or token changes.
Webhooks are how you learn the result when the customer never returns to your site, and how you learn about changes
made later (captures, refunds, chargebacks).

## Set up

1. In the Merchant Portal, go to Developer > Webhooks. Generate the webhook key ID and secret, and enter your
   endpoint URL (HTTPS). The secret is displayed for 60 seconds only: store it at once. Generating a new pair
   revokes the existing one immediately.
2. Store the key ID and secret like the API secret: configuration or a secret store, never in code.
3. You can also send up to five endpoint URLs with each request in `feedbacks.webhooksUrls`;
   `feedbacks.webhookUrl` is deprecated.
4. Let the platform reach your endpoint: whitelist its IP range in your firewall (see the Firewall documentation on
   the documentation portal).
5. Create the SDK's webhooks helper once at startup with a secret key store that holds the key ID and secret.
6. Check the setup with the `ValidateWebhookCredentials` operation (your key and secret) and the `SendTestWebhook`
   operation (a test event, type `payment.test`; your endpoint must answer 2xx).

```python
# Create the helper once. The key ID and secret come from the Merchant Portal (Developer > Webhooks).
# required_env fails at startup when a value is missing or blank. Keep the secret in your secret store, or for local
# development in an environment variable; never in the repository.
# In production you can pass your own SecretKeyStore subclass with get_secret_key(key_id) on top of your secret storage.
def create_webhooks_helper() -> WebhooksHelper:
    secret_key_store = InMemorySecretKeyStore.instance()
    secret_key_store.store_secret_key(required_env("onlinePayments_webhooks_keyId"),
                                      required_env("onlinePayments_webhooks_secret"))
    return WebhooksHelper(DefaultMarshaller.instance(), secret_key_store)
```

## Receive

Mandatory rule 4: verify every webhook with the SDK's webhooks helper before processing the event.

1. Read the raw request body as bytes or an unchanged string. The signature is calculated over the exact body; a
   body that was parsed and serialised again fails verification.
2. Pass the body and all request headers to the helper. It checks the `X-GCS-Signature` and `X-GCS-KeyId` headers
   and returns the parsed event. A repeated `X-GCS-Signature` or `X-GCS-KeyId` must fail verification, so never pass
   only the first value of a header. How to pass a repeated header depends on the helper: see `python3.md`.
3. If verification fails, answer with an error status and do not process the event. Do not add a way to skip
   verification, such as a configuration flag or a check for the development environment. For local testing, use a
   test webhook key ID and secret from the Merchant Portal, or send a test event with SendTestWebhook; both go
   through normal verification.
4. Save the verified event before you answer: a database row or a persistent queue, ignoring duplicates (the
   webhooks guide identifies a duplicate by identical `payment.id` and `type`). Then answer with HTTP 2xx right away,
   as the guide recommends, and do the work in the background. Do nothing else before the answer.
5. If the event passed verification but the SDK cannot read it (API version mismatch, malformed body), the sender
   is the platform, so do not answer with an error status. Save the raw body, log it with an alert, and answer 2xx.
   A retry would send the same body and fail the same way; the saved body can be replayed after you upgrade the
   SDK. Only a failed verification gets an error status.

When the platform gets no 2xx answer in time, it sends the event again: after 10 minutes, 1 hour, 2 hours, 8 hours
and 24 hours. Each delivery has a `retry-count` header: 0 for the first attempt, higher for a retry. Log it; it
tells a new event from a retry. A 2xx tells the platform the event arrived, so do not count on another delivery after
you answered 2xx. An event that is only in memory when the process dies can be lost, and retrying failed background
work does not make the platform send it again. Keep your own retry for saved events that failed. The guide also
recommends a back-up mechanism, so run a reconciliation job: for every order that stays pending longer than a
customer normally needs to pay, read the status with `GetPaymentDetails` (see "Payment status" in `flows.md`) and
update the order.

```python
# Call this from your HTTP endpoint with the raw body and the request headers, e.g. in Flask:
#   @app.post("/webhooks")
#   def webhooks():
#       return "", endpoint.receive(request.get_data(), request.headers.items())
# In Django use request.body and request.headers.items(); in FastAPI await request.body() and
# request.headers.items(). Pass the body unchanged, as bytes: parsing it as JSON first breaks the signature
# check, and the SDK's helper needs bytes.
# Returns the HTTP status to answer with.
def receive(self, body: bytes, headers: Iterable[Tuple[str, str]]) -> int:
    # Pass every received pair as its own header, never merge repeated headers: a merged value would hide
    # the duplicate X-GCS-Signature or X-GCS-KeyId that the helper rejects.
    request_headers = [RequestHeader(name, value) for name, value in headers]
    try:
        # Checks the X-GCS-Signature and X-GCS-KeyId headers before parsing the event.
        webhooks_event = self.__webhooks_helper.unmarshal(body, request_headers)
    except SignatureValidationException:
        # Wrong or missing signature, or an unknown key ID (SecretKeyNotAvailableException, a subclass).
        # Not sent by the platform, or the wrong secret is configured. Do nothing with it.
        return 401
    except (ApiVersionMismatchException, MarshallerSyntaxException):
        # The signature is valid, so the platform sent it, but this SDK version cannot read it (another API
        # version, or a malformed body). Neither exception is a SignatureValidationException. An error
        # status would only make the platform send the same body again. Save the raw body, replay it after
        # you upgrade the SDK, and alert someone.
        self.__inbox.save_unreadable(body)
        logger.critical("ALERT: verified webhook event cannot be read, raw body saved (%d bytes)", len(body),
                        exc_info=True)
        return 200

    # Save the event first, then answer. Do not count on the platform sending the event again after a 2xx,
    # so an event that is only in memory when the process dies can be lost. Process it in a background job.
    self.__inbox.save_event(webhooks_event)
    return 200
```

## Process

- **Duplicates are normal.** The same event can arrive more than once. Processing must be idempotent.
- **Order is not guaranteed.** A `payment.created` event can arrive after `payment.captured`.
- **Read the current status.** Treat the event as a signal: call `GetPaymentDetails` and update the order from its
  `statusOutput` (see "Payment status" in `flows.md`). This also makes duplicates and old events harmless. The
  `payment.id` of a payment changes when a maintenance operation (capture, refund, ...) is performed, and a hosted
  checkout session numbers its authorization attempts (`<id>_0`, `<id>_1`, ...). The platform strongly recommends not
  building your business operations around the ID. `GetPaymentDetails` with the ID of an earlier authorization
  attempt returns the payment's current state, with all operations in `operations` and the latest one as `id`, so
  reading the status by ID gives the current state even for an event about an older operation. Status changes made
  by the platform send webhooks too, without changing the `payment.id`.
- **Do not log the event or the request body.** The event's `payment` contains card details and customer data (see
  the logging rules in `errors.md`). Log the event `id`, `type` and the payment ID.
- **Find your order** with `payment.paymentOutput.references.merchantReference`, which holds the order reference you
  sent. The payment ID changes when you perform a maintenance operation such as a capture or refund, so do not use it as
  your only key.
- **Do not use webhooks for decisions during checkout.** While the customer waits, use `GetHostedCheckout` or
  `GetPaymentDetails`.

```python
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
```

## Event types

| Object | Types |
|---|---|
| Payment | `payment.created`, `payment.redirected`, `payment.authorization_requested`, `payment.pending_approval`, `payment.pending_completion`, `payment.pending_capture`, `payment.capture_requested`, `payment.captured`, `payment.rejected`, `payment.rejected_capture`, `payment.cancelled`, `payment.refunded` |
| Refund | `refund.refund_requested` |
| Payment link | `paymentlink.created`, `paymentlink.clicked`, `paymentlink.paid`, `paymentlink.cancelled`, `paymentlink.expired`, `paymentlink.payment.rejected`, `paymentlink.payment.cancelled` |
| Test | `payment.test` (sent by the SendTestWebhook operation) |

The event's `type` field holds the type. The object that changed is in the matching field of the event (`payment`,
`refund`, `paymentLink`, `payout`, `token`).

Webhooks guide: https://docs.direct.worldline-solutions.com/en/integration/api-developer-guide/webhooks

# Integration flows

Steps and code for each integration method of Online Payments, for the Python SDK.
The client setup is in `python3.md`. In the code, the order store stands for your own database code; replace
it.

Contents:

- Decision guide
- Hosted Checkout
- Payment attempt and idempotence key (server-to-server, Hosted Tokenization, Hosted Fields, client integration)
- Handling a CreatePayment response (server-to-server, Hosted Tokenization, Hosted Fields, client integration)
- Server-to-server
- Hosted Tokenization
- Hosted Fields
- Client integration
- Payment Links
- After-payment operations: capture, refund, cancel
- Recurring payments
- Payment status

## Decision guide

1. Does the user want the least work and no card data on their servers? Use **Hosted Checkout**.
2. Must the card form be part of their own checkout page? Use **Hosted Tokenization** (one iframe) or
   **Hosted Fields** (one field per iframe, more styling control).
3. Is it a native mobile app, or must the form be fully their own? Use **Client integration**.
4. Is the payer not on a checkout page at all (invoice, email, call centre)? Use **Payment Links**.
5. Do they already hold card data under PCI DSS SAQ D, or charge a stored token? Use **Server-to-server**.
6. Subscriptions and other charges without the customer: first payment with one of the methods above, later charges
   as in **Recurring payments**.

Card payments created from your server (all methods except Hosted Checkout and Payment Links) need 3-D Secure data:
the customer's browser details and a return URL.

## Hosted Checkout

The customer pays on a page hosted by the platform. Your server creates a session, redirects the customer, and reads
the result when the customer comes back.

1. Create the session with the amount, your order reference and a return URL that contains your own order reference.
   Build the return URL from configuration: an absolute public base URL of your shop, checked at startup. Never
   build it from the request's `Host` header, which the sender controls. Escape the order reference in the query
   string. The platform rejects a `returnUrl` without a protocol but does not check that it points to your shop, so
   check your base URL yourself. The order reference (`merchantReference`) is at most 40 characters; a longer one is
   rejected with a 400.
2. Store `HostedCheckoutId` and `RETURNMAC` with the order after the call (mandatory rule 2).
3. Redirect the customer to `redirectUrl` exactly as returned (mandatory rule 3). Do not open it in an iframe.
   It is valid for the session timeout: 3 hours by default (`sessionTimeout`, 1 to 1440 minutes).

```python
# The base URL comes from configuration, never from the request's Host header, which the sender controls.
# urlencode escapes the order reference, so it cannot add or change query parameters.
def build_return_url(self, order_id: str) -> str:
    return f"{self.__public_base_url.rstrip('/')}/return?{urlencode({'orderId': order_id})}"

# Returns the URL to redirect the customer to.
def start_checkout(self, order_id: str, amount_in_cents: int, currency_code: str) -> str:
    amount_of_money = AmountOfMoney()
    amount_of_money.amount = amount_in_cents
    amount_of_money.currency_code = currency_code

    references = OrderReferences()
    references.merchant_reference = order_id

    order = Order()
    order.amount_of_money = amount_of_money
    order.references = references

    hosted_checkout_input = HostedCheckoutSpecificInput()
    hosted_checkout_input.return_url = self.build_return_url(order_id)
    hosted_checkout_input.locale = "en-GB"

    request = CreateHostedCheckoutRequest()
    request.order = order
    request.hosted_checkout_specific_input = hosted_checkout_input

    response = self.create_with_retry(request)
    if response.hosted_checkout_id is None or response.returnmac is None or response.redirect_url is None:
        raise RuntimeError(f"Incomplete hosted checkout response for order {order_id}")

    # Store both values with the order before the customer leaves your site.
    self.__orders.save_hosted_checkout(order_id, response.hosted_checkout_id, response.returnmac)

    # Redirect to this URL exactly as returned. Do not build it from partial_redirect_url.
    return response.redirect_url
```

If the create call got no answer, or failed with an error marked `retriable`, send it again.
`CreateHostedCheckout` does not support idempotent requests (mandatory rule 1), so send no idempotence key: every
resend creates a new session. That is harmless until the customer pays in it; the unused session expires. The
waiting happens inside the customer's request, so the browser waits too: keep the attempts few and the delays
short.

```python
# CreateHostedCheckout does not support idempotent requests: the platform ignores an idempotence key, so every
# resend creates a new session. That is harmless until the customer pays in it; the unused session expires.
# Send it again after no answer or after an error marked retriable. The waiting happens inside the customer's
# request, so the browser waits too: keep the attempts few and the delays short, or move the call to a
# background job.
def create_with_retry(self, request: CreateHostedCheckoutRequest) -> CreateHostedCheckoutResponse:
    attempt = 1
    while True:
        try:
            return self.__merchant.hosted_checkout().create_hosted_checkout(request)
        except ApiException as e:
            # The error of a Hosted Checkout call is a plain error response (error ID and errors), so logging it
            # in full is fine here; log at least the error ID, status and error codes.
            codes = "; ".join(f"{error.error_code} {error.property_name}" for error in e.errors)
            logger.error("create_hosted_checkout failed, error_id %s, status %s: %s",
                         e.error_id, e.status_code, codes)
            # Only an error marked retriable is sent again: that request was not processed.
            # Other errors (400 invalid request, 403 wrong credentials, ...) reach the caller.
            if attempt >= 3 or not any(error.retriable is True for error in e.errors):
                raise
        except CommunicationException:
            # No answer: timeout or connection error. The checkout may or may not exist.
            if attempt >= 3:
                raise
        time.sleep(2 * attempt)
        attempt += 1
```

4. When the customer comes back, the platform appends `RETURNMAC` and `hostedCheckoutId` to the query string of your
   return URL, e.g. `https://shop.example/return?orderId=123&RETURNMAC=37159fa4-...&hostedCheckoutId=4501638561`. Load the
   stored values for the order and compare them in constant time: if `RETURNMAC` is missing or differs from the
   stored value, the request does not belong to this checkout; reject it and do not change the order.
5. Then call `GetHostedCheckout` to read the result. `status` is `PAYMENT_CREATED`, `IN_PROGRESS` or
   `CANCELLED_BY_CONSUMER`. When a payment was created, use its status as described in "Payment status". The created
   payment output also carries a payment status category (`paymentStatusCategory`: `SUCCESSFUL`, `REJECTED` or
   `STATUS_UNKNOWN`); decide on the payment's `statusOutput`, as everywhere else. `CANCELLED_BY_CONSUMER` means the
   customer cancelled or the session expired. For an expired session the created payment output holds a cancelled
   payment with the error id `CANCELLED_BY_EXPIRATION`; the order is cancelled. A session can hold several payment
   attempts (`<id>_0`, `<id>_1`, ...) that belong to one payment; `GetHostedCheckout` returns the latest attempt
   (see "Process" in `webhooks.md`).
6. Customers can close the browser before returning. The webhooks (see `webhooks.md`) cover that case.
   `GetHostedCheckout` can also fail with a not-found error (the API reference documents a 404 for this call). Then
   read the payment with `GetPaymentDetails` and the payment ID that your webhook handler stored. If no payment ID
   is stored yet, keep the order pending and let the webhook or your reconciliation job settle it; do not mark it
   failed. Handle only the not-found error this way; let other errors reach the caller. An expired session is not an
   error: `GetHostedCheckout` answers it with `CANCELLED_BY_CONSUMER` (step 5).

```python
# Called when the customer comes back on your return URL, e.g. with request.args.get("RETURNMAC") in Flask.
def handle_return(self, order_id: str, returnmac_from_query: Optional[str]) -> OrderPaymentState:
    stored = self.__orders.get_hosted_checkout(order_id)

    # The platform appends RETURNMAC to the return URL. It identifies the returning customer:
    # a missing or different value means the request does not belong to this checkout.
    # compare_digest compares in constant time, so the comparison does not reveal the stored value.
    # It takes bytes here because it raises TypeError for a str with non-ASCII characters.
    if not returnmac_from_query or not hmac.compare_digest(stored.returnmac.encode(),
                                                           returnmac_from_query.encode()):
        raise RuntimeError(f"RETURNMAC does not match the stored value for order {order_id}")

    # Never trust the redirect alone: read the result from the platform.
    try:
        hosted_checkout = self.__merchant.hosted_checkout().get_hosted_checkout(stored.hosted_checkout_id)
    except ReferenceException as e:
        # The API reference documents a 404 for this call. If it fails with not found, read the payment
        # instead, with the payment ID that your webhook handler stored. Other errors reach the caller,
        # including the 409 and 410 that the SDK also raises as ReferenceException.
        if e.status_code != 404:
            raise
        # refresh_payment_state returns PENDING, not FAILED, when no payment ID is stored
        # yet: the webhook or your reconciliation job settles the order.
        logger.warning("get_hosted_checkout failed for order %s, error_id %s, status %s", order_id, e.error_id,
                       e.status_code)
        return PaymentStatusExample(self.__merchant, self.__orders).refresh_payment_state(order_id)

    output = hosted_checkout.created_payment_output
    payment = output.payment if output is not None else None
    if hosted_checkout.status == "PAYMENT_CREATED" and payment is not None and payment.id is not None:
        self.__orders.save_payment_id(order_id, payment.id)
        state = PaymentStatusExample.to_order_state(payment.status, payment.status_output)
        self.__orders.save_state(order_id, state)
        return state
    if hosted_checkout.status == "CANCELLED_BY_CONSUMER":
        # The customer cancelled, or the session expired (the created payment is then cancelled with the
        # error id CANCELLED_BY_EXPIRATION).
        self.__orders.save_state(order_id, OrderPaymentState.CANCELLED)
        return OrderPaymentState.CANCELLED
    # IN_PROGRESS: the customer has not finished. A webhook will report the result.
    return OrderPaymentState.PENDING
```

## Payment attempt and idempotence key

Server-to-server, Hosted Tokenization, Hosted Fields and client integration all create the payment with a
`CreatePayment` call, which needs an idempotence key (mandatory rule 1). For `CreatePayment` one operation is one
payment attempt:

- Start an attempt when the customer begins to pay, for example when you show the payment form. Create the key and
  store it with the order before the first `CreatePayment` call.
- The request that creates the payment reads the stored key. A double submit, a retry after a timeout and a restart
  then send the same key, so the platform does not create a second payment: it returns the first result, or 409
  while the first request is still running (see `errors.md`).
- Start a new attempt before the customer tries again after a decline or a rejected request. With the old key the
  platform returns the old answer, even when the request is different.

```python
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
```

## Handling a CreatePayment response

Server-to-server, Hosted Tokenization, Hosted Fields and client integration all end with a `CreatePayment` call.
Handle the response the same way:

- Store the payment ID with the order.
- If `merchantAction.actionType` is `REDIRECT`, redirect the customer to `merchantAction.redirectData.redirectURL`
  (3-D Secure challenge or a third-party page). When the customer comes back on your return URL, read the status with
  `GetPaymentDetails` (see "Payment status").
- Otherwise the result is already in `payment.statusOutput`.
- The other action types are not covered by the examples; the API reference describes their data:
  - `SHOW_FORM`: show the customer a form (data in `merchantAction.showFormData`); the customer's input goes back to
    the platform in a `CompletePayment` request.
  - `SHOW_INSTRUCTIONS`: show the customer the payment instructions (`merchantAction.showInstructionsData.showData`).
  - `SHOW_TRANSACTION_RESULTS`: show the customer the transaction result.
  - `MOBILE_THREEDS_CHALLENGE`: the customer completes a 3-D Secure challenge inside your mobile app; pass
    `merchantAction.mobileThreeDSecureChallengeParameters` to the EMVCo-certified Mobile SDK.
  - `CALL_THIRD_PARTY`: your server calls a third party with the data from the response.

```python
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
```

3-D Secure needs the customer's browser details in `order.customer.device`:

```python
# 3-D Secure needs details about the customer's browser. Collect the browser values with JavaScript on the checkout
# page and read the rest from the HTTP request (e.g. in Flask: request.headers.get("Accept"),
# request.headers.get("User-Agent"), request.remote_addr).
def build_customer_device(accept_header: str, user_agent: str, ip_address: str, browser: BrowserInfo) -> CustomerDevice:
    browser_data = BrowserData()
    browser_data.color_depth = browser.color_depth
    browser_data.java_enabled = browser.java_enabled
    browser_data.java_script_enabled = True
    browser_data.screen_height = str(browser.screen_height)
    browser_data.screen_width = str(browser.screen_width)

    device = CustomerDevice()
    device.accept_header = accept_header
    device.user_agent = user_agent
    device.ip_address = ip_address
    device.locale = browser.locale
    device.timezone_offset_utc_minutes = str(browser.timezone_offset_utc_minutes)
    device.browser_data = browser_data
    return device
```

## Server-to-server

Your server sends the card data in `CreatePayment`. Only for merchants certified for PCI DSS SAQ D. Never log the
request (mandatory rule 6). `paymentProductId` is required with card data: without it the platform answers 400
`UNKNOWN_PRODUCT_ID`. The idempotence key is the stored key of the payment attempt (see "Payment attempt and idempotence
key").

```python
# Card data on your server puts you in scope of PCI DSS SAQ D.
# Use Hosted Tokenization or Hosted Fields unless you are certified for it.
def pay_with_card(self, order_id: str, amount_in_cents: int, currency_code: str, payment_product_id: int,
                  card: CardInput, device: CustomerDevice, return_url: str) -> PaymentStep:
    amount_of_money = AmountOfMoney()
    amount_of_money.amount = amount_in_cents
    amount_of_money.currency_code = currency_code

    references = OrderReferences()
    references.merchant_reference = order_id

    customer = Customer()
    customer.device = device

    order = Order()
    order.amount_of_money = amount_of_money
    order.references = references
    order.customer = customer

    card_data = Card()
    card_data.card_number = card.number
    card_data.cardholder_name = card.holder_name
    card_data.expiry_date = card.expiry_date
    card_data.cvv = card.cvv

    redirection_data = RedirectionData()
    redirection_data.return_url = return_url

    three_d_secure = ThreeDSecure()
    three_d_secure.redirection_data = redirection_data

    card_input = CardPaymentMethodSpecificInput()
    # e.g. 1 = Visa, 3 = Mastercard.
    card_input.payment_product_id = payment_product_id
    card_input.card = card_data
    # SALE: authorised and captured at once. Acquirers that do not support it ignore it.
    # FINAL_AUTHORIZATION: capture the full amount within 7 days.
    # PRE_AUTHORIZATION: can be reversed; capture the authorised amount or less within 30 days.
    card_input.authorization_mode = "SALE"
    card_input.three_d_secure = three_d_secure

    request = CreatePaymentRequest()
    request.order = order
    request.card_payment_method_specific_input = card_input

    context = CallContext(idempotence_key=payment_attempt_key(order_id, self.__orders))
    # Raises DeclinedPaymentException if the payment is declined, and other ApiException subclasses for errors;
    # see ErrorHandlingExample for handling each case.
    response = self.__merchant.payments().create_payment(request, context)
    return handle_create_payment_response(response, order_id, self.__orders)
```

If the payment is declined, the SDK reports a declined-payment error that holds the created payment; see `errors.md`.

## Hosted Tokenization

The card form is an iframe from the platform on your checkout page. Your server never sees the card data.

1. Server: create a session and send `hostedTokenizationUrl` and `sri` to the page.

```python
# Creates the session for the card form iframe on your checkout page.
def create_session(self) -> CreateHostedTokenizationResponse:
    request = CreateHostedTokenizationRequest()
    request.locale = "en-GB"
    # Optional: request.variant = "MyTemplate.html", the file name of a custom template.

    response = self.__merchant.hosted_tokenization().create_hosted_tokenization(request)

    # Send hosted_tokenization_url (iframe URL) and sri (script integrity) to the page.
    return response
```

2. Page: load `tokenizer.min.js` from the platform (not from your own server) with the `sri` value as `integrity`,
   create a `Tokenizer` with the `hostedTokenizationUrl` and the ID of the `div` for the iframe, and call
   `initialize()`. When the customer pays, call `submitTokenization()` and post `result.hostedTokenizationId` to your
   server, together with the browser details for 3-D Secure.
3. Server: create the payment with the `hostedTokenizationId` and handle the response as described above. If
   `submitTokenization()` has not completed, the platform answers 400 with the error id
   `HOSTED_TOKENIZATION_SESSION_NOT_SUBMITTED`; an unknown id gives `HOSTED_TOKENIZATION_SESSION_NOT_FOUND`. The
   idempotence key is the stored key of the payment attempt (see "Payment attempt and idempotence key").

```python
# The page calls tokenizer.submitTokenization() and posts result.hostedTokenizationId to your server.
def pay(self, order_id: str, hosted_tokenization_id: str, amount_in_cents: int, currency_code: str,
        device: CustomerDevice, return_url: str) -> PaymentStep:
    amount_of_money = AmountOfMoney()
    amount_of_money.amount = amount_in_cents
    amount_of_money.currency_code = currency_code

    references = OrderReferences()
    references.merchant_reference = order_id

    customer = Customer()
    customer.device = device

    order = Order()
    order.amount_of_money = amount_of_money
    order.references = references
    order.customer = customer

    redirection_data = RedirectionData()
    redirection_data.return_url = return_url

    three_d_secure = ThreeDSecure()
    three_d_secure.redirection_data = redirection_data

    card_input = CardPaymentMethodSpecificInput()
    card_input.authorization_mode = "SALE"
    card_input.three_d_secure = three_d_secure

    request = CreatePaymentRequest()
    request.hosted_tokenization_id = hosted_tokenization_id
    request.order = order
    request.card_payment_method_specific_input = card_input

    context = CallContext(idempotence_key=payment_attempt_key(order_id, self.__orders))
    response = self.__merchant.payments().create_payment(request, context)
    return handle_create_payment_response(response, order_id, self.__orders)
```

## Hosted Fields

Each card field (card number, cardholder name, card brands, expiry date, CVV) is a separate iframe that you place in
your page and customise with CSS.

1. Server: create a session (`locale` is required) and send `sdkUrl`, `sdkSri` and `sessionData` to the page. Pass
   `sessionData` on unchanged.

```python
# Creates the session that the Hosted Fields script on your checkout page needs.
def create_session(self, checkout_page_origin: str) -> CreateHostedFieldsSessionResponse:
    request = CreateHostedFieldsSessionRequest()
    request.locale = "en-GB"
    # The origin of your checkout page, e.g. https://shop.example
    request.origin = checkout_page_origin

    response = self.__merchant.hosted_fields().create_hosted_fields_session(request)

    # Send sdk_url, sdk_sri and session_data to the page. Pass session_data on unchanged
    # (as JSON: response.session_data.to_dictionary()).
    return response
```

2. Page: load the script from `sdkUrl` with `sdkSri` as `integrity` and `crossorigin="anonymous"`. Create the Hosted
   Fields instance with `sessionData` and the IDs of your field containers. On submit call `tokenize(storeToken)`;
   `true` stores the card for later use and needs the customer's consent. Then tell your server to pay.
3. Server: create the payment with the `hostedFieldsSessionId` and handle the response as described above. The
   session response has the ID at its top level and, with the same value, inside `sessionData`. If `tokenize()` has not
   completed, the platform answers 400 with the error id `HOSTED_FIELDS_SESSION_NOT_SUBMITTED` (property
   `hostedFieldsSessionId`). The idempotence key is the stored key of the payment attempt (see "Payment attempt and
   idempotence key").

```python
# The page calls tokenize() and tells your server the card is ready.
# hosted_fields_session_id is hosted_fields_session_id of the create_session response; session_data.hosted_fields_session_id holds the same value.
def pay(self, order_id: str, hosted_fields_session_id: str, amount_in_cents: int, currency_code: str,
        device: CustomerDevice, return_url: str) -> PaymentStep:
    amount_of_money = AmountOfMoney()
    amount_of_money.amount = amount_in_cents
    amount_of_money.currency_code = currency_code

    references = OrderReferences()
    references.merchant_reference = order_id

    customer = Customer()
    customer.device = device

    order = Order()
    order.amount_of_money = amount_of_money
    order.references = references
    order.customer = customer

    redirection_data = RedirectionData()
    redirection_data.return_url = return_url

    three_d_secure = ThreeDSecure()
    three_d_secure.redirection_data = redirection_data

    card_input = CardPaymentMethodSpecificInput()
    card_input.authorization_mode = "SALE"
    card_input.three_d_secure = three_d_secure

    request = CreatePaymentRequest()
    request.hosted_fields_session_id = hosted_fields_session_id
    request.order = order
    request.card_payment_method_specific_input = card_input

    context = CallContext(idempotence_key=payment_attempt_key(order_id, self.__orders))
    response = self.__merchant.payments().create_payment(request, context)
    return handle_create_payment_response(response, order_id, self.__orders)
```

## Client integration

A Client SDK (JavaScript, iOS, Android, Flutter, ...) encrypts the card data on the customer's device. Your server
creates the session and the payment.

1. Server: create a client session and send its values to the app. The API key never leaves your server.

```python
# Creates the session that a Client SDK (JavaScript, iOS, Android, Flutter...) needs to encrypt card data.
def create_client_session(self) -> SessionResponse:
    session = self.__merchant.sessions().create_session(SessionRequest())

    # Send client_session_id, customer_id, client_api_url and asset_url to the app. Never send your API key.
    return session
```

2. App: initialise the Client SDK with the session, collect the card data, and create the encrypted customer input.
   Post that string to your server. Client SDK documentation:
   https://docs.direct.worldline-solutions.com/en/integration/how-to-integrate/client-sdks/javascript
3. Server: create the payment with `encryptedCustomerInput` and handle the response as described above. The string
   holds encrypted card data and can be submitted only once: do not store it. It is at most 5000 characters. A string
   the platform cannot read is a 400 with the error id `INVALID_CONSUMER_INPUT_ENCRYPTION`. The idempotence key is the
   stored key of the payment attempt (see "Payment attempt and idempotence key").

```python
# The Client SDK returns an encrypted string; the app posts it to your server.
def pay(self, order_id: str, encrypted_customer_input: str, amount_in_cents: int, currency_code: str,
        device: CustomerDevice, return_url: str) -> PaymentStep:
    amount_of_money = AmountOfMoney()
    amount_of_money.amount = amount_in_cents
    amount_of_money.currency_code = currency_code

    references = OrderReferences()
    references.merchant_reference = order_id

    customer = Customer()
    customer.device = device

    order = Order()
    order.amount_of_money = amount_of_money
    order.references = references
    order.customer = customer

    redirection_data = RedirectionData()
    redirection_data.return_url = return_url

    three_d_secure = ThreeDSecure()
    three_d_secure.redirection_data = redirection_data

    card_input = CardPaymentMethodSpecificInput()
    card_input.authorization_mode = "SALE"
    card_input.three_d_secure = three_d_secure

    request = CreatePaymentRequest()
    request.encrypted_customer_input = encrypted_customer_input
    request.order = order
    request.card_payment_method_specific_input = card_input

    context = CallContext(idempotence_key=payment_attempt_key(order_id, self.__orders))
    response = self.__merchant.payments().create_payment(request, context)
    return handle_create_payment_response(response, order_id, self.__orders)
```

## Payment Links

The platform hosts the payment page behind a link that you send to the customer.

1. Create the link with the amount, your order reference and an expiry date. The expiry date is required, at most
   6 months ahead, in ISO 8601 with a UTC offset (or `Z`). A missing, past or too distant date is a 400 error.
2. Store `paymentLinkId` with the order and send `redirectionUrl` as returned.
3. The `paymentlink.paid` webhook tells you that a payment was processed with the link. You can also read the link
   with `GetPaymentLinkById` (status `ACTIVE`, `PAID`, `CANCELLED` or `EXPIRED`). Once paid it holds the payment ID.
   That ID has no attempt suffix: call `GetPaymentDetails` with the ID plus `_0`, then read the payment's status
   before you decide anything (mandatory rule 5).

```python
# Returns the link to send to the customer (email, chat, invoice).
def create_link(self, order_id: str, amount_in_cents: int, currency_code: str, description: str) -> PaymentLinkResponse:
    amount_of_money = AmountOfMoney()
    amount_of_money.amount = amount_in_cents
    amount_of_money.currency_code = currency_code

    references = OrderReferences()
    references.merchant_reference = order_id

    order = Order()
    order.amount_of_money = amount_of_money
    order.references = references

    link_input = PaymentLinkSpecificInput()
    link_input.description = description
    # Required. A datetime with a time zone, at most 6 months in the future.
    link_input.expiration_date = datetime.now(timezone.utc) + timedelta(days=7)

    request = CreatePaymentLinkRequest()
    request.order = order
    request.payment_link_specific_input = link_input

    # CreatePaymentLink does not support idempotent requests, so no idempotence key is sent.
    link = self.__merchant.payment_links().create_payment_link(request)

    # Store payment_link_id with the order. Send redirection_url exactly as returned.
    # The paymentlink.paid webhook (or get_payment_link_by_id) tells you when it is paid.
    # Once paid, the link's payment_id has no attempt suffix: use it with "_0" appended in
    # GetPaymentDetails, and read the payment's status.
    return link
```

## After-payment operations

Pass an idempotence key to every capture, refund and cancel. Create it once per operation; retry rules are in `errors.md`.
Sending the same request again with the same key returns the first result and does not run the operation twice.

**Capture.** Only for payments that are authorized and not captured: status `PENDING_CAPTURE`, status category
`PENDING_MERCHANT`. A payment with authorization mode `FINAL_AUTHORIZATION` must be captured for the full amount within
7 days. One with `PRE_AUTHORIZATION` can be captured within 30 days, also for less than the authorized amount. Without
an amount, the full amount is captured and the capture is final; `isFinal` true also makes a capture final. After a
final capture no further capture is accepted, and an amount above the authorized amount is rejected. A capture that is
not final leaves the payment in `PENDING_CAPTURE`. The capture response has status `CAPTURE_REQUESTED`. The capture is
done when its operation (for a final capture, the payment) reads `CAPTURED`, which does not happen immediately: check
again later.

```python
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
```

**Refund.** Only when `statusOutput.isRefundable` is true (the payment is captured; the flag is false while the status
is `CAPTURE_REQUESTED`). Several refunds, partial or full, are allowed on one payment as long as their total does not
exceed the amount paid; a refund above the remaining amount is rejected. A refund is `REFUND_REQUESTED` while the
platform waits for the result and then becomes `REFUNDED` or `REJECTED`. Check the refund `status`; only `REFUNDED` is
done. The payment becomes `REFUNDED` only when the full amount is refunded. A partly refunded payment stays
`COMPLETED`; its operations list the refunds.

```python
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
```

**Cancel.** Cancels an authorization that is not captured. Only when `statusOutput.isCancellable` is true. Without an
amount, the full amount is cancelled. The acquirer decides the result, so the payment in the response is in one of
three states:

- Status `CANCELLED`, category `UNSUCCESSFUL`, status code 6: the authorization is cancelled. This is final.
- Status `CANCELLED`, category `PENDING_MERCHANT`, status code 61 or 62: the platform is waiting for the acquirer's
  answer. This is not final; the payment moves to one of the other two states.
- Status `CANCELLATION_REJECTED`, category `UNSUCCESSFUL`, status code 63: the acquirer refused the cancel. The payment
  stays authorized: do not treat it as failed. You can try the cancel again; an authorization that is not captured
  expires.

```python
# Cancels (voids) an authorization that is not captured yet. No amount cancels the full amount.
def cancel(self, payment_id: str, idempotence_key: str) -> CancelPaymentResponse:
    details = self.__merchant.payments().get_payment_details(payment_id)
    if details.status_output is None or details.status_output.is_cancellable is not True:
        raise RuntimeError(f"Payment {payment_id} is not cancellable in status {details.status}")

    context = CallContext(idempotence_key=idempotence_key)
    return self.__merchant.payments().cancel_payment(payment_id, CancelPaymentRequest(), context)
```

An operation that the payment's current state does not allow (a capture after the final capture or after a cancel, a
refund before the capture or above the remaining amount, a second cancel) is answered with HTTP 400 and the error id
`ACTION_NOT_ALLOWED_ON_TRANSACTION`, without a property name. Read the payment with `GetPaymentDetails`; do not retry.

## Recurring payments

A subscription has one payment made by the customer and later charges that you start without the customer.

1. First payment: mark it as the first of a recurring series. With Hosted Checkout set
   `hostedCheckoutSpecificInput.isRecurring` to `true`; that marks the payment as the first of the series. The example
   uses Hosted Checkout and the same helpers as the Hosted Checkout flow: the return URL is built from your configured
   public base URL, and the create call uses the same retry helper. With `CreatePayment` set
   `cardPaymentMethodSpecificInput.isRecurring` to `true` and
   `cardPaymentMethodSpecificInput.recurring.recurringPaymentSequenceIndicator` to `first`.
2. When the first payment is authorised or captured (Hosted Checkout return or webhook), store its payment ID with
   the customer. The stored ID keeps working for later charges after a capture. A rejected first payment cannot be
   charged again: the subsequent payment fails with a 400 error (`ACTION_NOT_ALLOWED_ON_TRANSACTION`).

```python
# First payment of a subscription, made by the customer on the Hosted Checkout Page.
# The recurring flag marks it as the first payment of the series.
# It follows the Hosted Checkout flow: the return URL is built from your configuration and the call goes
# through the same retry helper. Handle the return as there.
def start_subscription(self, order_id: str, amount_in_cents: int, currency_code: str) -> str:
    amount_of_money = AmountOfMoney()
    amount_of_money.amount = amount_in_cents
    amount_of_money.currency_code = currency_code

    references = OrderReferences()
    references.merchant_reference = order_id

    order = Order()
    order.amount_of_money = amount_of_money
    order.references = references

    hosted_checkout_input = HostedCheckoutSpecificInput()
    hosted_checkout_input.return_url = self.__hosted_checkout.build_return_url(order_id)
    hosted_checkout_input.is_recurring = True

    request = CreateHostedCheckoutRequest()
    request.order = order
    request.hosted_checkout_specific_input = hosted_checkout_input

    response = self.__hosted_checkout.create_with_retry(request)
    if response.hosted_checkout_id is None or response.returnmac is None or response.redirect_url is None:
        raise RuntimeError(f"Incomplete hosted checkout response for order {order_id}")
    self.__orders.save_hosted_checkout(order_id, response.hosted_checkout_id, response.returnmac)
    return response.redirect_url

# When the first payment is authorised or captured, keep its payment ID: later charges refer to it.
def on_first_payment_succeeded(self, customer_id: str, first_payment_id: str) -> None:
    self.__orders.save_recurring_payment_id(customer_id, first_payment_id)
```

3. Later charges: call the subsequent payment operation on the first payment's ID with `subsequentType`
   `Recurring` (fixed amount, regular intervals of at most one year, started by you). The allowed values are
   `Recurring`, `Unscheduled`, `Installment`, `NoShow`, `DelayedCharge`, `PartialShipment`, `Resubmission`,
   `RecurringVariable` and `UnscheduledFixed`; any other value is a 400 error on `subsequentType`. The new payment is
   in the response (`payment`). A declined charge is reported like a declined `CreatePayment` (see `errors.md`).
   Create one idempotence key per charge and store it with the charge before the first call; retry rules are in
   `errors.md`.

```python
# Later charge started by you, without the customer (merchant-initiated).
# The caller creates ONE idempotence key per charge and stores it with the charge, before the first call:
# save_idempotence_key(order_id, key). Retries reuse or replace the key as described in errors.md.
def charge_renewal(self, customer_id: str, order_id: str, amount_in_cents: int, currency_code: str,
                   idempotence_key: str) -> OrderPaymentState:
    first_payment_id = self.__orders.get_recurring_payment_id(customer_id)

    amount_of_money = AmountOfMoney()
    amount_of_money.amount = amount_in_cents
    amount_of_money.currency_code = currency_code

    references = OrderReferences()
    references.merchant_reference = order_id

    order = Order()
    order.amount_of_money = amount_of_money
    order.references = references

    card_input = SubsequentCardPaymentMethodSpecificInput()
    # Recurring = fixed amount, regular intervals (at most one year), started by you.
    # Other allowed values: Unscheduled, Installment, NoShow, DelayedCharge, PartialShipment,
    # Resubmission, RecurringVariable, UnscheduledFixed.
    card_input.subsequent_type = "Recurring"
    # SALE: authorised and captured at once. Acquirers that do not support it ignore it.
    card_input.authorization_mode = "SALE"

    request = SubsequentPaymentRequest()
    request.order = order
    request.subsequentcard_payment_method_specific_input = card_input

    context = CallContext(idempotence_key=idempotence_key)
    # A declined charge raises DeclinedPaymentException, as for create_payment.
    response = self.__merchant.subsequent().subsequent_payment(first_payment_id, request, context)

    payment = response.payment
    if payment is None or payment.id is None:
        raise RuntimeError(f"The subsequent payment response for order {order_id} has no payment")
    self.__orders.save_payment_id(order_id, payment.id)
    state = PaymentStatusExample.to_order_state(payment.status, payment.status_output)
    self.__orders.save_state(order_id, state)
    return state
```

For one-click payments with a stored card (the customer is present), see the card-on-file guide:
https://docs.direct.worldline-solutions.com/en/payment-methods-and-features/advanced-features/card-on-file/api-endpoints-and-jsons-samples

## Payment status

Read the status with `GetPaymentDetails` after a redirect back to your site, after a webhook, after a
declined-payment error, after a capture or a refund, and whenever you are unsure. `GetHostedCheckout` keeps showing
the payment as captured after a refund.

`statusOutput.statusCategory` decides the order state:

| statusCategory | Meaning | What to do |
|---|---|---|
| `COMPLETED` | Paid (captured or sale). A partly refunded payment stays `COMPLETED`. | Fulfil the order. |
| `PENDING_MERCHANT` | Authorized and waiting for a capture (status `PENDING_CAPTURE`), or a cancelled payment waiting for its final result (status `CANCELLED`). | `PENDING_CAPTURE`: capture or cancel. `CANCELLED`: wait for a webhook or check again later. |
| `PENDING_PAYMENT`, `PENDING_CONNECT_OR_3RD_PARTY`, `CREATED` | Not final: waiting for the result of 3-D Secure, an authorization, a capture (`CAPTURE_REQUESTED`) or a refund (`REFUND_REQUESTED`). | Wait for a webhook or check again later. |
| `UNSUCCESSFUL` | Declined, cancelled or failed (`status` tells which). | Do not fulfil. |
| `REFUNDED` | Fully refunded. | Update the order. |
| `REVERSED` | Reversed. | Do not treat as paid; check the payment's operations and follow up. |

`status` (`CREATED`, `CANCELLED`, `REJECTED`, `REJECTED_CAPTURE`, `REDIRECTED`, `PENDING_PAYMENT`, `PENDING_COMPLETION`,
`PENDING_CAPTURE`, `AUTHORIZATION_REQUESTED`, `CAPTURE_REQUESTED`, `CAPTURED`, `REVERSED`, `REFUND_REQUESTED`,
`REFUNDED`) and `statusCode` give more detail. `isCancellable` and `isRefundable` say whether a cancel or a refund is
possible; `isAuthorized` says that the transaction was authorized.
`statusOutput` can be missing in a response. Treat a missing `statusOutput` or `statusCategory` as not final
(pending), never as paid.
Status reference: https://docs.direct.worldline-solutions.com/en/integration/api-developer-guide/statuses

```python
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
def to_order_state(status: Optional[str], status_output: Optional[PaymentStatusOutput]) -> OrderPaymentState:
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
```

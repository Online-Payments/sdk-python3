# Python SDK reference

How to install and set up the Python SDK (`onlinepayments-sdk-python3`), and the SDK calls for the API operations used in
this skill.
Source code and README: https://github.com/Online-Payments/sdk-python3

## Install

```
pip install onlinepayments-sdk-python3
```

Requires Python 3.7 or later. The SDK uses `requests` for HTTP and is imported
as `onlinepayments.sdk`. The SDK source has type annotations but no `py.typed` marker, so mypy treats the package as
untyped and does not check your SDK calls. Write the code as shown in this skill: a misspelled property name is not
an error at runtime either (see Conventions).

## Modules

The packages export nothing: import every class from its own module, e.g.
`from onlinepayments.sdk.domain.create_payment_request import CreatePaymentRequest`.

| Module | Contains |
|---|---|
| `onlinepayments.sdk.factory` | `Factory` |
| `onlinepayments.sdk.communicator_configuration` | `CommunicatorConfiguration` |
| `onlinepayments.sdk.authentication.authorization_type` | `AuthorizationType` (`AuthorizationType.V1HMAC`) |
| `onlinepayments.sdk.i_client`, `onlinepayments.sdk.merchant.i_merchant_client` | `IClient`, `IMerchantClient` (types of the client and the merchant client) |
| `onlinepayments.sdk.call_context` | `CallContext` |
| `onlinepayments.sdk.domain.<name>` | One module per request and response class, named in snake_case: `create_payment_request.CreatePaymentRequest`, `order.Order`, `amount_of_money.AmountOfMoney`, ...; `web_hooks_event.WebhooksEvent` |
| `onlinepayments.sdk.<name>_exception` | The API exceptions, e.g. `declined_payment_exception.DeclinedPaymentException`, `api_exception.ApiException` |
| `onlinepayments.sdk.communication` | `communication_exception.CommunicationException`, `request_header.RequestHeader` |
| `onlinepayments.sdk.webhooks` | `webhooks_helper.WebhooksHelper`, `in_memory_secret_key_store.InMemorySecretKeyStore`, `secret_key_store.SecretKeyStore`, `signature_validation_exception.SignatureValidationException`, `api_version_mismatch_exception.ApiVersionMismatchException` |
| `onlinepayments.sdk.json` | `default_marshaller.DefaultMarshaller`, `marshaller_syntax_exception.MarshallerSyntaxException` |
| `onlinepayments.sdk.log` | `python_communicator_logger.PythonCommunicatorLogger`, `sys_out_communicator_logger.SysOutCommunicatorLogger`, `communicator_logger.CommunicatorLogger`, `body_obfuscator.BodyObfuscator`, `obfuscation_rule` |

## Client setup

```python
# Create the client once when the application starts, reuse it for every request and close it on shutdown.
def create_client() -> IClient:
    configuration = CommunicatorConfiguration(
        # Test or live endpoint host, e.g. payment.direct.ecom.preprod.worldline-solutions.com (without a path).
        api_endpoint="https://" + required_env("onlinePayments_api_endpoint_host"),
        api_key_id=required_env("onlinePayments_api_v1hmac_apiKeyId"),
        secret_api_key=required_env("onlinePayments_api_v1hmac_secretApiKey"),
        # Required: without it, creating the client fails.
        authorization_type=AuthorizationType.V1HMAC,
        # Required: your company or application name; it identifies your requests in the platform logs.
        # The SDK raises ValueError("integrator is required") without it; reading it with required_env fails
        # at startup with a message that names the setting.
        integrator=required_env("onlinePayments_api_integrator"),
        # Required, in seconds.
        connect_timeout=5,
        socket_timeout=300,
        # Required: the size of the connection pool. Without it, the first API call fails.
        max_connections=CommunicatorConfiguration.DEFAULT_MAX_CONNECTIONS,
    )
    return Factory.create_client_from_configuration(configuration)


# The merchant ID is your PSPID. All API calls start from the merchant client.
def create_merchant_client(client: IClient) -> IMerchantClient:
    return client.merchant(required_env("onlinePayments_api_merchantId"))


# The absolute public base URL of your shop, e.g. https://shop.example. The return URL is built from it, never from
# the request's Host header, which the sender controls. Use https in production.
def required_public_base_url() -> str:
    value = required_env("shop_publicBaseUrl")
    parsed = urlparse(value)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise RuntimeError("shop_publicBaseUrl must be an absolute http(s) URL, e.g. https://shop.example")
    return value


# Read credentials from a secret store of your platform. For local development only, environment variables or a
# file outside the repository work too. Never hard-code them. Check every value once at startup and fail fast:
# a blank value is as wrong as a missing one.
def required_env(name: str) -> str:
    value = os.environ.get(name)
    if value is None or not value.strip():
        raise RuntimeError(f"Environment variable {name} is not set")
    return value.strip()
```

- Set every value shown. Without `authorization_type`, `connect_timeout` or `socket_timeout` (seconds), creating the
  client raises a `TypeError`. Without `max_connections` (connection pool size), the first API call raises a
  `TypeError`. The `integrator` is mandatory: an empty or missing one raises `ValueError: integrator is required`.
  Read it from configuration and check it at startup, like the credentials.
- `api_endpoint` is the scheme and host only (`https://payment.direct.ecom.preprod.worldline-solutions.com`); a path
  raises `ValueError: apiEndpoint should not contain a path`.
- The merchant ID is not part of the client configuration.
- `Factory.create_client_from_file(path, api_key_id, secret_api_key)` reads the other values from a properties file
  (section `[OnlinePaymentsSDK]`, keys such as `onlinePayments.api.endpoint.host`); keep the credentials out of that
  file.
- The client holds a connection pool. Create it once (module level in Flask or Django, the lifespan handler in
  FastAPI) and call `client.close()` on shutdown; `with create_client() as client:` closes it too. The client is
  thread-safe. `client.merchant(merchant_id)` is cheap.

## Conventions

- Calls are synchronous and return the response object. They raise exceptions (see below). In an `async def` handler
  (FastAPI, Starlette), run them in a thread, e.g. `await asyncio.to_thread(...)` or FastAPI's `run_in_threadpool`,
  or declare the handler with `def`.
- Request and response classes take no constructor arguments: create the object, then set its properties, e.g.
  `amount_of_money = AmountOfMoney()`, `amount_of_money.amount = 1000`. `AmountOfMoney(amount=1000)` raises
  `TypeError: AmountOfMoney() takes no arguments`. The names are the API names in snake_case (`order.amountOfMoney`
  is `order.amount_of_money`). Exceptions: `RETURNMAC` is `returnmac`, `subsequentcardPaymentMethodSpecificInput` is
  `subsequentcard_payment_method_specific_input`.
- A misspelled property name raises no error: the value is silently left out of the request. Copy the names from this
  skill or from the class.
- All properties can be `None` in responses: check `is not None` and compare flags with `is True`.
- Date and time properties (e.g. `expiration_date`) take a `datetime` with a time zone, e.g.
  `datetime.now(timezone.utc)`.
- `to_dictionary()` returns the object with the API property names, e.g. to send a response object to your page as
  JSON; `obj.from_dictionary(dict)` fills an object from such a dictionary and returns it.
- Every call has an optional `context` parameter. Set the idempotence key with
  `CallContext(idempotence_key=key)`, for example with `str(uuid.uuid4())`. `create_hosted_checkout` and
  `create_payment_link` ignore the key: send none. After the call,
  `context.idempotence_request_timestamp` is set if the platform returned the result of an earlier request with the
  same key. A `CallContext` is not thread-safe: create one per request.
- Properties and values marked deprecated in their docstring are deprecated in the API. Use the replacement named
  there.

## API operations used in this skill

All calls start from the merchant client: `merchant = client.merchant(merchant_id)`.

| API operation | SDK call | Used in |
|---|---|---|
| CreateHostedCheckout | `merchant.hosted_checkout().create_hosted_checkout(CreateHostedCheckoutRequest, context)` | Hosted Checkout, recurring payments |
| GetHostedCheckout | `merchant.hosted_checkout().get_hosted_checkout(hosted_checkout_id)` | Hosted Checkout |
| CreateHostedTokenization | `merchant.hosted_tokenization().create_hosted_tokenization(CreateHostedTokenizationRequest)` | Hosted Tokenization |
| CreateHostedFieldsSession | `merchant.hosted_fields().create_hosted_fields_session(CreateHostedFieldsSessionRequest)` | Hosted Fields |
| CreateSession | `merchant.sessions().create_session(SessionRequest)` | Client integration |
| CreatePayment | `merchant.payments().create_payment(CreatePaymentRequest, context)` | Server-to-server, Hosted Tokenization, Hosted Fields, client integration |
| GetPaymentDetails | `merchant.payments().get_payment_details(payment_id)` | Payment status, webhooks, error handling |
| CapturePayment | `merchant.payments().capture_payment(payment_id, CapturePaymentRequest, context)` | After-payment operations |
| RefundPayment | `merchant.payments().refund_payment(payment_id, RefundRequest, context)` | After-payment operations |
| CancelPayment | `merchant.payments().cancel_payment(payment_id, CancelPaymentRequest, context)` | After-payment operations |
| SubsequentPayment | `merchant.subsequent().subsequent_payment(payment_id, SubsequentPaymentRequest, context)` | Recurring payments |
| CreatePaymentLink | `merchant.payment_links().create_payment_link(CreatePaymentLinkRequest, context)` | Payment Links |
| GetPaymentLinkById | `merchant.payment_links().get_payment_link_by_id(payment_link_id)` | Payment Links |

For anything else, use the API reference; the SDK's sub-clients and method names are the operation names there in
snake_case.

## Exceptions

Each is in the module of the same name in snake_case under `onlinepayments.sdk` unless noted. Catch the specific
ones before `ApiException`.

| Exception | When |
|---|---|
| `DeclinedPaymentException` | The error response carries a payment result: a declined payment (seen with 402 and 403), also for `subsequent_payment`. The body decides, not the status. `create_payment_response` holds the created payment (`.payment.id`). |
| `DeclinedRefundException` | The error response carries a refund result (the body decides, not the status). `refund_response` holds it. |
| `IdempotenceException` | 409 on a call with an idempotence key, with a single error with error code `30001002`: a request with the same idempotence key is still running. Has `idempotence_key`. |
| `ValidationException` | 400: invalid request, including an operation that the payment's state does not allow (error `id` `ACTION_NOT_ALLOWED_ON_TRANSACTION`). |
| `AuthorizationException` | 403: wrong API key ID, secret or merchant ID (error `id` `ACCESS_TO_MERCHANT_NOT_ALLOWED`), or an action that is not allowed. |
| `ReferenceException` | 404 (object not found), 410, and a 409 that is not the idempotence case above. |
| `PlatformException` | 500, 502, 503. Retry only if an error has `retriable` true, with a new idempotence key. |
| `ApiException` | Base class of all the above; any other error status, including 401 and 402 without a payment result. Other `ApiException` subclasses, `ProblemDetailsException` and `DeclinedPayoutException`, are raised by operations this skill does not use. Has `status_code`, `error_id`, `errors`, `response_body`. `str(e)` includes `; response_body='...'`, so logging the exception (also with `logger.exception` or `exc_info=True`) logs the response body. |
| `communication.communication_exception.CommunicationException` | No valid response: a `requests` timeout or connection error (other errors while sending are not wrapped), or an error response with a content type that is not JSON (a 404 like that raises a `NotFoundException`). Not an `ApiException`. |
| `webhooks.signature_validation_exception.SignatureValidationException` | Webhook signature check failed. `SecretKeyNotAvailableException` (unknown key ID) is a subclass. |
| `webhooks.api_version_mismatch_exception.ApiVersionMismatchException` | Webhook event of another API version; the signature was valid. Not a `SignatureValidationException`. |
| `json.marshaller_syntax_exception.MarshallerSyntaxException` | Webhook body with a valid signature that is not readable JSON. An API call raises it too when the response has a JSON content type but invalid JSON. Not a `SignatureValidationException`. |

`errors` is a list of `APIError` with `error_code`, `property_name`, `message`, `http_status_code` and `retriable`.
Logging the exception is fine for Hosted Checkout calls, whose error body is a plain error response. For an error that
carries a payment (a declined payment), do not log `response_body` or the exception itself: log
`error_id`, `status_code` and the error codes. All exceptions are `RuntimeError` subclasses.

## Webhooks

`WebhooksHelper(DefaultMarshaller.instance(), secret_key_store)` and `helper.unmarshal(body, request_headers)`, where
`body` is the raw body as `bytes` (a `str` fails in this SDK) and `request_headers` is a list of
`RequestHeader(name, value)`, one for every header pair as received, not a dict. The helper rejects a repeated
`X-GCS-Signature` or `X-GCS-KeyId` with a `SignatureValidationException`, so never merge repeated headers; names are
compared case-insensitively. `unmarshal` raises `SignatureValidationException` (also a missing header or an unknown
key ID: `SecretKeyNotAvailableException`), then, only for a valid signature, `ApiVersionMismatchException` or
`MarshallerSyntaxException`.
`secret_key_store` is `InMemorySecretKeyStore.instance()` (one shared store; a second `store_secret_key` for the same
key ID overwrites) after `store_secret_key(key_id, secret)`, or your own
`SecretKeyStore` subclass with `get_secret_key(key_id)`. It returns a `WebhooksEvent` with `id`, `type`, `created`,
`merchant_id` and one of `payment`, `refund`, `payment_link`, `payout`, `token`. Read the body with
`request.get_data()` in Flask, `request.body` in Django or `await request.body()` in FastAPI, not as parsed JSON. See
`webhooks.md` for the full handler.

## Hosted Checkout output

`get_hosted_checkout(...)` returns an object with `status` and `created_payment_output`, whose `payment` holds the
payment. The payment status category on `created_payment_output` is `payment_status_category`; decide on
`payment.status_output.status_category` as everywhere else.

## Logging

`client.enable_logging(PythonCommunicatorLogger(logging.getLogger("onlinepayments"), logging.INFO))` or
`SysOutCommunicatorLogger.instance()` logs requests and responses with card data and secrets masked. Mask other
fields with `client.set_body_obfuscator(BodyObfuscator(additional_rules={"name": obfuscate_all()}))`, with the
rules in `onlinepayments.sdk.log.obfuscation_rule`. Do not log request or response objects yourself.

# Online Payments Python SDK

## Introduction

The Python SDK helps you to communicate with the payment platform server API. Its primary features are:

* convenient Python library for the API calls and responses
    * marshals Python request objects to HTTP requests
    * unmarshals HTTP responses to Python response objects or Python exceptions
* handling of all the details concerning authentication
* handling of required metadata

See the [Worldline Online Payments Developer Hub](https://docs.direct.worldline-solutions.com/documentation/sdk/server/python/) for more information on how to use the SDK.

## Structure of this repository

This repository consists out of three main components:

1. The source code of the SDK itself: `/onlinepayments/sdk/`
2. The source code of the SDK unit tests: `/tests/unit/`
3. The source code of the integration tests: `/tests/integration/`

Note that the source code of the unit tests and integration tests can only be found on GitHub.

## Requirements

Python 3.11 or higher is required. In addition, the following packages are required:

* [requests](https://requests.readthedocs.io/) 2.32.3 or higher
* [requests-toolbelt](https://toolbelt.readthedocs.io/) 1.0.0 or higher

These packages will be installed automatically if the SDK is installed manually or using pip following the below instructions.

## Installation

To install the SDK using pip, execute the following command:

    pip install onlinepayments-sdk-python3

Alternatively, you can install the SDK from a source distribution file:

1. Download the latest version of the Python SDK from GitHub. Choose the `onlinepayments-sdk-python3-x.y.z.zip` file from the [releases](https://github.com/wl-online-payments-direct/sdk-python3/releases) page, where `x.y.z` is the version number.
2. Execute the following command in the folder where the SDK was downloaded to:

    ```
    pip install onlinepayments-sdk-python3-x.y.z.zip
    ```

## Working with AI agents

The SDK comes with an agent skill for AI coding agents such as Claude Code, Codex, GitHub Copilot and Cursor. It tells the agent how to choose an integration method, which steps each flow needs, which rules every integration must follow, and gives code examples that are type-checked against this SDK version.

The skill for this version is available:

* online, as plain Markdown for agents: https://raw.githubusercontent.com/Online-Payments/sdk-python3/12.0.0/onlinepayments/sdk/skills/online-payments/SKILL.md
* online, on GitHub: https://github.com/Online-Payments/sdk-python3/blob/12.0.0/onlinepayments/sdk/skills/online-payments/SKILL.md
* in the installed package: `onlinepayments/sdk/skills/online-payments/` in your `site-packages` folder, e.g. `.venv/lib/python3.12/site-packages/onlinepayments/sdk/skills/online-payments/` (`.venv\Lib\site-packages\...` on Windows). This command prints the folder: `python -c "import onlinepayments.sdk, os; print(os.path.join(os.path.dirname(onlinepayments.sdk.__file__), 'skills', 'online-payments'))"`
* in this repository: `onlinepayments/sdk/skills/online-payments/`

To make your agent use it, add this to the `AGENTS.md` or `CLAUDE.md` file of your project:

```
For the Online Payments integration (onlinepayments-sdk-python3), read and follow the agent skill
onlinepayments/sdk/skills/online-payments/SKILL.md in the site-packages folder of the project's environment
(online: https://raw.githubusercontent.com/Online-Payments/sdk-python3/12.0.0/onlinepayments/sdk/skills/online-payments/SKILL.md)
Use the code shown in the skill; do not write SDK calls from memory.
```

Agents that support the Agent Skills format can also load the folder directly, for example by copying `onlinepayments/sdk/skills/online-payments/` from `site-packages` to `.claude/skills/online-payments/` in your project for Claude Code.

## Uninstalling

After the Python SDK has been installed, it can be uninstalled using the following command:

    pip uninstall onlinepayments-sdk-python3

The required packages can be uninstalled in the same way.

## Usage

### Creating a client

A client can be created from code, from environment variables or from an `.ini` file:

```python
from onlinepayments.sdk.factory import Factory

client = Factory.create_client(
    api_endpoint="https://payment.direct.ecom.preprod.worldline-solutions.com",
    api_key_id="...",
    secret_api_key="...",
    integrator="MyShop",
    connect_timeout=10,    # seconds
    socket_timeout=60,     # seconds
    # optional: max_connections, proxy_configuration, shopping_cart_extension
)

client = Factory.create_client_from_env()

client = Factory.create_client_from_file("configuration.ini", "api_key_id", "secret_api_key")
```

`Factory.create_client` and `Factory.create_client_from_env` accept keyword arguments only. `Factory.create_client_from_env` reads the following environment variables:

| Environment variable | Description |
|---|---|
| `ONLINEPAYMENTS_API_ENDPOINT` | Required. The API endpoint, for example `https://payment.direct.ecom.preprod.worldline-solutions.com` |
| `ONLINEPAYMENTS_API_KEY_ID` | Required. The API key id |
| `ONLINEPAYMENTS_SECRET_API_KEY` | Required. The secret API key |
| `ONLINEPAYMENTS_INTEGRATOR` | Required. The name of the integrator |
| `ONLINEPAYMENTS_CONNECT_TIMEOUT` | Required. The connect timeout in seconds |
| `ONLINEPAYMENTS_SOCKET_TIMEOUT` | Required. The socket timeout in seconds |

The merchant ID is not part of the client configuration; pass it to `client.merchant(merchant_id)`.

A client can be used in a `with` block, which closes it at the end of the block:

```python
with Factory.create_client_from_env() as client:
    ...
```

### Creating requests

Domain objects accept their fields as keyword arguments:

```python
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.create_payment_request import CreatePaymentRequest
from onlinepayments.sdk.domain.order import Order

request = CreatePaymentRequest(
    order=Order(amount_of_money=AmountOfMoney(amount=125000, currency_code="EUR")),
)
response = client.merchant(merchant_id).payments().create_payment(request, CallContext(idempotence_key="order-42"))
```

An unknown keyword argument raises a `TypeError`, and assigning an attribute that does not exist raises an `AttributeError`.
Printing a domain object shows its fields, with card numbers, CVVs and personal data masked.

### Handling errors

```python
from onlinepayments.sdk.api_exception import ApiException
from onlinepayments.sdk.communication.communication_exception import CommunicationException
from onlinepayments.sdk.declined_payment_exception import DeclinedPaymentException

try:
    client.merchant(merchant_id).payments().create_payment(request, CallContext(idempotence_key=key))
except DeclinedPaymentException as e:
    ...
except ApiException as e:
    log.error("Payment failed: %s", e)    # the response body in the message is masked
except CommunicationException as e:
    ...                                   # e.cause contains the original error
```

A timeout, a `CommunicationException` or a `PlatformException` during `create_payment` means the outcome of the payment is unknown.
Check the payment status with `get_payment`, and always send an idempotence key so that a retry does not create a second payment.

The unmasked response body is available in `response_body`.

## Running tests

There are two types of tests: unit tests and integration tests. The unit tests will work out-of-the-box; for the integration tests some configuration is required.
First, some environment variables need to be set:
* `ONLINEPAYMENTS_API_KEY_ID` for the API key id to use.
* `ONLINEPAYMENTS_SECRET_API_KEY` for the secret API key to use.
* `ONLINEPAYMENTS_MERCHANT_ID` for your merchant ID.
* Optionally, `ONLINEPAYMENTS_API_ENDPOINT` to use a different endpoint than the one in `tests/resources/configuration.v1hmac.ini`.

If any of the required variables is missing, the integration tests are skipped.

The file `.env.example` lists all variables. You can copy it to `.env` (which is ignored by git) and fill in your values.
The tests load `.env` from the root of the repository automatically. Variables that are already set in the environment take precedence.

The tests use [pytest](https://pytest.org/). To install the SDK together with the test dependencies, execute the following command from the root of the repository:

    pip install -e ".[test]"

The following commands can then be executed from the root of the repository to execute the tests:
* Unit tests:

    ```
    pytest tests/unit
    ```
* Integration tests:

    ```
    pytest tests/integration
    ```
* Both unit and integration tests:

    ```
    pytest
    ```

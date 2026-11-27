Online Payments Python SDK
==========================

Introduction
------------

The Python SDK helps you to communicate with the payment platform server
API. Its primary features are:

-  convenient Python library for the API calls and responses

   -  marshals Python request objects to HTTP requests
   -  unmarshals HTTP responses to Python response objects or Python exceptions

-  handling of all the details concerning authentication
-  handling of required metadata

Its use is demonstrated by an example for each possible call. The examples execute a call using the provided API key.

Structure of this repository
----------------------------

This repository consists out of three main components:

#. The source code of the SDK itself: ``/onlinepayments/sdk/``
#. The source code of the SDK unit tests: ``/tests/unit/``
#. The source code of the SDK integration tests: ``/tests/integration/``

Note that the source code of the unit tests and integration tests can only be found on GitHub.

Requirements
------------

Python 3.11 or higher is required. In addition, the following packages are required:

-  `requests <https://requests.readthedocs.io/>`__ 2.32.3 or higher
-  `requests-toolbelt <https://toolbelt.readthedocs.io/>`__ 1.0.0 or higher

These packages will be installed automatically if the SDK is installed manually or using pip following the below instructions.

Installation
------------

To install the SDK using pip, execute the following command:

.. code:: bash

   pip install onlinepayments-sdk-python3

Alternatively, you can install the SDK from a source distribution file:

#. Download the latest version of the Python SDK from GitHub. Choose the
   ``onlinepayments-sdk-python3-x.y.z.zip`` file from the
   `releases <https://github.com/wl-online-payments-direct/sdk-python3/releases>`__
   page, where ``x.y.z`` is the version number.
#. Execute the following command in the folder where the SDK was downloaded to:

   .. code:: bash

      pip install onlinepayments-sdk-python3-x.y.z.zip

Working with AI agents
----------------------

The SDK comes with an agent skill for AI coding agents such as Claude Code, Codex, GitHub Copilot and Cursor. It
tells the agent how to choose an integration method, which steps each flow needs, which rules every integration must
follow, and gives code examples that are type-checked against this SDK version.

The skill for this version is available:

- online, as plain Markdown for agents: https://raw.githubusercontent.com/Online-Payments/sdk-python3/11.1.0/onlinepayments/sdk/skills/online-payments/SKILL.md
- online, on GitHub: https://github.com/Online-Payments/sdk-python3/blob/11.1.0/onlinepayments/sdk/skills/online-payments/SKILL.md
- in the installed package: ``onlinepayments/sdk/skills/online-payments/`` in your ``site-packages`` folder, e.g.
  ``.venv/lib/python3.12/site-packages/onlinepayments/sdk/skills/online-payments/`` (``.venv\Lib\site-packages\...`` on Windows). This command prints
  the folder:

  .. code:: bash

     python -c "import onlinepayments.sdk, os; print(os.path.join(os.path.dirname(onlinepayments.sdk.__file__), 'skills', 'online-payments'))"

- in the source repository: ``onlinepayments/sdk/skills/online-payments/``

To make your agent use it, add this to the ``AGENTS.md`` or ``CLAUDE.md`` file of your project:

.. code:: text

   For the Online Payments integration (onlinepayments-sdk-python3), read and follow the agent skill
   onlinepayments/sdk/skills/online-payments/SKILL.md in the site-packages folder of the project's environment
   (online: https://raw.githubusercontent.com/Online-Payments/sdk-python3/11.1.0/onlinepayments/sdk/skills/online-payments/SKILL.md)
   Use the code shown in the skill; do not write SDK calls from memory.

Agents that support the Agent Skills format can also load the folder directly, for example by copying
``onlinepayments/sdk/skills/online-payments/`` from ``site-packages`` to ``.claude/skills/online-payments/`` in your project for Claude Code.

Uninstalling
------------

After the Python SDK has been installed, it can be uninstalled using the following command:

.. code:: bash

   pip uninstall onlinepayments-sdk-python3

The required packages can be uninstalled in the same way.

Usage
-----

Creating a client
~~~~~~~~~~~~~~~~~

A client can be created from code, from environment variables or from an ``.ini`` file:

.. code:: python

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

``Factory.create_client`` and ``Factory.create_client_from_env`` accept keyword arguments only. ``Factory.create_client_from_env`` reads the following environment variables:

-  ``ONLINEPAYMENTS_API_ENDPOINT``: required. The API endpoint, for example ``https://payment.direct.ecom.preprod.worldline-solutions.com``
-  ``ONLINEPAYMENTS_API_KEY_ID``: required. The API key id
-  ``ONLINEPAYMENTS_SECRET_API_KEY``: required. The secret API key
-  ``ONLINEPAYMENTS_INTEGRATOR``: required. The name of the integrator
-  ``ONLINEPAYMENTS_CONNECT_TIMEOUT``: required. The connect timeout in seconds
-  ``ONLINEPAYMENTS_SOCKET_TIMEOUT``: required. The socket timeout in seconds

The merchant ID is not part of the client configuration; pass it to ``client.merchant(merchant_id)``.

A client can be used in a ``with`` block, which closes it at the end of the block:

.. code:: python

   with Factory.create_client_from_env() as client:
       ...

Creating requests
~~~~~~~~~~~~~~~~~

Domain objects accept their fields as keyword arguments:

.. code:: python

   from onlinepayments.sdk.call_context import CallContext
   from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
   from onlinepayments.sdk.domain.create_payment_request import CreatePaymentRequest
   from onlinepayments.sdk.domain.order import Order

   request = CreatePaymentRequest(
       order=Order(amount_of_money=AmountOfMoney(amount=125000, currency_code="EUR")),
   )
   response = client.merchant(merchant_id).payments().create_payment(request, CallContext(idempotence_key="order-42"))

An unknown keyword argument raises a ``TypeError``, and assigning an attribute that does not exist raises an ``AttributeError``.
Printing a domain object shows its fields, with card numbers, CVVs and personal data masked.

Handling errors
~~~~~~~~~~~~~~~

.. code:: python

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

A timeout, a ``CommunicationException`` or a ``PlatformException`` during ``create_payment`` means the outcome of the payment is unknown.
Check the payment status with ``get_payment``, and always send an idempotence key so that a retry does not create a second payment.

The unmasked response body is available in ``response_body``.

Upgrading from version 10.x
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Python 3.11 or higher is required.
-  Errors raised by the ``requests`` library are now wrapped in a ``CommunicationException``. The original error is available through its ``cause``.
-  Domain objects use ``__slots__``. Adding your own attributes to SDK objects, ``vars(obj)`` and loading SDK objects that were pickled with an older version no longer work.
-  A ``%`` in the ``.ini`` file is read as-is. If you wrote ``%%`` to work around this, change it back to ``%``.
-  ``str(proxy_configuration)`` masks the password. Use ``proxy_configuration.to_url()`` for the full proxy URL.
-  ``CommunicatorConfiguration.authorization_type`` defaults to ``v1HMAC``.
-  Request bodies are sent as compact JSON.
-  ``ApiException.errors`` is always a list (it could be a tuple before).

Running tests
-------------

There are two types of tests: unit tests and integration tests. The unit tests will work out-of-the-box; for the integration tests some configuration is required.
First, some environment variables need to be set:

-  ``ONLINEPAYMENTS_API_KEY_ID`` for the API key id to use.
-  ``ONLINEPAYMENTS_SECRET_API_KEY`` for the secret API key to use.
-  ``ONLINEPAYMENTS_MERCHANT_ID`` for your merchant ID.
-  Optionally, ``ONLINEPAYMENTS_API_ENDPOINT`` to use a different endpoint than the one in ``tests/resources/configuration.v1hmac.ini``.

If any of the required variables is missing, the integration tests are skipped.

The file ``.env.example`` lists all variables. You can copy it to ``.env`` (which is ignored by git) and fill in your values.
The tests load ``.env`` from the root of the repository automatically. Variables that are already set in the environment take precedence.

In addition, to run the proxy integration tests, the proxy URI, username and password should be set in the ``tests/resources/configuration.proxy.ini`` file.

The tests use `pytest <https://pytest.org/>`__. To install the SDK together with the test dependencies, execute the following command from the root of the repository:

.. code:: bash

   pip install -e ".[test]"

The following commands can then be executed from the root of the repository to execute the tests:

-  Unit tests:

   .. code:: bash

      pytest tests/unit

-  Integration tests:

   .. code:: bash

      pytest tests/integration

-  Both unit and integration tests:

   .. code:: bash

      pytest

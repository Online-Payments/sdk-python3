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

Python 3.7 or higher is required. In addition, the following packages are required:

-  `requests <https://requests.readthedocs.io/>`__ 2.25.0 or higher
-  `requests-toolbelt <https://toolbelt.readthedocs.io/>`__ 0.8.0 or higher

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
#. Execute the following command in the folder where the SDK was
   downloaded to:

#. Execute the following command in the folder where the SDK was downloaded to:

   .. code:: bash

      pip install onlinepayments-sdk-python3-x.y.z.zip

Uninstalling
------------

After the Python SDK has been installed, it can be uninstalled using the following command:

.. code:: bash

   pip uninstall onlinepayments-sdk-python3

The required packages can be uninstalled in the same way.

Running tests
-------------

There are two types of tests: unit tests and integration tests. The unit tests will work out-of-the-box; for the integration tests some configuration is required.
First, some environment variables need to be set:
-  ``onlinePayments.api.v1hmac.apiKeyId`` for the API key id to use.
-  ``onlinePayments.api.v1hmac.secretApiKey`` for the secret API key to use.
-  ``onlinePayments.api.merchantId`` for your merchant ID.

In addition, to run the proxy integration tests, the proxy URI, username and password should be set in the ``tests/resources/configuration.proxy.ini`` file.

In order to run the unit and integration tests, the `mock <https://pypi.python.org/pypi/mock>`__ backport and `mockito <https://pypi.python.org/pypi/mockito>`__ are required. These can be installed using the following command:

.. code:: bash

   pip install mock mockito

The following commands can now be executed from the ``tests`` directory to execute the tests:

-  Unit tests:

   .. code:: bash

      python run_unit_tests.py

-  Integration tests:

   .. code:: bash

      python run_integration_tests.py

-  Both unit and integration tests:

   .. code:: bash

      python run_all_tests.py

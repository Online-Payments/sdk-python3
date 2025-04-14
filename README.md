# Online Payments Python SDK

## Introduction

The Python SDK helps you to communicate with the payment platform server API. Its primary features are:

* convenient Python library for the API calls and responses
    * marshals Python request objects to HTTP requests
    * unmarshals HTTP responses to Python response objects or Python exceptions
* handling of all the details concerning authentication
* handling of required metadata

See the [Online Payments Developer Hub](https://docs.direct.worldline-solutions.com/documentation/sdk/server/python/) for more information on how to use the SDK.

## Structure of this repository

This repository consists out of three main components:

1. The source code of the SDK itself: `/onlinepayments/sdk/`
2. The source code of the SDK unit tests: `/tests/unit/`
3. The source code of the integration tests: `/tests/integration/`

Note that the source code of the unit tests and integration tests can only be found on GitHub.

## Requirements

Python 3.7 or higher is required. In addition, the following packages are required:

* [requests](https://requests.readthedocs.io/) 2.25.0 or higher
* [requests-toolbelt](https://toolbelt.readthedocs.io/) 0.8.0 or higher

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

## Uninstalling

After the Python SDK has been installed, it can be uninstalled using the following command:

    pip uninstall onlinepayments-sdk-python3

The required packages can be uninstalled in the same way.

## Running tests

There are two types of tests: unit tests and integration tests. The unit tests will work out-of-the-box; for the integration tests some configuration is required.
First, some environment variables need to be set:
* `onlinePayments.api.v1hmac.apiKeyId` for the API key id to use.
* `onlinePayments.api.v1hmac.secretApiKey` for the secret API key to use.
* `onlinePayments.api.merchantId` for your merchant ID.

In order to run the unit and integration tests, the [mock](https://pypi.python.org/pypi/mock) backport and [mockito](https://pypi.python.org/pypi/mockito) packages are required. These can be installed using the following command:

    pip install mock mockito

The following commands can then be executed from the `tests` directory to execute the tests:
* Unit tests:

    ```
    python run_unit_tests.py
    ```
* Integration tests:

    ```
    python run_integration_tests.py
    ```
* Both unit and integration tests:

    ```
    python run_all_tests.py
    ```

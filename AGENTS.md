# AGENTS.md

## Using this SDK in your project

If you are writing code that integrates Online Payments with this SDK, read the agent skill
for this SDK version first and use the code it shows. Do not write SDK calls from memory.

- In the installed package: `onlinepayments/sdk/skills/online-payments/SKILL.md` in your site-packages folder
  (package folder: `python -c "import onlinepayments.sdk, os; print(os.path.dirname(onlinepayments.sdk.__file__))"`)
- Online: https://raw.githubusercontent.com/Online-Payments/sdk-python3/11.1.0/onlinepayments/sdk/skills/online-payments/SKILL.md

The skill matches SDK version 11.1.0. If your installed version is different, use the skill
from your installed package.

## Working on this SDK

- SDK source: `onlinepayments/sdk/`; unit tests: `tests/unit/`; integration tests: `tests/integration/`.
- Install the test dependencies with `pip install mock mockito`.
- From the `tests` folder, run the unit tests with `python run_unit_tests.py`, the integration tests with
  `python run_integration_tests.py`, and both with `python run_all_tests.py`.
- The integration tests need the environment variables `onlinePayments_api_v1hmac_apiKeyId`,
  `onlinePayments_api_v1hmac_secretApiKey` and `onlinePayments_api_merchantId`.
- See `README.md` for details.

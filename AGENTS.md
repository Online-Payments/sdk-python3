# AGENTS.md

## Using this SDK in your project

If you are writing code that integrates Online Payments with this SDK, read the agent skill
for this SDK version first and use the code it shows. Do not write SDK calls from memory.

- In the installed package: `onlinepayments/sdk/skills/online-payments/SKILL.md` in your site-packages folder
  (package folder: `python -c "import onlinepayments.sdk, os; print(os.path.dirname(onlinepayments.sdk.__file__))"`)
- Online: https://raw.githubusercontent.com/Online-Payments/sdk-python3/12.0.0/onlinepayments/sdk/skills/online-payments/SKILL.md

The skill matches SDK version 12.0.0. If your installed version is different, use the skill
from your installed package.

## Working on this SDK

- SDK source: `onlinepayments/sdk/`; unit tests: `tests/unit/`; integration tests: `tests/integration/`.
- Install the SDK with the test dependencies with `pip install -e ".[test]"`.
- From the root of the repository, run the unit tests with `pytest tests/unit`, the integration tests with
  `pytest tests/integration`, and both with `pytest`.
- The integration tests need the environment variables `ONLINEPAYMENTS_API_KEY_ID`,
  `ONLINEPAYMENTS_SECRET_API_KEY` and `ONLINEPAYMENTS_MERCHANT_ID`. They are read from the environment or from `.env`
  in the root of the repository (see `.env.example`); without them the integration tests are skipped.
- See `README.md` for details.

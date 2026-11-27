import os

import pytest

from tests.integration.init_utils import missing_environment_variables

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_UNIT_DIR = os.path.join(_TESTS_DIR, "unit")
_INTEGRATION_DIR = os.path.join(_TESTS_DIR, "integration")


def pytest_collection_modifyitems(config, items):
    missing = missing_environment_variables()
    skip_integration = pytest.mark.skip(reason="integration tests need the environment variables " + ", ".join(missing))
    for item in items:
        path = os.path.abspath(str(item.path))
        if path.startswith(_UNIT_DIR + os.sep):
            item.add_marker(pytest.mark.unit)
        elif path.startswith(_INTEGRATION_DIR + os.sep):
            item.add_marker(pytest.mark.integration)
            if missing:
                item.add_marker(skip_integration)

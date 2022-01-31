#!python
import os
import sys
import unittest
from pathlib import Path

# append to pythonpath to make imports work
sys.path.insert(0, (str(Path(__file__).parent.parent)))


def load_tests(loader, tests, pattern):
    """ Discover and load all tests tests in all files named ``test_*.py`` in ``tests``

    Overrides default test loading behavior to load all tests in subfolders
    """
    unit_dir = os.path.join(os.path.dirname(__file__), "unit")
    unit_tests = loader.discover(start_dir=unit_dir, pattern="test_*.py", top_level_dir=unit_dir)
    tests.addTests(unit_tests)
    integration_dir = os.path.join(os.path.dirname(__file__), "integration")
    integration_tests = loader.discover(start_dir=integration_dir, pattern="test_*.py", top_level_dir=integration_dir)
    tests.addTests(integration_tests)
    return tests


if __name__ == '__main__':
    unittest.main()

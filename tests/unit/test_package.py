import os
import unittest

import onlinepayments.sdk
from onlinepayments.sdk import _version

_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))


class PackageTest(unittest.TestCase):

    def test_GettingVersion_DefaultScenario_ReturnVersionFromVersionModule(self):
        self.assertEqual(_version.__version__, onlinepayments.sdk.__version__)

    def test_PackageData_DefaultScenario_ContainTypedMarkers(self):
        for package in ("onlinepayments", os.path.join("onlinepayments", "sdk")):
            with self.subTest(package=package):
                self.assertTrue(os.path.isfile(os.path.join(_ROOT_DIR, package, "py.typed")))


if __name__ == '__main__':
    unittest.main()

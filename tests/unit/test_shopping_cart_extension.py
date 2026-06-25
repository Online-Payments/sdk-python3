import unittest

from onlinepayments.sdk.domain.shopping_cart_extension import ShoppingCartExtension


class ShoppingCartExtensionTest(unittest.TestCase):

    def test_CreatedWithInvalidCreator_DefaultScenario_ThrowWhenCreatorIsNull(self):
        with self.assertRaises(ValueError):
            ShoppingCartExtension(None, "name", "1.0")

    def test_CreatedWithInvalidCreator_DefaultScenario_ThrowWhenCreatorIsBlank(self):
        with self.assertRaises(ValueError):
            ShoppingCartExtension("", "name", "1.0")

    def test_CreatedWithInvalidName_DefaultScenario_ThrowWhenNameIsNull(self):
        with self.assertRaises(ValueError):
            ShoppingCartExtension("creator", None, "1.0")

    def test_CreatedWithInvalidName_DefaultScenario_ThrowWhenNameIsBlank(self):
        with self.assertRaises(ValueError):
            ShoppingCartExtension("creator", "", "1.0")

    def test_CreatedWithInvalidVersion_DefaultScenario_ThrowWhenVersionIsNull(self):
        with self.assertRaises(ValueError):
            ShoppingCartExtension("creator", "name", None)

    def test_CreatedWithInvalidVersion_DefaultScenario_ThrowWhenVersionIsBlank(self):
        with self.assertRaises(ValueError):
            ShoppingCartExtension("creator", "name", "")

    def test_CreatedWithValidArguments_DefaultScenario_CreateInstanceWithExpectedValues(self):
        ext = ShoppingCartExtension("creator", "name", "1.0")
        self.assertEqual("creator", ext.creator)
        self.assertEqual("name", ext.name)
        self.assertEqual("1.0", ext.version)
        self.assertIsNone(ext.extension_id)

    def test_CreatedWithOptionalId_DefaultScenario_CreateInstanceWithExpectedValues(self):
        ext = ShoppingCartExtension("creator", "name", "1.0", "extension-id")
        self.assertEqual("creator", ext.creator)
        self.assertEqual("name", ext.name)
        self.assertEqual("1.0", ext.version)
        self.assertEqual("extension-id", ext.extension_id)

    def test_ConvertingToDictionary_DefaultScenario_IncludeRequiredFields(self):
        ext = ShoppingCartExtension("creator", "name", "1.0")
        dictionary = ext.to_dictionary()
        self.assertEqual("creator", dictionary["creator"])
        self.assertEqual("name", dictionary["name"])
        self.assertEqual("1.0", dictionary["version"])
        self.assertNotIn("extensionId", dictionary)

    def test_ConvertingToDictionary_DefaultScenario_IncludeExtensionId(self):
        ext = ShoppingCartExtension("creator", "name", "1.0", "ext-123")
        dictionary = ext.to_dictionary()
        self.assertEqual("ext-123", dictionary["extensionId"])

    def test_CreatingFromDictionary_DefaultScenario_CreateInstanceWithAllFields(self):
        dictionary = {"creator": "c", "name": "n", "version": "v", "extensionId": "e"}
        ext = ShoppingCartExtension.create_from_dictionary(dictionary)
        self.assertEqual("c", ext.creator)
        self.assertEqual("n", ext.name)
        self.assertEqual("v", ext.version)
        self.assertEqual("e", ext.extension_id)

    def test_CreatingFromDictionary_DefaultScenario_OmitExtensionIdWhenMissing(self):
        dictionary = {"creator": "c", "name": "n", "version": "v"}
        ext = ShoppingCartExtension.create_from_dictionary(dictionary)
        self.assertIsNone(ext.extension_id)

    def test_CreatingFromDictionary_DefaultScenario_ThrowWhenCreatorMissing(self):
        with self.assertRaises(ValueError):
            ShoppingCartExtension.create_from_dictionary({"name": "n", "version": "v"})

    def test_CreatingFromDictionary_DefaultScenario_ThrowWhenNameMissing(self):
        with self.assertRaises(ValueError):
            ShoppingCartExtension.create_from_dictionary({"creator": "c", "version": "v"})

    def test_CreatingFromDictionary_DefaultScenario_ThrowWhenVersionMissing(self):
        with self.assertRaises(ValueError):
            ShoppingCartExtension.create_from_dictionary({"creator": "c", "name": "n"})


if __name__ == '__main__':
    unittest.main()

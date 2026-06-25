import unittest

from onlinepayments.sdk.webhooks.in_memory_secret_key_store import InMemorySecretKeyStore
from onlinepayments.sdk.webhooks.secret_key_not_available_exception import SecretKeyNotAvailableException


class InMemorySecretKeyStoreTest(unittest.TestCase):

    def setUp(self):
        InMemorySecretKeyStore.instance().clear()

    def tearDown(self):
        InMemorySecretKeyStore.instance().clear()

    def test_AccessingSingleton_DefaultScenario_ReturnNonNullInstance(self):
        self.assertIsNotNone(InMemorySecretKeyStore.instance())

    def test_AccessingSingleton_DefaultScenario_ReturnSameInstanceOnMultipleAccess(self):
        instance1 = InMemorySecretKeyStore.instance()
        instance2 = InMemorySecretKeyStore.instance()
        self.assertIs(instance1, instance2)

    def test_StoringSecretKey_DefaultScenario_StoreValidKeyAndValue(self):
        store = InMemorySecretKeyStore.instance()
        store.store_secret_key("key-id-1", "secret-value-1")
        self.assertEqual("secret-value-1", store.get_secret_key("key-id-1"))

    def test_StoringSecretKey_DefaultScenario_ThrowExceptionWhenKeyIdIsNull(self):
        store = InMemorySecretKeyStore.instance()
        with self.assertRaises(ValueError):
            store.store_secret_key(None, "secret-value")

    def test_StoringSecretKey_DefaultScenario_ThrowExceptionWhenKeyIdIsEmpty(self):
        store = InMemorySecretKeyStore.instance()
        with self.assertRaises(ValueError):
            store.store_secret_key("", "secret-value")

    def test_StoringSecretKey_DefaultScenario_ThrowExceptionWhenKeyIdIsWhitespace(self):
        store = InMemorySecretKeyStore.instance()
        with self.assertRaises(ValueError):
            store.store_secret_key("   ", "secret-value")

    def test_StoringSecretKey_DefaultScenario_ThrowExceptionWhenSecretKeyIsNull(self):
        store = InMemorySecretKeyStore.instance()
        with self.assertRaises(ValueError):
            store.store_secret_key("key-id", None)

    def test_StoringSecretKey_DefaultScenario_ThrowExceptionWhenSecretKeyIsEmpty(self):
        store = InMemorySecretKeyStore.instance()
        with self.assertRaises(ValueError):
            store.store_secret_key("key-id", "")

    def test_StoringSecretKey_DefaultScenario_ThrowExceptionWhenSecretKeyIsWhitespace(self):
        store = InMemorySecretKeyStore.instance()
        with self.assertRaises(ValueError):
            store.store_secret_key("key-id", "   ")

    def test_StoringSecretKey_DefaultScenario_UpdateExistingKey(self):
        store = InMemorySecretKeyStore.instance()
        store.store_secret_key("key-id", "secret-1")
        store.store_secret_key("key-id", "secret-2")
        self.assertEqual("secret-2", store.get_secret_key("key-id"))

    def test_GettingSecretKey_DefaultScenario_ReturnExistingKey(self):
        store = InMemorySecretKeyStore.instance()
        store.store_secret_key("test-key", "test-secret")
        self.assertEqual("test-secret", store.get_secret_key("test-key"))

    def test_GettingSecretKey_DefaultScenario_ThrowExceptionWhenKeyNotFound(self):
        store = InMemorySecretKeyStore.instance()
        with self.assertRaises(SecretKeyNotAvailableException):
            store.get_secret_key("non-existent-key")

    def test_RemovingSecretKey_DefaultScenario_RemoveExistingKey(self):
        store = InMemorySecretKeyStore.instance()
        store.store_secret_key("key-to-remove", "secret")
        store.remove_secret_key("key-to-remove")
        with self.assertRaises(SecretKeyNotAvailableException):
            store.get_secret_key("key-to-remove")

    def test_RemovingSecretKey_DefaultScenario_RaiseKeyErrorWhenRemovingNonExistentKey(self):
        store = InMemorySecretKeyStore.instance()
        with self.assertRaises(KeyError):
            store.remove_secret_key("non-existent-key")

    def test_RemovingSecretKey_DefaultScenario_NotAffectOtherKeys(self):
        store = InMemorySecretKeyStore.instance()
        store.store_secret_key("key-1", "secret-1")
        store.store_secret_key("key-2", "secret-2")
        store.remove_secret_key("key-1")
        self.assertEqual("secret-2", store.get_secret_key("key-2"))

    def test_ClearingStore_DefaultScenario_RemoveAllKeys(self):
        store = InMemorySecretKeyStore.instance()
        store.store_secret_key("key-1", "secret-1")
        store.store_secret_key("key-2", "secret-2")
        store.store_secret_key("key-3", "secret-3")
        store.clear()
        with self.assertRaises(SecretKeyNotAvailableException):
            store.get_secret_key("key-1")
        with self.assertRaises(SecretKeyNotAvailableException):
            store.get_secret_key("key-2")
        with self.assertRaises(SecretKeyNotAvailableException):
            store.get_secret_key("key-3")

    def test_ClearingStore_DefaultScenario_AllowStoringNewKeysAfterClear(self):
        store = InMemorySecretKeyStore.instance()
        store.store_secret_key("old-key", "old-secret")
        store.clear()
        store.store_secret_key("new-key", "new-secret")
        self.assertEqual("new-secret", store.get_secret_key("new-key"))

    def test_WorkingWithMultipleKeys_DefaultScenario_StoreAndRetrieveMultipleKeys(self):
        store = InMemorySecretKeyStore.instance()
        store.store_secret_key("key-1", "secret-1")
        store.store_secret_key("key-2", "secret-2")
        store.store_secret_key("key-3", "secret-3")
        self.assertEqual("secret-1", store.get_secret_key("key-1"))
        self.assertEqual("secret-2", store.get_secret_key("key-2"))
        self.assertEqual("secret-3", store.get_secret_key("key-3"))

    def test_WorkingWithMultipleKeys_DefaultScenario_MaintainSeparateKeysIndependently(self):
        store = InMemorySecretKeyStore.instance()
        store.store_secret_key("api-key-1", "api-secret-1")
        store.store_secret_key("api-key-2", "api-secret-2")
        store.remove_secret_key("api-key-1")
        self.assertEqual("api-secret-2", store.get_secret_key("api-key-2"))
        with self.assertRaises(SecretKeyNotAvailableException):
            store.get_secret_key("api-key-1")

    def test_WorkingWithMultipleKeys_DefaultScenario_HandleSpecialCharactersInValues(self):
        store = InMemorySecretKeyStore.instance()
        special_secret = "secret!@#$%^&*()_+-=[]{}|;':./<>?"
        store.store_secret_key("special-key", special_secret)
        self.assertEqual(special_secret, store.get_secret_key("special-key"))

    def test_WorkingWithMultipleKeys_DefaultScenario_HandleLongSecretValues(self):
        store = InMemorySecretKeyStore.instance()
        long_secret = "a" * 10000
        store.store_secret_key("long-key", long_secret)
        self.assertEqual(long_secret, store.get_secret_key("long-key"))

    def test_GettingSecretKey_DefaultScenario_ThrowExceptionWithCorrectKeyId(self):
        store = InMemorySecretKeyStore.instance()
        try:
            store.get_secret_key("missing-key-id")
            self.fail("Expected SecretKeyNotAvailableException")
        except SecretKeyNotAvailableException as e:
            self.assertEqual("missing-key-id", e.key_id)

    def test_GettingSecretKey_DefaultScenario_ThrowExceptionWithCorrectMessage(self):
        store = InMemorySecretKeyStore.instance()
        try:
            store.get_secret_key("unknown-key")
            self.fail("Expected SecretKeyNotAvailableException")
        except SecretKeyNotAvailableException as e:
            self.assertIn("unknown-key", str(e))


if __name__ == '__main__':
    unittest.main()

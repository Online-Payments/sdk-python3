import unittest

from onlinepayments.sdk.defaultimpl.default_marshaller import DefaultMarshaller
from onlinepayments.sdk.webhooks.in_memory_secret_key_store import InMemorySecretKeyStore
from onlinepayments.sdk.webhooks.web_hooks import Webhooks


class WebhooksTest(unittest.TestCase):
    def test_create_helper(self):
        helper = Webhooks.create_helper(InMemorySecretKeyStore.INSTANCE())
        self.assertIs(DefaultMarshaller.INSTANCE(), helper.marshaller)
        self.assertIs(InMemorySecretKeyStore.INSTANCE(),
                      helper.secret_key_store)


if __name__ == '__main__':
    unittest.main()

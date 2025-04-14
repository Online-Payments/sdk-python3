import unittest

from onlinepayments.sdk.json.default_marshaller import DefaultMarshaller
from onlinepayments.sdk.webhooks.webhooks_helper import WebhooksHelper
from onlinepayments.sdk.webhooks.in_memory_secret_key_store import InMemorySecretKeyStore


class WebhooksTest(unittest.TestCase):
    def test_create_helper(self):
        helper = WebhooksHelper(DefaultMarshaller.instance(), InMemorySecretKeyStore.instance())
        self.assertIs(DefaultMarshaller.instance(), helper.marshaller)
        self.assertIs(InMemorySecretKeyStore.instance(), helper.secret_key_store)


if __name__ == '__main__':
    unittest.main()

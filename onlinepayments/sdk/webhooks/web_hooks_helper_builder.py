from onlinepayments.sdk.marshaller import Marshaller
from onlinepayments.sdk.webhooks.secret_key_store import SecretKeyStore
from onlinepayments.sdk.webhooks.web_hooks_helper import WebhooksHelper


class WebhooksHelperBuilder:
    """
    Builder for a WebhooksHelper object.
    """
    __marshaller = None
    __secret_key_store = None

    def with_marshaller(self, marshaller: Marshaller):
        """
        Sets the Marshaller to use.
        """
        self.__marshaller = marshaller
        return self

    def with_secret_key_store(self, secret_key_store: SecretKeyStore):
        """
        Sets the SecretKeyStore to use.
        """
        self.__secret_key_store = secret_key_store
        return self

    def build(self):
        """
        Creates a fully initialized WebhooksHelper object.

        :raise: ValueError: if not all required components are set
        """
        return WebhooksHelper(self.__marshaller, self.__secret_key_store)

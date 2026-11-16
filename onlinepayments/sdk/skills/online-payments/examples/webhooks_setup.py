from abc import ABC, abstractmethod

from onlinepayments.sdk.domain.web_hooks_event import WebhooksEvent
from onlinepayments.sdk.json.default_marshaller import DefaultMarshaller
from onlinepayments.sdk.webhooks.in_memory_secret_key_store import InMemorySecretKeyStore
from onlinepayments.sdk.webhooks.webhooks_helper import WebhooksHelper

from client_setup import required_env


# [START webhooks-setup]
# Create the helper once. The key ID and secret come from the Merchant Portal (Developer > Webhooks).
# required_env fails at startup when a value is missing or blank. Keep the secret in your secret store, or for local
# development in an environment variable; never in the repository.
# In production you can pass your own SecretKeyStore subclass with get_secret_key(key_id) on top of your secret storage.
def create_webhooks_helper() -> WebhooksHelper:
    secret_key_store = InMemorySecretKeyStore.instance()
    secret_key_store.store_secret_key(required_env("onlinePayments_webhooks_keyId"),
                                      required_env("onlinePayments_webhooks_secret"))
    return WebhooksHelper(DefaultMarshaller.instance(), secret_key_store)
# [END webhooks-setup]


class WebhookInbox(ABC):
    """
    Stand-in for durable storage: a database table or a persistent queue. A background job reads the saved
    events and processes them; it retries the ones that failed.
    """

    @abstractmethod
    def save_event(self, webhooks_event: WebhooksEvent) -> None:
        """
        Saves a verified event. Ignore a duplicate: the platform can send the same event more than once, and the
        webhooks guide identifies a duplicate by identical payment.id and type.
        """

    @abstractmethod
    def save_unreadable(self, raw_body: bytes) -> None:
        """
        Saves the raw body of an event that passed verification but that the SDK cannot read, to replay it
        after you upgrade the SDK.
        """

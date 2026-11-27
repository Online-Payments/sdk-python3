#
# This file was automatically generated.
#
from .data_object import DataObject


class Feedbacks(DataObject):

    __slots__ = (
        "__webhook_url",
        "__webhooks_urls",
    )

    __webhook_url: str | None
    __webhooks_urls: list[str] | None

    def __init__(
        self,
        *,
        webhook_url: str | None = None,
        webhooks_urls: list[str] | None = None,
    ) -> None:
        self.webhook_url = webhook_url
        self.webhooks_urls = webhooks_urls

    @property
    def webhook_url(self) -> str | None:
        """
        | The URL where the webhook will be dispatched for all status change events related to this payment.

        Type: str

        Deprecated; The URL where the webhook will be dispatched for all status change events related to this payment.
        """
        return self.__webhook_url

    @webhook_url.setter
    def webhook_url(self, value: str | None) -> None:
        self.__webhook_url = value

    @property
    def webhooks_urls(self) -> list[str] | None:
        """
        | The list of the URLs where the webhook will be dispatched for all status change events related to this payment.

        Type: list[str]
        """
        return self.__webhooks_urls

    @webhooks_urls.setter
    def webhooks_urls(self, value: list[str] | None) -> None:
        self.__webhooks_urls = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.webhook_url is not None:
            dictionary['webhookUrl'] = self.webhook_url
        if self.webhooks_urls is not None:
            dictionary['webhooksUrls'] = []
            for element in self.webhooks_urls:
                if element is not None:
                    dictionary['webhooksUrls'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'Feedbacks':
        super().from_dictionary(dictionary)
        if 'webhookUrl' in dictionary:
            self.webhook_url = dictionary['webhookUrl']
        if 'webhooksUrls' in dictionary:
            if not isinstance(dictionary['webhooksUrls'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['webhooksUrls']))
            self.webhooks_urls = []
            for element in dictionary['webhooksUrls']:
                self.webhooks_urls.append(element)
        return self

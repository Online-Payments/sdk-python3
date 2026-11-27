#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentProduct5001(DataObject):
    """
    Deprecated; Deprecated by pendingAuthentication. Contains the third party data for payment product 5001 (Bizum)
    """

    __slots__ = (
        "__message",
        "__polling_url",
    )

    __message: str | None
    __polling_url: str | None

    def __init__(
        self,
        *,
        message: str | None = None,
        polling_url: str | None = None,
    ) -> None:
        self.message = message
        self.polling_url = polling_url

    @property
    def message(self) -> str | None:
        """
        | A text string intended to be displayed to the consumer

        Type: str
        """
        return self.__message

    @message.setter
    def message(self, value: str | None) -> None:
        self.__message = value

    @property
    def polling_url(self) -> str | None:
        """
        | A URL that must be polled using JavaScript; it responds with either true or false to say if transaction is still pending or not. As long as the response status is 'true', the message should be shown and polling should continue. Once the status changes to 'false', you should verify the payment outcome and redirect the customer to your status page accordingly. Remember, a pending status 'false' indicates that the Bizum process has concluded, but it does not necessarily confirm a successful payment. And if you end the polling after a few minutes without receiving the status 'false', it means that the transaction can't be ended as accepted or refused yet. NB - If you try to call the polling endpoint with invalid data, you will receive an http 204.

        Type: str
        """
        return self.__polling_url

    @polling_url.setter
    def polling_url(self, value: str | None) -> None:
        self.__polling_url = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.message is not None:
            dictionary['message'] = self.message
        if self.polling_url is not None:
            dictionary['pollingUrl'] = self.polling_url
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct5001':
        super().from_dictionary(dictionary)
        if 'message' in dictionary:
            self.message = dictionary['message']
        if 'pollingUrl' in dictionary:
            self.polling_url = dictionary['pollingUrl']
        return self

#
# This file was automatically generated.
#
from .cancel_payment_request import CancelPaymentRequest
from .data_object import DataObject


class CancelPaymentBatchRequest(DataObject):

    __slots__ = (
        "__cancel",
        "__payment_id",
    )

    __cancel: CancelPaymentRequest | None
    __payment_id: str | None

    def __init__(
        self,
        *,
        cancel: CancelPaymentRequest | None = None,
        payment_id: str | None = None,
    ) -> None:
        self.cancel = cancel
        self.payment_id = payment_id

    @property
    def cancel(self) -> CancelPaymentRequest | None:
        """
        Type: :class:`onlinepayments.sdk.domain.cancel_payment_request.CancelPaymentRequest`
        """
        return self.__cancel

    @cancel.setter
    def cancel(self, value: CancelPaymentRequest | None) -> None:
        self.__cancel = value

    @property
    def payment_id(self) -> str | None:
        """
        | This is our unique payment transaction identifier.

        Type: str
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value: str | None) -> None:
        self.__payment_id = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.cancel is not None:
            dictionary['cancel'] = self.cancel.to_dictionary()
        if self.payment_id is not None:
            dictionary['paymentId'] = self.payment_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CancelPaymentBatchRequest':
        super().from_dictionary(dictionary)
        if 'cancel' in dictionary:
            if not isinstance(dictionary['cancel'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cancel']))
            value = CancelPaymentRequest()
            self.cancel = value.from_dictionary(dictionary['cancel'])
        if 'paymentId' in dictionary:
            self.payment_id = dictionary['paymentId']
        return self

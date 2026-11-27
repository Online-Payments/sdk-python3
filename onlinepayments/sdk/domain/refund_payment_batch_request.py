#
# This file was automatically generated.
#
from .data_object import DataObject
from .refund_request import RefundRequest


class RefundPaymentBatchRequest(DataObject):

    __slots__ = (
        "__payment_id",
        "__refund",
    )

    __payment_id: str | None
    __refund: RefundRequest | None

    def __init__(
        self,
        *,
        payment_id: str | None = None,
        refund: RefundRequest | None = None,
    ) -> None:
        self.payment_id = payment_id
        self.refund = refund

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

    @property
    def refund(self) -> RefundRequest | None:
        """
        Type: :class:`onlinepayments.sdk.domain.refund_request.RefundRequest`
        """
        return self.__refund

    @refund.setter
    def refund(self, value: RefundRequest | None) -> None:
        self.__refund = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.payment_id is not None:
            dictionary['paymentId'] = self.payment_id
        if self.refund is not None:
            dictionary['refund'] = self.refund.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RefundPaymentBatchRequest':
        super().from_dictionary(dictionary)
        if 'paymentId' in dictionary:
            self.payment_id = dictionary['paymentId']
        if 'refund' in dictionary:
            if not isinstance(dictionary['refund'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['refund']))
            value = RefundRequest()
            self.refund = value.from_dictionary(dictionary['refund'])
        return self

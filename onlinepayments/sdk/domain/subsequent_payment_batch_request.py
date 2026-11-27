#
# This file was automatically generated.
#
from .data_object import DataObject
from .subsequent_payment_request import SubsequentPaymentRequest


class SubsequentPaymentBatchRequest(DataObject):

    __slots__ = (
        "__payment_id",
        "__subsequent",
    )

    __payment_id: str | None
    __subsequent: SubsequentPaymentRequest | None

    def __init__(
        self,
        *,
        payment_id: str | None = None,
        subsequent: SubsequentPaymentRequest | None = None,
    ) -> None:
        self.payment_id = payment_id
        self.subsequent = subsequent

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
    def subsequent(self) -> SubsequentPaymentRequest | None:
        """
        Type: :class:`onlinepayments.sdk.domain.subsequent_payment_request.SubsequentPaymentRequest`
        """
        return self.__subsequent

    @subsequent.setter
    def subsequent(self, value: SubsequentPaymentRequest | None) -> None:
        self.__subsequent = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.payment_id is not None:
            dictionary['paymentId'] = self.payment_id
        if self.subsequent is not None:
            dictionary['subsequent'] = self.subsequent.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SubsequentPaymentBatchRequest':
        super().from_dictionary(dictionary)
        if 'paymentId' in dictionary:
            self.payment_id = dictionary['paymentId']
        if 'subsequent' in dictionary:
            if not isinstance(dictionary['subsequent'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['subsequent']))
            value = SubsequentPaymentRequest()
            self.subsequent = value.from_dictionary(dictionary['subsequent'])
        return self

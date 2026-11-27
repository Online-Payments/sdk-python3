#
# This file was automatically generated.
#
from .data_object import DataObject


class OmnichannelPayoutSpecificInput(DataObject):

    __slots__ = (
        "__operator_id",
        "__payment_id",
    )

    __operator_id: str | None
    __payment_id: str | None

    def __init__(
        self,
        *,
        operator_id: str | None = None,
        payment_id: str | None = None,
    ) -> None:
        self.operator_id = operator_id
        self.payment_id = payment_id

    @property
    def operator_id(self) -> str | None:
        """
        | Merchants may optionally include a user identifier to indicate which person within their organization initiated this request, enabling detailed audit trails and transaction accountability. If not provided, the field defaults to the merchant ID.

        Type: str
        """
        return self.__operator_id

    @operator_id.setter
    def operator_id(self, value: str | None) -> None:
        self.__operator_id = value

    @property
    def payment_id(self) -> str | None:
        """
        | The Payment Id of the transaction (either in-store or online), from which you request to make a refund.

        Type: str
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value: str | None) -> None:
        self.__payment_id = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.operator_id is not None:
            dictionary['operatorId'] = self.operator_id
        if self.payment_id is not None:
            dictionary['paymentId'] = self.payment_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'OmnichannelPayoutSpecificInput':
        super().from_dictionary(dictionary)
        if 'operatorId' in dictionary:
            self.operator_id = dictionary['operatorId']
        if 'paymentId' in dictionary:
            self.payment_id = dictionary['paymentId']
        return self

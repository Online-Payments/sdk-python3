#
# This file was automatically generated.
#
from .data_object import DataObject


class OmnichannelPaymentSpecificInput(DataObject):

    __slots__ = (
        "__operator_id",
    )

    __operator_id: str | None

    def __init__(
        self,
        *,
        operator_id: str | None = None,
    ) -> None:
        self.operator_id = operator_id

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

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.operator_id is not None:
            dictionary['operatorId'] = self.operator_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'OmnichannelPaymentSpecificInput':
        super().from_dictionary(dictionary)
        if 'operatorId' in dictionary:
            self.operator_id = dictionary['operatorId']
        return self

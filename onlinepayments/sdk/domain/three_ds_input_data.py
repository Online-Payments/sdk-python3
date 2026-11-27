#
# This file was automatically generated.
#
from .data_object import DataObject


class ThreeDsInputData(DataObject):

    __slots__ = (
        "__acquirer_id",
        "__acquirer_mid",
        "__requestor_id",
    )

    __acquirer_id: str | None
    __acquirer_mid: str | None
    __requestor_id: str | None

    def __init__(
        self,
        *,
        acquirer_id: str | None = None,
        acquirer_mid: str | None = None,
        requestor_id: str | None = None,
    ) -> None:
        self.acquirer_id = acquirer_id
        self.acquirer_mid = acquirer_mid
        self.requestor_id = requestor_id

    @property
    def acquirer_id(self) -> str | None:
        """
        | Merchant’s Acquirer ID.

        Type: str
        """
        return self.__acquirer_id

    @acquirer_id.setter
    def acquirer_id(self, value: str | None) -> None:
        self.__acquirer_id = value

    @property
    def acquirer_mid(self) -> str | None:
        """
        | Acquirer’s Merchant ID.

        Type: str
        """
        return self.__acquirer_mid

    @acquirer_mid.setter
    def acquirer_mid(self, value: str | None) -> None:
        self.__acquirer_mid = value

    @property
    def requestor_id(self) -> str | None:
        """
        | The ID assigned to the merchant for authentication request to initiate 3DS with MPI.

        Type: str
        """
        return self.__requestor_id

    @requestor_id.setter
    def requestor_id(self, value: str | None) -> None:
        self.__requestor_id = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.acquirer_id is not None:
            dictionary['acquirerId'] = self.acquirer_id
        if self.acquirer_mid is not None:
            dictionary['acquirerMid'] = self.acquirer_mid
        if self.requestor_id is not None:
            dictionary['requestorId'] = self.requestor_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ThreeDsInputData':
        super().from_dictionary(dictionary)
        if 'acquirerId' in dictionary:
            self.acquirer_id = dictionary['acquirerId']
        if 'acquirerMid' in dictionary:
            self.acquirer_mid = dictionary['acquirerMid']
        if 'requestorId' in dictionary:
            self.requestor_id = dictionary['requestorId']
        return self

#
# This file was automatically generated.
#
from .data_object import DataObject
from .payout_output import PayoutOutput
from .payout_status_output import PayoutStatusOutput


class PayoutResponse(DataObject):

    __slots__ = (
        "__id",
        "__payout_output",
        "__status",
        "__status_output",
    )

    __id: str | None
    __payout_output: PayoutOutput | None
    __status: str | None
    __status_output: PayoutStatusOutput | None

    def __init__(
        self,
        *,
        id: str | None = None,
        payout_output: PayoutOutput | None = None,
        status: str | None = None,
        status_output: PayoutStatusOutput | None = None,
    ) -> None:
        self.id = id
        self.payout_output = payout_output
        self.status = status
        self.status_output = status_output

    @property
    def id(self) -> str | None:
        """
        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: str | None) -> None:
        self.__id = value

    @property
    def payout_output(self) -> PayoutOutput | None:
        """
        Type: :class:`onlinepayments.sdk.domain.payout_output.PayoutOutput`
        """
        return self.__payout_output

    @payout_output.setter
    def payout_output(self, value: PayoutOutput | None) -> None:
        self.__payout_output = value

    @property
    def status(self) -> str | None:
        """
        | Current high-level status of the payout in a human-readable form.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: str | None) -> None:
        self.__status = value

    @property
    def status_output(self) -> PayoutStatusOutput | None:
        """
        Type: :class:`onlinepayments.sdk.domain.payout_status_output.PayoutStatusOutput`
        """
        return self.__status_output

    @status_output.setter
    def status_output(self, value: PayoutStatusOutput | None) -> None:
        self.__status_output = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.payout_output is not None:
            dictionary['payoutOutput'] = self.payout_output.to_dictionary()
        if self.status is not None:
            dictionary['status'] = self.status
        if self.status_output is not None:
            dictionary['statusOutput'] = self.status_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PayoutResponse':
        super().from_dictionary(dictionary)
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'payoutOutput' in dictionary:
            if not isinstance(dictionary['payoutOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payoutOutput']))
            value = PayoutOutput()
            self.payout_output = value.from_dictionary(dictionary['payoutOutput'])
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'statusOutput' in dictionary:
            if not isinstance(dictionary['statusOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['statusOutput']))
            value = PayoutStatusOutput()
            self.status_output = value.from_dictionary(dictionary['statusOutput'])
        return self

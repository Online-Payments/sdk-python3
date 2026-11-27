#
# This file was automatically generated.
#
from .data_object import DataObject


class AccountOnFileAttribute(DataObject):

    __slots__ = (
        "__key",
        "__must_write_reason",
        "__status",
        "__value",
    )

    __key: str | None
    __must_write_reason: str | None
    __status: str | None
    __value: str | None

    def __init__(
        self,
        *,
        key: str | None = None,
        must_write_reason: str | None = None,
        status: str | None = None,
        value: str | None = None,
    ) -> None:
        self.key = key
        self.must_write_reason = must_write_reason
        self.status = status
        self.value = value

    @property
    def key(self) -> str | None:
        """
        | Name of the key or property

        Type: str
        """
        return self.__key

    @key.setter
    def key(self, value: str | None) -> None:
        self.__key = value

    @property
    def must_write_reason(self) -> str | None:
        """
        | Deprecated: This field is not used by any payment product The reason why the status is MUST_WRITE. Currently only "IN_THE_PAST" is possible as value (for expiry date), but this can be extended with new values in the future.

        Type: str

        Deprecated; Deprecated
        """
        return self.__must_write_reason

    @must_write_reason.setter
    def must_write_reason(self, value: str | None) -> None:
        self.__must_write_reason = value

    @property
    def status(self) -> str | None:
        """
        | Possible values:
        
        * READ_ONLY - attribute cannot be updated and should be presented in that way to the user
        * CAN_WRITE - attribute can be updated and should be presented as an editable field, for example an expiration date that will expire very soon
        * MUST_WRITE - attribute should be updated and must be presented as an editable field, for example an expiration date that has already expired Any updated values that are entered for CAN_WRITE or MUST_WRITE will be used to update the values stored in the token.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: str | None) -> None:
        self.__status = value

    @property
    def value(self) -> str | None:
        """
        | Value of the key or property

        Type: str
        """
        return self.__value

    @value.setter
    def value(self, value: str | None) -> None:
        self.__value = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.key is not None:
            dictionary['key'] = self.key
        if self.must_write_reason is not None:
            dictionary['mustWriteReason'] = self.must_write_reason
        if self.status is not None:
            dictionary['status'] = self.status
        if self.value is not None:
            dictionary['value'] = self.value
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AccountOnFileAttribute':
        super().from_dictionary(dictionary)
        if 'key' in dictionary:
            self.key = dictionary['key']
        if 'mustWriteReason' in dictionary:
            self.must_write_reason = dictionary['mustWriteReason']
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'value' in dictionary:
            self.value = dictionary['value']
        return self

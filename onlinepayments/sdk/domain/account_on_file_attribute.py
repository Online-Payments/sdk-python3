# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class AccountOnFileAttribute(DataObject):
    """
    | Array containing the details of the stored token
    """

    __key = None
    __must_write_reason = None
    __status = None
    __value = None

    @property
    def key(self) -> str:
        """
        | Name of the key or property

        Type: str
        """
        return self.__key

    @key.setter
    def key(self, value: str):
        self.__key = value

    @property
    def must_write_reason(self) -> str:
        """
        | Deprecated: This field is not used by any payment product
        | The reason why the status is MUST_WRITE. Currently only "IN_THE_PAST" is possible as value (for expiry date), but this can be extended with new values in the future.

        Type: str
        """
        return self.__must_write_reason

    @must_write_reason.setter
    def must_write_reason(self, value: str):
        self.__must_write_reason = value

    @property
    def status(self) -> str:
        """
        | Possible values:
        | * READ_ONLY - attribute cannot be updated and should be presented in that way to the user
        | * CAN_WRITE - attribute can be updated and should be presented as an editable field, for example an expiration date that will expire very soon
        | * MUST_WRITE - attribute should be updated and must be presented as an editable field, for example an expiration date that has already expired
        | Any updated values that are entered for CAN_WRITE or MUST_WRITE will be used to update the values stored in the token.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: str):
        self.__status = value

    @property
    def value(self) -> str:
        """
        | Value of the key or property

        Type: str
        """
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def to_dictionary(self):
        dictionary = super(AccountOnFileAttribute, self).to_dictionary()
        if self.key is not None:
            dictionary['key'] = self.key
        if self.must_write_reason is not None:
            dictionary['mustWriteReason'] = self.must_write_reason
        if self.status is not None:
            dictionary['status'] = self.status
        if self.value is not None:
            dictionary['value'] = self.value
        return dictionary

    def from_dictionary(self, dictionary):
        super(AccountOnFileAttribute, self).from_dictionary(dictionary)
        if 'key' in dictionary:
            self.key = dictionary['key']
        if 'mustWriteReason' in dictionary:
            self.must_write_reason = dictionary['mustWriteReason']
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'value' in dictionary:
            self.value = dictionary['value']
        return self

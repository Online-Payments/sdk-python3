# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class CaptureStatusOutput(DataObject):
    """
    | This object has the numeric representation of the current capture status, timestamp of last status change and performable action on the current payment resource. In case of failed payments and negative scenarios, detailed error information is listed.
    """

    __status_code = None

    @property
    def status_code(self) -> int:
        """
        | Numeric status code of the legacy API. It is returned to ease the migration from the legacy APIs. You should not write new business logic based on this property as it will be deprecated in a future version of the API. The value can also be found in the BackOffice and in report files.

        Type: int
        """
        return self.__status_code

    @status_code.setter
    def status_code(self, value: int):
        self.__status_code = value

    def to_dictionary(self):
        dictionary = super(CaptureStatusOutput, self).to_dictionary()
        if self.status_code is not None:
            dictionary['statusCode'] = self.status_code
        return dictionary

    def from_dictionary(self, dictionary):
        super(CaptureStatusOutput, self).from_dictionary(dictionary)
        if 'statusCode' in dictionary:
            self.status_code = dictionary['statusCode']
        return self

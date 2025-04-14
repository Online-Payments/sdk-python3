# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class APIError(DataObject):

    __category: Optional[str] = None
    __code: Optional[str] = None
    __error_code: Optional[str] = None
    __http_status_code: Optional[int] = None
    __id: Optional[str] = None
    __message: Optional[str] = None
    __property_name: Optional[str] = None
    __retriable: Optional[bool] = None

    @property
    def category(self) -> Optional[str]:
        """
        | Category the error belongs to. The category should give an indication of the type of error you are dealing with. Possible values:
        
        * DIRECT_PLATFORM_ERROR - indicating that a functional error has occurred in the platform.
        * PAYMENT_PLATFORM_ERROR - indicating that a functional error has occurred in the payment platform.
        * IO_ERROR - indicating that a technical error has occurred within the payment platform or between the payment platform and third party systems.

        Type: str
        """
        return self.__category

    @category.setter
    def category(self, value: Optional[str]) -> None:
        self.__category = value

    @property
    def code(self) -> Optional[str]:
        """
        | Deprecated: Use errorCode instead. Error code

        Type: str

        Deprecated; Use errorCode instead. Error code
        """
        return self.__code

    @code.setter
    def code(self, value: Optional[str]) -> None:
        self.__code = value

    @property
    def error_code(self) -> Optional[str]:
        """
        | Error code

        Type: str
        """
        return self.__error_code

    @error_code.setter
    def error_code(self, value: Optional[str]) -> None:
        self.__error_code = value

    @property
    def http_status_code(self) -> Optional[int]:
        """
        | HTTP status code for this error that can be used to determine the type of error

        Type: int
        """
        return self.__http_status_code

    @http_status_code.setter
    def http_status_code(self, value: Optional[int]) -> None:
        self.__http_status_code = value

    @property
    def id(self) -> Optional[str]:
        """
        | ID of the error. This is a short human-readable message that briefly describes the error.

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: Optional[str]) -> None:
        self.__id = value

    @property
    def message(self) -> Optional[str]:
        """
        | Human-readable error message that is not meant to be relayed to customer as it might tip off people who are trying to commit fraud

        Type: str
        """
        return self.__message

    @message.setter
    def message(self, value: Optional[str]) -> None:
        self.__message = value

    @property
    def property_name(self) -> Optional[str]:
        """
        | Returned only if the error relates to a value that was missing or incorrect.
        |
        | Contains a location path to the value as a JSonata query.
        |
        | Some common examples:
        
        * a.b selects the value of property b of root property a,
        * a[1] selects the first element of the array in root property a,
        * a[b='some value'] selects all elements of the array in root property a that have a property b with value 'some value'.

        Type: str
        """
        return self.__property_name

    @property_name.setter
    def property_name(self, value: Optional[str]) -> None:
        self.__property_name = value

    @property
    def retriable(self) -> Optional[bool]:
        """
        | Flag indicating if the request is retriable. Retriable requests mean that a technical error happened and that the same request can safely be sent again with a new idempotence key.

        Type: bool
        """
        return self.__retriable

    @retriable.setter
    def retriable(self, value: Optional[bool]) -> None:
        self.__retriable = value

    def to_dictionary(self) -> dict:
        dictionary = super(APIError, self).to_dictionary()
        if self.category is not None:
            dictionary['category'] = self.category
        if self.code is not None:
            dictionary['code'] = self.code
        if self.error_code is not None:
            dictionary['errorCode'] = self.error_code
        if self.http_status_code is not None:
            dictionary['httpStatusCode'] = self.http_status_code
        if self.id is not None:
            dictionary['id'] = self.id
        if self.message is not None:
            dictionary['message'] = self.message
        if self.property_name is not None:
            dictionary['propertyName'] = self.property_name
        if self.retriable is not None:
            dictionary['retriable'] = self.retriable
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'APIError':
        super(APIError, self).from_dictionary(dictionary)
        if 'category' in dictionary:
            self.category = dictionary['category']
        if 'code' in dictionary:
            self.code = dictionary['code']
        if 'errorCode' in dictionary:
            self.error_code = dictionary['errorCode']
        if 'httpStatusCode' in dictionary:
            self.http_status_code = dictionary['httpStatusCode']
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'message' in dictionary:
            self.message = dictionary['message']
        if 'propertyName' in dictionary:
            self.property_name = dictionary['propertyName']
        if 'retriable' in dictionary:
            self.retriable = dictionary['retriable']
        return self

# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class APIError(DataObject):
    """
    | Contains detailed information on one single error.
    """

    __category = None
    __code = None
    __http_status_code = None
    __id = None
    __message = None
    __property_name = None

    @property
    def category(self) -> str:
        """
        | Category the error belongs to. The category should give an indication of the type of error you are dealing with. Possible values:
        | * DIRECT_PLATFORM_ERROR - indicating that a functional error has occurred in the platform.
        | * PAYMENT_PLATFORM_ERROR - indicating that a functional error has occurred in the payment platform.
        | * IO_ERROR - indicating that a technical error has occurred within the payment platform or between the payment platform and third party systems.

        Type: str
        """
        return self.__category

    @category.setter
    def category(self, value: str):
        self.__category = value

    @property
    def code(self) -> str:
        """
        | Error code

        Type: str
        """
        return self.__code

    @code.setter
    def code(self, value: str):
        self.__code = value

    @property
    def http_status_code(self) -> int:
        """
        | HTTP status code for this error that can be used to determine the type of error

        Type: int
        """
        return self.__http_status_code

    @http_status_code.setter
    def http_status_code(self, value: int):
        self.__http_status_code = value

    @property
    def id(self) -> str:
        """
        | ID of the error. This is a short human-readable message that briefly describes the error.

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value

    @property
    def message(self) -> str:
        """
        | Human-readable error message that is not meant to be relayed to customer as it might tip off people who are trying to commit fraud

        Type: str
        """
        return self.__message

    @message.setter
    def message(self, value: str):
        self.__message = value

    @property
    def property_name(self) -> str:
        """
        | Returned only if the error relates to a value that was missing or incorrect.
        
        | Contains a location path to the value as a JSonata query.
        
        | Some common examples:
        | * a.b selects the value of property b of root property a,
        | * a[1] selects the first element of the array in root property a,
        | * a[b='some value'] selects all elements of the array in root property a that have a property b with value 'some value'.

        Type: str
        """
        return self.__property_name

    @property_name.setter
    def property_name(self, value: str):
        self.__property_name = value

    def to_dictionary(self):
        dictionary = super(APIError, self).to_dictionary()
        if self.category is not None:
            dictionary['category'] = self.category
        if self.code is not None:
            dictionary['code'] = self.code
        if self.http_status_code is not None:
            dictionary['httpStatusCode'] = self.http_status_code
        if self.id is not None:
            dictionary['id'] = self.id
        if self.message is not None:
            dictionary['message'] = self.message
        if self.property_name is not None:
            dictionary['propertyName'] = self.property_name
        return dictionary

    def from_dictionary(self, dictionary):
        super(APIError, self).from_dictionary(dictionary)
        if 'category' in dictionary:
            self.category = dictionary['category']
        if 'code' in dictionary:
            self.code = dictionary['code']
        if 'httpStatusCode' in dictionary:
            self.http_status_code = dictionary['httpStatusCode']
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'message' in dictionary:
            self.message = dictionary['message']
        if 'propertyName' in dictionary:
            self.property_name = dictionary['propertyName']
        return self

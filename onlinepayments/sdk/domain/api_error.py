#
# This file was automatically generated.
#
from .data_object import DataObject


class APIError(DataObject):

    __slots__ = (
        "__category",
        "__code",
        "__error_code",
        "__http_status_code",
        "__id",
        "__message",
        "__property_name",
        "__retriable",
    )

    __category: str | None
    __code: str | None
    __error_code: str | None
    __http_status_code: int | None
    __id: str | None
    __message: str | None
    __property_name: str | None
    __retriable: bool | None

    def __init__(
        self,
        *,
        category: str | None = None,
        code: str | None = None,
        error_code: str | None = None,
        http_status_code: int | None = None,
        id: str | None = None,
        message: str | None = None,
        property_name: str | None = None,
        retriable: bool | None = None,
    ) -> None:
        self.category = category
        self.code = code
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.id = id
        self.message = message
        self.property_name = property_name
        self.retriable = retriable

    @property
    def category(self) -> str | None:
        """
        | Category the error belongs to. The category should give an indication of the type of error you are dealing with. Possible values:
        
        * DIRECT_PLATFORM_ERROR - indicating that a functional error has occurred in the platform.
        * PAYMENT_PLATFORM_ERROR - indicating that a functional error has occurred in the payment platform.
        * IO_ERROR - indicating that a technical error has occurred within the payment platform or between the payment platform and third party systems.

        Type: str
        """
        return self.__category

    @category.setter
    def category(self, value: str | None) -> None:
        self.__category = value

    @property
    def code(self) -> str | None:
        """
        | Deprecated: Use errorCode instead. Error code

        Type: str

        Deprecated; Use errorCode instead. Error code
        """
        return self.__code

    @code.setter
    def code(self, value: str | None) -> None:
        self.__code = value

    @property
    def error_code(self) -> str | None:
        """
        | Error code

        Type: str
        """
        return self.__error_code

    @error_code.setter
    def error_code(self, value: str | None) -> None:
        self.__error_code = value

    @property
    def http_status_code(self) -> int | None:
        """
        | HTTP status code for this error that can be used to determine the type of error

        Type: int
        """
        return self.__http_status_code

    @http_status_code.setter
    def http_status_code(self, value: int | None) -> None:
        self.__http_status_code = value

    @property
    def id(self) -> str | None:
        """
        | ID of the error. This is a short human-readable message that briefly describes the error.

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: str | None) -> None:
        self.__id = value

    @property
    def message(self) -> str | None:
        """
        | Human-readable error message that is not meant to be relayed to customer as it might tip off people who are trying to commit fraud

        Type: str
        """
        return self.__message

    @message.setter
    def message(self, value: str | None) -> None:
        self.__message = value

    @property
    def property_name(self) -> str | None:
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
    def property_name(self, value: str | None) -> None:
        self.__property_name = value

    @property
    def retriable(self) -> bool | None:
        """
        | Flag indicating if the request is retriable. Retriable requests mean that a technical error happened and that the same request can safely be sent again with a new idempotence key.

        Type: bool
        """
        return self.__retriable

    @retriable.setter
    def retriable(self, value: bool | None) -> None:
        self.__retriable = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
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
        super().from_dictionary(dictionary)
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

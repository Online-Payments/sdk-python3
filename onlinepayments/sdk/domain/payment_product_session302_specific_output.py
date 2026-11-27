#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentProductSession302SpecificOutput(DataObject):

    __slots__ = (
        "__session",
    )

    __session: str | None

    def __init__(
        self,
        *,
        session: str | None = None,
    ) -> None:
        self.session = session

    @property
    def session(self) -> str | None:
        """
        | The payment session object that must be passed to the Apple Pay API on the client side to initialize the Apple Pay payment sheet.

        Type: str
        """
        return self.__session

    @session.setter
    def session(self, value: str | None) -> None:
        self.__session = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.session is not None:
            dictionary['session'] = self.session
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductSession302SpecificOutput':
        super().from_dictionary(dictionary)
        if 'session' in dictionary:
            self.session = dictionary['session']
        return self

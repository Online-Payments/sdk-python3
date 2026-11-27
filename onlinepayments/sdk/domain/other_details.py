#
# This file was automatically generated.
#
from .data_object import DataObject


class OtherDetails(DataObject):

    __slots__ = (
        "__meta_data",
        "__travel_data",
    )

    __meta_data: str | None
    __travel_data: str | None

    def __init__(
        self,
        *,
        meta_data: str | None = None,
        travel_data: str | None = None,
    ) -> None:
        self.meta_data = meta_data
        self.travel_data = travel_data

    @property
    def meta_data(self) -> str | None:
        """
        | Information used by the following PaymentProducts [5300] to provide details on the item such as the color, size, etc. The field is in JSON format, with keys and values expected by the payment method at transaction creation. Please refer to the payment mean documentation.

        Type: str
        """
        return self.__meta_data

    @meta_data.setter
    def meta_data(self, value: str | None) -> None:
        self.__meta_data = value

    @property
    def travel_data(self) -> str | None:
        """
        | Information used by the following PaymentProducts [5110,5111,5112,5125,3104,3107,3108,3109].

        Type: str
        """
        return self.__travel_data

    @travel_data.setter
    def travel_data(self, value: str | None) -> None:
        self.__travel_data = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.meta_data is not None:
            dictionary['metaData'] = self.meta_data
        if self.travel_data is not None:
            dictionary['travelData'] = self.travel_data
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'OtherDetails':
        super().from_dictionary(dictionary)
        if 'metaData' in dictionary:
            self.meta_data = dictionary['metaData']
        if 'travelData' in dictionary:
            self.travel_data = dictionary['travelData']
        return self

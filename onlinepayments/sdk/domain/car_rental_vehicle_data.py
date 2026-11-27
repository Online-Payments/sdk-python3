#
# This file was automatically generated.
#
from .data_object import DataObject


class CarRentalVehicleData(DataObject):

    __slots__ = (
        "__class_id",
        "__identification_number",
    )

    __class_id: str | None
    __identification_number: str | None

    def __init__(
        self,
        *,
        class_id: str | None = None,
        identification_number: str | None = None,
    ) -> None:
        self.class_id = class_id
        self.identification_number = identification_number

    @property
    def class_id(self) -> str | None:
        """
        | This field contains a code that corresponds to the classification of the rental vehicle.

        Type: str
        """
        return self.__class_id

    @class_id.setter
    def class_id(self, value: str | None) -> None:
        self.__class_id = value

    @property
    def identification_number(self) -> str | None:
        """
        | This field contains a unique identifier assigned by the taxi company to the vehicle.

        Type: str
        """
        return self.__identification_number

    @identification_number.setter
    def identification_number(self, value: str | None) -> None:
        self.__identification_number = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.class_id is not None:
            dictionary['classId'] = self.class_id
        if self.identification_number is not None:
            dictionary['identificationNumber'] = self.identification_number
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CarRentalVehicleData':
        super().from_dictionary(dictionary)
        if 'classId' in dictionary:
            self.class_id = dictionary['classId']
        if 'identificationNumber' in dictionary:
            self.identification_number = dictionary['identificationNumber']
        return self

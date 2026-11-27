#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentLinkOverviewSorting(DataObject):

    __slots__ = (
        "__sort_direction",
        "__sort_property",
    )

    __sort_direction: str | None
    __sort_property: str | None

    def __init__(
        self,
        *,
        sort_direction: str | None = None,
        sort_property: str | None = None,
    ) -> None:
        self.sort_direction = sort_direction
        self.sort_property = sort_property

    @property
    def sort_direction(self) -> str | None:
        """
        | The direction to sort the results. Possible values are:
        
        * ascending - Sort in ascending order.
        * descending - Sort in descending order.

        Type: str
        """
        return self.__sort_direction

    @sort_direction.setter
    def sort_direction(self, value: str | None) -> None:
        self.__sort_direction = value

    @property
    def sort_property(self) -> str | None:
        """
        | The property to sort the results by. Possible values are:
        
        * creationDate - Sort by the date the payment link was created.
        * expirationDate - Sort by the expiration date of the payment link.
        * merchantId - Sort by the merchant ID of the payment link.
        * status - Sort by the status of the payment link.

        Type: str
        """
        return self.__sort_property

    @sort_property.setter
    def sort_property(self, value: str | None) -> None:
        self.__sort_property = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.sort_direction is not None:
            dictionary['sortDirection'] = self.sort_direction
        if self.sort_property is not None:
            dictionary['sortProperty'] = self.sort_property
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentLinkOverviewSorting':
        super().from_dictionary(dictionary)
        if 'sortDirection' in dictionary:
            self.sort_direction = dictionary['sortDirection']
        if 'sortProperty' in dictionary:
            self.sort_property = dictionary['sortProperty']
        return self

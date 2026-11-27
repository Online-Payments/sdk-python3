#
# This file was automatically generated.
#
from .data_object import DataObject
from .surcharge import Surcharge


class CalculateSurchargeResponse(DataObject):

    __slots__ = (
        "__surcharges",
    )

    __surcharges: list[Surcharge] | None

    def __init__(
        self,
        *,
        surcharges: list[Surcharge] | None = None,
    ) -> None:
        self.surcharges = surcharges

    @property
    def surcharges(self) -> list[Surcharge] | None:
        """
        | List of surcharge calculations matching the bin and paymentProductId if supplied

        Type: list[:class:`onlinepayments.sdk.domain.surcharge.Surcharge`]
        """
        return self.__surcharges

    @surcharges.setter
    def surcharges(self, value: list[Surcharge] | None) -> None:
        self.__surcharges = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.surcharges is not None:
            dictionary['surcharges'] = []
            for element in self.surcharges:
                if element is not None:
                    dictionary['surcharges'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CalculateSurchargeResponse':
        super().from_dictionary(dictionary)
        if 'surcharges' in dictionary:
            if not isinstance(dictionary['surcharges'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['surcharges']))
            self.surcharges = []
            for element in dictionary['surcharges']:
                value = Surcharge()
                self.surcharges.append(value.from_dictionary(element))
        return self

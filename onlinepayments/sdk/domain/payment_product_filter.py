#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentProductFilter(DataObject):

    __slots__ = (
        "__groups",
        "__products",
    )

    __groups: list[str] | None
    __products: list[int] | None

    def __init__(
        self,
        *,
        groups: list[str] | None = None,
        products: list[int] | None = None,
    ) -> None:
        self.groups = groups
        self.products = products

    @property
    def groups(self) -> list[str] | None:
        """
        | List containing all payment product groups that should either be restricted to in or excluded from the payment context. Currently, there is only one group, called 'cards'.

        Type: list[str]
        """
        return self.__groups

    @groups.setter
    def groups(self, value: list[str] | None) -> None:
        self.__groups = value

    @property
    def products(self) -> list[int] | None:
        """
        | List containing all payment product ids that should either be restricted to in or excluded from the payment context.

        Type: list[int]
        """
        return self.__products

    @products.setter
    def products(self, value: list[int] | None) -> None:
        self.__products = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.groups is not None:
            dictionary['groups'] = []
            for element in self.groups:
                if element is not None:
                    dictionary['groups'].append(element)
        if self.products is not None:
            dictionary['products'] = []
            for element in self.products:
                if element is not None:
                    dictionary['products'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductFilter':
        super().from_dictionary(dictionary)
        if 'groups' in dictionary:
            if not isinstance(dictionary['groups'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['groups']))
            self.groups = []
            for element in dictionary['groups']:
                self.groups.append(element)
        if 'products' in dictionary:
            if not isinstance(dictionary['products'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['products']))
            self.products = []
            for element in dictionary['products']:
                self.products.append(element)
        return self

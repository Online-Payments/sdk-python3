#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentProductFilterHostedTokenization(DataObject):

    __slots__ = (
        "__products",
    )

    __products: list[int] | None

    def __init__(
        self,
        *,
        products: list[int] | None = None,
    ) -> None:
        self.products = products

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
        if self.products is not None:
            dictionary['products'] = []
            for element in self.products:
                if element is not None:
                    dictionary['products'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductFilterHostedTokenization':
        super().from_dictionary(dictionary)
        if 'products' in dictionary:
            if not isinstance(dictionary['products'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['products']))
            self.products = []
            for element in dictionary['products']:
                self.products.append(element)
        return self

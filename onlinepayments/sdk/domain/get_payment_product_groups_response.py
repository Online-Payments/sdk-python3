#
# This file was automatically generated.
#
from .data_object import DataObject
from .payment_product_group import PaymentProductGroup


class GetPaymentProductGroupsResponse(DataObject):

    __slots__ = (
        "__payment_product_groups",
    )

    __payment_product_groups: list[PaymentProductGroup] | None

    def __init__(
        self,
        *,
        payment_product_groups: list[PaymentProductGroup] | None = None,
    ) -> None:
        self.payment_product_groups = payment_product_groups

    @property
    def payment_product_groups(self) -> list[PaymentProductGroup] | None:
        """
        | Array containing payment product groups and their characteristics

        Type: list[:class:`onlinepayments.sdk.domain.payment_product_group.PaymentProductGroup`]
        """
        return self.__payment_product_groups

    @payment_product_groups.setter
    def payment_product_groups(self, value: list[PaymentProductGroup] | None) -> None:
        self.__payment_product_groups = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.payment_product_groups is not None:
            dictionary['paymentProductGroups'] = []
            for element in self.payment_product_groups:
                if element is not None:
                    dictionary['paymentProductGroups'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'GetPaymentProductGroupsResponse':
        super().from_dictionary(dictionary)
        if 'paymentProductGroups' in dictionary:
            if not isinstance(dictionary['paymentProductGroups'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['paymentProductGroups']))
            self.payment_product_groups = []
            for element in dictionary['paymentProductGroups']:
                value = PaymentProductGroup()
                self.payment_product_groups.append(value.from_dictionary(element))
        return self

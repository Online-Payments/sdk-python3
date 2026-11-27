#
# This file was automatically generated.
#
from .data_object import DataObject
from .payment_link_response import PaymentLinkResponse


class PaymentLinksResponse(DataObject):

    __slots__ = ("__payment_links",)

    __payment_links: list[PaymentLinkResponse] | None

    def __init__(self, *, payment_links: list[PaymentLinkResponse] | None = None) -> None:
        self.payment_links = payment_links

    @property
    def payment_links(self) -> list[PaymentLinkResponse] | None:
        """
        Type: list[:class:`onlinepayments.sdk.domain.payment_link_response.PaymentLinkResponse`]
        """
        return self.__payment_links

    @payment_links.setter
    def payment_links(self, value: list[PaymentLinkResponse] | None) -> None:
        self.__payment_links = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.payment_links is not None:
            dictionary['PaymentLinks'] = []
            for element in self.payment_links:
                if element is not None:
                    dictionary['PaymentLinks'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentLinksResponse':
        super().from_dictionary(dictionary)
        if 'PaymentLinks' in dictionary:
            if not isinstance(dictionary['PaymentLinks'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['PaymentLinks']))
            self.payment_links = []
            for element in dictionary['PaymentLinks']:
                value = PaymentLinkResponse()
                self.payment_links.append(value.from_dictionary(element))
        return self

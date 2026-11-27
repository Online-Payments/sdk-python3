#
# This file was automatically generated.
#
from .data_object import DataObject


class HostedCheckoutSpecificOutput(DataObject):

    __slots__ = (
        "__hosted_checkout_id",
        "__variant",
    )

    __hosted_checkout_id: str | None
    __variant: str | None

    def __init__(
        self,
        *,
        hosted_checkout_id: str | None = None,
        variant: str | None = None,
    ) -> None:
        self.hosted_checkout_id = hosted_checkout_id
        self.variant = variant

    @property
    def hosted_checkout_id(self) -> str | None:
        """
        | The ID of the Hosted Checkout Session in which the payment was made.

        Type: str
        """
        return self.__hosted_checkout_id

    @hosted_checkout_id.setter
    def hosted_checkout_id(self, value: str | None) -> None:
        self.__hosted_checkout_id = value

    @property
    def variant(self) -> str | None:
        """
        | You can force the use of a custom template by specifying it in the variant field. This allows you to test out the effect of certain changes to your payment pages in a controlled manner. Please note that you need to specify the filename of the template or customization.

        Type: str
        """
        return self.__variant

    @variant.setter
    def variant(self, value: str | None) -> None:
        self.__variant = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.hosted_checkout_id is not None:
            dictionary['hostedCheckoutId'] = self.hosted_checkout_id
        if self.variant is not None:
            dictionary['variant'] = self.variant
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'HostedCheckoutSpecificOutput':
        super().from_dictionary(dictionary)
        if 'hostedCheckoutId' in dictionary:
            self.hosted_checkout_id = dictionary['hostedCheckoutId']
        if 'variant' in dictionary:
            self.variant = dictionary['variant']
        return self

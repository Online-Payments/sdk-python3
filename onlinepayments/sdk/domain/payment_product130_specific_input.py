#
# This file was automatically generated.
#
from .data_object import DataObject
from .payment_product130_specific_three_d_secure import PaymentProduct130SpecificThreeDSecure


class PaymentProduct130SpecificInput(DataObject):

    __slots__ = (
        "__three_d_secure",
    )

    __three_d_secure: PaymentProduct130SpecificThreeDSecure | None

    def __init__(
        self,
        *,
        three_d_secure: PaymentProduct130SpecificThreeDSecure | None = None,
    ) -> None:
        self.three_d_secure = three_d_secure

    @property
    def three_d_secure(self) -> PaymentProduct130SpecificThreeDSecure | None:
        """
        | Object containing specific data regarding 3-D Secure

        Type: :class:`onlinepayments.sdk.domain.payment_product130_specific_three_d_secure.PaymentProduct130SpecificThreeDSecure`
        """
        return self.__three_d_secure

    @three_d_secure.setter
    def three_d_secure(self, value: PaymentProduct130SpecificThreeDSecure | None) -> None:
        self.__three_d_secure = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.three_d_secure is not None:
            dictionary['threeDSecure'] = self.three_d_secure.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct130SpecificInput':
        super().from_dictionary(dictionary)
        if 'threeDSecure' in dictionary:
            if not isinstance(dictionary['threeDSecure'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['threeDSecure']))
            value = PaymentProduct130SpecificThreeDSecure()
            self.three_d_secure = value.from_dictionary(dictionary['threeDSecure'])
        return self

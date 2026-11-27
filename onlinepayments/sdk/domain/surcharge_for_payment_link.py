#
# This file was automatically generated.
#
from .data_object import DataObject


class SurchargeForPaymentLink(DataObject):

    __slots__ = (
        "__surcharge_mode",
    )

    __surcharge_mode: str | None

    def __init__(
        self,
        *,
        surcharge_mode: str | None = None,
    ) -> None:
        self.surcharge_mode = surcharge_mode

    @property
    def surcharge_mode(self) -> str | None:
        """
        | The surcharge mode which defines how a merchant will apply surcharging.
        
        * pass-through - Merchant to define and apply surcharge amount for a transaction for processing. This mode is not supported on Create Hosted Checkout Session.
        * on-behalf-of - Merchant to instruct the payment platform to calculate and apply a surcharge amount to a transaction, based on the merchant’s surcharge configuration, net amount, and payment product type.

        Type: str
        """
        return self.__surcharge_mode

    @surcharge_mode.setter
    def surcharge_mode(self, value: str | None) -> None:
        self.__surcharge_mode = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.surcharge_mode is not None:
            dictionary['surchargeMode'] = self.surcharge_mode
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SurchargeForPaymentLink':
        super().from_dictionary(dictionary)
        if 'surchargeMode' in dictionary:
            self.surcharge_mode = dictionary['surchargeMode']
        return self

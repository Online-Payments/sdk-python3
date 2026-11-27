#
# This file was automatically generated.
#
from .data_object import DataObject


class ProtectionEligibility(DataObject):

    __slots__ = (
        "__eligibility",
        "__type",
    )

    __eligibility: str | None
    __type: str | None

    def __init__(
        self,
        *,
        eligibility: str | None = None,
        type: str | None = None,
    ) -> None:
        self.eligibility = eligibility
        self.type = type

    @property
    def eligibility(self) -> str | None:
        """
        * Eligible - Merchant is protected by PayPal's Seller Protection Policy for Unauthorized Payment and Item Not Received
        * PartiallyEligible - Merchant is protected by PayPal's Seller Protection Policy for Item Not Received
        * Ineligible — Merchant is not protected under the Seller Protection Policy

        Type: str
        """
        return self.__eligibility

    @eligibility.setter
    def eligibility(self, value: str | None) -> None:
        self.__eligibility = value

    @property
    def type(self) -> str | None:
        """
        * ItemNotReceivedEligible - Merchant is protected by PayPal's Seller Protection Policy for Item Not Received
        * UnauthorizedPaymentEligible - Merchant is protected by PayPal's Seller Protection Policy for Unauthorized Payment
        * Ineligible - Merchant is not protected under the Seller Protection Policy

        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value: str | None) -> None:
        self.__type = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.eligibility is not None:
            dictionary['eligibility'] = self.eligibility
        if self.type is not None:
            dictionary['type'] = self.type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ProtectionEligibility':
        super().from_dictionary(dictionary)
        if 'eligibility' in dictionary:
            self.eligibility = dictionary['eligibility']
        if 'type' in dictionary:
            self.type = dictionary['type']
        return self

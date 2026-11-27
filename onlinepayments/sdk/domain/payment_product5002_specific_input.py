#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentProduct5002SpecificInput(DataObject):

    __slots__ = (
        "__checkout_response_signature",
        "__credit_card_brand",
    )

    __checkout_response_signature: str | None
    __credit_card_brand: str | None

    def __init__(
        self,
        *,
        checkout_response_signature: str | None = None,
        credit_card_brand: str | None = None,
    ) -> None:
        self.checkout_response_signature = checkout_response_signature
        self.credit_card_brand = credit_card_brand

    @property
    def checkout_response_signature(self) -> str | None:
        """
        Type: str
        """
        return self.__checkout_response_signature

    @checkout_response_signature.setter
    def checkout_response_signature(self, value: str | None) -> None:
        self.__checkout_response_signature = value

    @property
    def credit_card_brand(self) -> str | None:
        """
        Type: str
        """
        return self.__credit_card_brand

    @credit_card_brand.setter
    def credit_card_brand(self, value: str | None) -> None:
        self.__credit_card_brand = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.checkout_response_signature is not None:
            dictionary['checkoutResponseSignature'] = self.checkout_response_signature
        if self.credit_card_brand is not None:
            dictionary['creditCardBrand'] = self.credit_card_brand
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct5002SpecificInput':
        super().from_dictionary(dictionary)
        if 'checkoutResponseSignature' in dictionary:
            self.checkout_response_signature = dictionary['checkoutResponseSignature']
        if 'creditCardBrand' in dictionary:
            self.credit_card_brand = dictionary['creditCardBrand']
        return self

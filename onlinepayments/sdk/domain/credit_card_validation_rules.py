#
# This file was automatically generated.
#
from .data_object import DataObject


class CreditCardValidationRules(DataObject):

    __slots__ = (
        "__cvv_mandatory_for_existing_token",
        "__cvv_mandatory_for_new_token",
    )

    __cvv_mandatory_for_existing_token: bool | None
    __cvv_mandatory_for_new_token: bool | None

    def __init__(
        self,
        *,
        cvv_mandatory_for_existing_token: bool | None = None,
        cvv_mandatory_for_new_token: bool | None = None,
    ) -> None:
        self.cvv_mandatory_for_existing_token = cvv_mandatory_for_existing_token
        self.cvv_mandatory_for_new_token = cvv_mandatory_for_new_token

    @property
    def cvv_mandatory_for_existing_token(self) -> bool | None:
        """
        | Determines whether the Card Verification Value must be provided for existing tokens. This option overrides the payment method configuration for the session.

        Type: bool
        """
        return self.__cvv_mandatory_for_existing_token

    @cvv_mandatory_for_existing_token.setter
    def cvv_mandatory_for_existing_token(self, value: bool | None) -> None:
        self.__cvv_mandatory_for_existing_token = value

    @property
    def cvv_mandatory_for_new_token(self) -> bool | None:
        """
        | Determines whether the Card Verification Value must be provided for new tokens. This option overrides the payment method configuration for the session.

        Type: bool
        """
        return self.__cvv_mandatory_for_new_token

    @cvv_mandatory_for_new_token.setter
    def cvv_mandatory_for_new_token(self, value: bool | None) -> None:
        self.__cvv_mandatory_for_new_token = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.cvv_mandatory_for_existing_token is not None:
            dictionary['cvvMandatoryForExistingToken'] = self.cvv_mandatory_for_existing_token
        if self.cvv_mandatory_for_new_token is not None:
            dictionary['cvvMandatoryForNewToken'] = self.cvv_mandatory_for_new_token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreditCardValidationRules':
        super().from_dictionary(dictionary)
        if 'cvvMandatoryForExistingToken' in dictionary:
            self.cvv_mandatory_for_existing_token = dictionary['cvvMandatoryForExistingToken']
        if 'cvvMandatoryForNewToken' in dictionary:
            self.cvv_mandatory_for_new_token = dictionary['cvvMandatoryForNewToken']
        return self

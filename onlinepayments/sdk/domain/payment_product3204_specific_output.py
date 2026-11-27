#
# This file was automatically generated.
#
from .data_object import DataObject


class PaymentProduct3204SpecificOutput(DataObject):

    __slots__ = (
        "__banking_app_label",
    )

    __banking_app_label: str | None

    def __init__(
        self,
        *,
        banking_app_label: str | None = None,
    ) -> None:
        self.banking_app_label = banking_app_label

    @property
    def banking_app_label(self) -> str | None:
        """
        | The name given by the bank (the publisher of the mobile application) to identify the mobile account where the User will confirm the payment

        Type: str
        """
        return self.__banking_app_label

    @banking_app_label.setter
    def banking_app_label(self, value: str | None) -> None:
        self.__banking_app_label = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.banking_app_label is not None:
            dictionary['bankingAppLabel'] = self.banking_app_label
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct3204SpecificOutput':
        super().from_dictionary(dictionary)
        if 'bankingAppLabel' in dictionary:
            self.banking_app_label = dictionary['bankingAppLabel']
        return self

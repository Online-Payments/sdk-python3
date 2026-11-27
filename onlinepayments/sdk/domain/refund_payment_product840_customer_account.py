#
# This file was automatically generated.
#
from .data_object import DataObject


class RefundPaymentProduct840CustomerAccount(DataObject):

    __slots__ = (
        "__customer_account_status",
        "__customer_address_status",
        "__payer_id",
    )

    __customer_account_status: str | None
    __customer_address_status: str | None
    __payer_id: str | None

    def __init__(
        self,
        *,
        customer_account_status: str | None = None,
        customer_address_status: str | None = None,
        payer_id: str | None = None,
    ) -> None:
        self.customer_account_status = customer_account_status
        self.customer_address_status = customer_address_status
        self.payer_id = payer_id

    @property
    def customer_account_status(self) -> str | None:
        """
        Type: str
        """
        return self.__customer_account_status

    @customer_account_status.setter
    def customer_account_status(self, value: str | None) -> None:
        self.__customer_account_status = value

    @property
    def customer_address_status(self) -> str | None:
        """
        Type: str
        """
        return self.__customer_address_status

    @customer_address_status.setter
    def customer_address_status(self, value: str | None) -> None:
        self.__customer_address_status = value

    @property
    def payer_id(self) -> str | None:
        """
        | The unique identifier of a PayPal account and will never change in the life cycle of a PayPal account

        Type: str
        """
        return self.__payer_id

    @payer_id.setter
    def payer_id(self, value: str | None) -> None:
        self.__payer_id = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.customer_account_status is not None:
            dictionary['customerAccountStatus'] = self.customer_account_status
        if self.customer_address_status is not None:
            dictionary['customerAddressStatus'] = self.customer_address_status
        if self.payer_id is not None:
            dictionary['payerId'] = self.payer_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RefundPaymentProduct840CustomerAccount':
        super().from_dictionary(dictionary)
        if 'customerAccountStatus' in dictionary:
            self.customer_account_status = dictionary['customerAccountStatus']
        if 'customerAddressStatus' in dictionary:
            self.customer_address_status = dictionary['customerAddressStatus']
        if 'payerId' in dictionary:
            self.payer_id = dictionary['payerId']
        return self

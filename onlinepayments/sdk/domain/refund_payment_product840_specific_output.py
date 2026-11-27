#
# This file was automatically generated.
#
from .data_object import DataObject
from .refund_payment_product840_customer_account import RefundPaymentProduct840CustomerAccount


class RefundPaymentProduct840SpecificOutput(DataObject):

    __slots__ = (
        "__customer_account",
    )

    __customer_account: RefundPaymentProduct840CustomerAccount | None

    def __init__(
        self,
        *,
        customer_account: RefundPaymentProduct840CustomerAccount | None = None,
    ) -> None:
        self.customer_account = customer_account

    @property
    def customer_account(self) -> RefundPaymentProduct840CustomerAccount | None:
        """
        Type: :class:`onlinepayments.sdk.domain.refund_payment_product840_customer_account.RefundPaymentProduct840CustomerAccount`
        """
        return self.__customer_account

    @customer_account.setter
    def customer_account(self, value: RefundPaymentProduct840CustomerAccount | None) -> None:
        self.__customer_account = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.customer_account is not None:
            dictionary['customerAccount'] = self.customer_account.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RefundPaymentProduct840SpecificOutput':
        super().from_dictionary(dictionary)
        if 'customerAccount' in dictionary:
            if not isinstance(dictionary['customerAccount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerAccount']))
            value = RefundPaymentProduct840CustomerAccount()
            self.customer_account = value.from_dictionary(dictionary['customerAccount'])
        return self

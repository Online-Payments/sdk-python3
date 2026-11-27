#
# This file was automatically generated.
#
from .customer_bank_account import CustomerBankAccount
from .data_object import DataObject


class RedirectPaymentProduct5408SpecificInput(DataObject):

    __slots__ = (
        "__customer_bank_account",
        "__instant_payment_only",
    )

    __customer_bank_account: CustomerBankAccount | None
    __instant_payment_only: bool | None

    def __init__(
        self,
        *,
        customer_bank_account: CustomerBankAccount | None = None,
        instant_payment_only: bool | None = None,
    ) -> None:
        self.customer_bank_account = customer_bank_account
        self.instant_payment_only = instant_payment_only

    @property
    def customer_bank_account(self) -> CustomerBankAccount | None:
        """
        | Data of customer bank account

        Type: :class:`onlinepayments.sdk.domain.customer_bank_account.CustomerBankAccount`
        """
        return self.__customer_bank_account

    @customer_bank_account.setter
    def customer_bank_account(self, value: CustomerBankAccount | None) -> None:
        self.__customer_bank_account = value

    @property
    def instant_payment_only(self) -> bool | None:
        """
        * true - consumer can only use instant payment for Account to Account Bank transfer payments
        * false - consumer can only use standard payment for Account to Account Bank transfer payments

        Type: bool
        """
        return self.__instant_payment_only

    @instant_payment_only.setter
    def instant_payment_only(self, value: bool | None) -> None:
        self.__instant_payment_only = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.customer_bank_account is not None:
            dictionary['customerBankAccount'] = self.customer_bank_account.to_dictionary()
        if self.instant_payment_only is not None:
            dictionary['instantPaymentOnly'] = self.instant_payment_only
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentProduct5408SpecificInput':
        super().from_dictionary(dictionary)
        if 'customerBankAccount' in dictionary:
            if not isinstance(dictionary['customerBankAccount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerBankAccount']))
            value = CustomerBankAccount()
            self.customer_bank_account = value.from_dictionary(dictionary['customerBankAccount'])
        if 'instantPaymentOnly' in dictionary:
            self.instant_payment_only = dictionary['instantPaymentOnly']
        return self

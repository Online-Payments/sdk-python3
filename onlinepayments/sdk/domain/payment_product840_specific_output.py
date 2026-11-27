#
# This file was automatically generated.
#
from .address import Address
from .address_personal import AddressPersonal
from .data_object import DataObject
from .payment_product840_customer_account import PaymentProduct840CustomerAccount
from .protection_eligibility import ProtectionEligibility


class PaymentProduct840SpecificOutput(DataObject):

    __slots__ = (
        "__billing_address",
        "__billing_personal_address",
        "__customer_account",
        "__customer_address",
        "__pay_pal_transaction_id",
        "__protection_eligibility",
        "__shipping_address",
    )

    __billing_address: Address | None
    __billing_personal_address: AddressPersonal | None
    __customer_account: PaymentProduct840CustomerAccount | None
    __customer_address: Address | None
    __pay_pal_transaction_id: str | None
    __protection_eligibility: ProtectionEligibility | None
    __shipping_address: AddressPersonal | None

    def __init__(
        self,
        *,
        billing_address: Address | None = None,
        billing_personal_address: AddressPersonal | None = None,
        customer_account: PaymentProduct840CustomerAccount | None = None,
        customer_address: Address | None = None,
        pay_pal_transaction_id: str | None = None,
        protection_eligibility: ProtectionEligibility | None = None,
        shipping_address: AddressPersonal | None = None,
    ) -> None:
        self.billing_address = billing_address
        self.billing_personal_address = billing_personal_address
        self.customer_account = customer_account
        self.customer_address = customer_address
        self.pay_pal_transaction_id = pay_pal_transaction_id
        self.protection_eligibility = protection_eligibility
        self.shipping_address = shipping_address

    @property
    def billing_address(self) -> Address | None:
        """
        | Deprecated - Use billingPersonalAddress instead

        Type: :class:`onlinepayments.sdk.domain.address.Address`
        """
        return self.__billing_address

    @billing_address.setter
    def billing_address(self, value: Address | None) -> None:
        self.__billing_address = value

    @property
    def billing_personal_address(self) -> AddressPersonal | None:
        """
        | Object containing address information

        Type: :class:`onlinepayments.sdk.domain.address_personal.AddressPersonal`
        """
        return self.__billing_personal_address

    @billing_personal_address.setter
    def billing_personal_address(self, value: AddressPersonal | None) -> None:
        self.__billing_personal_address = value

    @property
    def customer_account(self) -> PaymentProduct840CustomerAccount | None:
        """
        | Object containing the details of the PayPal account

        Type: :class:`onlinepayments.sdk.domain.payment_product840_customer_account.PaymentProduct840CustomerAccount`
        """
        return self.__customer_account

    @customer_account.setter
    def customer_account(self, value: PaymentProduct840CustomerAccount | None) -> None:
        self.__customer_account = value

    @property
    def customer_address(self) -> Address | None:
        """
        | Deprecated - Use shippingAddress instead

        Type: :class:`onlinepayments.sdk.domain.address.Address`
        """
        return self.__customer_address

    @customer_address.setter
    def customer_address(self, value: Address | None) -> None:
        self.__customer_address = value

    @property
    def pay_pal_transaction_id(self) -> str | None:
        """
        | Id of a transaction given by PayPal

        Type: str
        """
        return self.__pay_pal_transaction_id

    @pay_pal_transaction_id.setter
    def pay_pal_transaction_id(self, value: str | None) -> None:
        self.__pay_pal_transaction_id = value

    @property
    def protection_eligibility(self) -> ProtectionEligibility | None:
        """
        | Kind of seller protection in force for the PayPal transaction

        Type: :class:`onlinepayments.sdk.domain.protection_eligibility.ProtectionEligibility`
        """
        return self.__protection_eligibility

    @protection_eligibility.setter
    def protection_eligibility(self, value: ProtectionEligibility | None) -> None:
        self.__protection_eligibility = value

    @property
    def shipping_address(self) -> AddressPersonal | None:
        """
        | Object containing address information

        Type: :class:`onlinepayments.sdk.domain.address_personal.AddressPersonal`
        """
        return self.__shipping_address

    @shipping_address.setter
    def shipping_address(self, value: AddressPersonal | None) -> None:
        self.__shipping_address = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.billing_address is not None:
            dictionary['billingAddress'] = self.billing_address.to_dictionary()
        if self.billing_personal_address is not None:
            dictionary['billingPersonalAddress'] = self.billing_personal_address.to_dictionary()
        if self.customer_account is not None:
            dictionary['customerAccount'] = self.customer_account.to_dictionary()
        if self.customer_address is not None:
            dictionary['customerAddress'] = self.customer_address.to_dictionary()
        if self.pay_pal_transaction_id is not None:
            dictionary['payPalTransactionId'] = self.pay_pal_transaction_id
        if self.protection_eligibility is not None:
            dictionary['protectionEligibility'] = self.protection_eligibility.to_dictionary()
        if self.shipping_address is not None:
            dictionary['shippingAddress'] = self.shipping_address.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProduct840SpecificOutput':
        super().from_dictionary(dictionary)
        if 'billingAddress' in dictionary:
            if not isinstance(dictionary['billingAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['billingAddress']))
            value = Address()
            self.billing_address = value.from_dictionary(dictionary['billingAddress'])
        if 'billingPersonalAddress' in dictionary:
            if not isinstance(dictionary['billingPersonalAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['billingPersonalAddress']))
            value = AddressPersonal()
            self.billing_personal_address = value.from_dictionary(dictionary['billingPersonalAddress'])
        if 'customerAccount' in dictionary:
            if not isinstance(dictionary['customerAccount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerAccount']))
            value = PaymentProduct840CustomerAccount()
            self.customer_account = value.from_dictionary(dictionary['customerAccount'])
        if 'customerAddress' in dictionary:
            if not isinstance(dictionary['customerAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerAddress']))
            value = Address()
            self.customer_address = value.from_dictionary(dictionary['customerAddress'])
        if 'payPalTransactionId' in dictionary:
            self.pay_pal_transaction_id = dictionary['payPalTransactionId']
        if 'protectionEligibility' in dictionary:
            if not isinstance(dictionary['protectionEligibility'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['protectionEligibility']))
            value = ProtectionEligibility()
            self.protection_eligibility = value.from_dictionary(dictionary['protectionEligibility'])
        if 'shippingAddress' in dictionary:
            if not isinstance(dictionary['shippingAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['shippingAddress']))
            value = AddressPersonal()
            self.shipping_address = value.from_dictionary(dictionary['shippingAddress'])
        return self

#
# This file was automatically generated.
#
from .amount_of_money import AmountOfMoney
from .data_object import DataObject
from .surcharge_for_payment_link import SurchargeForPaymentLink


class PaymentLinkOrderOutput(DataObject):

    __slots__ = (
        "__amount",
        "__merchant_reference",
        "__surcharge_specific_output",
    )

    __amount: AmountOfMoney | None
    __merchant_reference: str | None
    __surcharge_specific_output: SurchargeForPaymentLink | None

    def __init__(
        self,
        *,
        amount: AmountOfMoney | None = None,
        merchant_reference: str | None = None,
        surcharge_specific_output: SurchargeForPaymentLink | None = None,
    ) -> None:
        self.amount = amount
        self.merchant_reference = merchant_reference
        self.surcharge_specific_output = surcharge_specific_output

    @property
    def amount(self) -> AmountOfMoney | None:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount

    @amount.setter
    def amount(self, value: AmountOfMoney | None) -> None:
        self.__amount = value

    @property
    def merchant_reference(self) -> str | None:
        """
        | Your unique reference of the transaction that is also returned in our report files. This is almost always used for your reconciliation of our report files. It is highly recommended to provide a single MerchantReference per unique order on your side

        Type: str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value: str | None) -> None:
        self.__merchant_reference = value

    @property
    def surcharge_specific_output(self) -> SurchargeForPaymentLink | None:
        """
        | Object containing details how surcharge will be applied to a payment link.

        Type: :class:`onlinepayments.sdk.domain.surcharge_for_payment_link.SurchargeForPaymentLink`
        """
        return self.__surcharge_specific_output

    @surcharge_specific_output.setter
    def surcharge_specific_output(self, value: SurchargeForPaymentLink | None) -> None:
        self.__surcharge_specific_output = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.amount is not None:
            dictionary['amount'] = self.amount.to_dictionary()
        if self.merchant_reference is not None:
            dictionary['merchantReference'] = self.merchant_reference
        if self.surcharge_specific_output is not None:
            dictionary['surchargeSpecificOutput'] = self.surcharge_specific_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentLinkOrderOutput':
        super().from_dictionary(dictionary)
        if 'amount' in dictionary:
            if not isinstance(dictionary['amount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amount']))
            value = AmountOfMoney()
            self.amount = value.from_dictionary(dictionary['amount'])
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        if 'surchargeSpecificOutput' in dictionary:
            if not isinstance(dictionary['surchargeSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['surchargeSpecificOutput']))
            value = SurchargeForPaymentLink()
            self.surcharge_specific_output = value.from_dictionary(dictionary['surchargeSpecificOutput'])
        return self

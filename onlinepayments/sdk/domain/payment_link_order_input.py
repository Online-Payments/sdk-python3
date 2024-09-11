# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.surcharge_for_payment_link import SurchargeForPaymentLink


class PaymentLinkOrderInput(DataObject):
    """
    | An object containing the details of the related payment input.
    
    | Deprecated: All properties in `paymentLinkOrder` are deprecated.  
    | Use corresponding values as noted below:  
    | | Property | Replacement |
    | | - | - |
    | | merchantReference | `order/references/merchantReference` |  
    | | amount | `order/amountOfMoney` |  
    | | surchargeSpecificInput | `order/surchargeSpecificInput` |
    """

    __amount = None
    __merchant_reference = None
    __surcharge_specific_input = None

    @property
    def amount(self) -> AmountOfMoney:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount

    @amount.setter
    def amount(self, value: AmountOfMoney):
        self.__amount = value

    @property
    def merchant_reference(self) -> str:
        """
        | Your unique reference of the transaction that is also returned in our report files. This is almost always used for your reconciliation of our report files.
        | It is highly recommended to provide a single MerchantReference per unique order on your side

        Type: str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value: str):
        self.__merchant_reference = value

    @property
    def surcharge_specific_input(self) -> SurchargeForPaymentLink:
        """
        | Object containing details how surcharge will be applied to a payment link.

        Type: :class:`onlinepayments.sdk.domain.surcharge_for_payment_link.SurchargeForPaymentLink`
        """
        return self.__surcharge_specific_input

    @surcharge_specific_input.setter
    def surcharge_specific_input(self, value: SurchargeForPaymentLink):
        self.__surcharge_specific_input = value

    def to_dictionary(self):
        dictionary = super(PaymentLinkOrderInput, self).to_dictionary()
        if self.amount is not None:
            dictionary['amount'] = self.amount.to_dictionary()
        if self.merchant_reference is not None:
            dictionary['merchantReference'] = self.merchant_reference
        if self.surcharge_specific_input is not None:
            dictionary['surchargeSpecificInput'] = self.surcharge_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentLinkOrderInput, self).from_dictionary(dictionary)
        if 'amount' in dictionary:
            if not isinstance(dictionary['amount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amount']))
            value = AmountOfMoney()
            self.amount = value.from_dictionary(dictionary['amount'])
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        if 'surchargeSpecificInput' in dictionary:
            if not isinstance(dictionary['surchargeSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['surchargeSpecificInput']))
            value = SurchargeForPaymentLink()
            self.surcharge_specific_input = value.from_dictionary(dictionary['surchargeSpecificInput'])
        return self

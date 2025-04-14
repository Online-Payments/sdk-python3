# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .amount_of_money import AmountOfMoney
from .card_payout_method_specific_input import CardPayoutMethodSpecificInput
from .data_object import DataObject
from .feedbacks import Feedbacks
from .omnichannel_payout_specific_input import OmnichannelPayoutSpecificInput
from .payment_references import PaymentReferences


class CreatePayoutRequest(DataObject):

    __amount_of_money: Optional[AmountOfMoney] = None
    __card_payout_method_specific_input: Optional[CardPayoutMethodSpecificInput] = None
    __descriptor: Optional[str] = None
    __feedbacks: Optional[Feedbacks] = None
    __omnichannel_payout_specific_input: Optional[OmnichannelPayoutSpecificInput] = None
    __references: Optional[PaymentReferences] = None

    @property
    def amount_of_money(self) -> Optional[AmountOfMoney]:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value: Optional[AmountOfMoney]) -> None:
        self.__amount_of_money = value

    @property
    def card_payout_method_specific_input(self) -> Optional[CardPayoutMethodSpecificInput]:
        """
        | Object containing the payout details for a card

        Type: :class:`onlinepayments.sdk.domain.card_payout_method_specific_input.CardPayoutMethodSpecificInput`
        """
        return self.__card_payout_method_specific_input

    @card_payout_method_specific_input.setter
    def card_payout_method_specific_input(self, value: Optional[CardPayoutMethodSpecificInput]) -> None:
        self.__card_payout_method_specific_input = value

    @property
    def descriptor(self) -> Optional[str]:
        """
        | Descriptive text that is used towards to customer, either during an online checkout at a third party and/or on the statement of the customer. For card transactions this is usually referred to as a Soft Descriptor. The maximum allowed length varies per card acquirer:
        
        * AIB - 22 characters
        * American Express - 25 characters
        * Atos Origin BNP - 15 characters
        * Barclays - 25 characters
        * Catella - 22 characters
        * CBA - 20 characters
        * Elavon - 25 characters
        * First Data - 25 characters
        * INICIS (INIPAY) - 22-30 characters
        * JCB - 25 characters
        * Merchant Solutions - 22-25 characters
        * Payvision (EU & HK) - 25 characters
        * SEB Euroline - 22 characters
        * Sub1 Argentina - 15 characters
        * Wells Fargo - 25 characters Note that we advise you to use 22 characters as the max length as beyond this our experience is that issuers will start to truncate. We currently also only allow per API call overrides for AIB and Barclays For alternative payment products the maximum allowed length varies per payment product:
        * 402 e-Przelewy - 30 characters
        * 404 INICIS - 80 characters
        * 802 Nordea ePayment Finland - 234 characters
        * 809 iDeal - 32 characters
        * 836 SOFORT - 42 characters
        * 840 PayPal - 127 characters
        * 841 WebMoney - 175 characters
        * 849 Yandex - 64 characters
        * 861 Alipay - 256 characters
        * 863 WeChat Pay - 32 characters
        * 880 BOKU - 20 characters
        * 8580 Qiwi - 255 characters
        * 1504 Konbini - 80 characters All other payment products do not support a descriptor.

        Type: str
        """
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, value: Optional[str]) -> None:
        self.__descriptor = value

    @property
    def feedbacks(self) -> Optional[Feedbacks]:
        """
        | This section will contain feedback Urls to provide feedback on the payment.

        Type: :class:`onlinepayments.sdk.domain.feedbacks.Feedbacks`
        """
        return self.__feedbacks

    @feedbacks.setter
    def feedbacks(self, value: Optional[Feedbacks]) -> None:
        self.__feedbacks = value

    @property
    def omnichannel_payout_specific_input(self) -> Optional[OmnichannelPayoutSpecificInput]:
        """
        | Object containing the additional payout details for a Omnichannel merchants

        Type: :class:`onlinepayments.sdk.domain.omnichannel_payout_specific_input.OmnichannelPayoutSpecificInput`
        """
        return self.__omnichannel_payout_specific_input

    @omnichannel_payout_specific_input.setter
    def omnichannel_payout_specific_input(self, value: Optional[OmnichannelPayoutSpecificInput]) -> None:
        self.__omnichannel_payout_specific_input = value

    @property
    def references(self) -> Optional[PaymentReferences]:
        """
        | Object that holds all reference properties that are linked to this transaction. **Deprecated for capture/refund**: Use operationReferences instead.

        Type: :class:`onlinepayments.sdk.domain.payment_references.PaymentReferences`
        """
        return self.__references

    @references.setter
    def references(self, value: Optional[PaymentReferences]) -> None:
        self.__references = value

    def to_dictionary(self) -> dict:
        dictionary = super(CreatePayoutRequest, self).to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.card_payout_method_specific_input is not None:
            dictionary['cardPayoutMethodSpecificInput'] = self.card_payout_method_specific_input.to_dictionary()
        if self.descriptor is not None:
            dictionary['descriptor'] = self.descriptor
        if self.feedbacks is not None:
            dictionary['feedbacks'] = self.feedbacks.to_dictionary()
        if self.omnichannel_payout_specific_input is not None:
            dictionary['omnichannelPayoutSpecificInput'] = self.omnichannel_payout_specific_input.to_dictionary()
        if self.references is not None:
            dictionary['references'] = self.references.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreatePayoutRequest':
        super(CreatePayoutRequest, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'cardPayoutMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cardPayoutMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPayoutMethodSpecificInput']))
            value = CardPayoutMethodSpecificInput()
            self.card_payout_method_specific_input = value.from_dictionary(dictionary['cardPayoutMethodSpecificInput'])
        if 'descriptor' in dictionary:
            self.descriptor = dictionary['descriptor']
        if 'feedbacks' in dictionary:
            if not isinstance(dictionary['feedbacks'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['feedbacks']))
            value = Feedbacks()
            self.feedbacks = value.from_dictionary(dictionary['feedbacks'])
        if 'omnichannelPayoutSpecificInput' in dictionary:
            if not isinstance(dictionary['omnichannelPayoutSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['omnichannelPayoutSpecificInput']))
            value = OmnichannelPayoutSpecificInput()
            self.omnichannel_payout_specific_input = value.from_dictionary(dictionary['omnichannelPayoutSpecificInput'])
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = PaymentReferences()
            self.references = value.from_dictionary(dictionary['references'])
        return self

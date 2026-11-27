#
# This file was automatically generated.
#
from .amount_of_money import AmountOfMoney
from .card_payout_method_specific_input import CardPayoutMethodSpecificInput
from .data_object import DataObject
from .feedbacks import Feedbacks
from .omnichannel_payout_specific_input import OmnichannelPayoutSpecificInput
from .payment_references import PaymentReferences


class CreatePayoutRequest(DataObject):

    __slots__ = (
        "__amount_of_money",
        "__card_payout_method_specific_input",
        "__descriptor",
        "__feedbacks",
        "__omnichannel_payout_specific_input",
        "__references",
    )

    __amount_of_money: AmountOfMoney | None
    __card_payout_method_specific_input: CardPayoutMethodSpecificInput | None
    __descriptor: str | None
    __feedbacks: Feedbacks | None
    __omnichannel_payout_specific_input: OmnichannelPayoutSpecificInput | None
    __references: PaymentReferences | None

    def __init__(
        self,
        *,
        amount_of_money: AmountOfMoney | None = None,
        card_payout_method_specific_input: CardPayoutMethodSpecificInput | None = None,
        descriptor: str | None = None,
        feedbacks: Feedbacks | None = None,
        omnichannel_payout_specific_input: OmnichannelPayoutSpecificInput | None = None,
        references: PaymentReferences | None = None,
    ) -> None:
        self.amount_of_money = amount_of_money
        self.card_payout_method_specific_input = card_payout_method_specific_input
        self.descriptor = descriptor
        self.feedbacks = feedbacks
        self.omnichannel_payout_specific_input = omnichannel_payout_specific_input
        self.references = references

    @property
    def amount_of_money(self) -> AmountOfMoney | None:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value: AmountOfMoney | None) -> None:
        self.__amount_of_money = value

    @property
    def card_payout_method_specific_input(self) -> CardPayoutMethodSpecificInput | None:
        """
        | Object containing the payout details for a card

        Type: :class:`onlinepayments.sdk.domain.card_payout_method_specific_input.CardPayoutMethodSpecificInput`
        """
        return self.__card_payout_method_specific_input

    @card_payout_method_specific_input.setter
    def card_payout_method_specific_input(self, value: CardPayoutMethodSpecificInput | None) -> None:
        self.__card_payout_method_specific_input = value

    @property
    def descriptor(self) -> str | None:
        """
        | **Deprecated**: It is recommended to use the new merchantReconciliationReference for the same usage, and the new softDescriptor on top only in case you start needing another specific value to be pushed to the cardholder statement.

        Type: str
        """
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, value: str | None) -> None:
        self.__descriptor = value

    @property
    def feedbacks(self) -> Feedbacks | None:
        """
        | This section will contain feedback Urls to provide feedback on the payment.

        Type: :class:`onlinepayments.sdk.domain.feedbacks.Feedbacks`
        """
        return self.__feedbacks

    @feedbacks.setter
    def feedbacks(self, value: Feedbacks | None) -> None:
        self.__feedbacks = value

    @property
    def omnichannel_payout_specific_input(self) -> OmnichannelPayoutSpecificInput | None:
        """
        | Object containing the additional payout details for an Omnichannel merchant

        Type: :class:`onlinepayments.sdk.domain.omnichannel_payout_specific_input.OmnichannelPayoutSpecificInput`
        """
        return self.__omnichannel_payout_specific_input

    @omnichannel_payout_specific_input.setter
    def omnichannel_payout_specific_input(self, value: OmnichannelPayoutSpecificInput | None) -> None:
        self.__omnichannel_payout_specific_input = value

    @property
    def references(self) -> PaymentReferences | None:
        """
        | Object that holds all reference properties that are linked to this transaction. **Deprecated for capture/refund**: Use operationReferences instead.

        Type: :class:`onlinepayments.sdk.domain.payment_references.PaymentReferences`
        """
        return self.__references

    @references.setter
    def references(self, value: PaymentReferences | None) -> None:
        self.__references = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
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
        super().from_dictionary(dictionary)
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

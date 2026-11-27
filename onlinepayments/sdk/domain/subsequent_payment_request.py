#
# This file was automatically generated.
#
from .data_object import DataObject
from .omnichannel_subsequent_specific_input import OmnichannelSubsequentSpecificInput
from .order import Order
from .subsequent_card_payment_method_specific_input import SubsequentCardPaymentMethodSpecificInput
from .subsequent_payment_product5001_specific_input import SubsequentPaymentProduct5001SpecificInput


class SubsequentPaymentRequest(DataObject):

    __slots__ = (
        "__omnichannel_subsequent_specific_input",
        "__order",
        "__subsequent_payment_product5001_specific_input",
        "__subsequentcard_payment_method_specific_input",
    )

    __omnichannel_subsequent_specific_input: OmnichannelSubsequentSpecificInput | None
    __order: Order | None
    __subsequent_payment_product5001_specific_input: SubsequentPaymentProduct5001SpecificInput | None
    __subsequentcard_payment_method_specific_input: SubsequentCardPaymentMethodSpecificInput | None

    def __init__(
        self,
        *,
        omnichannel_subsequent_specific_input: OmnichannelSubsequentSpecificInput | None = None,
        order: Order | None = None,
        subsequent_payment_product5001_specific_input: SubsequentPaymentProduct5001SpecificInput | None = None,
        subsequentcard_payment_method_specific_input: SubsequentCardPaymentMethodSpecificInput | None = None,
    ) -> None:
        self.omnichannel_subsequent_specific_input = omnichannel_subsequent_specific_input
        self.order = order
        self.subsequent_payment_product5001_specific_input = subsequent_payment_product5001_specific_input
        self.subsequentcard_payment_method_specific_input = subsequentcard_payment_method_specific_input

    @property
    def omnichannel_subsequent_specific_input(self) -> OmnichannelSubsequentSpecificInput | None:
        """
        | This object contains additional subsequent details for omnichannel merchants.

        Type: :class:`onlinepayments.sdk.domain.omnichannel_subsequent_specific_input.OmnichannelSubsequentSpecificInput`
        """
        return self.__omnichannel_subsequent_specific_input

    @omnichannel_subsequent_specific_input.setter
    def omnichannel_subsequent_specific_input(self, value: OmnichannelSubsequentSpecificInput | None) -> None:
        self.__omnichannel_subsequent_specific_input = value

    @property
    def order(self) -> Order | None:
        """
        | The order object contains order-related data; Please note that this object is required to submit the amount.

        Type: :class:`onlinepayments.sdk.domain.order.Order`
        """
        return self.__order

    @order.setter
    def order(self, value: Order | None) -> None:
        self.__order = value

    @property
    def subsequent_payment_product5001_specific_input(self) -> SubsequentPaymentProduct5001SpecificInput | None:
        """
        | Specific data is required for Bizum subsequent payment.

        Type: :class:`onlinepayments.sdk.domain.subsequent_payment_product5001_specific_input.SubsequentPaymentProduct5001SpecificInput`
        """
        return self.__subsequent_payment_product5001_specific_input

    @subsequent_payment_product5001_specific_input.setter
    def subsequent_payment_product5001_specific_input(self, value: SubsequentPaymentProduct5001SpecificInput | None) -> None:
        self.__subsequent_payment_product5001_specific_input = value

    @property
    def subsequentcard_payment_method_specific_input(self) -> SubsequentCardPaymentMethodSpecificInput | None:
        """
        | Object containing the specific input details for subsequent card payments

        Type: :class:`onlinepayments.sdk.domain.subsequent_card_payment_method_specific_input.SubsequentCardPaymentMethodSpecificInput`
        """
        return self.__subsequentcard_payment_method_specific_input

    @subsequentcard_payment_method_specific_input.setter
    def subsequentcard_payment_method_specific_input(self, value: SubsequentCardPaymentMethodSpecificInput | None) -> None:
        self.__subsequentcard_payment_method_specific_input = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.omnichannel_subsequent_specific_input is not None:
            dictionary['omnichannelSubsequentSpecificInput'] = self.omnichannel_subsequent_specific_input.to_dictionary()
        if self.order is not None:
            dictionary['order'] = self.order.to_dictionary()
        if self.subsequent_payment_product5001_specific_input is not None:
            dictionary['subsequentPaymentProduct5001SpecificInput'] = self.subsequent_payment_product5001_specific_input.to_dictionary()
        if self.subsequentcard_payment_method_specific_input is not None:
            dictionary['subsequentcardPaymentMethodSpecificInput'] = self.subsequentcard_payment_method_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SubsequentPaymentRequest':
        super().from_dictionary(dictionary)
        if 'omnichannelSubsequentSpecificInput' in dictionary:
            if not isinstance(dictionary['omnichannelSubsequentSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['omnichannelSubsequentSpecificInput']))
            value = OmnichannelSubsequentSpecificInput()
            self.omnichannel_subsequent_specific_input = value.from_dictionary(dictionary['omnichannelSubsequentSpecificInput'])
        if 'order' in dictionary:
            if not isinstance(dictionary['order'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['order']))
            value = Order()
            self.order = value.from_dictionary(dictionary['order'])
        if 'subsequentPaymentProduct5001SpecificInput' in dictionary:
            if not isinstance(dictionary['subsequentPaymentProduct5001SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['subsequentPaymentProduct5001SpecificInput']))
            value = SubsequentPaymentProduct5001SpecificInput()
            self.subsequent_payment_product5001_specific_input = value.from_dictionary(dictionary['subsequentPaymentProduct5001SpecificInput'])
        if 'subsequentcardPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['subsequentcardPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['subsequentcardPaymentMethodSpecificInput']))
            value = SubsequentCardPaymentMethodSpecificInput()
            self.subsequentcard_payment_method_specific_input = value.from_dictionary(dictionary['subsequentcardPaymentMethodSpecificInput'])
        return self

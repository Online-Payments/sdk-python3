# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class CardRecurrenceDetails(DataObject):
    """
    | Object containing data related to recurring
    """

    __recurring_payment_sequence_indicator = None

    @property
    def recurring_payment_sequence_indicator(self) -> str:
        """
        | * first = This transaction is the first of a series of recurring transactions
        | * recurring = This transaction is a subsequent transaction in a series of recurring transactions
        
        | Note: For any first of a recurring the system will automatically create a token as you will need to use a token for any subsequent recurring transactions. In case a token already exists this is indicated in the response with a value of False for the isNewToken property in the response.

        Type: str
        """
        return self.__recurring_payment_sequence_indicator

    @recurring_payment_sequence_indicator.setter
    def recurring_payment_sequence_indicator(self, value: str):
        self.__recurring_payment_sequence_indicator = value

    def to_dictionary(self):
        dictionary = super(CardRecurrenceDetails, self).to_dictionary()
        if self.recurring_payment_sequence_indicator is not None:
            dictionary['recurringPaymentSequenceIndicator'] = self.recurring_payment_sequence_indicator
        return dictionary

    def from_dictionary(self, dictionary):
        super(CardRecurrenceDetails, self).from_dictionary(dictionary)
        if 'recurringPaymentSequenceIndicator' in dictionary:
            self.recurring_payment_sequence_indicator = dictionary['recurringPaymentSequenceIndicator']
        return self

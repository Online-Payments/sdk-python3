# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.currency_conversion_result import CurrencyConversionResult
from onlinepayments.sdk.domain.dcc_proposal import DccProposal


class CurrencyConversionResponse(DataObject):
    """
    | Payload of the response to a rate inquiry request
    """

    __dcc_session_id = None
    __proposal = None
    __result = None

    @property
    def dcc_session_id(self) -> str:
        """
        | The identifier of the Dynamic Currency Conversion(DCC) session that has been created. 'dccSessionId' will be populated exclusively when the result is "Allowed" for other outcomes such as "InvalidCard", "InvalidMerchant", "NoRate" or "NotAvailable" this field value will be an empty string.

        Type: str
        """
        return self.__dcc_session_id

    @dcc_session_id.setter
    def dcc_session_id(self, value: str):
        self.__dcc_session_id = value

    @property
    def proposal(self) -> DccProposal:
        """
        | Details of currency conversion to be proposed to the cardholder

        Type: :class:`onlinepayments.sdk.domain.dcc_proposal.DccProposal`
        """
        return self.__proposal

    @proposal.setter
    def proposal(self, value: DccProposal):
        self.__proposal = value

    @property
    def result(self) -> CurrencyConversionResult:
        """
        | Result of a requested currency conversion

        Type: :class:`onlinepayments.sdk.domain.currency_conversion_result.CurrencyConversionResult`
        """
        return self.__result

    @result.setter
    def result(self, value: CurrencyConversionResult):
        self.__result = value

    def to_dictionary(self):
        dictionary = super(CurrencyConversionResponse, self).to_dictionary()
        if self.dcc_session_id is not None:
            dictionary['dccSessionId'] = self.dcc_session_id
        if self.proposal is not None:
            dictionary['proposal'] = self.proposal.to_dictionary()
        if self.result is not None:
            dictionary['result'] = self.result.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CurrencyConversionResponse, self).from_dictionary(dictionary)
        if 'dccSessionId' in dictionary:
            self.dcc_session_id = dictionary['dccSessionId']
        if 'proposal' in dictionary:
            if not isinstance(dictionary['proposal'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['proposal']))
            value = DccProposal()
            self.proposal = value.from_dictionary(dictionary['proposal'])
        if 'result' in dictionary:
            if not isinstance(dictionary['result'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['result']))
            value = CurrencyConversionResult()
            self.result = value.from_dictionary(dictionary['result'])
        return self

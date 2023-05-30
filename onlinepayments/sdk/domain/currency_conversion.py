# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.dcc_proposal import DccProposal


class CurrencyConversion(DataObject):
    __accepted_by_user = None
    __proposal = None

    @property
    def accepted_by_user(self) -> bool:
        """
        | Dynamic Currency Conversion(DCC) Proposal accepted by user

        Type: bool
        """
        return self.__accepted_by_user

    @accepted_by_user.setter
    def accepted_by_user(self, value: bool):
        self.__accepted_by_user = value

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

    def to_dictionary(self):
        dictionary = super(CurrencyConversion, self).to_dictionary()
        if self.accepted_by_user is not None:
            dictionary['acceptedByUser'] = self.accepted_by_user
        if self.proposal is not None:
            dictionary['proposal'] = self.proposal.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CurrencyConversion, self).from_dictionary(dictionary)
        if 'acceptedByUser' in dictionary:
            self.accepted_by_user = dictionary['acceptedByUser']
        if 'proposal' in dictionary:
            if not isinstance(dictionary['proposal'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['proposal']))
            value = DccProposal()
            self.proposal = value.from_dictionary(dictionary['proposal'])
        return self

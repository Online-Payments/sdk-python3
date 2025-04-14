# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .dcc_proposal import DccProposal


class CurrencyConversion(DataObject):

    __accepted_by_user: Optional[bool] = None
    __proposal: Optional[DccProposal] = None

    @property
    def accepted_by_user(self) -> Optional[bool]:
        """
        | Dynamic Currency Conversion(DCC) Proposal accepted by user

        Type: bool
        """
        return self.__accepted_by_user

    @accepted_by_user.setter
    def accepted_by_user(self, value: Optional[bool]) -> None:
        self.__accepted_by_user = value

    @property
    def proposal(self) -> Optional[DccProposal]:
        """
        | Details of currency conversion to be proposed to the cardholder

        Type: :class:`onlinepayments.sdk.domain.dcc_proposal.DccProposal`
        """
        return self.__proposal

    @proposal.setter
    def proposal(self, value: Optional[DccProposal]) -> None:
        self.__proposal = value

    def to_dictionary(self) -> dict:
        dictionary = super(CurrencyConversion, self).to_dictionary()
        if self.accepted_by_user is not None:
            dictionary['acceptedByUser'] = self.accepted_by_user
        if self.proposal is not None:
            dictionary['proposal'] = self.proposal.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CurrencyConversion':
        super(CurrencyConversion, self).from_dictionary(dictionary)
        if 'acceptedByUser' in dictionary:
            self.accepted_by_user = dictionary['acceptedByUser']
        if 'proposal' in dictionary:
            if not isinstance(dictionary['proposal'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['proposal']))
            value = DccProposal()
            self.proposal = value.from_dictionary(dictionary['proposal'])
        return self

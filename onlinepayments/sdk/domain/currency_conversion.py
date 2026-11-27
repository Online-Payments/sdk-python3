#
# This file was automatically generated.
#
from .data_object import DataObject
from .dcc_proposal import DccProposal


class CurrencyConversion(DataObject):

    __slots__ = (
        "__accepted_by_user",
        "__proposal",
    )

    __accepted_by_user: bool | None
    __proposal: DccProposal | None

    def __init__(
        self,
        *,
        accepted_by_user: bool | None = None,
        proposal: DccProposal | None = None,
    ) -> None:
        self.accepted_by_user = accepted_by_user
        self.proposal = proposal

    @property
    def accepted_by_user(self) -> bool | None:
        """
        | Dynamic Currency Conversion(DCC) Proposal accepted by user

        Type: bool
        """
        return self.__accepted_by_user

    @accepted_by_user.setter
    def accepted_by_user(self, value: bool | None) -> None:
        self.__accepted_by_user = value

    @property
    def proposal(self) -> DccProposal | None:
        """
        | Details of currency conversion to be proposed to the cardholder

        Type: :class:`onlinepayments.sdk.domain.dcc_proposal.DccProposal`
        """
        return self.__proposal

    @proposal.setter
    def proposal(self, value: DccProposal | None) -> None:
        self.__proposal = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.accepted_by_user is not None:
            dictionary['acceptedByUser'] = self.accepted_by_user
        if self.proposal is not None:
            dictionary['proposal'] = self.proposal.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CurrencyConversion':
        super().from_dictionary(dictionary)
        if 'acceptedByUser' in dictionary:
            self.accepted_by_user = dictionary['acceptedByUser']
        if 'proposal' in dictionary:
            if not isinstance(dictionary['proposal'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['proposal']))
            value = DccProposal()
            self.proposal = value.from_dictionary(dictionary['proposal'])
        return self

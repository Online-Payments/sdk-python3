# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .acceptance import Acceptance
from .currency_conversion import CurrencyConversion
from .data_object import DataObject
from .reattempt_instructions import ReattemptInstructions


class RefundCardMethodSpecificOutput(DataObject):

    __acceptance: Optional[Acceptance] = None
    __authorisation_code: Optional[str] = None
    __currency_conversion: Optional[CurrencyConversion] = None
    __reattempt_instructions: Optional[ReattemptInstructions] = None
    __total_amount_paid: Optional[int] = None
    __total_amount_refunded: Optional[int] = None

    @property
    def acceptance(self) -> Optional[Acceptance]:
        """
        | This object contains the acceptance information for the card payment authorization.

        Type: :class:`onlinepayments.sdk.domain.acceptance.Acceptance`
        """
        return self.__acceptance

    @acceptance.setter
    def acceptance(self, value: Optional[Acceptance]) -> None:
        self.__acceptance = value

    @property
    def authorisation_code(self) -> Optional[str]:
        """
        | Card Authorization code as returned by the acquirer

        Type: str
        """
        return self.__authorisation_code

    @authorisation_code.setter
    def authorisation_code(self, value: Optional[str]) -> None:
        self.__authorisation_code = value

    @property
    def currency_conversion(self) -> Optional[CurrencyConversion]:
        """
        Type: :class:`onlinepayments.sdk.domain.currency_conversion.CurrencyConversion`
        """
        return self.__currency_conversion

    @currency_conversion.setter
    def currency_conversion(self, value: Optional[CurrencyConversion]) -> None:
        self.__currency_conversion = value

    @property
    def reattempt_instructions(self) -> Optional[ReattemptInstructions]:
        """
        | Instructions for reattempting a declined authorization. Provided only in case of declined authorization, for those acquirers that may respond with explicit instructions regarding potential reattempt processing.

        Type: :class:`onlinepayments.sdk.domain.reattempt_instructions.ReattemptInstructions`
        """
        return self.__reattempt_instructions

    @reattempt_instructions.setter
    def reattempt_instructions(self, value: Optional[ReattemptInstructions]) -> None:
        self.__reattempt_instructions = value

    @property
    def total_amount_paid(self) -> Optional[int]:
        """
        Type: int
        """
        return self.__total_amount_paid

    @total_amount_paid.setter
    def total_amount_paid(self, value: Optional[int]) -> None:
        self.__total_amount_paid = value

    @property
    def total_amount_refunded(self) -> Optional[int]:
        """
        Type: int
        """
        return self.__total_amount_refunded

    @total_amount_refunded.setter
    def total_amount_refunded(self, value: Optional[int]) -> None:
        self.__total_amount_refunded = value

    def to_dictionary(self) -> dict:
        dictionary = super(RefundCardMethodSpecificOutput, self).to_dictionary()
        if self.acceptance is not None:
            dictionary['acceptance'] = self.acceptance.to_dictionary()
        if self.authorisation_code is not None:
            dictionary['authorisationCode'] = self.authorisation_code
        if self.currency_conversion is not None:
            dictionary['currencyConversion'] = self.currency_conversion.to_dictionary()
        if self.reattempt_instructions is not None:
            dictionary['reattemptInstructions'] = self.reattempt_instructions.to_dictionary()
        if self.total_amount_paid is not None:
            dictionary['totalAmountPaid'] = self.total_amount_paid
        if self.total_amount_refunded is not None:
            dictionary['totalAmountRefunded'] = self.total_amount_refunded
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RefundCardMethodSpecificOutput':
        super(RefundCardMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'acceptance' in dictionary:
            if not isinstance(dictionary['acceptance'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['acceptance']))
            value = Acceptance()
            self.acceptance = value.from_dictionary(dictionary['acceptance'])
        if 'authorisationCode' in dictionary:
            self.authorisation_code = dictionary['authorisationCode']
        if 'currencyConversion' in dictionary:
            if not isinstance(dictionary['currencyConversion'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['currencyConversion']))
            value = CurrencyConversion()
            self.currency_conversion = value.from_dictionary(dictionary['currencyConversion'])
        if 'reattemptInstructions' in dictionary:
            if not isinstance(dictionary['reattemptInstructions'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['reattemptInstructions']))
            value = ReattemptInstructions()
            self.reattempt_instructions = value.from_dictionary(dictionary['reattemptInstructions'])
        if 'totalAmountPaid' in dictionary:
            self.total_amount_paid = dictionary['totalAmountPaid']
        if 'totalAmountRefunded' in dictionary:
            self.total_amount_refunded = dictionary['totalAmountRefunded']
        return self

# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .mobile_three_d_secure_challenge_parameters import MobileThreeDSecureChallengeParameters
from .redirect_data import RedirectData
from .show_form_data import ShowFormData
from .show_instructions_data import ShowInstructionsData


class MerchantAction(DataObject):

    __action_type: Optional[str] = None
    __mobile_three_d_secure_challenge_parameters: Optional[MobileThreeDSecureChallengeParameters] = None
    __redirect_data: Optional[RedirectData] = None
    __show_form_data: Optional[ShowFormData] = None
    __show_instructions_data: Optional[ShowInstructionsData] = None

    @property
    def action_type(self) -> Optional[str]:
        """
        | Action merchants needs to take in the online payment process. Possible values are:
        
        * REDIRECT - The customer needs to be redirected using the details found in redirectData
        * SHOW_FORM - The customer needs to be shown a form with the fields found in formFields. You can submit the data entered by the user in a Complete payment request.
        * SHOW_INSTRUCTIONS - The customer needs to be shown payment instruction using the details found in showData. Alternatively the instructions can be rendered by us using the instructionsRenderingData
        * SHOW_TRANSACTION_RESULTS - The customer needs to be shown the transaction results using the details found in showData. Alternatively the instructions can be rendered by us using the instructionsRenderingData
        * MOBILE_THREEDS_CHALLENGE - The customer needs to complete a challenge as part of the 3D Secure authentication inside your mobile app. The details contained in mobileThreeDSecureChallengeParameters need to be provided to the EMVco certified Mobile SDK as a challengeParameters object.
        * CALL_THIRD_PARTY - The merchant needs to call a third party using the data found in thirdPartyData

        Type: str
        """
        return self.__action_type

    @action_type.setter
    def action_type(self, value: Optional[str]) -> None:
        self.__action_type = value

    @property
    def mobile_three_d_secure_challenge_parameters(self) -> Optional[MobileThreeDSecureChallengeParameters]:
        """
        | Mobile 3D Secure Challenge Parameters

        Type: :class:`onlinepayments.sdk.domain.mobile_three_d_secure_challenge_parameters.MobileThreeDSecureChallengeParameters`
        """
        return self.__mobile_three_d_secure_challenge_parameters

    @mobile_three_d_secure_challenge_parameters.setter
    def mobile_three_d_secure_challenge_parameters(self, value: Optional[MobileThreeDSecureChallengeParameters]) -> None:
        self.__mobile_three_d_secure_challenge_parameters = value

    @property
    def redirect_data(self) -> Optional[RedirectData]:
        """
        | Object containing all data needed to redirect the customer

        Type: :class:`onlinepayments.sdk.domain.redirect_data.RedirectData`
        """
        return self.__redirect_data

    @redirect_data.setter
    def redirect_data(self, value: Optional[RedirectData]) -> None:
        self.__redirect_data = value

    @property
    def show_form_data(self) -> Optional[ShowFormData]:
        """
        | Object returned for the SHOW_FORM actionType.

        Type: :class:`onlinepayments.sdk.domain.show_form_data.ShowFormData`
        """
        return self.__show_form_data

    @show_form_data.setter
    def show_form_data(self, value: Optional[ShowFormData]) -> None:
        self.__show_form_data = value

    @property
    def show_instructions_data(self) -> Optional[ShowInstructionsData]:
        """
        | Object returned for the SHOW_INSTRUCTIONS actionType.

        Type: :class:`onlinepayments.sdk.domain.show_instructions_data.ShowInstructionsData`
        """
        return self.__show_instructions_data

    @show_instructions_data.setter
    def show_instructions_data(self, value: Optional[ShowInstructionsData]) -> None:
        self.__show_instructions_data = value

    def to_dictionary(self) -> dict:
        dictionary = super(MerchantAction, self).to_dictionary()
        if self.action_type is not None:
            dictionary['actionType'] = self.action_type
        if self.mobile_three_d_secure_challenge_parameters is not None:
            dictionary['mobileThreeDSecureChallengeParameters'] = self.mobile_three_d_secure_challenge_parameters.to_dictionary()
        if self.redirect_data is not None:
            dictionary['redirectData'] = self.redirect_data.to_dictionary()
        if self.show_form_data is not None:
            dictionary['showFormData'] = self.show_form_data.to_dictionary()
        if self.show_instructions_data is not None:
            dictionary['showInstructionsData'] = self.show_instructions_data.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MerchantAction':
        super(MerchantAction, self).from_dictionary(dictionary)
        if 'actionType' in dictionary:
            self.action_type = dictionary['actionType']
        if 'mobileThreeDSecureChallengeParameters' in dictionary:
            if not isinstance(dictionary['mobileThreeDSecureChallengeParameters'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mobileThreeDSecureChallengeParameters']))
            value = MobileThreeDSecureChallengeParameters()
            self.mobile_three_d_secure_challenge_parameters = value.from_dictionary(dictionary['mobileThreeDSecureChallengeParameters'])
        if 'redirectData' in dictionary:
            if not isinstance(dictionary['redirectData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectData']))
            value = RedirectData()
            self.redirect_data = value.from_dictionary(dictionary['redirectData'])
        if 'showFormData' in dictionary:
            if not isinstance(dictionary['showFormData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['showFormData']))
            value = ShowFormData()
            self.show_form_data = value.from_dictionary(dictionary['showFormData'])
        if 'showInstructionsData' in dictionary:
            if not isinstance(dictionary['showInstructionsData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['showInstructionsData']))
            value = ShowInstructionsData()
            self.show_instructions_data = value.from_dictionary(dictionary['showInstructionsData'])
        return self

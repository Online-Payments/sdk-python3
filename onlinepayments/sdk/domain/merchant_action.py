# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.redirect_data import RedirectData


class MerchantAction(DataObject):
    """
    | Object that contains the action, including the needed data, that you should perform next, like showing instructions, showing the transaction results or redirect to a third party to complete the payment
    """

    __action_type = None
    __redirect_data = None

    @property
    def action_type(self) -> str:
        """
        | Action merchants needs to take in the online payment process. Possible values are: 
        |  * REDIRECT - The customer needs to be redirected using the details found in redirectData 
        |  * SHOW_FORM - The customer needs to be shown a form with the fields found in formFields. You can submit the data entered by the user in a Complete payment request. 
        |  * SHOW_INSTRUCTIONS - The customer needs to be shown payment instruction using the details found in showData. Alternatively the instructions can be rendered by us using the instructionsRenderingData 
        |  * SHOW_TRANSACTION_RESULTS - The customer needs to be shown the transaction results using the details found in showData. Alternatively the instructions can be rendered by us using the instructionsRenderingData 
        |  * MOBILE_THREEDS_CHALLENGE - The customer needs to complete a challenge as part of the 3D Secure authentication inside your mobile app. The details contained in mobileThreeDSecureChallengeParameters need to be provided to the EMVco certified Mobile SDK as a challengeParameters object. 
        |  * CALL_THIRD_PARTY - The merchant needs to call a third party using the data found in thirdPartyData

        Type: str
        """
        return self.__action_type

    @action_type.setter
    def action_type(self, value: str):
        self.__action_type = value

    @property
    def redirect_data(self) -> RedirectData:
        """
        | Object containing all data needed to redirect the customer

        Type: :class:`onlinepayments.sdk.domain.redirect_data.RedirectData`
        """
        return self.__redirect_data

    @redirect_data.setter
    def redirect_data(self, value: RedirectData):
        self.__redirect_data = value

    def to_dictionary(self):
        dictionary = super(MerchantAction, self).to_dictionary()
        if self.action_type is not None:
            dictionary['actionType'] = self.action_type
        if self.redirect_data is not None:
            dictionary['redirectData'] = self.redirect_data.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(MerchantAction, self).from_dictionary(dictionary)
        if 'actionType' in dictionary:
            self.action_type = dictionary['actionType']
        if 'redirectData' in dictionary:
            if not isinstance(dictionary['redirectData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectData']))
            value = RedirectData()
            self.redirect_data = value.from_dictionary(dictionary['redirectData'])
        return self

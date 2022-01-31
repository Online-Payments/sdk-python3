# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.mandate_merchant_action import MandateMerchantAction
from onlinepayments.sdk.domain.mandate_response import MandateResponse


class CreateMandateResponse(DataObject):
    """
    | Object containing the Create Mandate response
    """

    __mandate = None
    __merchant_action = None

    @property
    def mandate(self) -> MandateResponse:
        """
        | Object containing the created mandate.

        Type: :class:`onlinepayments.sdk.domain.mandate_response.MandateResponse`
        """
        return self.__mandate

    @mandate.setter
    def mandate(self, value: MandateResponse):
        self.__mandate = value

    @property
    def merchant_action(self) -> MandateMerchantAction:
        """
        | Object that contains the action, including the needed data, that you should perform next, showing the redirect to a third party to complete the payment or like showing instructions.

        Type: :class:`onlinepayments.sdk.domain.mandate_merchant_action.MandateMerchantAction`
        """
        return self.__merchant_action

    @merchant_action.setter
    def merchant_action(self, value: MandateMerchantAction):
        self.__merchant_action = value

    def to_dictionary(self):
        dictionary = super(CreateMandateResponse, self).to_dictionary()
        if self.mandate is not None:
            dictionary['mandate'] = self.mandate.to_dictionary()
        if self.merchant_action is not None:
            dictionary['merchantAction'] = self.merchant_action.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreateMandateResponse, self).from_dictionary(dictionary)
        if 'mandate' in dictionary:
            if not isinstance(dictionary['mandate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mandate']))
            value = MandateResponse()
            self.mandate = value.from_dictionary(dictionary['mandate'])
        if 'merchantAction' in dictionary:
            if not isinstance(dictionary['merchantAction'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['merchantAction']))
            value = MandateMerchantAction()
            self.merchant_action = value.from_dictionary(dictionary['merchantAction'])
        return self

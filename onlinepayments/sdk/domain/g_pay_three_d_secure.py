# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .redirection_data import RedirectionData


class GPayThreeDSecure(DataObject):

    __challenge_canvas_size: Optional[str] = None
    __challenge_indicator: Optional[str] = None
    __exemption_request: Optional[str] = None
    __redirection_data: Optional[RedirectionData] = None
    __skip_authentication: Optional[bool] = None

    @property
    def challenge_canvas_size(self) -> Optional[str]:
        """
        | Dimensions of the challenge window that potentially will be displayed to the customer. The challenge content is formatted to appropriately render in this window to provide the best possible user experience. Preconfigured sizes are width x height in pixels of the window displayed in the customer browser window. Possible values are
        
        * 250x400 (default)
        * 390x400
        * 500x600
        * 600x400
        * full-screen

        Type: str
        """
        return self.__challenge_canvas_size

    @challenge_canvas_size.setter
    def challenge_canvas_size(self, value: Optional[str]) -> None:
        self.__challenge_canvas_size = value

    @property
    def challenge_indicator(self) -> Optional[str]:
        """
        | Allows you to indicate if you want the customer to be challenged for extra security on this transaction. Possible values:
        
        * no-preference - You have no preference whether or not to challenge the customer (default)
        * no-challenge-requested - you prefer the cardholder not to be challenged
        * challenge-requested - you prefer the customer to be challenged
        * challenge-required - you require the customer to be challenged
        * no-challenge-requested-risk-analysis-performed â€“ letting the issuer know that you have already assessed the transaction with fraud prevention tool
        * no-challenge-requested-data-share-only â€“ sharing data only with the DS
        * no-challenge-requested-consumer-authentication-performed â€“ authentication already happened at your side â€“ when login in to your website
        * no-challenge-requested-use-whitelist-exemption â€“ cardholder has whitelisted you at with the issuer
        * challenge-requested-whitelist-prompt-requested â€“ cardholder is trying to whitelist you
        * request-scoring-without-connecting-to-acs â€“ sending information to CB DS for a fraud scoring

        Type: str
        """
        return self.__challenge_indicator

    @challenge_indicator.setter
    def challenge_indicator(self, value: Optional[str]) -> None:
        self.__challenge_indicator = value

    @property
    def exemption_request(self) -> Optional[str]:
        """
        | In PSD2, the ExemptionRequest field is used by merchants requesting an exemption when not using authentication on a transaction, in order to keep the conversion up.
        
        * none = No exemption requested
        * transaction-risk-analysis = Fraud analysis has been done already by your own fraud module and transaction scored as low risk
        * low-value = Bellow 30 euros
        * whitelist = The cardholder has whitelisted you with their issuer

        Type: str
        """
        return self.__exemption_request

    @exemption_request.setter
    def exemption_request(self, value: Optional[str]) -> None:
        self.__exemption_request = value

    @property
    def redirection_data(self) -> Optional[RedirectionData]:
        """
        | Object containing browser specific redirection related data

        Type: :class:`onlinepayments.sdk.domain.redirection_data.RedirectionData`
        """
        return self.__redirection_data

    @redirection_data.setter
    def redirection_data(self, value: Optional[RedirectionData]) -> None:
        self.__redirection_data = value

    @property
    def skip_authentication(self) -> Optional[bool]:
        """
        * true = 3D Secure authentication will be skipped for this transaction. This setting should be used when isRecurring is set to true and recurringPaymentSequenceIndicator is set to "recurring"
        * false = 3D Secure authentication will not be skipped for this transaction
        
        | Note: This is only possible if your account in our system is setup for 3D Secure authentication and if your configuration in our system allows you to override it per transaction

        Type: bool
        """
        return self.__skip_authentication

    @skip_authentication.setter
    def skip_authentication(self, value: Optional[bool]) -> None:
        self.__skip_authentication = value

    def to_dictionary(self) -> dict:
        dictionary = super(GPayThreeDSecure, self).to_dictionary()
        if self.challenge_canvas_size is not None:
            dictionary['challengeCanvasSize'] = self.challenge_canvas_size
        if self.challenge_indicator is not None:
            dictionary['challengeIndicator'] = self.challenge_indicator
        if self.exemption_request is not None:
            dictionary['exemptionRequest'] = self.exemption_request
        if self.redirection_data is not None:
            dictionary['redirectionData'] = self.redirection_data.to_dictionary()
        if self.skip_authentication is not None:
            dictionary['skipAuthentication'] = self.skip_authentication
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'GPayThreeDSecure':
        super(GPayThreeDSecure, self).from_dictionary(dictionary)
        if 'challengeCanvasSize' in dictionary:
            self.challenge_canvas_size = dictionary['challengeCanvasSize']
        if 'challengeIndicator' in dictionary:
            self.challenge_indicator = dictionary['challengeIndicator']
        if 'exemptionRequest' in dictionary:
            self.exemption_request = dictionary['exemptionRequest']
        if 'redirectionData' in dictionary:
            if not isinstance(dictionary['redirectionData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectionData']))
            value = RedirectionData()
            self.redirection_data = value.from_dictionary(dictionary['redirectionData'])
        if 'skipAuthentication' in dictionary:
            self.skip_authentication = dictionary['skipAuthentication']
        return self

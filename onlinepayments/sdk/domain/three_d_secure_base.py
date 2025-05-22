# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .three_d_secure_data import ThreeDSecureData


class ThreeDSecureBase(DataObject):

    __authentication_amount: Optional[int] = None
    __challenge_canvas_size: Optional[str] = None
    __challenge_indicator: Optional[str] = None
    __exemption_request: Optional[str] = None
    __merchant_fraud_rate: Optional[int] = None
    __prior_three_d_secure_data: Optional[ThreeDSecureData] = None
    __secure_corporate_payment: Optional[bool] = None
    __skip_authentication: Optional[bool] = None
    __skip_soft_decline: Optional[bool] = None

    @property
    def authentication_amount(self) -> Optional[int]:
        """
        | The amount to be authenticated. This field should be populated if the amount to be authenticated differs from the amount to be authorized (by default they are considered equal). Amount in cents and always having 2 decimals.

        Type: int
        """
        return self.__authentication_amount

    @authentication_amount.setter
    def authentication_amount(self, value: Optional[int]) -> None:
        self.__authentication_amount = value

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
        * no-challenge-requested-risk-analysis-performed – letting the issuer know that you have already assessed the transaction with fraud prevention tool
        * no-challenge-requested-data-share-only – sharing data only with the DS
        * no-challenge-requested-consumer-authentication-performed – authentication already happened at your side – when login in to your website
        * no-challenge-requested-use-whitelist-exemption – cardholder has whitelisted you at with the issuer
        * challenge-requested-whitelist-prompt-requested – cardholder is trying to whitelist you
        * request-scoring-without-connecting-to-acs – sending information to CB DS for a fraud scoring

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
    def merchant_fraud_rate(self) -> Optional[int]:
        """
        | Merchant fraud rate in the EEA (all EEA card fraud divided by all EEA card volumes) calculated as per PSD2 RTS. Mastercard will not calculate or validate the merchant fraud score Values accepted :
        
        * 1 - represents fraud rate less than or equal to 1 basis point [bp], which is 0.01%
        * 2 - represents fraud rate between 1 bp + - and 6 bps
        * 3 - represents fraud rate between 6 bps + - and 13 bps
        * 4 - represents fraud rate between 13 bps + - and 25 bps
        * 5 - represents fraud rate greater than 25 bps

        Type: int
        """
        return self.__merchant_fraud_rate

    @merchant_fraud_rate.setter
    def merchant_fraud_rate(self, value: Optional[int]) -> None:
        self.__merchant_fraud_rate = value

    @property
    def prior_three_d_secure_data(self) -> Optional[ThreeDSecureData]:
        """
        | Object containing data regarding the customer authentication that occurred prior to the current transaction

        Type: :class:`onlinepayments.sdk.domain.three_d_secure_data.ThreeDSecureData`
        """
        return self.__prior_three_d_secure_data

    @prior_three_d_secure_data.setter
    def prior_three_d_secure_data(self, value: Optional[ThreeDSecureData]) -> None:
        self.__prior_three_d_secure_data = value

    @property
    def secure_corporate_payment(self) -> Optional[bool]:
        """
        | Indicates dedicated payment processes and procedures were used, potential secure corporate payment exemption applies Logically this field should only be set to yes if the acquirer exemption field is blank. A merchant cannot claim both acquirer exemption and  secure payment. However, the DS will not validate the conditions in the extension. DS will pass data as presented.

        Type: bool
        """
        return self.__secure_corporate_payment

    @secure_corporate_payment.setter
    def secure_corporate_payment(self, value: Optional[bool]) -> None:
        self.__secure_corporate_payment = value

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

    @property
    def skip_soft_decline(self) -> Optional[bool]:
        """
        * true = Soft Decline retry mechanism will be skipped for this transaction. The transaction will result in "Authorization Declined" status. This setting should be used when skipAuthentication is set to true and the merchant does not want to use Soft Decline retry mechanism.
        * false = Soft Decline retry mechanism will not be skipped for this transaction.
        
        | Note: skipSoftDecline defaults to false if empty. This is only possible if your account in our system is setup for 3D Secure authentication and if your configuration in our system allows you to override it per transaction.

        Type: bool
        """
        return self.__skip_soft_decline

    @skip_soft_decline.setter
    def skip_soft_decline(self, value: Optional[bool]) -> None:
        self.__skip_soft_decline = value

    def to_dictionary(self) -> dict:
        dictionary = super(ThreeDSecureBase, self).to_dictionary()
        if self.authentication_amount is not None:
            dictionary['authenticationAmount'] = self.authentication_amount
        if self.challenge_canvas_size is not None:
            dictionary['challengeCanvasSize'] = self.challenge_canvas_size
        if self.challenge_indicator is not None:
            dictionary['challengeIndicator'] = self.challenge_indicator
        if self.exemption_request is not None:
            dictionary['exemptionRequest'] = self.exemption_request
        if self.merchant_fraud_rate is not None:
            dictionary['merchantFraudRate'] = self.merchant_fraud_rate
        if self.prior_three_d_secure_data is not None:
            dictionary['priorThreeDSecureData'] = self.prior_three_d_secure_data.to_dictionary()
        if self.secure_corporate_payment is not None:
            dictionary['secureCorporatePayment'] = self.secure_corporate_payment
        if self.skip_authentication is not None:
            dictionary['skipAuthentication'] = self.skip_authentication
        if self.skip_soft_decline is not None:
            dictionary['skipSoftDecline'] = self.skip_soft_decline
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ThreeDSecureBase':
        super(ThreeDSecureBase, self).from_dictionary(dictionary)
        if 'authenticationAmount' in dictionary:
            self.authentication_amount = dictionary['authenticationAmount']
        if 'challengeCanvasSize' in dictionary:
            self.challenge_canvas_size = dictionary['challengeCanvasSize']
        if 'challengeIndicator' in dictionary:
            self.challenge_indicator = dictionary['challengeIndicator']
        if 'exemptionRequest' in dictionary:
            self.exemption_request = dictionary['exemptionRequest']
        if 'merchantFraudRate' in dictionary:
            self.merchant_fraud_rate = dictionary['merchantFraudRate']
        if 'priorThreeDSecureData' in dictionary:
            if not isinstance(dictionary['priorThreeDSecureData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['priorThreeDSecureData']))
            value = ThreeDSecureData()
            self.prior_three_d_secure_data = value.from_dictionary(dictionary['priorThreeDSecureData'])
        if 'secureCorporatePayment' in dictionary:
            self.secure_corporate_payment = dictionary['secureCorporatePayment']
        if 'skipAuthentication' in dictionary:
            self.skip_authentication = dictionary['skipAuthentication']
        if 'skipSoftDecline' in dictionary:
            self.skip_soft_decline = dictionary['skipSoftDecline']
        return self

# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.redirect_payment_product809_specific_input import RedirectPaymentProduct809SpecificInput
from onlinepayments.sdk.domain.redirect_payment_product840_specific_input import RedirectPaymentProduct840SpecificInput
from onlinepayments.sdk.domain.redirection_data import RedirectionData


class RedirectPaymentMethodSpecificInput(DataObject):
    """
    | Object containing the specific input details for payments that involve redirects to 3rd parties to complete, like iDeal and PayPal
    """

    __payment_option = None
    __payment_product809_specific_input = None
    __payment_product840_specific_input = None
    __payment_product_id = None
    __redirection_data = None
    __requires_approval = None
    __token = None
    __tokenize = None

    @property
    def payment_option(self) -> str:
        """
        | The specific payment option for the payment. To be used as a complement of the more generic paymentProductId (oney, banquecasino, cofidis), which allows to define a variation of the selected paymentProductId (ex: facilypay3x, banquecasino4x, cofidis3x-sansfrais, ...). List of modalities included in the payment product page.

        Type: str
        """
        return self.__payment_option

    @payment_option.setter
    def payment_option(self, value: str):
        self.__payment_option = value

    @property
    def payment_product809_specific_input(self) -> RedirectPaymentProduct809SpecificInput:
        """
        | Object containing specific input required for iDeal payments (Payment product ID 809)

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_product809_specific_input.RedirectPaymentProduct809SpecificInput`
        """
        return self.__payment_product809_specific_input

    @payment_product809_specific_input.setter
    def payment_product809_specific_input(self, value: RedirectPaymentProduct809SpecificInput):
        self.__payment_product809_specific_input = value

    @property
    def payment_product840_specific_input(self) -> RedirectPaymentProduct840SpecificInput:
        """
        | Object containing specific input required for PayPal payments (Payment product ID 840)

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_product840_specific_input.RedirectPaymentProduct840SpecificInput`
        """
        return self.__payment_product840_specific_input

    @payment_product840_specific_input.setter
    def payment_product840_specific_input(self, value: RedirectPaymentProduct840SpecificInput):
        self.__payment_product840_specific_input = value

    @property
    def payment_product_id(self) -> int:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: int):
        self.__payment_product_id = value

    @property
    def redirection_data(self) -> RedirectionData:
        """
        | Object containing browser specific redirection related data

        Type: :class:`onlinepayments.sdk.domain.redirection_data.RedirectionData`
        """
        return self.__redirection_data

    @redirection_data.setter
    def redirection_data(self, value: RedirectionData):
        self.__redirection_data = value

    @property
    def requires_approval(self) -> bool:
        """
        | * true = the payment requires approval before the funds will be captured using the Approve payment or Capture payment API
        | * false = the payment does not require approval, and the funds will be captured automatically

        Type: bool
        """
        return self.__requires_approval

    @requires_approval.setter
    def requires_approval(self, value: bool):
        self.__requires_approval = value

    @property
    def token(self) -> str:
        """
        | ID of the token to use to create the payment.

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: str):
        self.__token = value

    @property
    def tokenize(self) -> bool:
        """
        | Indicates if this transaction should be tokenized
        |   * true - Tokenize the transaction.
        |   * false - Do not tokenize the transaction, unless it would be tokenized by other means such as auto-tokenization of recurring payments.

        Type: bool
        """
        return self.__tokenize

    @tokenize.setter
    def tokenize(self, value: bool):
        self.__tokenize = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentMethodSpecificInput, self).to_dictionary()
        if self.payment_option is not None:
            dictionary['paymentOption'] = self.payment_option
        if self.payment_product809_specific_input is not None:
            dictionary['paymentProduct809SpecificInput'] = self.payment_product809_specific_input.to_dictionary()
        if self.payment_product840_specific_input is not None:
            dictionary['paymentProduct840SpecificInput'] = self.payment_product840_specific_input.to_dictionary()
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        if self.redirection_data is not None:
            dictionary['redirectionData'] = self.redirection_data.to_dictionary()
        if self.requires_approval is not None:
            dictionary['requiresApproval'] = self.requires_approval
        if self.token is not None:
            dictionary['token'] = self.token
        if self.tokenize is not None:
            dictionary['tokenize'] = self.tokenize
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'paymentOption' in dictionary:
            self.payment_option = dictionary['paymentOption']
        if 'paymentProduct809SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct809SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct809SpecificInput']))
            value = RedirectPaymentProduct809SpecificInput()
            self.payment_product809_specific_input = value.from_dictionary(dictionary['paymentProduct809SpecificInput'])
        if 'paymentProduct840SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct840SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct840SpecificInput']))
            value = RedirectPaymentProduct840SpecificInput()
            self.payment_product840_specific_input = value.from_dictionary(dictionary['paymentProduct840SpecificInput'])
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'redirectionData' in dictionary:
            if not isinstance(dictionary['redirectionData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['redirectionData']))
            value = RedirectionData()
            self.redirection_data = value.from_dictionary(dictionary['redirectionData'])
        if 'requiresApproval' in dictionary:
            self.requires_approval = dictionary['requiresApproval']
        if 'token' in dictionary:
            self.token = dictionary['token']
        if 'tokenize' in dictionary:
            self.tokenize = dictionary['tokenize']
        return self

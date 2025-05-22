# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject
from .redirect_payment_product3203_specific_input import RedirectPaymentProduct3203SpecificInput
from .redirect_payment_product3204_specific_input import RedirectPaymentProduct3204SpecificInput
from .redirect_payment_product3302_specific_input import RedirectPaymentProduct3302SpecificInput
from .redirect_payment_product3306_specific_input import RedirectPaymentProduct3306SpecificInput
from .redirect_payment_product5001_specific_input import RedirectPaymentProduct5001SpecificInput
from .redirect_payment_product5300_specific_input import RedirectPaymentProduct5300SpecificInput
from .redirect_payment_product5402_specific_input import RedirectPaymentProduct5402SpecificInput
from .redirect_payment_product5403_specific_input import RedirectPaymentProduct5403SpecificInput
from .redirect_payment_product5406_specific_input import RedirectPaymentProduct5406SpecificInput
from .redirect_payment_product5408_specific_input import RedirectPaymentProduct5408SpecificInput
from .redirect_payment_product5410_specific_input import RedirectPaymentProduct5410SpecificInput
from .redirect_payment_product809_specific_input import RedirectPaymentProduct809SpecificInput
from .redirect_payment_product840_specific_input import RedirectPaymentProduct840SpecificInput
from .redirection_data import RedirectionData


class RedirectPaymentMethodSpecificInput(DataObject):

    __payment_option: Optional[str] = None
    __payment_product3203_specific_input: Optional[RedirectPaymentProduct3203SpecificInput] = None
    __payment_product3204_specific_input: Optional[RedirectPaymentProduct3204SpecificInput] = None
    __payment_product3302_specific_input: Optional[RedirectPaymentProduct3302SpecificInput] = None
    __payment_product3306_specific_input: Optional[RedirectPaymentProduct3306SpecificInput] = None
    __payment_product5001_specific_input: Optional[RedirectPaymentProduct5001SpecificInput] = None
    __payment_product5300_specific_input: Optional[RedirectPaymentProduct5300SpecificInput] = None
    __payment_product5402_specific_input: Optional[RedirectPaymentProduct5402SpecificInput] = None
    __payment_product5403_specific_input: Optional[RedirectPaymentProduct5403SpecificInput] = None
    __payment_product5406_specific_input: Optional[RedirectPaymentProduct5406SpecificInput] = None
    __payment_product5408_specific_input: Optional[RedirectPaymentProduct5408SpecificInput] = None
    __payment_product5410_specific_input: Optional[RedirectPaymentProduct5410SpecificInput] = None
    __payment_product809_specific_input: Optional[RedirectPaymentProduct809SpecificInput] = None
    __payment_product840_specific_input: Optional[RedirectPaymentProduct840SpecificInput] = None
    __payment_product_id: Optional[int] = None
    __redirection_data: Optional[RedirectionData] = None
    __requires_approval: Optional[bool] = None
    __token: Optional[str] = None
    __tokenize: Optional[bool] = None

    @property
    def payment_option(self) -> Optional[str]:
        """
        | The specific payment option for the payment. To be used as a complement of the more generic paymentProductId (oney, banquecasino, cofidis), which allows to define a variation of the selected paymentProductId (ex: facilypay3x, banquecasino4x, cofidis3x-sansfrais, ...). List of modalities included in the payment product page.

        Type: str
        """
        return self.__payment_option

    @payment_option.setter
    def payment_option(self, value: Optional[str]) -> None:
        self.__payment_option = value

    @property
    def payment_product3203_specific_input(self) -> Optional[RedirectPaymentProduct3203SpecificInput]:
        """
        | Object containing specific input for PostFinancePay payments (Payment product ID 3203).

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_product3203_specific_input.RedirectPaymentProduct3203SpecificInput`
        """
        return self.__payment_product3203_specific_input

    @payment_product3203_specific_input.setter
    def payment_product3203_specific_input(self, value: Optional[RedirectPaymentProduct3203SpecificInput]) -> None:
        self.__payment_product3203_specific_input = value

    @property
    def payment_product3204_specific_input(self) -> Optional[RedirectPaymentProduct3204SpecificInput]:
        """
        | BLIK (payment product 3204) specific details

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_product3204_specific_input.RedirectPaymentProduct3204SpecificInput`
        """
        return self.__payment_product3204_specific_input

    @payment_product3204_specific_input.setter
    def payment_product3204_specific_input(self, value: Optional[RedirectPaymentProduct3204SpecificInput]) -> None:
        self.__payment_product3204_specific_input = value

    @property
    def payment_product3302_specific_input(self) -> Optional[RedirectPaymentProduct3302SpecificInput]:
        """
        | Object containing specific input required for Klarna PayLater payment (Payment product ID 3302)

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_product3302_specific_input.RedirectPaymentProduct3302SpecificInput`
        """
        return self.__payment_product3302_specific_input

    @payment_product3302_specific_input.setter
    def payment_product3302_specific_input(self, value: Optional[RedirectPaymentProduct3302SpecificInput]) -> None:
        self.__payment_product3302_specific_input = value

    @property
    def payment_product3306_specific_input(self) -> Optional[RedirectPaymentProduct3306SpecificInput]:
        """
        | Object containing specific input required for Klarna payments (Payment product ID 3306)

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_product3306_specific_input.RedirectPaymentProduct3306SpecificInput`
        """
        return self.__payment_product3306_specific_input

    @payment_product3306_specific_input.setter
    def payment_product3306_specific_input(self, value: Optional[RedirectPaymentProduct3306SpecificInput]) -> None:
        self.__payment_product3306_specific_input = value

    @property
    def payment_product5001_specific_input(self) -> Optional[RedirectPaymentProduct5001SpecificInput]:
        """
        | Object containing specific input required for Bizum payments

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_product5001_specific_input.RedirectPaymentProduct5001SpecificInput`
        """
        return self.__payment_product5001_specific_input

    @payment_product5001_specific_input.setter
    def payment_product5001_specific_input(self, value: Optional[RedirectPaymentProduct5001SpecificInput]) -> None:
        self.__payment_product5001_specific_input = value

    @property
    def payment_product5300_specific_input(self) -> Optional[RedirectPaymentProduct5300SpecificInput]:
        """
        | Pledg (payment product 5300) specific details

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_product5300_specific_input.RedirectPaymentProduct5300SpecificInput`
        """
        return self.__payment_product5300_specific_input

    @payment_product5300_specific_input.setter
    def payment_product5300_specific_input(self, value: Optional[RedirectPaymentProduct5300SpecificInput]) -> None:
        self.__payment_product5300_specific_input = value

    @property
    def payment_product5402_specific_input(self) -> Optional[RedirectPaymentProduct5402SpecificInput]:
        """
        | Object containing specific input required for E-Voucher payments (Payment product ID 5402)

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_product5402_specific_input.RedirectPaymentProduct5402SpecificInput`
        """
        return self.__payment_product5402_specific_input

    @payment_product5402_specific_input.setter
    def payment_product5402_specific_input(self, value: Optional[RedirectPaymentProduct5402SpecificInput]) -> None:
        self.__payment_product5402_specific_input = value

    @property
    def payment_product5403_specific_input(self) -> Optional[RedirectPaymentProduct5403SpecificInput]:
        """
        | Object containing specific input required for Chèque-Vacances Connect payments (Payment product ID 5403)

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_product5403_specific_input.RedirectPaymentProduct5403SpecificInput`
        """
        return self.__payment_product5403_specific_input

    @payment_product5403_specific_input.setter
    def payment_product5403_specific_input(self, value: Optional[RedirectPaymentProduct5403SpecificInput]) -> None:
        self.__payment_product5403_specific_input = value

    @property
    def payment_product5406_specific_input(self) -> Optional[RedirectPaymentProduct5406SpecificInput]:
        """
        | Object containing specific input for EPS payments (Payment product ID 5406)

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_product5406_specific_input.RedirectPaymentProduct5406SpecificInput`
        """
        return self.__payment_product5406_specific_input

    @payment_product5406_specific_input.setter
    def payment_product5406_specific_input(self, value: Optional[RedirectPaymentProduct5406SpecificInput]) -> None:
        self.__payment_product5406_specific_input = value

    @property
    def payment_product5408_specific_input(self) -> Optional[RedirectPaymentProduct5408SpecificInput]:
        """
        | Object containing specific input for Account to Account payments (Payment product ID 5408)

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_product5408_specific_input.RedirectPaymentProduct5408SpecificInput`
        """
        return self.__payment_product5408_specific_input

    @payment_product5408_specific_input.setter
    def payment_product5408_specific_input(self, value: Optional[RedirectPaymentProduct5408SpecificInput]) -> None:
        self.__payment_product5408_specific_input = value

    @property
    def payment_product5410_specific_input(self) -> Optional[RedirectPaymentProduct5410SpecificInput]:
        """
        | iDealin3 (payment product 5410) specific details

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_product5410_specific_input.RedirectPaymentProduct5410SpecificInput`
        """
        return self.__payment_product5410_specific_input

    @payment_product5410_specific_input.setter
    def payment_product5410_specific_input(self, value: Optional[RedirectPaymentProduct5410SpecificInput]) -> None:
        self.__payment_product5410_specific_input = value

    @property
    def payment_product809_specific_input(self) -> Optional[RedirectPaymentProduct809SpecificInput]:
        """
        | Deprecated, this is no longer used.

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_product809_specific_input.RedirectPaymentProduct809SpecificInput`
        """
        return self.__payment_product809_specific_input

    @payment_product809_specific_input.setter
    def payment_product809_specific_input(self, value: Optional[RedirectPaymentProduct809SpecificInput]) -> None:
        self.__payment_product809_specific_input = value

    @property
    def payment_product840_specific_input(self) -> Optional[RedirectPaymentProduct840SpecificInput]:
        """
        | Object containing specific input required for PayPal payments (Payment product ID 840)

        Type: :class:`onlinepayments.sdk.domain.redirect_payment_product840_specific_input.RedirectPaymentProduct840SpecificInput`
        """
        return self.__payment_product840_specific_input

    @payment_product840_specific_input.setter
    def payment_product840_specific_input(self, value: Optional[RedirectPaymentProduct840SpecificInput]) -> None:
        self.__payment_product840_specific_input = value

    @property
    def payment_product_id(self) -> Optional[int]:
        """
        | Payment product identifier - Please see Products documentation for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: Optional[int]) -> None:
        self.__payment_product_id = value

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
    def requires_approval(self) -> Optional[bool]:
        """
        * true = the payment requires approval before the funds will be captured using the Approve payment or Capture payment API
        * false = the payment does not require approval, and the funds will be captured automatically

        Type: bool
        """
        return self.__requires_approval

    @requires_approval.setter
    def requires_approval(self, value: Optional[bool]) -> None:
        self.__requires_approval = value

    @property
    def token(self) -> Optional[str]:
        """
        | ID of the token to use to create the payment.

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value: Optional[str]) -> None:
        self.__token = value

    @property
    def tokenize(self) -> Optional[bool]:
        """
        | Indicates if this transaction should be tokenized
        
        * true - Tokenize the transaction.
        * false - Do not tokenize the transaction, unless it would be tokenized by other means such as auto-tokenization of recurring payments.

        Type: bool
        """
        return self.__tokenize

    @tokenize.setter
    def tokenize(self, value: Optional[bool]) -> None:
        self.__tokenize = value

    def to_dictionary(self) -> dict:
        dictionary = super(RedirectPaymentMethodSpecificInput, self).to_dictionary()
        if self.payment_option is not None:
            dictionary['paymentOption'] = self.payment_option
        if self.payment_product3203_specific_input is not None:
            dictionary['paymentProduct3203SpecificInput'] = self.payment_product3203_specific_input.to_dictionary()
        if self.payment_product3204_specific_input is not None:
            dictionary['paymentProduct3204SpecificInput'] = self.payment_product3204_specific_input.to_dictionary()
        if self.payment_product3302_specific_input is not None:
            dictionary['paymentProduct3302SpecificInput'] = self.payment_product3302_specific_input.to_dictionary()
        if self.payment_product3306_specific_input is not None:
            dictionary['paymentProduct3306SpecificInput'] = self.payment_product3306_specific_input.to_dictionary()
        if self.payment_product5001_specific_input is not None:
            dictionary['paymentProduct5001SpecificInput'] = self.payment_product5001_specific_input.to_dictionary()
        if self.payment_product5300_specific_input is not None:
            dictionary['paymentProduct5300SpecificInput'] = self.payment_product5300_specific_input.to_dictionary()
        if self.payment_product5402_specific_input is not None:
            dictionary['paymentProduct5402SpecificInput'] = self.payment_product5402_specific_input.to_dictionary()
        if self.payment_product5403_specific_input is not None:
            dictionary['paymentProduct5403SpecificInput'] = self.payment_product5403_specific_input.to_dictionary()
        if self.payment_product5406_specific_input is not None:
            dictionary['paymentProduct5406SpecificInput'] = self.payment_product5406_specific_input.to_dictionary()
        if self.payment_product5408_specific_input is not None:
            dictionary['paymentProduct5408SpecificInput'] = self.payment_product5408_specific_input.to_dictionary()
        if self.payment_product5410_specific_input is not None:
            dictionary['paymentProduct5410SpecificInput'] = self.payment_product5410_specific_input.to_dictionary()
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

    def from_dictionary(self, dictionary: dict) -> 'RedirectPaymentMethodSpecificInput':
        super(RedirectPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'paymentOption' in dictionary:
            self.payment_option = dictionary['paymentOption']
        if 'paymentProduct3203SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct3203SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct3203SpecificInput']))
            value = RedirectPaymentProduct3203SpecificInput()
            self.payment_product3203_specific_input = value.from_dictionary(dictionary['paymentProduct3203SpecificInput'])
        if 'paymentProduct3204SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct3204SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct3204SpecificInput']))
            value = RedirectPaymentProduct3204SpecificInput()
            self.payment_product3204_specific_input = value.from_dictionary(dictionary['paymentProduct3204SpecificInput'])
        if 'paymentProduct3302SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct3302SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct3302SpecificInput']))
            value = RedirectPaymentProduct3302SpecificInput()
            self.payment_product3302_specific_input = value.from_dictionary(dictionary['paymentProduct3302SpecificInput'])
        if 'paymentProduct3306SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct3306SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct3306SpecificInput']))
            value = RedirectPaymentProduct3306SpecificInput()
            self.payment_product3306_specific_input = value.from_dictionary(dictionary['paymentProduct3306SpecificInput'])
        if 'paymentProduct5001SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct5001SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct5001SpecificInput']))
            value = RedirectPaymentProduct5001SpecificInput()
            self.payment_product5001_specific_input = value.from_dictionary(dictionary['paymentProduct5001SpecificInput'])
        if 'paymentProduct5300SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct5300SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct5300SpecificInput']))
            value = RedirectPaymentProduct5300SpecificInput()
            self.payment_product5300_specific_input = value.from_dictionary(dictionary['paymentProduct5300SpecificInput'])
        if 'paymentProduct5402SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct5402SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct5402SpecificInput']))
            value = RedirectPaymentProduct5402SpecificInput()
            self.payment_product5402_specific_input = value.from_dictionary(dictionary['paymentProduct5402SpecificInput'])
        if 'paymentProduct5403SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct5403SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct5403SpecificInput']))
            value = RedirectPaymentProduct5403SpecificInput()
            self.payment_product5403_specific_input = value.from_dictionary(dictionary['paymentProduct5403SpecificInput'])
        if 'paymentProduct5406SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct5406SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct5406SpecificInput']))
            value = RedirectPaymentProduct5406SpecificInput()
            self.payment_product5406_specific_input = value.from_dictionary(dictionary['paymentProduct5406SpecificInput'])
        if 'paymentProduct5408SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct5408SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct5408SpecificInput']))
            value = RedirectPaymentProduct5408SpecificInput()
            self.payment_product5408_specific_input = value.from_dictionary(dictionary['paymentProduct5408SpecificInput'])
        if 'paymentProduct5410SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct5410SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct5410SpecificInput']))
            value = RedirectPaymentProduct5410SpecificInput()
            self.payment_product5410_specific_input = value.from_dictionary(dictionary['paymentProduct5410SpecificInput'])
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

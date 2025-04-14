# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from onlinepayments.sdk.communication.param_request import ParamRequest
from onlinepayments.sdk.communication.request_param import RequestParam


class GetPaymentProductParams(ParamRequest):
    """
    Query parameters for Get payment product
    """

    __country_code: Optional[str] = None
    __currency_code: Optional[str] = None
    __locale: Optional[str] = None
    __amount: Optional[int] = None
    __is_recurring: Optional[bool] = None
    __hide: Optional[List[str]] = None

    @property
    def country_code(self) -> Optional[str]:
        """
        | ISO 3166-1 alpha-2 country code of the transaction

        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value: Optional[str]) -> None:
        self.__country_code = value

    @property
    def currency_code(self) -> Optional[str]:
        """
        | Three-letter ISO currency code representing the currency for the amount

        Type: str
        """
        return self.__currency_code

    @currency_code.setter
    def currency_code(self, value: Optional[str]) -> None:
        self.__currency_code = value

    @property
    def locale(self) -> Optional[str]:
        """
        | Locale used in the GUI towards the consumer.

        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value: Optional[str]) -> None:
        self.__locale = value

    @property
    def amount(self) -> Optional[int]:
        """
        | Whole amount in cents (not containing any decimals)

        Type: int
        """
        return self.__amount

    @amount.setter
    def amount(self, value: Optional[int]) -> None:
        self.__amount = value

    @property
    def is_recurring(self) -> Optional[bool]:
        """
        | This allows you to filter payment products based on their support for recurring payments.
        
        * true - return only payment products that support recurring payments,
        * false - return all payment products that support one-time transactions. Payment products that support recurring products are usually also part of this list.

        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value: Optional[bool]) -> None:
        self.__is_recurring = value

    @property
    def hide(self) -> Optional[List[str]]:
        """
        | Allows you to hide elements from the response, reducing the amount of data that needs to be returned to your client. Possible options are:
        
        * fields - Do not return any data on fields of the payment product
        * accountsOnFile - Do not return any accounts on file data
        * translations - Do not return any label texts associated with the payment products
        * productsWithoutFields - Do not return products that require any additional data to be captured
        * productsWithoutInstructions - Do not return products that show instructions
        * productsWithRedirects - Do not return products that require a redirect to a 3rd party. Note that products that involve potential redirects related to 3D Secure authentication are not hidden

        Type: list[str]
        """
        return self.__hide

    @hide.setter
    def hide(self, value: Optional[List[str]]) -> None:
        self.__hide = value

    def add_hide(self, value: str) -> None:
        """
        :param value: str
        """
        if self.hide is None:
            self.hide = []
        self.hide.append(value)

    def to_request_parameters(self) -> List[RequestParam]:
        """
        :return: list[RequestParam]
        """
        result = []
        if self.country_code is not None:
            result.append(RequestParam("countryCode", self.country_code))
        if self.currency_code is not None:
            result.append(RequestParam("currencyCode", self.currency_code))
        if self.locale is not None:
            result.append(RequestParam("locale", self.locale))
        if self.amount is not None:
            result.append(RequestParam("amount", str(self.amount)))
        if self.is_recurring is not None:
            result.append(RequestParam("isRecurring", str(self.is_recurring)))
        if self.hide is not None:
            for hide_element in self.hide:
                if hide_element is not None:
                    result.append(RequestParam("hide", hide_element))
        return result

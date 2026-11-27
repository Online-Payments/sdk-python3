#
# This file was automatically generated.
#
from onlinepayments.sdk.communication.param_request import ParamRequest
from onlinepayments.sdk.communication.request_param import RequestParam


class GetPaymentProductNetworksParams(ParamRequest):
    """
    Query parameters for Get payment product networks
    """

    __country_code: str | None = None
    __currency_code: str | None = None
    __amount: int | None = None
    __is_recurring: bool | None = None

    @property
    def country_code(self) -> str | None:
        """
        | ISO 3166-1 alpha-2 country code

        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value: str | None) -> None:
        self.__country_code = value

    @property
    def currency_code(self) -> str | None:
        """
        | Three-letter ISO currency code representing the currency for the amount

        Type: str
        """
        return self.__currency_code

    @currency_code.setter
    def currency_code(self, value: str | None) -> None:
        self.__currency_code = value

    @property
    def amount(self) -> int | None:
        """
        | Amount in cents and always having 2 decimals

        Type: int
        """
        return self.__amount

    @amount.setter
    def amount(self, value: int | None) -> None:
        self.__amount = value

    @property
    def is_recurring(self) -> bool | None:
        """
        | This allows you to filter networks based on their support for recurring or not
        
        * true
        * false

        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value: bool | None) -> None:
        self.__is_recurring = value

    def to_request_parameters(self) -> list[RequestParam]:
        """
        :return: list[RequestParam]
        """
        result = []
        if self.country_code is not None:
            result.append(RequestParam("countryCode", self.country_code))
        if self.currency_code is not None:
            result.append(RequestParam("currencyCode", self.currency_code))
        if self.amount is not None:
            result.append(RequestParam("amount", str(self.amount)))
        if self.is_recurring is not None:
            result.append(RequestParam("isRecurring", str(self.is_recurring)))
        return result

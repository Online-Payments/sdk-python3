#
# This file was automatically generated.
#
from onlinepayments.sdk.communication.param_request import ParamRequest
from onlinepayments.sdk.communication.request_param import RequestParam


class GetProductDirectoryParams(ParamRequest):
    """
    Query parameters for Get payment product directory
    """

    __country_code: str | None = None
    __currency_code: str | None = None

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
        | Three-letter ISO currency code representing the currency of the transaction

        Type: str
        """
        return self.__currency_code

    @currency_code.setter
    def currency_code(self, value: str | None) -> None:
        self.__currency_code = value

    def to_request_parameters(self) -> list[RequestParam]:
        """
        :return: list[RequestParam]
        """
        result = []
        if self.country_code is not None:
            result.append(RequestParam("countryCode", self.country_code))
        if self.currency_code is not None:
            result.append(RequestParam("currencyCode", self.currency_code))
        return result

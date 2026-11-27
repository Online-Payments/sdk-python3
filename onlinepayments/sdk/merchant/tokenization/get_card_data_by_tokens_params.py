#
# This file was automatically generated.
#
from onlinepayments.sdk.communication.param_request import ParamRequest
from onlinepayments.sdk.communication.request_param import RequestParam


class GetCardDataByTokensParams(ParamRequest):
    """
    Query parameters for Get sensitive card details by card alias tokens
    """

    __tokens: list[str] | None = None

    @property
    def tokens(self) -> list[str] | None:
        """
        | This object contains the details for detokenizing a payment token.

        Type: list[str]
        """
        return self.__tokens

    @tokens.setter
    def tokens(self, value: list[str] | None) -> None:
        self.__tokens = value

    def add_tokens(self, value: str) -> None:
        """
        :param value: str
        """
        if self.tokens is None:
            self.tokens = []
        self.tokens.append(value)

    def to_request_parameters(self) -> list[RequestParam]:
        """
        :return: list[RequestParam]
        """
        result = []
        if self.tokens is not None:
            for tokens_element in self.tokens:
                if tokens_element is not None:
                    result.append(RequestParam("tokens", tokens_element))
        return result

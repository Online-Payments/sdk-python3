#
# This file was automatically generated.
#
from onlinepayments.sdk.communication.param_request import ParamRequest
from onlinepayments.sdk.communication.request_param import RequestParam


class GetPaymentLinksInBulkParams(ParamRequest):
    """
    Query parameters for Get payment links
    """

    __operation_group_reference: str | None = None

    @property
    def operation_group_reference(self) -> str | None:
        """
        Type: str
        """
        return self.__operation_group_reference

    @operation_group_reference.setter
    def operation_group_reference(self, value: str | None) -> None:
        self.__operation_group_reference = value

    def to_request_parameters(self) -> list[RequestParam]:
        """
        :return: list[RequestParam]
        """
        result = []
        if self.operation_group_reference is not None:
            result.append(RequestParam("operationGroupReference", self.operation_group_reference))
        return result

# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from onlinepayments.sdk.communication.param_request import ParamRequest
from onlinepayments.sdk.communication.request_param import RequestParam


class GetPaymentLinksInBulkParams(ParamRequest):
    """
    Query parameters for Get payment links
    """

    __operation_group_reference: Optional[str] = None

    @property
    def operation_group_reference(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__operation_group_reference

    @operation_group_reference.setter
    def operation_group_reference(self, value: Optional[str]) -> None:
        self.__operation_group_reference = value

    def to_request_parameters(self) -> List[RequestParam]:
        """
        :return: list[RequestParam]
        """
        result = []
        if self.operation_group_reference is not None:
            result.append(RequestParam("operationGroupReference", self.operation_group_reference))
        return result

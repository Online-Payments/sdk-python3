# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from onlinepayments.sdk.communication.param_request import ParamRequest
from onlinepayments.sdk.communication.request_param import RequestParam


class GetPrivacyPolicyParams(ParamRequest):
    """
    Query parameters for Get Privacy Policy
    """

    __locale: Optional[str] = None
    __payment_product_id: Optional[int] = None

    @property
    def locale(self) -> Optional[str]:
        """
        | Locale in which the privacy policy will be returned.

        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value: Optional[str]) -> None:
        self.__locale = value

    @property
    def payment_product_id(self) -> Optional[int]:
        """
        | ID of the specific payment product for which you wish to retrieve the privacy policy. When none is provided you will receive a complete policy for all the payment methods available for the specified merchantId.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value: Optional[int]) -> None:
        self.__payment_product_id = value

    def to_request_parameters(self) -> List[RequestParam]:
        """
        :return: list[RequestParam]
        """
        result = []
        if self.locale is not None:
            result.append(RequestParam("locale", self.locale))
        if self.payment_product_id is not None:
            result.append(RequestParam("paymentProductId", str(self.payment_product_id)))
        return result

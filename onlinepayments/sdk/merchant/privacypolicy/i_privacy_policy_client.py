# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from abc import ABC, abstractmethod
from typing import Optional

from .get_privacy_policy_params import GetPrivacyPolicyParams

from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.domain.get_privacy_policy_response import GetPrivacyPolicyResponse


class IPrivacyPolicyClient(ABC):
    """
    PrivacyPolicy client interface. Thread-safe.
    """

    @abstractmethod
    def get_privacy_policy(self, query: GetPrivacyPolicyParams, context: Optional[CallContext] = None) -> GetPrivacyPolicyResponse:
        """
        Resource /v2/{merchantId}/services/privacypolicy - Get Privacy Policy

        :param query:    :class:`onlinepayments.sdk.merchant.privacypolicy.get_privacy_policy_params.GetPrivacyPolicyParams`
        :param context:  :class:`onlinepayments.sdk.call_context.CallContext`
        :return: :class:`onlinepayments.sdk.domain.get_privacy_policy_response.GetPrivacyPolicyResponse`
        :raise IdempotenceException: if an idempotent request caused a conflict (HTTP status code 409)
        :raise ValidationException: if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise AuthorizationException: if the request was not allowed (HTTP status code 403)
        :raise ReferenceException: if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise PlatformException: if something went wrong at the payment platform,
                   the payment platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise ApiException: if the payment platform returned any other error
        """

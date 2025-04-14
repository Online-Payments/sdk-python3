# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Mapping, Optional

from .get_privacy_policy_params import GetPrivacyPolicyParams
from .i_privacy_policy_client import IPrivacyPolicyClient

from onlinepayments.sdk.api_resource import ApiResource
from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.communication.response_exception import ResponseException
from onlinepayments.sdk.domain.error_response import ErrorResponse
from onlinepayments.sdk.domain.get_privacy_policy_response import GetPrivacyPolicyResponse
from onlinepayments.sdk.exception_factory import create_exception


class PrivacyPolicyClient(ApiResource, IPrivacyPolicyClient):
    """
    PrivacyPolicy client. Thread-safe.
    """

    def __init__(self, parent: ApiResource, path_context: Optional[Mapping[str, str]]):
        """
        :param parent:       :class:`onlinepayments.sdk.api_resource.ApiResource`
        :param path_context: Mapping[str, str]
        """
        super(PrivacyPolicyClient, self).__init__(parent=parent, path_context=path_context)

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
        uri = self._instantiate_uri("/v2/{merchantId}/services/privacypolicy", None)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    GetPrivacyPolicyResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

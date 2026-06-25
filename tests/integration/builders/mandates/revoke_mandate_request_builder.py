from onlinepayments.sdk.domain.revoke_mandate_request import RevokeMandateRequest


class RevokeMandateRequestBuilder:

    def __init__(self):
        self._revocation_reason = "userAction"

    def with_revocation_reason(self, revocation_reason):
        self._revocation_reason = revocation_reason
        return self

    def build(self):
        request = RevokeMandateRequest()
        request.revocation_reason = self._revocation_reason

        return request

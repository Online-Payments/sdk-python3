from onlinepayments.sdk.domain.create_hosted_fields_session_request import CreateHostedFieldsSessionRequest


class CreateHostedFieldsSessionRequestBuilder:

    def __init__(self):
        self._locale = "en_US"
        self._tokens = None

    def with_locale(self, locale):
        self._locale = locale
        return self

    def with_tokens(self, tokens):
        self._tokens = tokens
        return self

    def build(self):
        request = CreateHostedFieldsSessionRequest()
        request.locale = self._locale
        if self._tokens is not None:
            request.tokens = self._tokens

        return request

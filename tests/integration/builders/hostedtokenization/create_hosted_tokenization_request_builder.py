from onlinepayments.sdk.domain.create_hosted_tokenization_request import CreateHostedTokenizationRequest


class CreateHostedTokenizationRequestBuilder:

    def __init__(self):
        self._ask_consumer_consent = True
        self._locale = "en_US"
        self._tokens = []

    def with_ask_consumer_consent(self, ask_consumer_consent):
        self._ask_consumer_consent = ask_consumer_consent
        return self

    def with_locale(self, locale):
        self._locale = locale
        return self

    def with_token(self, token):
        self._tokens.append(token)
        return self

    def with_tokens(self, *tokens):
        self._tokens = list(tokens)
        return self

    def build(self):
        request = CreateHostedTokenizationRequest()
        request.ask_consumer_consent = self._ask_consumer_consent
        request.locale = self._locale
        request.tokens = ",".join(self._tokens) if self._tokens else None

        return request

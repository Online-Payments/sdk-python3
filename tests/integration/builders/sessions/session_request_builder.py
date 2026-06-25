from onlinepayments.sdk.domain.session_request import SessionRequest


class SessionRequestBuilder:

    def __init__(self):
        self._tokens = []

    def with_token(self, token):
        self._tokens.append(token)
        return self

    def with_tokens(self, *tokens):
        self._tokens = list(tokens)
        return self

    def build(self):
        request = SessionRequest()
        request.tokens = None if not self._tokens else self._tokens

        return request

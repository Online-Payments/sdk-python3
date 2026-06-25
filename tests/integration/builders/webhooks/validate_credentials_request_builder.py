from onlinepayments.sdk.domain.validate_credentials_request import ValidateCredentialsRequest


class ValidateCredentialsRequestBuilder:

    def __init__(self):
        self._key = None
        self._secret = None

    def with_key(self, key):
        self._key = key
        return self

    def with_secret(self, secret):
        self._secret = secret
        return self

    def build(self):
        request = ValidateCredentialsRequest()

        if self._key is not None:
            request.key = self._key

        if self._secret is not None:
            request.secret = self._secret

        return request

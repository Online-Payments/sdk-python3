from onlinepayments.sdk.domain.send_test_request import SendTestRequest


class SendTestRequestBuilder:

    def __init__(self):
        self._url = None

    def with_url(self, url):
        self._url = url
        return self

    def build(self):
        request = SendTestRequest()

        if self._url is not None:
            request.url = self._url

        return request

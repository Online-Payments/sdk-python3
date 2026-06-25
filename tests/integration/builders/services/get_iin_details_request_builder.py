from onlinepayments.sdk.domain.get_iin_details_request import GetIINDetailsRequest


class GetIINDetailsRequestBuilder:

    def __init__(self):
        self._bin = "401200"

    def with_bin(self, bin_value):
        self._bin = bin_value
        return self

    def build(self):
        request = GetIINDetailsRequest()
        request.bin = self._bin

        return request

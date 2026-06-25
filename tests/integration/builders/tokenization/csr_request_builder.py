from onlinepayments.sdk.domain.csr_request import CsrRequest

VALID_CSR = (
    "-----BEGIN CERTIFICATE REQUEST-----\n"
    "MIICljCCAX4CAQAwDQYJKoZIhvcNAQEBBQAwDTELMAkGA1UEAwwCQ0EwggEiMA0G\n"
    "CSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCQfbsVzv0L8pKH2l8q6EJf0fzxnDlW\n"
    "-----END CERTIFICATE REQUEST-----"
)

class CsrRequestBuilder:

    def __init__(self):
        self._csr = VALID_CSR

    def with_csr(self, csr):
        self._csr = csr
        return self

    def build(self):
        request = CsrRequest()
        request.csr = self._csr

        return request

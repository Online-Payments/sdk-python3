import os
import unittest

from onlinepayments.sdk.communication.request_header import RequestHeader
from onlinepayments.sdk.webhooks.in_memory_secret_key_store import InMemorySecretKeyStore
from onlinepayments.sdk.webhooks.secret_key_not_available_exception import SecretKeyNotAvailableException
from onlinepayments.sdk.webhooks.signature_validation_exception import SignatureValidationException
from onlinepayments.sdk.webhooks.signature_validator import SignatureValidator

from tests import file_utils


SIGNATURE_HEADER = "X-GCS-Signature"
SIGNATURE = "2S7doBj/GnJnacIjSJzr5fxGM5xmfQyFAwxv1I53ZEk="
KEY_ID_HEADER = "X-GCS-KeyId"
KEY_ID = "dummy-key-id"
SECRET_KEY = "hello+world"


def _read_resource(resource):
    output = file_utils.read_file(os.path.join("webhooks", resource))
    output = output.replace("\r", "")
    return str.encode(output)


def _valid_headers():
    return [
        RequestHeader(SIGNATURE_HEADER, SIGNATURE),
        RequestHeader(KEY_ID_HEADER, KEY_ID),
    ]


class SignatureValidatorTest(unittest.TestCase):

    def setUp(self):
        InMemorySecretKeyStore.instance().clear()
        self._store = InMemorySecretKeyStore.instance()
        self._validator = SignatureValidator(self._store)

    def tearDown(self):
        InMemorySecretKeyStore.instance().clear()

    def test_Constructing_DefaultScenario_ThrowWhenSecretKeyStoreIsNull(self):
        with self.assertRaises(ValueError):
            SignatureValidator(None)

    def test_Constructing_DefaultScenario_StoreSecretKeyStore(self):
        self.assertIs(self._store, self._validator.secret_key_store)

    def test_ValidatingSignature_FromByteArray_NotThrowWhenRequestIsValid(self):
        self._store.store_secret_key(KEY_ID, SECRET_KEY)
        body = _read_resource("valid-body")
        self._validator.validate(body, _valid_headers())

    def test_ValidatingSignature_FromByteArray_ThrowSecretKeyNotAvailableExceptionWhenSecretKeyIsMissing(self):
        body = _read_resource("valid-body")
        with self.assertRaises(SecretKeyNotAvailableException) as ctx:
            self._validator.validate(body, _valid_headers())
        self.assertEqual(KEY_ID, ctx.exception.key_id)

    def test_ValidatingSignature_FromByteArray_ThrowSignatureValidationExceptionWhenHeadersAreMissing(self):
        self._store.store_secret_key(KEY_ID, SECRET_KEY)
        body = _read_resource("valid-body")
        with self.assertRaises(SignatureValidationException):
            self._validator.validate(body, [])

    def test_ValidatingSignature_FromByteArray_ThrowSignatureValidationExceptionWhenHeadersAreDuplicated(self):
        self._store.store_secret_key(KEY_ID, SECRET_KEY)
        body = _read_resource("valid-body")
        headers = [
            RequestHeader(SIGNATURE_HEADER, SIGNATURE),
            RequestHeader(KEY_ID_HEADER, KEY_ID),
            RequestHeader(SIGNATURE_HEADER, SIGNATURE + "1"),
        ]
        with self.assertRaises(SignatureValidationException):
            self._validator.validate(body, headers)

    def test_ValidatingSignature_FromByteArray_ThrowSignatureValidationExceptionWhenBodyIsInvalid(self):
        self._store.store_secret_key(KEY_ID, SECRET_KEY)
        body = _read_resource("invalid-body")
        with self.assertRaises(SignatureValidationException):
            self._validator.validate(body, _valid_headers())

    def test_ValidatingSignature_FromByteArray_ThrowSignatureValidationExceptionWhenSecretKeyIsInvalid(self):
        self._store.store_secret_key(KEY_ID, "1" + SECRET_KEY)
        body = _read_resource("valid-body")
        with self.assertRaises(SignatureValidationException):
            self._validator.validate(body, _valid_headers())

    def test_ValidatingSignature_FromByteArray_ThrowSignatureValidationExceptionWhenSignatureIsInvalid(self):
        self._store.store_secret_key(KEY_ID, SECRET_KEY)
        body = _read_resource("valid-body")
        headers = [
            RequestHeader(SIGNATURE_HEADER, "1" + SIGNATURE),
            RequestHeader(KEY_ID_HEADER, KEY_ID),
        ]
        with self.assertRaises(SignatureValidationException):
            self._validator.validate(body, headers)


if __name__ == '__main__':
    unittest.main()

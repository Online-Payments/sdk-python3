import os
import unittest

from mockito import mock, when

from tests import file_utils

from onlinepayments.sdk.communication.request_header import RequestHeader
from onlinepayments.sdk.domain.web_hooks_event import WebhooksEvent
from onlinepayments.sdk.json.default_marshaller import DefaultMarshaller
from onlinepayments.sdk.json.marshaller import Marshaller
from onlinepayments.sdk.webhooks.api_version_mismatch_exception import ApiVersionMismatchException
from onlinepayments.sdk.webhooks.in_memory_secret_key_store import InMemorySecretKeyStore
from onlinepayments.sdk.webhooks.secret_key_not_available_exception import SecretKeyNotAvailableException
from onlinepayments.sdk.webhooks.signature_validation_exception import SignatureValidationException
from onlinepayments.sdk.webhooks.webhooks_helper import WebhooksHelper


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


def _create_helper(marshaller=None):
    if marshaller is None:
        marshaller = DefaultMarshaller.instance()
    return WebhooksHelper(marshaller, InMemorySecretKeyStore.instance())


class WebhooksHelperTest(unittest.TestCase):

    def setUp(self):
        InMemorySecretKeyStore.instance().clear()

    def tearDown(self):
        InMemorySecretKeyStore.instance().clear()

    def test_UnmarshallingEvent_DefaultScenario_ThrowApiVersionMismatchExceptionWhenApiVersionDoesNotMatch(self):
        marshaller = mock(Marshaller)
        event = WebhooksEvent()
        event.api_version = "v0"
        body = _read_resource("valid-body")
        when(marshaller).unmarshal(body.decode("utf-8"), WebhooksEvent).thenReturn(event)
        helper = _create_helper(marshaller)
        InMemorySecretKeyStore.instance().store_secret_key(KEY_ID, SECRET_KEY)

        with self.assertRaises(ApiVersionMismatchException) as ctx:
            helper.unmarshal(body, _valid_headers())

        self.assertEqual("v0", ctx.exception.event_api_version)
        self.assertEqual("v1", ctx.exception.sdk_api_version)

    def test_UnmarshallingEvent_FromByteArray_ReturnValidEventWhenRequestIsValid(self):
        helper = _create_helper()
        InMemorySecretKeyStore.instance().store_secret_key(KEY_ID, SECRET_KEY)
        body = _read_resource("valid-body")

        event = helper.unmarshal(body, _valid_headers())

        self.assertEqual("v1", event.api_version)
        self.assertEqual("8ee793f6-4553-4749-85dc-f2ef095c5ab0", event.id)
        self.assertEqual("2017-02-02T11:24:14.040+0100", event.created)
        self.assertEqual("20000", event.merchant_id)
        self.assertEqual("payment.paid", event.type)

    def test_UnmarshallingEvent_FromByteArray_ThrowSecretKeyNotAvailableExceptionWhenSecretKeyIsMissing(self):
        helper = _create_helper()
        body = _read_resource("valid-body")
        with self.assertRaises(SecretKeyNotAvailableException) as ctx:
            helper.unmarshal(body, _valid_headers())
        self.assertEqual(KEY_ID, ctx.exception.key_id)

    def test_UnmarshallingEvent_FromByteArray_ThrowSignatureValidationExceptionWhenHeadersAreMissing(self):
        helper = _create_helper()
        InMemorySecretKeyStore.instance().store_secret_key(KEY_ID, SECRET_KEY)
        body = _read_resource("valid-body")
        with self.assertRaises(SignatureValidationException):
            helper.unmarshal(body, [])

    def test_UnmarshallingEvent_FromByteArray_ThrowSignatureValidationExceptionWhenHeadersAreDuplicated(self):
        helper = _create_helper()
        InMemorySecretKeyStore.instance().store_secret_key(KEY_ID, SECRET_KEY)
        body = _read_resource("valid-body")
        headers = [
            RequestHeader(SIGNATURE_HEADER, SIGNATURE),
            RequestHeader(KEY_ID_HEADER, KEY_ID),
            RequestHeader(SIGNATURE_HEADER, SIGNATURE + "1"),
        ]
        with self.assertRaises(SignatureValidationException):
            helper.unmarshal(body, headers)

    def test_UnmarshallingEvent_FromByteArray_ThrowSignatureValidationExceptionWhenBodyIsInvalid(self):
        helper = _create_helper()
        InMemorySecretKeyStore.instance().store_secret_key(KEY_ID, SECRET_KEY)
        body = _read_resource("invalid-body")
        with self.assertRaises(SignatureValidationException):
            helper.unmarshal(body, _valid_headers())

    def test_UnmarshallingEvent_FromByteArray_ThrowSignatureValidationExceptionWhenSecretKeyIsInvalid(self):
        helper = _create_helper()
        InMemorySecretKeyStore.instance().store_secret_key(KEY_ID, "1" + SECRET_KEY)
        body = _read_resource("valid-body")
        with self.assertRaises(SignatureValidationException):
            helper.unmarshal(body, _valid_headers())

    def test_UnmarshallingEvent_FromByteArray_ThrowSignatureValidationExceptionWhenSignatureIsInvalid(self):
        helper = _create_helper()
        InMemorySecretKeyStore.instance().store_secret_key(KEY_ID, SECRET_KEY)
        body = _read_resource("valid-body")
        headers = [
            RequestHeader(SIGNATURE_HEADER, "1" + SIGNATURE),
            RequestHeader(KEY_ID_HEADER, KEY_ID),
        ]
        with self.assertRaises(SignatureValidationException):
            helper.unmarshal(body, headers)


if __name__ == '__main__':
    unittest.main()

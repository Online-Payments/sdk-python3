import os
import unittest
import uuid

from mockito import *

from onlinepayments.sdk.defaultimpl.default_marshaller import DefaultMarshaller
from onlinepayments.sdk.domain.web_hooks_event import WebhooksEvent
from onlinepayments.sdk.marshaller import Marshaller
from onlinepayments.sdk.request_header import RequestHeader
from onlinepayments.sdk.webhooks.api_version_mismatch_exception import ApiVersionMismatchException
from onlinepayments.sdk.webhooks.in_memory_secret_key_store import InMemorySecretKeyStore
from onlinepayments.sdk.webhooks.secret_key_not_available_exception import SecretKeyNotAvailableException
from onlinepayments.sdk.webhooks.signature_validation_exception import SignatureValidationException
from onlinepayments.sdk.webhooks.web_hooks_helper import WebhooksHelper
from tests import file_utils


class WebhooksHelperTest(unittest.TestCase):
    __SIGNATURE_HEADER = "X-GCS-Signature"
    __SIGNATURE = "e8BGs0pD+09kWQkASiLgmHQdPAFllvCicwsC7EKFcVU="
    __KEY_ID_HEADER = "X-GCS-KeyId"
    __KEY_ID = "dummy-key-id"
    __SECRET_KEY = "hello+world"
    connection = None

    def clear_public_key_cache(self):
        InMemorySecretKeyStore.INSTANCE().clear()

    def test_unmarshal_api_version_mismatch(self):
        marshaller = mock(Marshaller)
        event = WebhooksEvent()
        event.api_version = "v0"
        body = self.__read_resource("valid-body")
        when(marshaller).unmarshal(body.decode('utf-8'), WebhooksEvent).thenReturn(event)
        helper = self.__create_helper(marshaller)
        InMemorySecretKeyStore.INSTANCE().store_secret_key(self.__KEY_ID, self.__SECRET_KEY)
        request_headers = [
            RequestHeader(self.__SIGNATURE_HEADER, self.__SIGNATURE),
            RequestHeader(self.__KEY_ID_HEADER, self.__KEY_ID)]
        self.assertRaises(ApiVersionMismatchException, helper.unmarshal, body, request_headers)

    def test_unmarshal_no_secret_key_available(self):
        self.clear_public_key_cache()
        helper = self.__create_helper()
        body = self.__read_resource("valid-body")
        request_headers = [
            RequestHeader(self.__SIGNATURE_HEADER, self.__SIGNATURE),
            RequestHeader(self.__KEY_ID_HEADER, self.__KEY_ID)]
        self.assertRaises(SecretKeyNotAvailableException, helper.unmarshal, body, request_headers)

    def test_unmarshal_missing_headers(self):
        helper = self.__create_helper()
        InMemorySecretKeyStore.INSTANCE().store_secret_key(self.__KEY_ID, self.__SECRET_KEY)
        body = self.__read_resource("valid-body")
        self.assertRaises(SignatureValidationException, helper.unmarshal, body, ())

    def test_unmarshal_duplicate_headers(self):
        helper = self.__create_helper()
        InMemorySecretKeyStore.INSTANCE().store_secret_key(self.__KEY_ID, self.__SECRET_KEY)
        body = self.__read_resource("valid-body")
        request_headers = [
            RequestHeader(self.__SIGNATURE_HEADER, self.__SIGNATURE),
            RequestHeader(self.__KEY_ID_HEADER, self.__KEY_ID),
            RequestHeader(self.__SIGNATURE_HEADER, self.__SIGNATURE + "1")]
        self.assertRaises(SignatureValidationException, helper.unmarshal, body,
                          request_headers)

    def test_unmarshal_string_success(self):
        helper = self.__create_helper()
        InMemorySecretKeyStore.INSTANCE().store_secret_key(self.__KEY_ID, self.__SECRET_KEY)
        body = self.__read_resource("valid-body")
        request_headers = [
            RequestHeader(self.__SIGNATURE_HEADER, self.__SIGNATURE),
            RequestHeader(self.__KEY_ID_HEADER, self.__KEY_ID)]
        event = helper.unmarshal(body, request_headers)
        self.assertEqual("v1", event.api_version)
        self.assertEqual("8ee793f6-4553-4749-85dc-f2ef095c5ab0", event.id)
        self.assertEqual("2020-01-01T12:00:00.000+0100", event.created)
        self.assertEqual("1", event.merchant_id)
        self.assertEqual("payment.paid", event.type)

        self.assertIsNone(event.payout)
        self.assertIsNone(event.refund)
        self.assertIsNone(event.token)

        self.assertIsNotNone(event.payment)
        self.assertEqual("1_1", event.payment.id)
        self.assertIsNotNone(event.payment.payment_output)
        self.assertIsNotNone(event.payment.payment_output.amount_of_money)
        self.assertEqual(1000, event.payment.payment_output.amount_of_money.amount)
        self.assertEqual("EUR", event.payment.payment_output.amount_of_money.currency_code)
        self.assertIsNotNone(event.payment.payment_output.amount_of_money.currency_code)
        self.assertIsNotNone(event.payment.payment_output.references)
        self.assertEqual("12345", event.payment.payment_output.references.merchant_reference)
        self.assertEqual("card", event.payment.payment_output.payment_method)

        self.assertIsNotNone(event.payment.payment_output.card_payment_method_specific_output)
        self.assertIsNone(event.payment.payment_output.redirect_payment_method_specific_output)
        self.assertIsNone(event.payment.payment_output.sepa_direct_debit_payment_method_specific_output)
        self.assertEqual(1, event.payment.payment_output.card_payment_method_specific_output.payment_product_id)

        self.assertEqual("CAPTURED", event.payment.status)
        self.assertIsNotNone(event.payment.status_output)
        self.assertEqual(False, event.payment.status_output.is_cancellable)
        self.assertEqual("COMPLETED", event.payment.status_output.status_category)
        self.assertEqual(9, event.payment.status_output.status_code)
        self.assertEqual("20200101120000", event.payment.status_output.status_code_change_date_time)
        self.assertEqual(True, event.payment.status_output.is_authorized)

    def test_unmarshal_string_invalid_body(self):
        helper = self.__create_helper()
        InMemorySecretKeyStore.INSTANCE().store_secret_key(self.__KEY_ID, self.__SECRET_KEY)

        body = self.__read_resource("invalid-body")
        request_headers = [
            RequestHeader(self.__SIGNATURE_HEADER, self.__SIGNATURE),
            RequestHeader(self.__KEY_ID_HEADER, self.__KEY_ID)]
        self.assertRaises(SignatureValidationException, helper.unmarshal, body, request_headers)

    def test_unmarshal_string_invalid_secret_key(self):
        helper = self.__create_helper()
        invalid_secret_key = "1"
        InMemorySecretKeyStore.INSTANCE().store_secret_key(self.__KEY_ID, invalid_secret_key)
        body = self.__read_resource("valid-body")
        request_headers = [
            RequestHeader(self.__SIGNATURE_HEADER, self.__SIGNATURE),
            RequestHeader(self.__KEY_ID_HEADER, self.__KEY_ID)]
        self.assertRaises(SignatureValidationException, helper.unmarshal, body, request_headers)

    def test_unmarshal_string_invalid_signature(self):
        helper = self.__create_helper()
        InMemorySecretKeyStore.INSTANCE().store_secret_key(self.__KEY_ID, self.__SECRET_KEY)
        body = self.__read_resource("valid-body")
        request_headers = [
            RequestHeader(self.__SIGNATURE_HEADER, "1" + self.__SIGNATURE),
            RequestHeader(self.__KEY_ID_HEADER, self.__KEY_ID)]
        self.assertRaises(SignatureValidationException, helper.unmarshal, body, request_headers)

    def __read_resource(self, resource):
        output = file_utils.read_file(os.path.join("webhooks", resource))
        output = output.replace("\r", "")
        return str.encode(output)

    def test_are_equal_signatures_equal(self):
        signature = str(uuid.uuid4())
        large = self.__repeat(signature, 100)
        self.assertTrue(WebhooksHelper.are_equal_signatures(signature, signature))
        self.assertTrue(WebhooksHelper.are_equal_signatures(large, large))

    def test_are_equal_signatures_not_equal(self):
        signature = str(uuid.uuid4())
        large = self.__repeat(signature, 100)
        self.assertFalse(WebhooksHelper.are_equal_signatures("abc", signature))
        self.assertFalse(WebhooksHelper.are_equal_signatures(signature, "abc"))
        self.assertFalse(WebhooksHelper.are_equal_signatures(signature, signature + "1"))
        self.assertFalse(WebhooksHelper.are_equal_signatures(signature + "1", signature))
        self.assertFalse(WebhooksHelper.are_equal_signatures(signature.lower(), signature.upper()))
        self.assertFalse(WebhooksHelper.are_equal_signatures(signature.upper(), signature.lower()))

        self.assertFalse(WebhooksHelper.are_equal_signatures("abc", large))
        self.assertFalse(WebhooksHelper.are_equal_signatures(large, "abc"))
        self.assertFalse(WebhooksHelper.are_equal_signatures(large + "1", large))
        self.assertFalse(WebhooksHelper.are_equal_signatures(large, large + "1"))
        self.assertFalse(WebhooksHelper.are_equal_signatures(large.lower(), large.upper()))
        self.assertFalse(WebhooksHelper.are_equal_signatures(large.upper(), large.lower()))

        self.assertFalse(WebhooksHelper.are_equal_signatures(signature, large))
        self.assertFalse(WebhooksHelper.are_equal_signatures(large, signature))

    def __repeat(self, s, times):
        return s * times

    def __create_helper(self, marshaller=DefaultMarshaller.INSTANCE()):
        return WebhooksHelper(marshaller, InMemorySecretKeyStore.INSTANCE())

    if __name__ == '__main__':
        unittest.main()

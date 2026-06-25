import gzip
import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer

from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.communication.multipart_form_data_object import MultipartFormDataObject
from onlinepayments.sdk.communicator_configuration import CommunicatorConfiguration
from onlinepayments.sdk.factory import Factory
from onlinepayments.sdk.domain.data_object import DataObject
from onlinepayments.sdk.json.default_marshaller import DefaultMarshaller


class GzipTestRequestHandler(BaseHTTPRequestHandler):
    last_content_encoding = None
    last_decoded_body = None
    last_raw_body = None
    last_path = None
    last_method = None

    def do_POST(self):
        content_length_header = self.headers.get("Content-Length") or "0"
        content_length = int(content_length_header)
        raw_body = self.rfile.read(content_length)
        content_encoding = self.headers.get("Content-Encoding")

        if content_encoding == "gzip":
            decoded_body = gzip.decompress(raw_body).decode("utf-8")
        else:
            decoded_body = raw_body.decode("utf-8")

        GzipTestRequestHandler.last_content_encoding = content_encoding
        GzipTestRequestHandler.last_decoded_body = decoded_body
        GzipTestRequestHandler.last_raw_body = raw_body
        GzipTestRequestHandler.last_path = self.path
        GzipTestRequestHandler.last_method = self.command

        response_payload = json.dumps(
            {
                "status": "ok",
                "contentEncoding": content_encoding,
                "decodedBody": decoded_body,
            }
        ).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response_payload)))
        self.end_headers()
        self.wfile.write(response_payload)

    def log_message(self, format_string, *args):
        return


class GzipTestHeader(DataObject):
    def __init__(self, operation_type=None, item_count=None):
        self.operation_type = operation_type
        self.item_count = item_count

    def to_dictionary(self):
        dictionary = super(GzipTestHeader, self).to_dictionary()
        if self.operation_type is not None:
            dictionary["operationType"] = self.operation_type
        if self.item_count is not None:
            dictionary["itemCount"] = self.item_count
        return dictionary


class GzipTestItem(DataObject):
    def __init__(self, amount=None, currency_code=None):
        self.amount = amount
        self.currency_code = currency_code

    def to_dictionary(self):
        dictionary = super(GzipTestItem, self).to_dictionary()
        if self.amount is not None:
            dictionary["amount"] = self.amount
        if self.currency_code is not None:
            dictionary["currencyCode"] = self.currency_code
        return dictionary


class GzipTestRequest(DataObject):
    def __init__(self, header=None, items=None):
        self.header = header
        self.items = items or []

    def to_dictionary(self):
        dictionary = super(GzipTestRequest, self).to_dictionary()
        if self.header is not None:
            dictionary["header"] = self.header.to_dictionary()
        if self.items is not None:
            dictionary["items"] = [item.to_dictionary() for item in self.items]
        return dictionary


class GzipTestResponse(DataObject):
    status = None

    def from_dictionary(self, dictionary):
        super(GzipTestResponse, self).from_dictionary(dictionary)
        if "status" in dictionary:
            self.status = dictionary["status"]
        return self


class DefaultGzipRequestTest(unittest.TestCase):

    def setUp(self):
        GzipTestRequestHandler.last_content_encoding = None
        GzipTestRequestHandler.last_decoded_body = None
        GzipTestRequestHandler.last_raw_body = None
        GzipTestRequestHandler.last_path = None
        GzipTestRequestHandler.last_method = None

        self.server = HTTPServer(("localhost", 0), GzipTestRequestHandler)
        self.port = self.server.server_address[1]
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.server_thread.join()

    def _create_configuration(self):
        mock_api_endpoint = f"http://localhost:{self.port}"
        return CommunicatorConfiguration(
            None,
            mock_api_endpoint,
            "someAPIKeyId",
            "someAPISecretKey",
            "v1HMAC",
            5000,
            30000,
            1,
            None,
            "INTEGRATOR",
            None)

    def test_PostingWithGzipEnabled_DefaultScenario_SendGzipCompressedRequestBody(self):
        configuration = self._create_configuration()

        request_body = GzipTestRequest(
            header=GzipTestHeader(operation_type="CreatePayment", item_count=2),
            items=[
                GzipTestItem(amount=10000, currency_code="EUR"),
                GzipTestItem(amount=20000, currency_code="EUR"),
            ],
        )

        call_context = CallContext()
        call_context.gzip = True

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.post(
                "/gzip-request",
                None,
                None,
                request_body,
                GzipTestResponse,
                call_context,
            )

        self.assertIsInstance(response, GzipTestResponse)
        self.assertEqual(response.status, "ok")

        self.assertEqual("POST", GzipTestRequestHandler.last_method)
        self.assertEqual("/gzip-request", GzipTestRequestHandler.last_path)
        self.assertEqual("gzip", GzipTestRequestHandler.last_content_encoding)

        self.assertIsNotNone(GzipTestRequestHandler.last_decoded_body)
        self.assertNotEqual("", GzipTestRequestHandler.last_decoded_body)

        decoded_json = json.loads(GzipTestRequestHandler.last_decoded_body)
        header_node = decoded_json["header"]
        self.assertEqual("CreatePayment", header_node["operationType"])
        self.assertEqual(2, header_node["itemCount"])
        self.assertEqual(2, len(decoded_json["items"]))
        self.assertEqual(10000, decoded_json["items"][0]["amount"])
        self.assertEqual("EUR", decoded_json["items"][0]["currencyCode"])

        expected_json = json.loads(DefaultMarshaller.instance().marshal(request_body))
        self.assertEqual(expected_json, decoded_json)

        plain_json_bytes = DefaultMarshaller.instance().marshal(request_body).encode("utf-8")
        self.assertNotEqual(GzipTestRequestHandler.last_raw_body, plain_json_bytes)

    def test_PostingWithGzipDisabled_DefaultScenario_NotSendGzipHeaderWhenGzipIsDisabled(self):
        configuration = self._create_configuration()

        request_body = GzipTestRequest(
            header=GzipTestHeader(operation_type="CreatePayment", item_count=1),
            items=[GzipTestItem(amount=10000, currency_code="EUR")],
        )

        call_context = CallContext()
        call_context.gzip = False

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.post(
                "/gzip-request",
                None,
                None,
                request_body,
                GzipTestResponse,
                call_context,
            )

        self.assertIsInstance(response, GzipTestResponse)

        self.assertEqual("POST", GzipTestRequestHandler.last_method)
        self.assertEqual("/gzip-request", GzipTestRequestHandler.last_path)
        self.assertIsNone(GzipTestRequestHandler.last_content_encoding)

        decoded_json = json.loads(GzipTestRequestHandler.last_decoded_body)
        expected_json = json.loads(DefaultMarshaller.instance().marshal(request_body))
        self.assertEqual(expected_json, decoded_json)

    def test_PostingWithGzipUnset_DefaultScenario_NotSendGzipHeaderWhenGzipIsNotSet(self):
        configuration = self._create_configuration()

        request_body = GzipTestRequest(
            header=GzipTestHeader(operation_type="CreatePayment", item_count=1),
            items=[GzipTestItem(amount=10000, currency_code="EUR")],
        )

        call_context = CallContext()

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.post(
                "/gzip-request",
                None,
                None,
                request_body,
                GzipTestResponse,
                call_context,
            )

        self.assertIsInstance(response, GzipTestResponse)
        self.assertEqual("POST", GzipTestRequestHandler.last_method)
        self.assertEqual("/gzip-request", GzipTestRequestHandler.last_path)
        self.assertIsNone(GzipTestRequestHandler.last_content_encoding)

        decoded_json = json.loads(GzipTestRequestHandler.last_decoded_body)
        expected_json = json.loads(DefaultMarshaller.instance().marshal(request_body))
        self.assertEqual(expected_json, decoded_json)

    def test_PostingMultipartWithGzipEnabled_DefaultScenario_NotGzipMultipartBody(self):
        configuration = self._create_configuration()

        multipart_body = MultipartFormDataObject()
        multipart_body.add_value("operationType", "CreatePayment")

        call_context = CallContext()
        call_context.gzip = True

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.post(
                "/gzip-request",
                None,
                None,
                multipart_body,
                GzipTestResponse,
                call_context,
            )

        self.assertIsInstance(response, GzipTestResponse)
        self.assertEqual("POST", GzipTestRequestHandler.last_method)
        self.assertEqual("/gzip-request", GzipTestRequestHandler.last_path)

        self.assertIsNone(GzipTestRequestHandler.last_content_encoding)

        self.assertIn("operationType", GzipTestRequestHandler.last_decoded_body)
        self.assertIn("CreatePayment", GzipTestRequestHandler.last_decoded_body)


if __name__ == "__main__":
    unittest.main()

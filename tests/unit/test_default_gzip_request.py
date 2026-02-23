import gzip
import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer

import tests.integration.init_utils as init_utils

from onlinepayments.sdk.call_context import CallContext
from onlinepayments.sdk.factory import Factory
from onlinepayments.sdk.domain.data_object import DataObject
from onlinepayments.sdk.json.default_marshaller import DefaultMarshaller


class GzipTestRequestHandler(BaseHTTPRequestHandler):
    last_content_encoding = None
    last_decoded_body = None
    last_raw_body = None

    def do_POST(self):
        content_length_header = self.headers.get("Content-Length") or "0"
        content_length = int(content_length_header)
        raw_body = self.rfile.read(content_length)
        content_encoding = self.headers.get("Content-Encoding")

        decoded_body = ""
        if content_encoding == "gzip":
            decoded_body = gzip.decompress(raw_body).decode("utf-8")

        GzipTestRequestHandler.last_content_encoding = content_encoding
        GzipTestRequestHandler.last_decoded_body = decoded_body
        GzipTestRequestHandler.last_raw_body = raw_body

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


class GzipTestItem(DataObject):
    def __init__(self, amount=None, currency_code=None):
        self.amount = amount
        self.currency_code = currency_code


class GzipTestRequest(DataObject):
    def __init__(self, header=None, items=None):
        self.header = header
        self.items = items or []


class GzipTestResponse(DataObject):
    status = None

    def from_dictionary(self, dictionary):
        super(GzipTestResponse, self).from_dictionary(dictionary)
        if "status" in dictionary:
            self.status = dictionary["status"]
        return self


class DefaultGzipRequestTest(unittest.TestCase):
    """Tests that a request with Content-Encoding: gzip sends a compressed JSON body."""

    def setUp(self):
        self.port = 8080
        self.server = HTTPServer(("localhost", self.port), GzipTestRequestHandler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.server_thread.join()

    def test_post_with_gzip_content_encoding_sends_compressed_body(self):
        mock_api_endpoint = f"http://localhost:{self.port}"

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = mock_api_endpoint

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

        self.assertEqual("gzip", GzipTestRequestHandler.last_content_encoding)
        self.assertIsNotNone(GzipTestRequestHandler.last_decoded_body)
        self.assertNotEqual("", GzipTestRequestHandler.last_decoded_body)

        actual_json = json.loads(GzipTestRequestHandler.last_decoded_body)
        expected_json = json.loads(DefaultMarshaller.instance().marshal(request_body))

        self.assertEqual(expected_json, actual_json)

        plain_json_bytes = DefaultMarshaller.instance().marshal(request_body).encode("utf-8")
        self.assertNotEqual(GzipTestRequestHandler.last_raw_body, plain_json_bytes)

if __name__ == "__main__":
    unittest.main()

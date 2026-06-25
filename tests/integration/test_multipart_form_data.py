import json
import unittest
import responses

import tests.integration.init_utils as init_utils

from onlinepayments.sdk.factory import Factory
from onlinepayments.sdk.communication.multipart_form_data_object import MultipartFormDataObject
from onlinepayments.sdk.communication.multipart_form_data_request import MultipartFormDataRequest
from onlinepayments.sdk.domain.data_object import DataObject
from onlinepayments.sdk.domain.uploadable_file import UploadableFile

MOCK_API_ENDPOINT = "https://mock.local"

class MultipartFormDataTest(unittest.TestCase):

    @staticmethod
    def _multipart_callback(request):
        content_type = request.headers.get("Content-Type") or request.headers.get("content-type")
        body = request.body
        if isinstance(body, (bytes, bytearray)):
            body = body.decode("utf-8", errors="replace")

        assert content_type is not None and content_type.startswith("multipart/form-data"), (
            f"Unexpected Content-Type: {content_type}"
        )

        assert 'name="value"' in body, 'Missing "value" form field'
        assert "Hello World" in body, 'Missing "Hello World" value'
        assert 'name="file"' in body, 'Missing "file" form field'
        assert 'filename="file.txt"' in body, 'Missing filename "file.txt"'
        assert "file-content" in body, 'Missing file content "file-content"'

        response_body = json.dumps(
            {
                "form": {"value": "Hello World"},
                "files": {"file": "file-content"},
            }
        )
        headers = {"Content-Type": "application/json"}
        return 200, headers, response_body

    @classmethod
    def _register_multipart_stubs(cls, responses_module):

        responses_module.add_callback(
            responses.POST,
            MOCK_API_ENDPOINT + "/post",
            callback=cls._multipart_callback,
            content_type="application/json",
        )

        responses_module.add_callback(
            responses.PUT,
            MOCK_API_ENDPOINT + "/put",
            callback=cls._multipart_callback,
            content_type="application/json",
        )

    @responses.activate
    def test_post_multipart_form_data_object_returns_json_response(self):
        self._register_multipart_stubs(responses)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        communicator = Factory.create_communicator_from_configuration(configuration)
        try:
            response = communicator.post('/post', None, None, multipart, HttpBinResponse, None)
        finally:
            communicator.close()

        self.assertEqual(response.form['value'], 'Hello World')
        self.assertEqual(response.files['file'], 'file-content')

    @responses.activate
    def test_post_multipart_form_data_request_returns_json_response(self):
        self._register_multipart_stubs(responses)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        communicator = Factory.create_communicator_from_configuration(configuration)
        try:
            response = communicator.post('/post', None, None, MultipartFormDataObjectWrapper(multipart),
                                         HttpBinResponse, None)
        finally:
            communicator.close()

        self.assertEqual(response.form['value'], 'Hello World')
        self.assertEqual(response.files['file'], 'file-content')

    @responses.activate
    def test_post_with_binary_response_multipart_form_data_object_returns_binary_content(self):
        self._register_multipart_stubs(responses)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        communicator = Factory.create_communicator_from_configuration(configuration)
        try:
            response = communicator.post_with_binary_response('/post', None, None, multipart, None)
        finally:
            communicator.close()

        data = ''
        for chunk in response[1]:
            data += chunk.decode('utf-8')
        response = json.loads(data)
        self.assertEqual(response['form']['value'], 'Hello World')
        self.assertEqual(response['files']['file'], 'file-content')

    @responses.activate
    def test_post_with_binary_response_multipart_form_data_request_returns_binary_content(self):
        self._register_multipart_stubs(responses)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        communicator = Factory.create_communicator_from_configuration(configuration)
        try:
            response = communicator.post_with_binary_response('/post', None, None,
                                                              MultipartFormDataObjectWrapper(multipart), None)
        finally:
            communicator.close()

        data = ''
        for chunk in response[1]:
            data += chunk.decode('utf-8')
        response = json.loads(data)
        self.assertEqual(response['form']['value'], 'Hello World')
        self.assertEqual(response['files']['file'], 'file-content')

    @responses.activate
    def test_put_multipart_form_data_object_returns_json_response(self):
        self._register_multipart_stubs(responses)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        communicator = Factory.create_communicator_from_configuration(configuration)
        try:
            response = communicator.put('/put', None, None, multipart, HttpBinResponse, None)
        finally:
            communicator.close()

        self.assertEqual(response.form['value'], 'Hello World')
        self.assertEqual(response.files['file'], 'file-content')

    @responses.activate
    def test_put_multipart_form_data_request_returns_json_response(self):
        self._register_multipart_stubs(responses)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        communicator = Factory.create_communicator_from_configuration(configuration)
        try:
            response = communicator.put('/put', None, None, MultipartFormDataObjectWrapper(multipart), HttpBinResponse, None)
        finally:
            communicator.close()

        self.assertEqual(response.form['value'], 'Hello World')
        self.assertEqual(response.files['file'], 'file-content')

    @responses.activate
    def test_put_with_binary_response_multipart_form_data_object_returns_binary_content(self):
        self._register_multipart_stubs(responses)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        communicator = Factory.create_communicator_from_configuration(configuration)
        try:
            response = communicator.put_with_binary_response('/put', None, None, multipart, None)
        finally:
            communicator.close()

        data = ''
        for chunk in response[1]:
            data += chunk.decode('utf-8')
        response = json.loads(data)
        self.assertEqual(response['form']['value'], 'Hello World')
        self.assertEqual(response['files']['file'], 'file-content')

    @responses.activate
    def test_put_with_binary_response_multipart_form_data_request_returns_binary_content(self):
        self._register_multipart_stubs(responses)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        communicator = Factory.create_communicator_from_configuration(configuration)
        try:
            response = communicator.put_with_binary_response('/put', None, None, MultipartFormDataObjectWrapper(multipart), None)
        finally:
            communicator.close()

        data = ''
        for chunk in response[1]:
            data += chunk.decode('utf-8')
        response = json.loads(data)
        self.assertEqual(response['form']['value'], 'Hello World')
        self.assertEqual(response['files']['file'], 'file-content')

    @responses.activate
    def test_post_two_files_returns_all_files_in_response(self):
        responses.add(responses.POST, MOCK_API_ENDPOINT + "/post",
                      json={"files": {"firstFile": "firstContent", "secondFile": "secondContent"}},
                      status=200)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('firstFile', UploadableFile('first.txt', 'firstContent', 'text/plain'))
        multipart.add_file('secondFile', UploadableFile('second.txt', 'secondContent', 'text/plain'))

        communicator = Factory.create_communicator_from_configuration(configuration)
        try:
            response = communicator.post('/post', None, None, multipart, HttpBinResponse, None)
        finally:
            communicator.close()

        self.assertIsNotNone(response)
        self.assertEqual(2, len(response.files))
        self.assertEqual('firstContent', response.files['firstFile'])
        self.assertEqual('secondContent', response.files['secondFile'])

    @responses.activate
    def test_post_three_files_with_different_mime_types_returns_all_files_in_response(self):
        responses.add(responses.POST, MOCK_API_ENDPOINT + "/post",
                      json={"files": {"textFile": "text", "jsonFile": "json", "xmlFile": "xml"}},
                      status=200)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('textFile', UploadableFile('file.txt', 'text', 'text/plain'))
        multipart.add_file('jsonFile', UploadableFile('file.json', 'json', 'application/json'))
        multipart.add_file('xmlFile', UploadableFile('file.xml', 'xml', 'application/xml'))

        communicator = Factory.create_communicator_from_configuration(configuration)
        try:
            response = communicator.post('/post', None, None, multipart, HttpBinResponse, None)
        finally:
            communicator.close()

        self.assertIsNotNone(response)
        self.assertEqual(3, len(response.files))

    @responses.activate
    def test_post_two_form_values_returns_all_values_in_response(self):
        responses.add(responses.POST, MOCK_API_ENDPOINT + "/post",
                      json={"form": {"firstKey": "firstValue", "secondKey": "secondValue"}},
                      status=200)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_value('firstKey', 'firstValue')
        multipart.add_value('secondKey', 'secondValue')

        communicator = Factory.create_communicator_from_configuration(configuration)
        try:
            response = communicator.post('/post', None, None, multipart, HttpBinResponse, None)
        finally:
            communicator.close()

        self.assertIsNotNone(response)
        self.assertEqual(2, len(response.form))
        self.assertEqual('firstValue', response.form['firstKey'])
        self.assertEqual('secondValue', response.form['secondKey'])

    @responses.activate
    def test_post_three_form_values_returns_all_values_in_response(self):
        responses.add(responses.POST, MOCK_API_ENDPOINT + "/post",
                      json={"form": {"name": "John", "age": "30", "city": "NYC"}},
                      status=200)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_value('name', 'John')
        multipart.add_value('age', '30')
        multipart.add_value('city', 'NYC')

        communicator = Factory.create_communicator_from_configuration(configuration)
        try:
            response = communicator.post('/post', None, None, multipart, HttpBinResponse, None)
        finally:
            communicator.close()

        self.assertIsNotNone(response)
        self.assertEqual(3, len(response.form))

    @responses.activate
    def test_post_single_file_without_values_returns_file_in_response(self):
        responses.add(responses.POST, MOCK_API_ENDPOINT + "/post",
                      json={"files": {"document": "doc content"}},
                      status=200)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('document', UploadableFile('doc.pdf', 'doc content', 'application/pdf'))

        communicator = Factory.create_communicator_from_configuration(configuration)
        try:
            response = communicator.post('/post', None, None, multipart, HttpBinResponse, None)
        finally:
            communicator.close()

        self.assertIsNotNone(response)
        self.assertEqual('doc content', response.files['document'])

    @responses.activate
    def test_post_single_value_without_files_returns_value_in_response(self):
        responses.add(responses.POST, MOCK_API_ENDPOINT + "/post",
                      json={"form": {"message": "Hello"}},
                      status=200)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_value('message', 'Hello')

        communicator = Factory.create_communicator_from_configuration(configuration)
        try:
            response = communicator.post('/post', None, None, multipart, HttpBinResponse, None)
        finally:
            communicator.close()

        self.assertIsNotNone(response)
        self.assertEqual('Hello', response.form['message'])

    @responses.activate
    def test_post_pdf_file_returns_response(self):
        responses.add(responses.POST, MOCK_API_ENDPOINT + "/post",
                      json={"files": {"pdf": "pdf content"}},
                      status=200)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('pdf', UploadableFile('document.pdf', 'pdf content', 'application/pdf'))

        communicator = Factory.create_communicator_from_configuration(configuration)
        try:
            response = communicator.post('/post', None, None, multipart, HttpBinResponse, None)
        finally:
            communicator.close()

        self.assertIsNotNone(response)

    @responses.activate
    def test_post_image_file_returns_response(self):
        responses.add(responses.POST, MOCK_API_ENDPOINT + "/post",
                      json={"files": {"image": "image content"}},
                      status=200)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('image', UploadableFile('photo.jpg', 'image content', 'image/jpeg'))

        communicator = Factory.create_communicator_from_configuration(configuration)
        try:
            response = communicator.post('/post', None, None, multipart, HttpBinResponse, None)
        finally:
            communicator.close()

        self.assertIsNotNone(response)

    @responses.activate
    def test_post_json_file_returns_response(self):
        responses.add(responses.POST, MOCK_API_ENDPOINT + "/post",
                      json={"files": {"data": "json content"}},
                      status=200)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('data', UploadableFile('data.json', 'json content', 'application/json'))

        communicator = Factory.create_communicator_from_configuration(configuration)
        try:
            response = communicator.post('/post', None, None, multipart, HttpBinResponse, None)
        finally:
            communicator.close()

        self.assertIsNotNone(response)

    @responses.activate
    def test_post_file_with_known_content_length_returns_response(self):
        responses.add(responses.POST, MOCK_API_ENDPOINT + "/post",
                      json={"files": {"file": "content"}},
                      status=200)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'content', 'text/plain', 7))

        communicator = Factory.create_communicator_from_configuration(configuration)
        try:
            response = communicator.post('/post', None, None, multipart, HttpBinResponse, None)
        finally:
            communicator.close()

        self.assertIsNotNone(response)

    @responses.activate
    def test_post_file_with_unknown_content_length_returns_response(self):
        responses.add(responses.POST, MOCK_API_ENDPOINT + "/post",
                      json={"files": {"file": "content"}},
                      status=200)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'content', 'text/plain'))

        communicator = Factory.create_communicator_from_configuration(configuration)
        try:
            response = communicator.post('/post', None, None, multipart, HttpBinResponse, None)
        finally:
            communicator.close()

        self.assertIsNotNone(response)

    @responses.activate
    def test_add_file_with_known_content_length_stores_file_correctly(self):
        file = UploadableFile("file.txt", b"content", "text/plain", 7)
        multipart = MultipartFormDataObject()

        multipart.add_file("document", file)

        self.assertEqual(1, len(multipart.files))
        self.assertIn("document", multipart.files)
        self.assertIs(file, multipart.files["document"])

    @responses.activate
    def test_add_file_with_unknown_content_length_stores_file_with_minus_one_length(self):
        file = UploadableFile("file.txt", b"content", "text/plain")
        multipart = MultipartFormDataObject()

        multipart.add_file("document", file)

        self.assertEqual(1, len(multipart.files))
        self.assertEqual(-1, multipart.files["document"].content_length)

    @responses.activate
    def test_add_file_null_file_raises_exception(self):
        multipart = MultipartFormDataObject()

        with self.assertRaises((ValueError, TypeError, Exception)) as ctx:
            multipart.add_file("file", None)

        self.assertIsNotNone(ctx.exception)

    @responses.activate
    def test_add_file_null_parameter_name_raises_exception(self):
        file = UploadableFile("file.txt", b"content", "text/plain")
        multipart = MultipartFormDataObject()

        with self.assertRaises((ValueError, TypeError, Exception)) as ctx:
            multipart.add_file(None, file)

        self.assertIsNotNone(ctx.exception)

    @responses.activate
    def test_add_file_empty_parameter_name_raises_exception(self):
        file = UploadableFile("file.txt", b"content", "text/plain")
        multipart = MultipartFormDataObject()

        with self.assertRaises((ValueError, TypeError, Exception)) as ctx:
            multipart.add_file("", file)

        self.assertIsNotNone(ctx.exception)

    @responses.activate
    def test_add_file_duplicate_parameter_name_already_used_by_file_raises_exception(self):
        first_file = UploadableFile("first.txt", b"firstContent", "text/plain")
        second_file = UploadableFile("second.txt", b"secondContent", "text/plain")
        multipart = MultipartFormDataObject()
        multipart.add_file("document", first_file)

        with self.assertRaises((ValueError, TypeError, Exception)) as ctx:
            multipart.add_file("document", second_file)

        self.assertIsNotNone(ctx.exception)

    @responses.activate
    def test_add_file_duplicate_parameter_name_already_used_by_value_raises_exception(self):
        file = UploadableFile("file.txt", b"content", "text/plain")
        multipart = MultipartFormDataObject()
        multipart.add_value("field", "value")

        with self.assertRaises((ValueError, TypeError, Exception)) as ctx:
            multipart.add_file("field", file)

        self.assertIsNotNone(ctx.exception)

    @responses.activate
    def test_add_value_single_value_stores_value_correctly(self):
        multipart = MultipartFormDataObject()

        multipart.add_value("key", "value")

        self.assertEqual(1, len(multipart.values))
        self.assertIn("key", multipart.values)
        self.assertEqual("value", multipart.values["key"])

    @responses.activate
    def test_add_value_multiple_values_stores_all_values_correctly(self):
        multipart = MultipartFormDataObject()

        multipart.add_value("firstKey", "firstValue")
        multipart.add_value("secondKey", "secondValue")
        multipart.add_value("thirdKey", "thirdValue")

        self.assertEqual(3, len(multipart.values))
        self.assertEqual("firstValue", multipart.values["firstKey"])
        self.assertEqual("secondValue", multipart.values["secondKey"])
        self.assertEqual("thirdValue", multipart.values["thirdKey"])

    @responses.activate
    def test_add_value_null_value_raises_exception(self):
        multipart = MultipartFormDataObject()

        with self.assertRaises((ValueError, TypeError, Exception)) as ctx:
            multipart.add_value("key", None)

        self.assertIsNotNone(ctx.exception)

    @responses.activate
    def test_add_value_null_parameter_name_raises_exception(self):
        multipart = MultipartFormDataObject()

        with self.assertRaises((ValueError, TypeError, Exception)) as ctx:
            multipart.add_value(None, "value")

        self.assertIsNotNone(ctx.exception)

    @responses.activate
    def test_add_value_empty_parameter_name_raises_exception(self):
        multipart = MultipartFormDataObject()

        with self.assertRaises((ValueError, TypeError, Exception)) as ctx:
            multipart.add_value("", "value")

        self.assertIsNotNone(ctx.exception)

    @responses.activate
    def test_add_value_duplicate_parameter_name_already_used_by_value_raises_exception(self):
        multipart = MultipartFormDataObject()
        multipart.add_value("key", "value1")

        with self.assertRaises((ValueError, TypeError, Exception)) as ctx:
            multipart.add_value("key", "value2")

        self.assertIsNotNone(ctx.exception)

    @responses.activate
    def test_add_value_duplicate_parameter_name_already_used_by_file_raises_exception(self):
        file = UploadableFile("file.txt", b"content", "text/plain")
        multipart = MultipartFormDataObject()
        multipart.add_file("field", file)

        with self.assertRaises((ValueError, TypeError, Exception)) as ctx:
            multipart.add_value("field", "value")

        self.assertIsNotNone(ctx.exception)

    @responses.activate
    def test_get_boundary_two_separate_instances_returns_different_boundaries(self):
        multipart_first = MultipartFormDataObject()
        multipart_second = MultipartFormDataObject()

        boundary_first = multipart_first.boundary
        boundary_second = multipart_second.boundary

        self.assertIsNotNone(boundary_first)
        self.assertIsNotNone(boundary_second)
        self.assertNotEqual(
            boundary_first,
            boundary_second,
            "Boundaries should be unique per instance",
        )

    @responses.activate
    def test_get_content_type_new_instance_contains_boundary_value(self):
        multipart = MultipartFormDataObject()

        content_type = multipart.content_type
        boundary = multipart.boundary

        self.assertIn(boundary, content_type)
        self.assertTrue(
            content_type.startswith("multipart/form-data; boundary="),
            f"Expected content_type to start with 'multipart/form-data; boundary=', got: {content_type}",
        )

    @responses.activate
    def test_get_content_type_new_instance_starts_with_multipart_form_data(self):
        multipart = MultipartFormDataObject()

        content_type = multipart.content_type

        self.assertTrue(
            content_type.startswith("multipart/form-data"),
            f"Expected content_type to start with 'multipart/form-data', got: {content_type}",
        )
        self.assertIn("boundary=", content_type)

    @responses.activate
    def test_new_uploadable_file_with_known_content_length_sets_all_properties_correctly(self):
        file = UploadableFile("test.txt", b"test content", "text/plain", 12)

        self.assertEqual("test.txt", file.file_name)
        self.assertEqual("text/plain", file.content_type)
        self.assertEqual(12, file.content_length)
        self.assertIsNotNone(file.content)

    @responses.activate
    def test_new_uploadable_file_without_content_length_sets_content_length_to_minus_one(self):
        file = UploadableFile("test.txt", b"test content", "text/plain")

        self.assertEqual("test.txt", file.file_name)
        self.assertEqual("text/plain", file.content_type)
        self.assertEqual(-1, file.content_length)
        self.assertIsNotNone(file.content)

    @responses.activate
    def test_new_uploadable_file_with_negative_content_length_normalizes_to_minus_one(self):
        file = UploadableFile("file.txt", b"content", "text/plain", -100)

        self.assertEqual(-1, file.content_length)

    @responses.activate
    def test_new_uploadable_file_null_filename_raises_exception(self):
        with self.assertRaises((ValueError, TypeError, Exception)) as ctx:
            UploadableFile(None, b"content", "text/plain")

        self.assertIsNotNone(ctx.exception)

    @responses.activate
    def test_new_uploadable_file_empty_filename_raises_exception(self):
        with self.assertRaises((ValueError, TypeError, Exception)) as ctx:
            UploadableFile("", b"content", "text/plain")

        self.assertIsNotNone(ctx.exception)

    @responses.activate
    def test_new_uploadable_file_null_content_raises_exception(self):
        with self.assertRaises((ValueError, TypeError, Exception)) as ctx:
            UploadableFile("file.txt", None, "text/plain")

        self.assertIsNotNone(ctx.exception)

    @responses.activate
    def test_new_uploadable_file_null_content_type_raises_exception(self):
        with self.assertRaises((ValueError, TypeError, Exception)) as ctx:
            UploadableFile("file.txt", b"content", None)

        self.assertIsNotNone(ctx.exception)

    @responses.activate
    def test_new_uploadable_file_empty_content_type_raises_exception(self):
        with self.assertRaises((ValueError, TypeError, Exception)) as ctx:
            UploadableFile("file.txt", b"content", "")

        self.assertIsNotNone(ctx.exception)


class HttpBinResponse(DataObject):
    form = None
    files = None

    def from_dictionary(self, dictionary):
        super(HttpBinResponse, self).from_dictionary(dictionary)
        if 'form' in dictionary:
            self.form = dictionary['form']
        if 'files' in dictionary:
            self.files = dictionary['files']
        return self


class MultipartFormDataObjectWrapper(MultipartFormDataRequest):
    __multipart = None

    def __init__(self, multipart):
        self.__multipart = multipart

    def to_multipart_form_data_object(self):
        return self.__multipart


if __name__ == '__main__':
    unittest.main()

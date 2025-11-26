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
    """Test multipart/form-data uploads"""

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
        """
        Register POST and PUT endpoints with the same multipart expectation and response.
        """
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
    def test_multipart_form_data_upload_post_multipart_form_data_object_with_response(self):
        """Test a multipart/form-data POST upload with a response"""
        self._register_multipart_stubs(responses)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.post('/post', None, None, multipart, HttpBinResponse, None)

        self.assertEqual(response.form['value'], 'Hello World')
        self.assertEqual(response.files['file'], 'file-content')

    @responses.activate
    def test_multipart_form_data_upload_post_multipart_form_data_request_with_response(self):
        """Test a multipart/form-data POST upload with a response"""
        self._register_multipart_stubs(responses)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.post('/post', None, None, MultipartFormDataObjectWrapper(multipart),
                                         HttpBinResponse, None)

        self.assertEqual(response.form['value'], 'Hello World')
        self.assertEqual(response.files['file'], 'file-content')

    @responses.activate
    def test_multipart_form_data_upload_post_multipart_form_data_object_with_binary_response(self):
        """Test a multipart/form-data POST upload with a binary response"""
        self._register_multipart_stubs(responses)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.post_with_binary_response('/post', None, None, multipart, None)

        data = ''
        for chunk in response[1]:
            data += chunk.decode('utf-8')
        response = json.loads(data)
        self.assertEqual(response['form']['value'], 'Hello World')
        self.assertEqual(response['files']['file'], 'file-content')

    @responses.activate
    def test_multipart_form_data_upload_post_multipart_form_data_request_with_binary_response(self):
        """Test a multipart/form-data POST upload with a binary response"""
        self._register_multipart_stubs(responses)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.post_with_binary_response('/post', None, None,
                                                              MultipartFormDataObjectWrapper(multipart), None)

        data = ''
        for chunk in response[1]:
            data += chunk.decode('utf-8')
        response = json.loads(data)
        self.assertEqual(response['form']['value'], 'Hello World')
        self.assertEqual(response['files']['file'], 'file-content')

    @responses.activate
    def test_multipart_form_data_upload_put_multipart_form_data_object_with_response(self):
        """Test a multipart/form-data PUT upload with a response"""
        self._register_multipart_stubs(responses)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.put('/put', None, None, multipart, HttpBinResponse, None)

        self.assertEqual(response.form['value'], 'Hello World')
        self.assertEqual(response.files['file'], 'file-content')

    @responses.activate
    def test_multipart_form_data_upload_put_multipart_form_data_request_with_response(self):
        """Test a multipart/form-data PUT upload with a response"""
        self._register_multipart_stubs(responses)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.put('/put', None, None, MultipartFormDataObjectWrapper(multipart), HttpBinResponse, None)

        self.assertEqual(response.form['value'], 'Hello World')
        self.assertEqual(response.files['file'], 'file-content')

    @responses.activate
    def test_multipart_form_data_upload_put_multipart_form_data_object_with_binary_response(self):
        """Test a multipart/form-data PUT upload with a binary response"""
        self._register_multipart_stubs(responses)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.put_with_binary_response('/put', None, None, multipart, None)

        data = ''
        for chunk in response[1]:
            data += chunk.decode('utf-8')
        response = json.loads(data)
        self.assertEqual(response['form']['value'], 'Hello World')
        self.assertEqual(response['files']['file'], 'file-content')

    @responses.activate
    def test_multipart_form_data_upload_put_multipart_form_data_request_with_binary_response(self):
        """Test a multipart/form-data PUT upload with a binary response"""
        self._register_multipart_stubs(responses)

        configuration = init_utils.create_communicator_configuration()
        configuration.api_endpoint = MOCK_API_ENDPOINT

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
        multipart.add_value('value', 'Hello World')

        with Factory.create_communicator_from_configuration(configuration) as communicator:
            response = communicator.put_with_binary_response('/put', None, None, MultipartFormDataObjectWrapper(multipart), None)

        data = ''
        for chunk in response[1]:
            data += chunk.decode('utf-8')
        response = json.loads(data)
        self.assertEqual(response['form']['value'], 'Hello World')
        self.assertEqual(response['files']['file'], 'file-content')

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

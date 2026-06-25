import unittest

from onlinepayments.sdk.communication.multipart_form_data_object import MultipartFormDataObject
from onlinepayments.sdk.domain.uploadable_file import UploadableFile


def _make_uploadable_file(file_name="test.txt", content_type="text/plain"):
    return UploadableFile(file_name, b"file content", content_type)


class MultipartFormDataObjectTest(unittest.TestCase):

    def test_Constructing_DefaultScenario_InitializeWithValidBoundaryAndContentType(self):
        obj = MultipartFormDataObject()
        self.assertIsNotNone(obj.boundary)
        self.assertIsNotNone(obj.content_type)
        self.assertTrue(obj.content_type.startswith("multipart/form-data; boundary="))
        self.assertIn(obj.boundary, obj.content_type)

    def test_GettingProperties_DefaultScenario_ReturnBoundaryString(self):
        obj = MultipartFormDataObject()
        boundary = obj.boundary
        self.assertIsNotNone(boundary)
        self.assertGreater(len(boundary), 0)

    def test_GettingProperties_DefaultScenario_ReturnContentTypeWithBoundary(self):
        obj = MultipartFormDataObject()
        self.assertEqual("multipart/form-data; boundary=" + obj.boundary, obj.content_type)

    def test_GettingProperties_DefaultScenario_ReturnEmptyValuesMapInitially(self):
        obj = MultipartFormDataObject()
        self.assertIsNotNone(obj.values)
        self.assertEqual(0, len(obj.values))

    def test_GettingProperties_DefaultScenario_ReturnEmptyFilesMapInitially(self):
        obj = MultipartFormDataObject()
        self.assertIsNotNone(obj.files)
        self.assertEqual(0, len(obj.files))

    def test_GettingProperties_DefaultScenario_ReturnUniqueBoundaryPerInstance(self):
        self.assertNotEqual(MultipartFormDataObject().boundary, MultipartFormDataObject().boundary)

    def test_AddingValues_DefaultScenario_AddSingleValue(self):
        obj = MultipartFormDataObject()
        obj.add_value("fieldName", "fieldValue")
        self.assertEqual(1, len(obj.values))
        self.assertEqual("fieldValue", obj.values["fieldName"])

    def test_AddingValues_DefaultScenario_AddMultipleValues(self):
        obj = MultipartFormDataObject()
        obj.add_value("field1", "value1")
        obj.add_value("field2", "value2")
        obj.add_value("field3", "value3")
        self.assertEqual(3, len(obj.values))
        self.assertEqual("value1", obj.values["field1"])
        self.assertEqual("value2", obj.values["field2"])
        self.assertEqual("value3", obj.values["field3"])

    def test_AddingValues_DefaultScenario_ThrowExceptionWhenParameterNameIsNull(self):
        obj = MultipartFormDataObject()
        with self.assertRaises(ValueError):
            obj.add_value(None, "value")

    def test_AddingValues_DefaultScenario_ThrowExceptionWhenParameterNameIsEmpty(self):
        obj = MultipartFormDataObject()
        with self.assertRaises(ValueError):
            obj.add_value("", "value")

    def test_AddingValues_DefaultScenario_ThrowExceptionWhenParameterNameIsWhitespace(self):
        obj = MultipartFormDataObject()
        with self.assertRaises(ValueError):
            obj.add_value("   ", "value")

    def test_AddingValues_DefaultScenario_ThrowExceptionWhenValueIsNull(self):
        obj = MultipartFormDataObject()
        with self.assertRaises(ValueError):
            obj.add_value("fieldName", None)

    def test_AddingValues_DefaultScenario_ThrowExceptionWhenAddingDuplicateValue(self):
        obj = MultipartFormDataObject()
        obj.add_value("fieldName", "value1")
        with self.assertRaises(ValueError) as ctx:
            obj.add_value("fieldName", "value2")
        self.assertIn("duplicate parameterName: fieldName", str(ctx.exception))

    def test_AddingFiles_DefaultScenario_AddSingleFile(self):
        obj = MultipartFormDataObject()
        file = _make_uploadable_file()
        obj.add_file("fileName", file)
        self.assertEqual(1, len(obj.files))
        self.assertIs(file, obj.files["fileName"])

    def test_AddingFiles_DefaultScenario_AddMultipleFiles(self):
        obj = MultipartFormDataObject()
        file1 = _make_uploadable_file("file1.txt")
        file2 = _make_uploadable_file("file2.txt")
        file3 = _make_uploadable_file("file3.txt")
        obj.add_file("file1", file1)
        obj.add_file("file2", file2)
        obj.add_file("file3", file3)
        self.assertEqual(3, len(obj.files))
        self.assertIs(file1, obj.files["file1"])
        self.assertIs(file2, obj.files["file2"])
        self.assertIs(file3, obj.files["file3"])

    def test_AddingFiles_DefaultScenario_ThrowExceptionWhenParameterNameIsNull(self):
        obj = MultipartFormDataObject()
        with self.assertRaises(ValueError):
            obj.add_file(None, _make_uploadable_file())

    def test_AddingFiles_DefaultScenario_ThrowExceptionWhenParameterNameIsEmpty(self):
        obj = MultipartFormDataObject()
        with self.assertRaises(ValueError):
            obj.add_file("", _make_uploadable_file())

    def test_AddingFiles_DefaultScenario_ThrowExceptionWhenParameterNameIsWhitespace(self):
        obj = MultipartFormDataObject()
        with self.assertRaises(ValueError):
            obj.add_file("   ", _make_uploadable_file())

    def test_AddingFiles_DefaultScenario_ThrowExceptionWhenFileIsNull(self):
        obj = MultipartFormDataObject()
        with self.assertRaises(ValueError):
            obj.add_file("fileName", None)

    def test_AddingFiles_DefaultScenario_ThrowExceptionWhenAddingDuplicateFile(self):
        obj = MultipartFormDataObject()
        obj.add_file("fileName", _make_uploadable_file("file1.txt"))
        with self.assertRaises(ValueError) as ctx:
            obj.add_file("fileName", _make_uploadable_file("file2.txt"))
        self.assertIn("duplicate parameterName: fileName", str(ctx.exception))

    def test_MixingValuesAndFiles_DefaultScenario_ThrowExceptionWhenAddingValueForExistingFileParameter(self):
        obj = MultipartFormDataObject()
        obj.add_file("paramName", _make_uploadable_file())
        with self.assertRaises(ValueError) as ctx:
            obj.add_value("paramName", "value")
        self.assertIn("duplicate parameterName: paramName", str(ctx.exception))

    def test_MixingValuesAndFiles_DefaultScenario_ThrowExceptionWhenAddingFileForExistingValueParameter(self):
        obj = MultipartFormDataObject()
        obj.add_value("paramName", "value")
        with self.assertRaises(ValueError) as ctx:
            obj.add_file("paramName", _make_uploadable_file())
        self.assertIn("duplicate parameterName: paramName", str(ctx.exception))

    def test_AccessingMaps_DefaultScenario_ReturnMutableValuesMap(self):
        obj = MultipartFormDataObject()
        obj.add_value("key", "value")
        values = obj.values
        values["newKey"] = "newValue"
        self.assertEqual("newValue", obj.values["newKey"])

    def test_AccessingMaps_DefaultScenario_ReturnMutableFilesMap(self):
        obj = MultipartFormDataObject()
        obj.add_file("key", _make_uploadable_file())
        files = obj.files
        new_file = _make_uploadable_file("new.txt")
        files["newKey"] = new_file
        self.assertIs(new_file, obj.files["newKey"])


if __name__ == '__main__':
    unittest.main()

import unittest
from datetime import date, datetime, timedelta, timezone

from onlinepayments.sdk.domain.data_object import DataObject
from onlinepayments.sdk.json.default_marshaller import DefaultMarshaller
from onlinepayments.sdk.json.marshaller_syntax_exception import MarshallerSyntaxException


class _BasicObject(DataObject):
    def __init__(self):
        self.id = None

    def from_dictionary(self, dictionary):
        super().from_dictionary(dictionary)
        if 'id' in dictionary:
            self.id = dictionary['id']
        return self

    def to_dictionary(self):
        d = {}
        if self.id is not None:
            d['id'] = self.id
        return d


class _ObjectWithExtraField(_BasicObject):
    def __init__(self):
        super().__init__()
        self.extra_field = None

    def from_dictionary(self, dictionary):
        super().from_dictionary(dictionary)
        if 'extraField' in dictionary:
            self.extra_field = dictionary['extraField']
        return self

    def to_dictionary(self):
        d = super().to_dictionary()
        if self.extra_field is not None:
            d['extraField'] = self.extra_field
        return d


class _ObjectWithDates(DataObject):
    def __init__(self):
        self.date = None
        self.date_time = None

    def from_dictionary(self, dictionary):
        super().from_dictionary(dictionary)
        if 'date' in dictionary:
            self.date = DataObject.parse_date(dictionary['date'])
        if 'dateTime' in dictionary:
            self.date_time = DataObject.parse_datetime(dictionary['dateTime'])
        return self

    def to_dictionary(self):
        d = {}
        if self.date is not None:
            d['date'] = DataObject.format_date(self.date)
        if self.date_time is not None:
            d['dateTime'] = DataObject.format_datetime(self.date_time)
        return d


class _ObjectWithListField(DataObject):
    def __init__(self):
        self.values = None

    def from_dictionary(self, dictionary):
        super().from_dictionary(dictionary)
        if 'values' in dictionary:
            self.values = dictionary['values']
        return self

    def to_dictionary(self):
        d = {}
        if self.values is not None:
            d['values'] = self.values
        return d


class DefaultMarshallerTest(unittest.TestCase):

    def test_UnmarshallingObjectWithExtraFields_DefaultScenario_IgnoreUnknownFields(self):
        original = _ObjectWithExtraField()
        original.id = "1234"
        original.extra_field = "extra-field-value"
        json_str = DefaultMarshaller.instance().marshal(original)
        unmarshalled = DefaultMarshaller.instance().unmarshal(json_str, _BasicObject)

        self.assertEqual("1234", unmarshalled.id)

    def test_MarshallingObjectWithDateAndDateTime_DefaultScenario_ReturnExpectedJsonValues(self):
        obj = _ObjectWithDates()
        obj.date = date(2023, 12, 31)
        obj.date_time = datetime(2023, 12, 31, 13, 24, 59, 123_456, tzinfo=timezone(timedelta(hours=2)))
        json_str = DefaultMarshaller.instance().marshal(obj)

        self.assertIn('"2023-12-31"', json_str)
        self.assertIn('"2023-12-31T13:24:59.123+02:00"', json_str)

    def test_UnmarshallingDateAndDateTimeJson_DefaultScenario_ReturnExpectedObject(self):
        json_str = '{"date": "2023-12-31", "dateTime": "2023-12-31T13:24:59.123+02:00"}'
        obj = DefaultMarshaller.instance().unmarshal(json_str, _ObjectWithDates)
        expected_dt = datetime(2023, 12, 31, 13, 24, 59, 123_000, tzinfo=timezone(timedelta(hours=2)))

        self.assertEqual(date(2023, 12, 31), obj.date)
        self.assertEqual(expected_dt, obj.date_time)

    def test_UnmarshallingZuluDateTime_DefaultScenario_ReturnUtcZonedDateTime(self):
        json_str = '{"dateTime": "2023-12-31T13:24:59.123Z"}'
        obj = DefaultMarshaller.instance().unmarshal(json_str, _ObjectWithDates)
        expected_dt = datetime(2023, 12, 31, 13, 24, 59, 123_000, tzinfo=timezone.utc)

        self.assertEqual(expected_dt, obj.date_time)
        self.assertEqual(timedelta(0), obj.date_time.utcoffset())

    def test_MarshallingObjectWithNullDateFields_DefaultScenario_NotSerializeNullDateFields(self):
        obj = _ObjectWithDates()
        obj.date = None
        obj.date_time = None
        json_str = DefaultMarshaller.instance().marshal(obj)

        self.assertEqual("{}", json_str)

    def test_MarshallingObjectWithListField_DefaultScenario_RoundTripObjectWithListField(self):
        original = _ObjectWithListField()
        original.values = ["first", "second", "third"]
        json_str = DefaultMarshaller.instance().marshal(original)
        unmarshalled = DefaultMarshaller.instance().unmarshal(json_str, _ObjectWithListField)

        self.assertEqual(original.values, unmarshalled.values)

    def test_MarshallingNullObject_DefaultScenario_ReturnJsonNull(self):
        json_str = DefaultMarshaller.instance().marshal(None)
        self.assertEqual("null", json_str)

    def test_UnmarshallingNull_DefaultScenario_ReturnNull(self):
        result = DefaultMarshaller.instance().unmarshal(None, _BasicObject)
        self.assertIsNone(result)

    def test_UnmarshallingWithBytesInput_DefaultScenario_ReturnExpectedObject(self):
        json_bytes = b'{"date": "2023-12-31", "dateTime": "2023-12-31T13:24:59.123+02:00"}'
        obj = DefaultMarshaller.instance().unmarshal(json_bytes, _ObjectWithDates)
        expected_dt = datetime(2023, 12, 31, 13, 24, 59, 123_000, tzinfo=timezone(timedelta(hours=2)))

        self.assertEqual(date(2023, 12, 31), obj.date)
        self.assertEqual(expected_dt, obj.date_time)

    def test_UnmarshallingEmptyString_DefaultScenario_ReturnNull(self):
        result = DefaultMarshaller.instance().unmarshal("", _BasicObject)
        self.assertIsNone(result)

    def test_UnmarshallingNonDataObjectType_DefaultScenario_ReturnGenericObjectWithAttributes(self):
        json_str = '{"id": "1234", "value": 42}'
        result = DefaultMarshaller.instance().unmarshal(json_str, object)

        self.assertEqual("1234", result.id)
        self.assertEqual(42, result.value)

    def test_UnmarshallingInvalidJson_DefaultScenario_RaiseMarshallerSyntaxException(self):
        invalid_json = "not valid json {"
        with self.assertRaises(MarshallerSyntaxException):
            DefaultMarshaller.instance().unmarshal(invalid_json, _BasicObject)


if __name__ == '__main__':
    unittest.main()

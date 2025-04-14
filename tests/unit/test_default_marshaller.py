import unittest

from onlinepayments.sdk.domain.data_object import DataObject
from onlinepayments.sdk.json.default_marshaller import DefaultMarshaller


class DefaultMarshallerTest(unittest.TestCase):
    """Tests that the default marshaller is able to marshal an object
    and unmarshal that same object to a more generic version
    """

    def test_unmarshal_with_extra_fields(self):
        """Tests if the marshaller is able to marshal an object and unmarshal it as an instance of a parent class"""
        dummy_object = JsonDummyExtended()
        mini_dummy = JsonMiniDummy()
        mini_mini_dummy = JsonMiniMiniDummy()
        mini_mini_dummy.foo = "hiddenfoo"
        mini_dummy.foo = mini_mini_dummy
        dummy_object.foo = mini_dummy
        dummy_object.bar = True
        dummy_object.boo = 0o1
        dummy_object.far = "close"
        dummy_object.extra_field = "something else"
        marshaller = DefaultMarshaller.instance()

        json = marshaller.marshal(dummy_object)
        unmarshalled = marshaller.unmarshal(json, JsonDummy)

        self.assertEqual(True, unmarshalled.bar)
        self.assertEqual(0o1, unmarshalled.boo)
        self.assertEqual("close", unmarshalled.far)
        self.assertEqual("hiddenfoo", unmarshalled.foo.foo.foo)


# --------------- A number of dummy objects for testing -------------

class JsonMiniMiniDummy(DataObject):
    foo = "standardfoo"

    def to_dictionary(self):
        dictionary = super(JsonMiniMiniDummy, self).to_dictionary()
        if self.foo is not None:
            dictionary['foo'] = self.foo

        return dictionary

    def from_dictionary(self, dictionary):
        super(JsonMiniMiniDummy, self).from_dictionary(dictionary)
        if 'foo' in dictionary:
            self.foo = dictionary['foo']
        return self


class JsonMiniDummy(DataObject):
    foo = JsonMiniMiniDummy()

    def to_dictionary(self):
        dictionary = super(JsonMiniDummy, self).to_dictionary()
        if self.foo is not None:
            dictionary['foo'] = self.foo.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(JsonMiniDummy, self).from_dictionary(dictionary)
        if 'foo' in dictionary:
            if not isinstance(dictionary['foo'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['foo']))
            value = JsonMiniMiniDummy()
            self.foo = value.from_dictionary(dictionary['foo'])
        return self


class JsonDummy(DataObject):
    foo = JsonMiniDummy()
    bar = False
    boo = 00
    far = "far"

    def to_dictionary(self):
        dictionary = super(JsonDummy, self).to_dictionary()
        if self.foo is not None:
            dictionary['foo'] = self.foo
        if self.bar is not None:
            dictionary['bar'] = self.bar
        if self.boo is not None:
            dictionary['boo'] = self.boo
        if self.far is not None:
            dictionary['far'] = self.far

        return dictionary

    def from_dictionary(self, dictionary):
        super(JsonDummy, self).from_dictionary(dictionary)
        if 'foo' in dictionary:
            if not isinstance(dictionary['foo'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['foo']))
            value = JsonMiniDummy()
            self.foo = value.from_dictionary(dictionary['foo'])
        if 'bar' in dictionary:
            self.bar = dictionary['bar']
        if 'boo' in dictionary:
            self.boo = dictionary['boo']
        if 'far' in dictionary:
            self.far = dictionary['far']

        return self


class JsonDummyExtended(JsonDummy):
    extra_field = "something something"

    def to_dictionary(self):
        dictionary = super(JsonDummyExtended, self).to_dictionary()
        if self.extra_field is not None:
            dictionary['extraField'] = self.extra_field
        return dictionary

    def from_dictionary(self, dictionary):
        super(JsonDummyExtended, self).from_dictionary(dictionary)
        if 'extraField' in dictionary:
            self.far = dictionary['extraField']
        return self


if __name__ == '__main__':
    unittest.main()

import os
import unittest

from tests import file_utils

from onlinepayments.sdk.log.body_obfuscator import BodyObfuscator


def _read_resource(file_name):
    return file_utils.read_file(os.path.join("log", file_name))


class BodyObfuscatorTest(unittest.TestCase):

    def test_ObfuscatingBody_NullBody_ReturnNull(self):
        obfuscated_body = BodyObfuscator.default_body_obfuscator().obfuscate_body(None)
        self.assertIsNone(obfuscated_body)

    def test_ObfuscatingBody_EmptyBody_ReturnOriginalBody(self):
        obfuscated_body = BodyObfuscator.default_body_obfuscator().obfuscate_body("")
        self.assertEqual("", obfuscated_body)

    def test_ObfuscatingBody_BodyContainingCard_ReturnObfuscatedBody(self):
        self.obfuscate_body_match("bodyWithCardOriginal.json", "bodyWithCardObfuscated.json")

    def test_ObfuscatingBody_BodyContainingCard_ReturnBodyObfuscatedWithCustomRule(self):
        def obfuscate_custom(value):
            start = 6
            end = len(value) - 4
            value_between = '*' * (end - start)
            return value[:start] + value_between + value[end:]

        body_obfuscator = BodyObfuscator(additional_rules={"cardNumber": obfuscate_custom})
        self.obfuscate_body_match("bodyWithCardOriginal.json",
                                  "bodyWithCardCustomObfuscated.json",
                                  body_obfuscator=body_obfuscator)

    def test_ObfuscatingBody_BodyContainingIban_ReturnObfuscatedBody(self):
        self.obfuscate_body_match("bodyWithIbanOriginal.json", "bodyWithIbanObfuscated.json")

    def test_ObfuscatingBody_BodyContainingBin_ReturnObfuscatedBody(self):
        self.obfuscate_body_match("bodyWithBinOriginal.json", "bodyWithBinObfuscated.json")

    def test_ObfuscatingBody_WithoutMatchingFields_ReturnOriginalBody(self):
        self.obfuscate_body_no_match("bodyNoObfuscation.json")

    def test_ObfuscatingBody_BodyContainingNestedObject_ReturnObfuscatedBody(self):
        self.obfuscate_body_match("bodyWithObjectOriginal.json", "bodyWithObjectObfuscated.json")

    def test_ObfuscatingBody_BytesAndCharset_ReturnObfuscatedBody(self):
        body = _read_resource("bodyWithCardOriginal.json")
        expected = _read_resource("bodyWithCardObfuscated.json")
        obfuscated_body = BodyObfuscator.default_body_obfuscator().obfuscate_body(body.encode("utf-8"), "utf-8")
        self.assertEqual(expected, obfuscated_body)

    def obfuscate_body_match(self, original_resource, obfuscated_resource, body_obfuscator=None):
        if body_obfuscator is None:
            body_obfuscator = BodyObfuscator.default_body_obfuscator()
        body = _read_resource(original_resource)
        expected = _read_resource(obfuscated_resource)

        obfuscated_body = body_obfuscator.obfuscate_body(body)

        self.assertEqual(expected, obfuscated_body)

    def obfuscate_body_no_match(self, resource):
        self.obfuscate_body_match(resource, resource)


if __name__ == '__main__':
    unittest.main()

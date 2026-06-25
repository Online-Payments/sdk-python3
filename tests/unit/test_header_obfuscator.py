import unittest

from onlinepayments.sdk.log.header_obfuscator import HeaderObfuscator
from onlinepayments.sdk.log.obfuscation_rule import (
    obfuscate_all,
    obfuscate_with_fixed_length,
    obfuscate_all_but_first,
    obfuscate_all_but_last,
)


class HeaderObfuscatorTest(unittest.TestCase):

    def test_GettingDefaultObfuscator_DefaultScenario_ReturnNonNullInstance(self):
        self.assertIsNotNone(HeaderObfuscator.default_header_obfuscator())

    def test_GettingDefaultObfuscator_DefaultScenario_ReturnSingletonInstance(self):
        self.assertIs(HeaderObfuscator.default_header_obfuscator(),
                      HeaderObfuscator.default_header_obfuscator())

    def test_GettingDefaultObfuscator_DefaultScenario_ObfuscateAuthorizationHeader(self):
        result = HeaderObfuscator.default_header_obfuscator().obfuscate_header("Authorization", "Bearer secret-token")
        self.assertEqual("********", result)

    def test_CreatingCustomObfuscator_DefaultScenario_ReturnNonNullInstance(self):
        obfuscator = HeaderObfuscator(additional_rules={"X-Custom": obfuscate_all()})
        self.assertIsNotNone(obfuscator)

    def test_CreatingCustomObfuscator_DefaultScenario_HavePreDefinedObfuscationRules(self):
        obfuscator = HeaderObfuscator(additional_rules={"X-Custom": obfuscate_all()})
        self.assertEqual("********", obfuscator.obfuscate_header("Authorization", "Bearer token"))

    def test_ObfuscatingWithObfuscateAll_DefaultScenario_ReplaceAllCharactersWithAsterisks(self):
        obfuscator = HeaderObfuscator(additional_rules={"Content-Type": obfuscate_all()})
        self.assertEqual("****************", obfuscator.obfuscate_header("Content-Type", "application/json"))

    def test_ObfuscatingWithObfuscateAll_DefaultScenario_HandleNullValue(self):
        obfuscator = HeaderObfuscator(additional_rules={"X-Custom-Header": obfuscate_all()})
        self.assertIsNone(obfuscator.obfuscate_header("X-Custom-Header", None))

    def test_ObfuscatingWithObfuscateAll_DefaultScenario_HandleEmptyValue(self):
        obfuscator = HeaderObfuscator(additional_rules={"X-Custom-Header": obfuscate_all()})
        self.assertEqual("", obfuscator.obfuscate_header("X-Custom-Header", ""))

    def test_ObfuscatingWithObfuscateAll_DefaultScenario_BeCaseInsensitive(self):
        obfuscator = HeaderObfuscator(additional_rules={"Content-Type": obfuscate_all()})
        self.assertEqual("****************", obfuscator.obfuscate_header("content-type", "application/json"))
        self.assertEqual("****************", obfuscator.obfuscate_header("CONTENT-TYPE", "application/json"))

    def test_ObfuscatingWithObfuscateWithFixedLength_DefaultScenario_CreateFixedLengthMask(self):
        obfuscator = HeaderObfuscator(additional_rules={"X-Custom-Header": obfuscate_with_fixed_length(4)})
        self.assertEqual("****", obfuscator.obfuscate_header("X-Custom-Header", "very-long-value"))

    def test_ObfuscatingWithObfuscateWithFixedLength_DefaultScenario_RespectDifferentLengths(self):
        obfuscator4 = HeaderObfuscator(additional_rules={"Header1": obfuscate_with_fixed_length(4)})
        obfuscator8 = HeaderObfuscator(additional_rules={"Header2": obfuscate_with_fixed_length(8)})
        obfuscator16 = HeaderObfuscator(additional_rules={"Header3": obfuscate_with_fixed_length(16)})

        self.assertEqual("****", obfuscator4.obfuscate_header("Header1", "value"))
        self.assertEqual("********", obfuscator8.obfuscate_header("Header2", "value"))
        self.assertEqual("****************", obfuscator16.obfuscate_header("Header3", "value"))

    def test_ObfuscatingWithObfuscateWithFixedLength_DefaultScenario_HandleNullValue(self):
        obfuscator = HeaderObfuscator(additional_rules={"X-Token": obfuscate_with_fixed_length(8)})
        self.assertEqual("********", obfuscator.obfuscate_header("X-Token", None))

    def test_ObfuscatingWithObfuscateWithFixedLength_DefaultScenario_HandleEmptyValue(self):
        obfuscator = HeaderObfuscator(additional_rules={"X-Token": obfuscate_with_fixed_length(8)})
        self.assertEqual("********", obfuscator.obfuscate_header("X-Token", ""))

    def test_ObfuscatingWithObfuscateAllButFirst_DefaultScenario_KeepFirstCharacterAndObfuscateRest(self):
        obfuscator = HeaderObfuscator(additional_rules={"X-Token": obfuscate_all_but_first(1)})
        self.assertEqual("s********", obfuscator.obfuscate_header("X-Token", "secret123"))

    def test_ObfuscatingWithObfuscateAllButFirst_DefaultScenario_KeepSpecifiedNumberOfCharacters(self):
        obfuscator1 = HeaderObfuscator(additional_rules={"Header1": obfuscate_all_but_first(1)})
        obfuscator3 = HeaderObfuscator(additional_rules={"Header2": obfuscate_all_but_first(3)})
        obfuscator5 = HeaderObfuscator(additional_rules={"Header3": obfuscate_all_but_first(5)})

        self.assertEqual("s********", obfuscator1.obfuscate_header("Header1", "secret123"))
        self.assertEqual("sec******", obfuscator3.obfuscate_header("Header2", "secret123"))
        self.assertEqual("secre****", obfuscator5.obfuscate_header("Header3", "secret123"))

    def test_ObfuscatingWithObfuscateAllButFirst_DefaultScenario_HandleNullValue(self):
        obfuscator = HeaderObfuscator(additional_rules={"X-Token": obfuscate_all_but_first(3)})
        self.assertIsNone(obfuscator.obfuscate_header("X-Token", None))

    def test_ObfuscatingWithObfuscateAllButFirst_DefaultScenario_HandleEmptyValue(self):
        obfuscator = HeaderObfuscator(additional_rules={"X-Token": obfuscate_all_but_first(3)})
        self.assertEqual("", obfuscator.obfuscate_header("X-Token", ""))

    def test_ObfuscatingWithObfuscateAllButLast_DefaultScenario_KeepLastCharacterAndObfuscateRest(self):
        obfuscator = HeaderObfuscator(additional_rules={"X-Token": obfuscate_all_but_last(1)})
        self.assertEqual("********3", obfuscator.obfuscate_header("X-Token", "secret123"))

    def test_ObfuscatingWithObfuscateAllButLast_DefaultScenario_KeepSpecifiedNumberOfCharacters(self):
        obfuscator1 = HeaderObfuscator(additional_rules={"Header1": obfuscate_all_but_last(1)})
        obfuscator3 = HeaderObfuscator(additional_rules={"Header2": obfuscate_all_but_last(3)})
        obfuscator5 = HeaderObfuscator(additional_rules={"Header3": obfuscate_all_but_last(5)})

        self.assertEqual("********3", obfuscator1.obfuscate_header("Header1", "secret123"))
        self.assertEqual("******123", obfuscator3.obfuscate_header("Header2", "secret123"))
        self.assertEqual("****et123", obfuscator5.obfuscate_header("Header3", "secret123"))

    def test_ObfuscatingWithObfuscateAllButLast_DefaultScenario_HandleNullValue(self):
        obfuscator = HeaderObfuscator(additional_rules={"X-Token": obfuscate_all_but_last(3)})
        self.assertIsNone(obfuscator.obfuscate_header("X-Token", None))

    def test_ObfuscatingWithObfuscateAllButLast_DefaultScenario_HandleEmptyValue(self):
        obfuscator = HeaderObfuscator(additional_rules={"X-Token": obfuscate_all_but_last(3)})
        self.assertEqual("", obfuscator.obfuscate_header("X-Token", ""))

    def test_CustomObfuscationRule_DefaultScenario_NotObfuscateWhenRuleIsNone(self):
        obfuscator = HeaderObfuscator(additional_rules={"X-Custom": None})
        self.assertEqual("test-value", obfuscator.obfuscate_header("X-Custom", "test-value"))

    def test_CustomObfuscationRule_DefaultScenario_ApplyCustomRule(self):
        def custom_rule(value):
            return ("CUSTOM_" + str(len(value))) if value else value

        obfuscator = HeaderObfuscator(additional_rules={"X-Custom": custom_rule})
        self.assertEqual("CUSTOM_10", obfuscator.obfuscate_header("X-Custom", "test-value"))

    def test_CustomObfuscationRule_DefaultScenario_AllowMultipleCustomRules(self):
        def rule1(value):
            return ("RULE1_" + value) if value else value

        def rule2(value):
            return ("RULE2_" + value) if value else value

        obfuscator = HeaderObfuscator(additional_rules={"X-Header1": rule1, "X-Header2": rule2})
        self.assertEqual("RULE1_test1", obfuscator.obfuscate_header("X-Header1", "test1"))
        self.assertEqual("RULE2_test2", obfuscator.obfuscate_header("X-Header2", "test2"))

    def test_ObfuscatingHeader_DefaultScenario_ReturnExpectedValueWithDefaultObfuscator(self):
        obfuscator = HeaderObfuscator.default_header_obfuscator()
        for name in ("Authorization", "authorization", "AUTHORIZATION"):
            self.assertEqual("********", obfuscator.obfuscate_header(name, "Basic QWxhZGRpbjpPcGVuU2VzYW1l"))
        for name in ("Content-Type", "content-type", "CONTENT-TYPE"):
            self.assertEqual("application/json", obfuscator.obfuscate_header(name, "application/json"))

    def test_ObfuscatingHeader_DefaultScenario_ReturnExpectedValueWithCustomObfuscator(self):
        obfuscator = HeaderObfuscator(additional_rules={"content-type": obfuscate_all()})
        for name in ("Authorization", "authorization", "AUTHORIZATION"):
            self.assertEqual("********", obfuscator.obfuscate_header(name, "Basic QWxhZGRpbjpPcGVuU2VzYW1l"))
        for name in ("Content-Type", "content-type", "CONTENT-TYPE"):
            self.assertEqual("****************", obfuscator.obfuscate_header(name, "application/json"))


if __name__ == '__main__':
    unittest.main()

import codecs
import re

from typing import List


class LoggingUtil:
    """
    A utility class to support logging.
    """

    class Obfuscator:

        __obfuscators = None
        __obfuscator_keys = None

        def __init__(self, case_insensitive, values: List[str] = None, sensitive_values: List[str] = None):
            obfuscators = {}
            self.case_insensitive = case_insensitive
            if values:
                obfuscator = self.ValueObfuscator()
                for value in values:
                    obfuscators[value] = obfuscator
            if sensitive_values:
                value_obfuscator = self.SensitiveValueObfuscator()
                for value in sensitive_values:
                    obfuscators[value] = value_obfuscator
            self.__obfuscators = tuple(obfuscators.items())
            self.__obfuscator_keys = tuple(obfuscators)

        def obfuscate_value(self, key, value):
            obfuscator = self.find_obfuscator(key)
            if obfuscator is not None:
                return obfuscator.obfuscate_value(value)
            return value

        def find_obfuscator(self, key):
            for item in self.__obfuscators:
                x, y = item
                if self.case_insensitive:
                    if x.lower() == key.lower():
                        return y
                else:
                    if x == key:
                        return y
            return None

        class ValueObfuscator:
            def obfuscate_value(self, value):
                return '*' + str(len(value)) if value else value

        class SensitiveValueObfuscator:
            def obfuscate_value(self, value):
                return '***' if value else value

        def build_property_pattern(self, property_names):
            if not property_names:
                return re.compile("$^")
            s = "([\"'])("
            for p in property_names:
                s += '|' + re.escape(p)
            s += ")\\1\\s*:\\s*(?:([\"'])(.*?)(?<!\\\\)\\3|([^\"'\\s\\[\\{]((?!,)\\S)*))"
            return re.compile(s, re.DOTALL)

        def obfuscate(self, body):
            if body is None:
                return None
            if not body:
                return ""
            index = 0
            s_obfuscate = ""
            pattern = self.build_property_pattern(self.__obfuscator_keys)
            matcher = pattern.finditer(body)
            for x in matcher:
                property_name = x.group(2)
                value = x.group(4)
                value_start = x.start(4)
                value_end = x.end(4)
                if not value:
                    value = x.group(5)
                    value_start = x.start(5)
                    value_end = x.end(5)
                obfuscated_value = self.obfuscate_value(property_name, value)
                s_obfuscate += body[index:value_start] + obfuscated_value
                index = value_end
            return s_obfuscate + body[index:]

    __properties = ["accountNumber",
                    "additionalInfo",
                    "bin",
                    "cardNumber",
                    "cardholderName",
                    "cvv",
                    "dateOfBirth",
                    "emailAddress",
                    "expiryDate",
                    "faxNumber",
                    "firstName",
                    "houseNumber",
                    "iban",
                    "mobilePhoneNumber",
                    "passengerName",
                    "phoneNumber",
                    "reformattedAccountNumber",
                    "street",
                    "surname",
                    "value",
                    "workPhoneNumber",
                    "zip"]
    __sensitive_properties = ["decryptedPayload",
                              "encryptedCustomerInput",
                              "encryptedPayload",
                              "keyId",
                              "publicKey",
                              "secretKey",
                              "userAuthenticationToken"]
    __property_obfuscator = Obfuscator(False, __properties, __sensitive_properties)

    __sensitive_headers = ["Authorization",
                           "Proxy-Authenticate",
                           "Proxy-Authorization",
                           "X-GCS-Authentication-Token",
                           "WWW-Authenticate",
                           "X-GCS-CallerPassword"]
    __header_obfuscator = Obfuscator(True, sensitive_values=__sensitive_headers)

    @staticmethod
    def obfuscate_body(body, charset=None):
        """
        Obfuscates the body from the given stream as necessary.
        :param body: The body stream to obfuscate
        :param charset: The charset to use to read the body input stream.
        """
        if charset is None:
            return LoggingUtil.__property_obfuscator.obfuscate(body)
        else:  # possible dead code
            return LoggingUtil.obfuscate_body(codecs.decode(body, charset))

    @staticmethod
    def obfuscate_header(name, value):
        """
        Obfuscates the value for the given header as necessary.
        """
        return LoggingUtil.__header_obfuscator.obfuscate_value(name, value)

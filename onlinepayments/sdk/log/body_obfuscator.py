import re

from re import Pattern
from collections.abc import Mapping, Sequence

from .obfuscation_rule import ObfuscationRule, obfuscate_all, obfuscate_with_fixed_length, obfuscate_all_but_first, obfuscate_all_but_last


class BodyObfuscator:
    """
    A class that can be used to obfuscate properties in JSON bodies.
    """

    __obfuscation_rules: dict[str, ObfuscationRule]
    __property_pattern: Pattern[str]

    def __init__(self, additional_rules: Mapping[str, ObfuscationRule] | None = None):
        """
        Creates a new  body obfuscator.
        This will contain some pre-defined obfuscation rules, as well as any provided custom rules

        :param additional_rules: An optional mapping from property names to obfuscation rules,
         where an obfuscation rule is a function that obfuscates a single string,
        """
        self.__obfuscation_rules = {
            "additionalInfo": obfuscate_all(),
            "cardholderName": obfuscate_all(),
            "dateOfBirth": obfuscate_all(),
            "emailAddress": obfuscate_all(),
            "faxNumber": obfuscate_all(),
            "firstName": obfuscate_all(),
            "houseNumber": obfuscate_all(),
            "mobilePhoneNumber": obfuscate_all(),
            "passengerName": obfuscate_all(),
            "phoneNumber": obfuscate_all(),
            "street": obfuscate_all(),
            "workPhoneNumber": obfuscate_all(),
            "zip": obfuscate_all(),
            "cardNumber": obfuscate_all_but_last(4),
            "expiryDate": obfuscate_all_but_last(2),
            "cvv": obfuscate_all(),
            "iban": obfuscate_all_but_last(4),
            "accountNumber": obfuscate_all_but_last(4),
            "reformattedAccountNumber": obfuscate_all_but_last(4),
            "bin": obfuscate_all_but_first(6),
            "value": obfuscate_all(),
            "keyId": obfuscate_with_fixed_length(8),
            "secretKey": obfuscate_with_fixed_length(8),
            "publicKey": obfuscate_with_fixed_length(8),
            "userAuthenticationToken": obfuscate_with_fixed_length(8),
            "encryptedPayload": obfuscate_with_fixed_length(8),
            "decryptedPayload": obfuscate_with_fixed_length(8),
            "encryptedCustomerInput": obfuscate_with_fixed_length(8),
            "networkToken": obfuscate_all_but_last(4),
            "dpan": obfuscate_all_but_last(4),
            "tokenExpiryDate": obfuscate_all_but_last(2),
            "cryptogram": obfuscate_with_fixed_length(8),
            "cavv": obfuscate_with_fixed_length(8),
            "xid": obfuscate_with_fixed_length(8),
            "secret": obfuscate_with_fixed_length(8),
            "encryptionKey": obfuscate_with_fixed_length(8),
            "ephemeralKey": obfuscate_with_fixed_length(8),
            "sessionToken": obfuscate_with_fixed_length(8),
            "pairingToken": obfuscate_with_fixed_length(8),
            "paymentRequestToken": obfuscate_with_fixed_length(8),
            "surname": obfuscate_all(),
            "surnamePrefix": obfuscate_all(),
            "cardHolderName": obfuscate_all(),
            "accountHolderName": obfuscate_all(),
            "fiscalNumber": obfuscate_all(),
            "birthZipCode": obfuscate_all(),
            "bankAccountIban": obfuscate_all_but_last(4),
            "paymentIBAN": obfuscate_all_but_last(4),
            "encryptedCardNumber": obfuscate_with_fixed_length(8),
            "encryptedPaymentData": obfuscate_with_fixed_length(8),
            "driverTaxNumber": obfuscate_all(),
            "driverIdentificationNumber": obfuscate_all(),
            "loyaltyCardNumber": obfuscate_all(),
            "renterName": obfuscate_all(),
            "recipientName": obfuscate_all(),
        }
        if additional_rules:
            for name, rule in additional_rules.items():
                self.__obfuscation_rules[name] = rule

        property_names = tuple(self.__obfuscation_rules.keys())
        self.__property_pattern = self.__build_property_pattern(property_names)

    @staticmethod
    def __build_property_pattern(property_names: Sequence[str]) -> Pattern[str]:
        if not property_names:
            return re.compile("$^")
        s = "([\"'])("
        for p in property_names:
            s += '|' + re.escape(p)
        # Groups: 1: quote of the property name, 2: property name, 3: quote of the value, 4: quoted value,
        # 5: non-quoted value.
        s += ")\\1\\s*:\\s*(?:([\"'])((?:\\\\.|(?!\\3)[^\\\\])*)\\3|([^\"'\\s\\[\\{]((?!,)\\S)*))"
        return re.compile(s, re.DOTALL)

    def __obfuscate_value(self, property_name: str, value: str) -> str:
        obfuscation_rule = self.__obfuscation_rules.get(property_name)
        if obfuscation_rule:
            return obfuscation_rule(value)
        return value

    def obfuscate_body(self, body: str | bytes | None, charset: str | None = None) -> str | None:
        """
        Obfuscates the body from the given stream as necessary.
        :param body: The body to obfuscate, as string or bytes.
        :param charset: The charset to use to read the body bytes.
        """
        if body is None:
            return None
        if isinstance(body, bytes):
            body = body.decode(charset or "utf-8")

        if not body:
            return ""
        index = 0
        s_obfuscate = ""
        matcher = self.__property_pattern.finditer(body)
        for x in matcher:
            property_name = x.group(2)
            value = x.group(4)
            value_start = x.start(4)
            value_end = x.end(4)
            if not value:
                value = x.group(5)
                value_start = x.start(5)
                value_end = x.end(5)
            obfuscated_value = self.__obfuscate_value(property_name, value)
            s_obfuscate += body[index:value_start] + obfuscated_value
            index = value_end
        return s_obfuscate + body[index:]

    @staticmethod
    def default_body_obfuscator() -> 'BodyObfuscator':
        return _DEFAULT_BODY_OBFUSCATOR


_DEFAULT_BODY_OBFUSCATOR = BodyObfuscator()

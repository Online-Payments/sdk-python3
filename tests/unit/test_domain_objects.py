import copy
import pickle
import unittest

from onlinepayments.sdk.communication.metadata_provider import MetadataProvider
from onlinepayments.sdk.domain.airline_passenger import AirlinePassenger
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.card import Card
from onlinepayments.sdk.domain.card_payment_method_specific_input import CardPaymentMethodSpecificInput
from onlinepayments.sdk.domain.create_payment_request import CreatePaymentRequest
from onlinepayments.sdk.domain.data_object import DataObject
from onlinepayments.sdk.domain.detokenized_token_response import DetokenizedTokenResponse
from onlinepayments.sdk.domain.mobile_payment_data import MobilePaymentData
from onlinepayments.sdk.domain.network_token_data import NetworkTokenData
from onlinepayments.sdk.domain.order import Order
from onlinepayments.sdk.domain.shopping_cart_extension import ShoppingCartExtension
from onlinepayments.sdk.domain.validate_credentials_request import ValidateCredentialsRequest
from onlinepayments.sdk.domain.web_hooks_event import WebhooksEvent
from onlinepayments.sdk.json.default_marshaller import DefaultMarshaller
from onlinepayments.sdk.log.body_obfuscator import BodyObfuscator


class _DictionaryObject(DataObject):
    __slots__ = ("__dictionary",)

    def __init__(self, dictionary: dict):
        self.__dictionary = dictionary

    def to_dictionary(self) -> dict:
        return dict(self.__dictionary)


class _FailingObject(DataObject):
    __slots__ = ()

    def to_dictionary(self) -> dict:
        raise RuntimeError("to_dictionary failed")


def _create_payment_request_with_constructors() -> CreatePaymentRequest:
    return CreatePaymentRequest(
        order=Order(
            amount_of_money=AmountOfMoney(currency_code="EUR", amount=125000),
        ),
        card_payment_method_specific_input=CardPaymentMethodSpecificInput(
            card=Card(cvv="123", card_number="5300000000000006", expiry_date="0124", cardholder_name="John Doe"),
            payment_product_id=3,
        ),
    )


def _create_payment_request_with_setters() -> CreatePaymentRequest:
    amount_of_money = AmountOfMoney()
    amount_of_money.currency_code = "EUR"
    amount_of_money.amount = 125000
    order = Order()
    order.amount_of_money = amount_of_money

    card = Card()
    card.cvv = "123"
    card.card_number = "5300000000000006"
    card.expiry_date = "0124"
    card.cardholder_name = "John Doe"
    card_payment_method_specific_input = CardPaymentMethodSpecificInput()
    card_payment_method_specific_input.card = card
    card_payment_method_specific_input.payment_product_id = 3

    payment_request = CreatePaymentRequest()
    payment_request.order = order
    payment_request.card_payment_method_specific_input = card_payment_method_specific_input
    return payment_request


class DomainObjectTest(unittest.TestCase):

    def test_ConstructingWithNamedArguments_DefaultScenario_SetFields(self):
        amount_of_money = AmountOfMoney(amount=1, currency_code="EUR")
        self.assertEqual({"amount": 1, "currencyCode": "EUR"}, amount_of_money.to_dictionary())

    def test_ConstructingWithoutArguments_DefaultScenario_SetAllFieldsToNone(self):
        amount_of_money = AmountOfMoney()
        self.assertIsNone(amount_of_money.amount)
        self.assertIsNone(amount_of_money.currency_code)
        self.assertEqual({}, amount_of_money.to_dictionary())

    def test_ConstructingWithPositionalArguments_DefaultScenario_RaiseTypeError(self):
        with self.assertRaises(TypeError):
            AmountOfMoney(1, "EUR")

    def test_ConstructingWithUnknownArgument_DefaultScenario_RaiseTypeError(self):
        with self.assertRaises(TypeError):
            AmountOfMoney(currancy_code="EUR")

    def test_SettingUnknownAttribute_DefaultScenario_RaiseAttributeError(self):
        amount_of_money = AmountOfMoney()
        with self.assertRaises(AttributeError):
            amount_of_money.currancy_code = "EUR"

    def test_GettingInstanceDictionary_DefaultScenario_NotExist(self):
        self.assertFalse(hasattr(AmountOfMoney(), "__dict__"))

    def test_ConstructingNestedRequest_DefaultScenario_ProduceSameJsonAsSetters(self):
        marshaller = DefaultMarshaller.instance()
        self.assertEqual(marshaller.marshal(_create_payment_request_with_setters()),
                         marshaller.marshal(_create_payment_request_with_constructors()))

    def test_UnmarshallingResponse_DefaultScenario_PopulateFieldsFromDictionary(self):
        amount_of_money = DefaultMarshaller.instance().unmarshal('{"amount": 1, "currencyCode": "EUR"}',
                                                                 AmountOfMoney)
        self.assertEqual(1, amount_of_money.amount)
        self.assertEqual("EUR", amount_of_money.currency_code)

    def test_Copying_DefaultScenario_PreserveFields(self):
        payment_request = _create_payment_request_with_constructors()

        shallow_copy = copy.copy(payment_request)
        deep_copy = copy.deepcopy(payment_request)

        self.assertEqual(payment_request.to_dictionary(), shallow_copy.to_dictionary())
        self.assertIs(payment_request.order, shallow_copy.order)
        self.assertEqual(payment_request.to_dictionary(), deep_copy.to_dictionary())
        self.assertIsNot(payment_request.order, deep_copy.order)

    def test_Pickling_DefaultScenario_PreserveFields(self):
        payment_request = _create_payment_request_with_constructors()
        unpickled = pickle.loads(pickle.dumps(payment_request))
        self.assertIsInstance(unpickled, CreatePaymentRequest)
        self.assertEqual(payment_request.to_dictionary(), unpickled.to_dictionary())

    def test_ConvertingToString_DefaultScenario_ShowClassNameAndMaskedFields(self):
        card = Card(cvv="123", card_number="5300000000000006", expiry_date="0124", cardholder_name="John Doe")
        self.assertEqual('Card({"cardNumber": "************0006", "cardholderName": "********", '
                         '"cvv": "***", "expiryDate": "**24"})', repr(card))

    def test_ConvertingToString_ValueEndingWithBackslash_MaskFollowingFields(self):
        card = Card(cvv="123", card_number="5300000000000006", cardholder_name="John\\")
        self.assertEqual('Card({"cardNumber": "************0006", "cardholderName": "******", "cvv": "***"})',
                         repr(card))

    def test_ConvertingToString_NetworkTokenData_MaskTokenCryptogramAndExpiryDate(self):
        data = NetworkTokenData(network_token="5555444433332222", cryptogram="AAABBBCCC", token_expiry_date="1230",
                                eci=5)
        self.assertEqual('NetworkTokenData({"cryptogram": "********", "eci": 5, "networkToken": "************2222", '
                         '"tokenExpiryDate": "**30"})', repr(data))

    def test_ConvertingToString_MobilePaymentData_MaskDpan(self):
        data = MobilePaymentData(dpan="5555444433332222")
        self.assertEqual('MobilePaymentData({"dpan": "************2222"})', repr(data))

    def test_ConvertingToString_AirlinePassenger_MaskSurname(self):
        passenger = AirlinePassenger(first_name="Ann", surname="Smith", surname_prefix="van")
        self.assertEqual('AirlinePassenger({"firstName": "***", "surname": "*****", "surnamePrefix": "***"})',
                         repr(passenger))

    def test_ConvertingToString_ValidateCredentialsRequest_MaskWebhookSecret(self):
        request = ValidateCredentialsRequest(key="key-id", secret="topsecret")
        self.assertNotIn("topsecret", repr(request))
        self.assertEqual('ValidateCredentialsRequest({"key": "key-id", "secret": "********"})', repr(request))

    def test_ConvertingToString_DetokenizedTokenResponse_MaskHolderNameAndEncryptedCardNumber(self):
        response = DetokenizedTokenResponse(card_holder_name="John Doe", encrypted_card_number="ZW5jcnlwdGVk")
        self.assertEqual('DetokenizedTokenResponse({"cardHolderName": "********", '
                         '"encryptedCardNumber": "********"})', repr(response))

    def test_ConvertingToString_DefaultScenario_OmitFieldsWithoutValue(self):
        self.assertEqual('AmountOfMoney({"amount": 1})', repr(AmountOfMoney(amount=1)))

    def test_ConvertingToString_DefaultScenario_NotContainOriginalValueForAnyObfuscationRule(self):
        property_names = BodyObfuscator.default_body_obfuscator()._BodyObfuscator__obfuscation_rules.keys()
        for property_name in property_names:
            with self.subTest(property_name=property_name):
                value = "sensitive-value-1234567890"
                text = repr(_DictionaryObject({property_name: value}))
                self.assertNotIn(value, text)

    def test_ConvertingToString_DefaultScenario_FallBackToDefaultRepresentationOnError(self):
        text = repr(_FailingObject())
        self.assertTrue(text.startswith("<"))
        self.assertIn("_FailingObject object at", text)


class HandWrittenDomainObjectTest(unittest.TestCase):

    def test_ShoppingCartExtension_DefaultScenario_RejectUnknownAttributes(self):
        shopping_cart_extension = ShoppingCartExtension("Creator", "Name", "1.0")
        with self.assertRaises(AttributeError):
            shopping_cart_extension.unknown_attribute = "value"

    def test_ShoppingCartExtension_DefaultScenario_SupportCopyAndPickle(self):
        shopping_cart_extension = ShoppingCartExtension("Creator", "Name", "1.0", "ExtensionId")
        expected = shopping_cart_extension.to_dictionary()
        self.assertEqual(expected, copy.deepcopy(shopping_cart_extension).to_dictionary())
        self.assertEqual(expected, pickle.loads(pickle.dumps(shopping_cart_extension)).to_dictionary())

    def test_WebhooksEvent_DefaultScenario_ConstructWithNamedArgumentsAndRejectUnknownAttributes(self):
        event = WebhooksEvent(api_version="v1", id="event-id")
        self.assertEqual({"apiVersion": "v1", "id": "event-id"}, event.to_dictionary())
        with self.assertRaises(AttributeError):
            event.unknown_attribute = "value"

    def test_ServerMetaInfo_DefaultScenario_ConstructWithNamedArguments(self):
        server_meta_info = MetadataProvider.ServerMetaInfo(platform_identifier="Platform", sdk_identifier="SDK",
                                                           sdk_creator="Creator", integrator="Integrator")
        self.assertEqual({"platformIdentifier": "Platform", "sdkIdentifier": "SDK", "sdkCreator": "Creator",
                          "integrator": "Integrator"}, server_meta_info.to_dictionary())


if __name__ == '__main__':
    unittest.main()

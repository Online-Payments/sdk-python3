#
# This file was automatically generated.
#
from .data_object import DataObject


class CardPaymentMethodSpecificInputForHostedCheckout(DataObject):

    __slots__ = (
        "__click_to_pay",
        "__group_cards",
        "__payment_product_preferred_order",
        "__tokenization_mode",
    )

    __click_to_pay: bool | None
    __group_cards: bool | None
    __payment_product_preferred_order: list[int] | None
    __tokenization_mode: str | None

    def __init__(
        self,
        *,
        click_to_pay: bool | None = None,
        group_cards: bool | None = None,
        payment_product_preferred_order: list[int] | None = None,
        tokenization_mode: str | None = None,
    ) -> None:
        self.click_to_pay = click_to_pay
        self.group_cards = group_cards
        self.payment_product_preferred_order = payment_product_preferred_order
        self.tokenization_mode = tokenization_mode

    @property
    def click_to_pay(self) -> bool | None:
        """
        * true - Default - Hosted Checkout will show Click to Pay, with cards grouped as one payment method
        * false - Hosted Checkout will show cards as separate payment methods without Click to Pay

        Type: bool
        """
        return self.__click_to_pay

    @click_to_pay.setter
    def click_to_pay(self, value: bool | None) -> None:
        self.__click_to_pay = value

    @property
    def group_cards(self) -> bool | None:
        """
        * true - Hosted Checkout will allow to show cards grouped as one payment method
        * false - Default - Hosted Checkout will show cards as separate payment methods

        Type: bool
        """
        return self.__group_cards

    @group_cards.setter
    def group_cards(self, value: bool | None) -> None:
        self.__group_cards = value

    @property
    def payment_product_preferred_order(self) -> list[int] | None:
        """
        | This array contains the payment product identifiers representing the brands. For co-badged cards, this displays their available brands in the order defined by this array, when groupCards is activated.

        Type: list[int]
        """
        return self.__payment_product_preferred_order

    @payment_product_preferred_order.setter
    def payment_product_preferred_order(self, value: list[int] | None) -> None:
        self.__payment_product_preferred_order = value

    @property
    def tokenization_mode(self) -> str | None:
        """
        | Controls the generation and use of a token within a hosted checkout session.
        
        * createWithConsent - Presents the payer with a capture consent checkbox to decide whether they would like to tokenize their payment information for future use.
        * createAlways - Tokenizes the payment information automatically without presenting the capture consent checkbox to the payer; please ensure consent is captured on your interface.
        * useExplicitly - The payer can only use the token supplied in cardpaymentmethodspecificinput.token; if the token is invalid or no token is provided, the request will fail.
        * noTokenization - The payer's payment information will not be tokenized and the payer will not be presented with the ability to tokenize their payment information; use this for one-off payments. Note: This property is not allowed when cardpaymentmethodspecificinput.tokenize is specified.

        Type: str
        """
        return self.__tokenization_mode

    @tokenization_mode.setter
    def tokenization_mode(self, value: str | None) -> None:
        self.__tokenization_mode = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.click_to_pay is not None:
            dictionary['clickToPay'] = self.click_to_pay
        if self.group_cards is not None:
            dictionary['groupCards'] = self.group_cards
        if self.payment_product_preferred_order is not None:
            dictionary['paymentProductPreferredOrder'] = []
            for element in self.payment_product_preferred_order:
                if element is not None:
                    dictionary['paymentProductPreferredOrder'].append(element)
        if self.tokenization_mode is not None:
            dictionary['tokenizationMode'] = self.tokenization_mode
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardPaymentMethodSpecificInputForHostedCheckout':
        super().from_dictionary(dictionary)
        if 'clickToPay' in dictionary:
            self.click_to_pay = dictionary['clickToPay']
        if 'groupCards' in dictionary:
            self.group_cards = dictionary['groupCards']
        if 'paymentProductPreferredOrder' in dictionary:
            if not isinstance(dictionary['paymentProductPreferredOrder'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['paymentProductPreferredOrder']))
            self.payment_product_preferred_order = []
            for element in dictionary['paymentProductPreferredOrder']:
                self.payment_product_preferred_order.append(element)
        if 'tokenizationMode' in dictionary:
            self.tokenization_mode = dictionary['tokenizationMode']
        return self

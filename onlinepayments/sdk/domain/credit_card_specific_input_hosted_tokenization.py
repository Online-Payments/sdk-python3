#
# This file was automatically generated.
#
from .credit_card_validation_rules import CreditCardValidationRules
from .data_object import DataObject


class CreditCardSpecificInputHostedTokenization(DataObject):

    __slots__ = (
        "__validation_rules",
        "__payment_product_preferred_order",
    )

    __validation_rules: CreditCardValidationRules | None
    __payment_product_preferred_order: list[int] | None

    def __init__(
        self,
        *,
        validation_rules: CreditCardValidationRules | None = None,
        payment_product_preferred_order: list[int] | None = None,
    ) -> None:
        self.validation_rules = validation_rules
        self.payment_product_preferred_order = payment_product_preferred_order

    @property
    def validation_rules(self) -> CreditCardValidationRules | None:
        """
        | Object containing specific validation rules for creditCard.

        Type: :class:`onlinepayments.sdk.domain.credit_card_validation_rules.CreditCardValidationRules`
        """
        return self.__validation_rules

    @validation_rules.setter
    def validation_rules(self, value: CreditCardValidationRules | None) -> None:
        self.__validation_rules = value

    @property
    def payment_product_preferred_order(self) -> list[int] | None:
        """
        | This array contains the payment product identifiers representing the brands. For co-badged cards, this displays their available brands in the order defined by this array.

        Type: list[int]
        """
        return self.__payment_product_preferred_order

    @payment_product_preferred_order.setter
    def payment_product_preferred_order(self, value: list[int] | None) -> None:
        self.__payment_product_preferred_order = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.validation_rules is not None:
            dictionary['ValidationRules'] = self.validation_rules.to_dictionary()
        if self.payment_product_preferred_order is not None:
            dictionary['paymentProductPreferredOrder'] = []
            for element in self.payment_product_preferred_order:
                if element is not None:
                    dictionary['paymentProductPreferredOrder'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreditCardSpecificInputHostedTokenization':
        super().from_dictionary(dictionary)
        if 'ValidationRules' in dictionary:
            if not isinstance(dictionary['ValidationRules'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['ValidationRules']))
            value = CreditCardValidationRules()
            self.validation_rules = value.from_dictionary(dictionary['ValidationRules'])
        if 'paymentProductPreferredOrder' in dictionary:
            if not isinstance(dictionary['paymentProductPreferredOrder'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['paymentProductPreferredOrder']))
            self.payment_product_preferred_order = []
            for element in dictionary['paymentProductPreferredOrder']:
                self.payment_product_preferred_order.append(element)
        return self

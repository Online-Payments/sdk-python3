#
# This file was automatically generated.
#
from .additional_order_input import AdditionalOrderInput
from .amount_of_money import AmountOfMoney
from .customer import Customer
from .data_object import DataObject
from .discount import Discount
from .order_references import OrderReferences
from .shipping import Shipping
from .shopping_cart import ShoppingCart
from .surcharge_specific_input import SurchargeSpecificInput


class Order(DataObject):

    __slots__ = (
        "__additional_input",
        "__amount_of_money",
        "__customer",
        "__discount",
        "__references",
        "__shipping",
        "__shopping_cart",
        "__surcharge_specific_input",
        "__tax_percentage",
        "__total_tax_amount",
    )

    __additional_input: AdditionalOrderInput | None
    __amount_of_money: AmountOfMoney | None
    __customer: Customer | None
    __discount: Discount | None
    __references: OrderReferences | None
    __shipping: Shipping | None
    __shopping_cart: ShoppingCart | None
    __surcharge_specific_input: SurchargeSpecificInput | None
    __tax_percentage: float | None
    __total_tax_amount: int | None

    def __init__(
        self,
        *,
        additional_input: AdditionalOrderInput | None = None,
        amount_of_money: AmountOfMoney | None = None,
        customer: Customer | None = None,
        discount: Discount | None = None,
        references: OrderReferences | None = None,
        shipping: Shipping | None = None,
        shopping_cart: ShoppingCart | None = None,
        surcharge_specific_input: SurchargeSpecificInput | None = None,
        tax_percentage: float | None = None,
        total_tax_amount: int | None = None,
    ) -> None:
        self.additional_input = additional_input
        self.amount_of_money = amount_of_money
        self.customer = customer
        self.discount = discount
        self.references = references
        self.shipping = shipping
        self.shopping_cart = shopping_cart
        self.surcharge_specific_input = surcharge_specific_input
        self.tax_percentage = tax_percentage
        self.total_tax_amount = total_tax_amount

    @property
    def additional_input(self) -> AdditionalOrderInput | None:
        """
        | This object contains additional input on the order.

        Type: :class:`onlinepayments.sdk.domain.additional_order_input.AdditionalOrderInput`
        """
        return self.__additional_input

    @additional_input.setter
    def additional_input(self, value: AdditionalOrderInput | None) -> None:
        self.__additional_input = value

    @property
    def amount_of_money(self) -> AmountOfMoney | None:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value: AmountOfMoney | None) -> None:
        self.__amount_of_money = value

    @property
    def customer(self) -> Customer | None:
        """
        | Object containing the details of the customer

        Type: :class:`onlinepayments.sdk.domain.customer.Customer`
        """
        return self.__customer

    @customer.setter
    def customer(self, value: Customer | None) -> None:
        self.__customer = value

    @property
    def discount(self) -> Discount | None:
        """
        | Object to apply a discount to the total basket by adding a discount line.

        Type: :class:`onlinepayments.sdk.domain.discount.Discount`
        """
        return self.__discount

    @discount.setter
    def discount(self, value: Discount | None) -> None:
        self.__discount = value

    @property
    def references(self) -> OrderReferences | None:
        """
        | Object that holds all reference properties that are linked to this transaction

        Type: :class:`onlinepayments.sdk.domain.order_references.OrderReferences`
        """
        return self.__references

    @references.setter
    def references(self, value: OrderReferences | None) -> None:
        self.__references = value

    @property
    def shipping(self) -> Shipping | None:
        """
        | Object containing information regarding shipping / delivery

        Type: :class:`onlinepayments.sdk.domain.shipping.Shipping`
        """
        return self.__shipping

    @shipping.setter
    def shipping(self, value: Shipping | None) -> None:
        self.__shipping = value

    @property
    def shopping_cart(self) -> ShoppingCart | None:
        """
        | Shopping cart data, including items and specific amounts.

        Type: :class:`onlinepayments.sdk.domain.shopping_cart.ShoppingCart`
        """
        return self.__shopping_cart

    @shopping_cart.setter
    def shopping_cart(self, value: ShoppingCart | None) -> None:
        self.__shopping_cart = value

    @property
    def surcharge_specific_input(self) -> SurchargeSpecificInput | None:
        """
        | Object containing specific input required to apply surcharging to an order.

        Type: :class:`onlinepayments.sdk.domain.surcharge_specific_input.SurchargeSpecificInput`
        """
        return self.__surcharge_specific_input

    @surcharge_specific_input.setter
    def surcharge_specific_input(self, value: SurchargeSpecificInput | None) -> None:
        self.__surcharge_specific_input = value

    @property
    def tax_percentage(self) -> float | None:
        """
        | tax percentage, in hundredths of a percent. For example, for a tax percentage of 21%, this field should be set to 2100. Omit if not applicable or not known.

        Type: float
        """
        return self.__tax_percentage

    @tax_percentage.setter
    def tax_percentage(self, value: float | None) -> None:
        self.__tax_percentage = value

    @property
    def total_tax_amount(self) -> int | None:
        """
        | Tax amount, in minor currency units of the order. Omit if not applicable or not known. This amount is assumed to be included in the order.AmountOfMoney for the payment. There is no validation on this field, outside the fact the amount should be lower than the total payment amount.

        Type: int
        """
        return self.__total_tax_amount

    @total_tax_amount.setter
    def total_tax_amount(self, value: int | None) -> None:
        self.__total_tax_amount = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.additional_input is not None:
            dictionary['additionalInput'] = self.additional_input.to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.customer is not None:
            dictionary['customer'] = self.customer.to_dictionary()
        if self.discount is not None:
            dictionary['discount'] = self.discount.to_dictionary()
        if self.references is not None:
            dictionary['references'] = self.references.to_dictionary()
        if self.shipping is not None:
            dictionary['shipping'] = self.shipping.to_dictionary()
        if self.shopping_cart is not None:
            dictionary['shoppingCart'] = self.shopping_cart.to_dictionary()
        if self.surcharge_specific_input is not None:
            dictionary['surchargeSpecificInput'] = self.surcharge_specific_input.to_dictionary()
        if self.tax_percentage is not None:
            dictionary['taxPercentage'] = self.tax_percentage
        if self.total_tax_amount is not None:
            dictionary['totalTaxAmount'] = self.total_tax_amount
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'Order':
        super().from_dictionary(dictionary)
        if 'additionalInput' in dictionary:
            if not isinstance(dictionary['additionalInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['additionalInput']))
            value = AdditionalOrderInput()
            self.additional_input = value.from_dictionary(dictionary['additionalInput'])
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = Customer()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'discount' in dictionary:
            if not isinstance(dictionary['discount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['discount']))
            value = Discount()
            self.discount = value.from_dictionary(dictionary['discount'])
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = OrderReferences()
            self.references = value.from_dictionary(dictionary['references'])
        if 'shipping' in dictionary:
            if not isinstance(dictionary['shipping'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['shipping']))
            value = Shipping()
            self.shipping = value.from_dictionary(dictionary['shipping'])
        if 'shoppingCart' in dictionary:
            if not isinstance(dictionary['shoppingCart'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['shoppingCart']))
            value = ShoppingCart()
            self.shopping_cart = value.from_dictionary(dictionary['shoppingCart'])
        if 'surchargeSpecificInput' in dictionary:
            if not isinstance(dictionary['surchargeSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['surchargeSpecificInput']))
            value = SurchargeSpecificInput()
            self.surcharge_specific_input = value.from_dictionary(dictionary['surchargeSpecificInput'])
        if 'taxPercentage' in dictionary:
            self.tax_percentage = dictionary['taxPercentage']
        if 'totalTaxAmount' in dictionary:
            self.total_tax_amount = dictionary['totalTaxAmount']
        return self

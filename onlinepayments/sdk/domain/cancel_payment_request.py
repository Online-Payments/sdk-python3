#
# This file was automatically generated.
#
from .amount_of_money import AmountOfMoney
from .data_object import DataObject
from .line_item_detail import LineItemDetail
from .operation_payment_references import OperationPaymentReferences
from .shipping_detail import ShippingDetail


class CancelPaymentRequest(DataObject):

    __slots__ = (
        "__amount_of_money",
        "__is_final",
        "__line_item_details",
        "__operation_references",
        "__shipping",
    )

    __amount_of_money: AmountOfMoney | None
    __is_final: bool | None
    __line_item_details: list[LineItemDetail] | None
    __operation_references: OperationPaymentReferences | None
    __shipping: ShippingDetail | None

    def __init__(
        self,
        *,
        amount_of_money: AmountOfMoney | None = None,
        is_final: bool | None = None,
        line_item_details: list[LineItemDetail] | None = None,
        operation_references: OperationPaymentReferences | None = None,
        shipping: ShippingDetail | None = None,
    ) -> None:
        self.amount_of_money = amount_of_money
        self.is_final = is_final
        self.line_item_details = line_item_details
        self.operation_references = operation_references
        self.shipping = shipping

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
    def is_final(self) -> bool | None:
        """
        | This property indicates whether this will be the final operation. The default value for this property is false.

        Type: bool
        """
        return self.__is_final

    @is_final.setter
    def is_final(self, value: bool | None) -> None:
        self.__is_final = value

    @property
    def line_item_details(self) -> list[LineItemDetail] | None:
        """
        | List of lineItemIds and quantities for capture/refund/cancellation.

        Type: list[:class:`onlinepayments.sdk.domain.line_item_detail.LineItemDetail`]
        """
        return self.__line_item_details

    @line_item_details.setter
    def line_item_details(self, value: list[LineItemDetail] | None) -> None:
        self.__line_item_details = value

    @property
    def operation_references(self) -> OperationPaymentReferences | None:
        """
        | Object that holds all reference properties that are linked to this transaction

        Type: :class:`onlinepayments.sdk.domain.operation_payment_references.OperationPaymentReferences`
        """
        return self.__operation_references

    @operation_references.setter
    def operation_references(self, value: OperationPaymentReferences | None) -> None:
        self.__operation_references = value

    @property
    def shipping(self) -> ShippingDetail | None:
        """
        | Object containing the details of the shipping of the order

        Type: :class:`onlinepayments.sdk.domain.shipping_detail.ShippingDetail`
        """
        return self.__shipping

    @shipping.setter
    def shipping(self, value: ShippingDetail | None) -> None:
        self.__shipping = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.is_final is not None:
            dictionary['isFinal'] = self.is_final
        if self.line_item_details is not None:
            dictionary['lineItemDetails'] = []
            for element in self.line_item_details:
                if element is not None:
                    dictionary['lineItemDetails'].append(element.to_dictionary())
        if self.operation_references is not None:
            dictionary['operationReferences'] = self.operation_references.to_dictionary()
        if self.shipping is not None:
            dictionary['shipping'] = self.shipping.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CancelPaymentRequest':
        super().from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'isFinal' in dictionary:
            self.is_final = dictionary['isFinal']
        if 'lineItemDetails' in dictionary:
            if not isinstance(dictionary['lineItemDetails'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['lineItemDetails']))
            self.line_item_details = []
            for element in dictionary['lineItemDetails']:
                value = LineItemDetail()
                self.line_item_details.append(value.from_dictionary(element))
        if 'operationReferences' in dictionary:
            if not isinstance(dictionary['operationReferences'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['operationReferences']))
            value = OperationPaymentReferences()
            self.operation_references = value.from_dictionary(dictionary['operationReferences'])
        if 'shipping' in dictionary:
            if not isinstance(dictionary['shipping'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['shipping']))
            value = ShippingDetail()
            self.shipping = value.from_dictionary(dictionary['shipping'])
        return self

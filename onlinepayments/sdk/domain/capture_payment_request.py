#
# This file was automatically generated.
#
from .data_object import DataObject
from .line_item_detail import LineItemDetail
from .operation_payment_references import OperationPaymentReferences
from .payment_references import PaymentReferences
from .shipping_detail import ShippingDetail


class CapturePaymentRequest(DataObject):

    __slots__ = (
        "__amount",
        "__is_final",
        "__line_item_details",
        "__operation_references",
        "__references",
        "__shipping",
    )

    __amount: int | None
    __is_final: bool | None
    __line_item_details: list[LineItemDetail] | None
    __operation_references: OperationPaymentReferences | None
    __references: PaymentReferences | None
    __shipping: ShippingDetail | None

    def __init__(
        self,
        *,
        amount: int | None = None,
        is_final: bool | None = None,
        line_item_details: list[LineItemDetail] | None = None,
        operation_references: OperationPaymentReferences | None = None,
        references: PaymentReferences | None = None,
        shipping: ShippingDetail | None = None,
    ) -> None:
        self.amount = amount
        self.is_final = is_final
        self.line_item_details = line_item_details
        self.operation_references = operation_references
        self.references = references
        self.shipping = shipping

    @property
    def amount(self) -> int | None:
        """
        | Here you can specify the amount that you want to capture (specified in cents, where single digit currencies are presumed to have 2 digits). The amount can be lower than the amount that was authorized, but not higher. If left empty, the full amount will be captured and the request will be final. If the full amount is captured, the request will also be final.

        Type: int
        """
        return self.__amount

    @amount.setter
    def amount(self, value: int | None) -> None:
        self.__amount = value

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
    def references(self) -> PaymentReferences | None:
        """
        | Object that holds all reference properties that are linked to this transaction. **Deprecated for capture/refund**: Use operationReferences instead.

        Type: :class:`onlinepayments.sdk.domain.payment_references.PaymentReferences`
        """
        return self.__references

    @references.setter
    def references(self, value: PaymentReferences | None) -> None:
        self.__references = value

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
        if self.amount is not None:
            dictionary['amount'] = self.amount
        if self.is_final is not None:
            dictionary['isFinal'] = self.is_final
        if self.line_item_details is not None:
            dictionary['lineItemDetails'] = []
            for element in self.line_item_details:
                if element is not None:
                    dictionary['lineItemDetails'].append(element.to_dictionary())
        if self.operation_references is not None:
            dictionary['operationReferences'] = self.operation_references.to_dictionary()
        if self.references is not None:
            dictionary['references'] = self.references.to_dictionary()
        if self.shipping is not None:
            dictionary['shipping'] = self.shipping.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CapturePaymentRequest':
        super().from_dictionary(dictionary)
        if 'amount' in dictionary:
            self.amount = dictionary['amount']
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
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = PaymentReferences()
            self.references = value.from_dictionary(dictionary['references'])
        if 'shipping' in dictionary:
            if not isinstance(dictionary['shipping'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['shipping']))
            value = ShippingDetail()
            self.shipping = value.from_dictionary(dictionary['shipping'])
        return self

#
# This file was automatically generated.
#
from .amount_of_money import AmountOfMoney
from .data_object import DataObject
from .line_item_detail import LineItemDetail
from .omnichannel_refund_specific_input import OmnichannelRefundSpecificInput
from .operation_payment_references import OperationPaymentReferences
from .payment_references import PaymentReferences
from .refund_redirect_payment_method_specific_input import RefundRedirectPaymentMethodSpecificInput


class RefundRequest(DataObject):

    __slots__ = (
        "__amount_of_money",
        "__capture_id",
        "__is_final",
        "__line_item_details",
        "__omnichannel_refund_specific_input",
        "__operation_references",
        "__reason",
        "__references",
        "__refund_redirect_payment_method_specific_input",
    )

    __amount_of_money: AmountOfMoney | None
    __capture_id: str | None
    __is_final: bool | None
    __line_item_details: list[LineItemDetail] | None
    __omnichannel_refund_specific_input: OmnichannelRefundSpecificInput | None
    __operation_references: OperationPaymentReferences | None
    __reason: str | None
    __references: PaymentReferences | None
    __refund_redirect_payment_method_specific_input: RefundRedirectPaymentMethodSpecificInput | None

    def __init__(
        self,
        *,
        amount_of_money: AmountOfMoney | None = None,
        capture_id: str | None = None,
        is_final: bool | None = None,
        line_item_details: list[LineItemDetail] | None = None,
        omnichannel_refund_specific_input: OmnichannelRefundSpecificInput | None = None,
        operation_references: OperationPaymentReferences | None = None,
        reason: str | None = None,
        references: PaymentReferences | None = None,
        refund_redirect_payment_method_specific_input: RefundRedirectPaymentMethodSpecificInput | None = None,
    ) -> None:
        self.amount_of_money = amount_of_money
        self.capture_id = capture_id
        self.is_final = is_final
        self.line_item_details = line_item_details
        self.omnichannel_refund_specific_input = omnichannel_refund_specific_input
        self.operation_references = operation_references
        self.reason = reason
        self.references = references
        self.refund_redirect_payment_method_specific_input = refund_redirect_payment_method_specific_input

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
    def capture_id(self) -> str | None:
        """
        | The identifier of the capture that is used for partial refund. CaptureId is only necessary for Paypal/PostfinancePay multi-capture payments.

        Type: str
        """
        return self.__capture_id

    @capture_id.setter
    def capture_id(self, value: str | None) -> None:
        self.__capture_id = value

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
    def omnichannel_refund_specific_input(self) -> OmnichannelRefundSpecificInput | None:
        """
        | Object containing the additional refund details for an Omnichannel merchant

        Type: :class:`onlinepayments.sdk.domain.omnichannel_refund_specific_input.OmnichannelRefundSpecificInput`
        """
        return self.__omnichannel_refund_specific_input

    @omnichannel_refund_specific_input.setter
    def omnichannel_refund_specific_input(self, value: OmnichannelRefundSpecificInput | None) -> None:
        self.__omnichannel_refund_specific_input = value

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
    def reason(self) -> str | None:
        """
        | The reason for the refund. This will be available in our portal and reports for your information only. It will NOT appear in the consumer bank statement or yours.§

        Type: str
        """
        return self.__reason

    @reason.setter
    def reason(self, value: str | None) -> None:
        self.__reason = value

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
    def refund_redirect_payment_method_specific_input(self) -> RefundRedirectPaymentMethodSpecificInput | None:
        """
        | Object containing the specific input details for refunds for redirection payment methods.

        Type: :class:`onlinepayments.sdk.domain.refund_redirect_payment_method_specific_input.RefundRedirectPaymentMethodSpecificInput`
        """
        return self.__refund_redirect_payment_method_specific_input

    @refund_redirect_payment_method_specific_input.setter
    def refund_redirect_payment_method_specific_input(self, value: RefundRedirectPaymentMethodSpecificInput | None) -> None:
        self.__refund_redirect_payment_method_specific_input = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.amount_of_money is not None:
            dictionary['amountOfMoney'] = self.amount_of_money.to_dictionary()
        if self.capture_id is not None:
            dictionary['captureId'] = self.capture_id
        if self.is_final is not None:
            dictionary['isFinal'] = self.is_final
        if self.line_item_details is not None:
            dictionary['lineItemDetails'] = []
            for element in self.line_item_details:
                if element is not None:
                    dictionary['lineItemDetails'].append(element.to_dictionary())
        if self.omnichannel_refund_specific_input is not None:
            dictionary['omnichannelRefundSpecificInput'] = self.omnichannel_refund_specific_input.to_dictionary()
        if self.operation_references is not None:
            dictionary['operationReferences'] = self.operation_references.to_dictionary()
        if self.reason is not None:
            dictionary['reason'] = self.reason
        if self.references is not None:
            dictionary['references'] = self.references.to_dictionary()
        if self.refund_redirect_payment_method_specific_input is not None:
            dictionary['refundRedirectPaymentMethodSpecificInput'] = self.refund_redirect_payment_method_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'RefundRequest':
        super().from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'captureId' in dictionary:
            self.capture_id = dictionary['captureId']
        if 'isFinal' in dictionary:
            self.is_final = dictionary['isFinal']
        if 'lineItemDetails' in dictionary:
            if not isinstance(dictionary['lineItemDetails'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['lineItemDetails']))
            self.line_item_details = []
            for element in dictionary['lineItemDetails']:
                value = LineItemDetail()
                self.line_item_details.append(value.from_dictionary(element))
        if 'omnichannelRefundSpecificInput' in dictionary:
            if not isinstance(dictionary['omnichannelRefundSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['omnichannelRefundSpecificInput']))
            value = OmnichannelRefundSpecificInput()
            self.omnichannel_refund_specific_input = value.from_dictionary(dictionary['omnichannelRefundSpecificInput'])
        if 'operationReferences' in dictionary:
            if not isinstance(dictionary['operationReferences'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['operationReferences']))
            value = OperationPaymentReferences()
            self.operation_references = value.from_dictionary(dictionary['operationReferences'])
        if 'reason' in dictionary:
            self.reason = dictionary['reason']
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = PaymentReferences()
            self.references = value.from_dictionary(dictionary['references'])
        if 'refundRedirectPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['refundRedirectPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['refundRedirectPaymentMethodSpecificInput']))
            value = RefundRedirectPaymentMethodSpecificInput()
            self.refund_redirect_payment_method_specific_input = value.from_dictionary(dictionary['refundRedirectPaymentMethodSpecificInput'])
        return self

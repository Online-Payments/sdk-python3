#
# This file was automatically generated.
#
from .batch_metadata import BatchMetadata
from .cancel_payment_batch_request import CancelPaymentBatchRequest
from .capture_payment_batch_request import CapturePaymentBatchRequest
from .create_payment_link_request import CreatePaymentLinkRequest
from .create_payment_request import CreatePaymentRequest
from .create_payout_request import CreatePayoutRequest
from .data_object import DataObject
from .refund_payment_batch_request import RefundPaymentBatchRequest
from .subsequent_payment_batch_request import SubsequentPaymentBatchRequest


class SubmitBatchRequestBody(DataObject):

    __slots__ = (
        "__cancel_payments",
        "__capture_payments",
        "__create_payment_links",
        "__create_payments",
        "__create_payouts",
        "__header",
        "__refund_payments",
        "__subsequent_payments",
    )

    __cancel_payments: list[CancelPaymentBatchRequest] | None
    __capture_payments: list[CapturePaymentBatchRequest] | None
    __create_payment_links: list[CreatePaymentLinkRequest] | None
    __create_payments: list[CreatePaymentRequest] | None
    __create_payouts: list[CreatePayoutRequest] | None
    __header: BatchMetadata | None
    __refund_payments: list[RefundPaymentBatchRequest] | None
    __subsequent_payments: list[SubsequentPaymentBatchRequest] | None

    def __init__(
        self,
        *,
        cancel_payments: list[CancelPaymentBatchRequest] | None = None,
        capture_payments: list[CapturePaymentBatchRequest] | None = None,
        create_payment_links: list[CreatePaymentLinkRequest] | None = None,
        create_payments: list[CreatePaymentRequest] | None = None,
        create_payouts: list[CreatePayoutRequest] | None = None,
        header: BatchMetadata | None = None,
        refund_payments: list[RefundPaymentBatchRequest] | None = None,
        subsequent_payments: list[SubsequentPaymentBatchRequest] | None = None,
    ) -> None:
        self.cancel_payments = cancel_payments
        self.capture_payments = capture_payments
        self.create_payment_links = create_payment_links
        self.create_payments = create_payments
        self.create_payouts = create_payouts
        self.header = header
        self.refund_payments = refund_payments
        self.subsequent_payments = subsequent_payments

    @property
    def cancel_payments(self) -> list[CancelPaymentBatchRequest] | None:
        """
        | Array of cancel payment requests to be submitted in batch.

        Type: list[:class:`onlinepayments.sdk.domain.cancel_payment_batch_request.CancelPaymentBatchRequest`]
        """
        return self.__cancel_payments

    @cancel_payments.setter
    def cancel_payments(self, value: list[CancelPaymentBatchRequest] | None) -> None:
        self.__cancel_payments = value

    @property
    def capture_payments(self) -> list[CapturePaymentBatchRequest] | None:
        """
        | Array of capture payment requests to be submitted in batch.

        Type: list[:class:`onlinepayments.sdk.domain.capture_payment_batch_request.CapturePaymentBatchRequest`]
        """
        return self.__capture_payments

    @capture_payments.setter
    def capture_payments(self, value: list[CapturePaymentBatchRequest] | None) -> None:
        self.__capture_payments = value

    @property
    def create_payment_links(self) -> list[CreatePaymentLinkRequest] | None:
        """
        | An array containing multiple payment link generation requests that will be processed as a batch. Each item represents an individual payment link to be created.

        Type: list[:class:`onlinepayments.sdk.domain.create_payment_link_request.CreatePaymentLinkRequest`]
        """
        return self.__create_payment_links

    @create_payment_links.setter
    def create_payment_links(self, value: list[CreatePaymentLinkRequest] | None) -> None:
        self.__create_payment_links = value

    @property
    def create_payments(self) -> list[CreatePaymentRequest] | None:
        """
        | Array of payment creation requests to be submitted in batch.

        Type: list[:class:`onlinepayments.sdk.domain.create_payment_request.CreatePaymentRequest`]
        """
        return self.__create_payments

    @create_payments.setter
    def create_payments(self, value: list[CreatePaymentRequest] | None) -> None:
        self.__create_payments = value

    @property
    def create_payouts(self) -> list[CreatePayoutRequest] | None:
        """
        | Array of payout creation requests to be submitted in batch.

        Type: list[:class:`onlinepayments.sdk.domain.create_payout_request.CreatePayoutRequest`]
        """
        return self.__create_payouts

    @create_payouts.setter
    def create_payouts(self, value: list[CreatePayoutRequest] | None) -> None:
        self.__create_payouts = value

    @property
    def header(self) -> BatchMetadata | None:
        """
        | Type of operation, including the merchant batch reference and the total count of items in the batch

        Type: :class:`onlinepayments.sdk.domain.batch_metadata.BatchMetadata`
        """
        return self.__header

    @header.setter
    def header(self, value: BatchMetadata | None) -> None:
        self.__header = value

    @property
    def refund_payments(self) -> list[RefundPaymentBatchRequest] | None:
        """
        | Array of refund payment requests to be submitted in batch.

        Type: list[:class:`onlinepayments.sdk.domain.refund_payment_batch_request.RefundPaymentBatchRequest`]
        """
        return self.__refund_payments

    @refund_payments.setter
    def refund_payments(self, value: list[RefundPaymentBatchRequest] | None) -> None:
        self.__refund_payments = value

    @property
    def subsequent_payments(self) -> list[SubsequentPaymentBatchRequest] | None:
        """
        | Array of subsequent payment requests to be submitted in batch.

        Type: list[:class:`onlinepayments.sdk.domain.subsequent_payment_batch_request.SubsequentPaymentBatchRequest`]
        """
        return self.__subsequent_payments

    @subsequent_payments.setter
    def subsequent_payments(self, value: list[SubsequentPaymentBatchRequest] | None) -> None:
        self.__subsequent_payments = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.cancel_payments is not None:
            dictionary['cancelPayments'] = []
            for element in self.cancel_payments:
                if element is not None:
                    dictionary['cancelPayments'].append(element.to_dictionary())
        if self.capture_payments is not None:
            dictionary['capturePayments'] = []
            for element in self.capture_payments:
                if element is not None:
                    dictionary['capturePayments'].append(element.to_dictionary())
        if self.create_payment_links is not None:
            dictionary['createPaymentLinks'] = []
            for element in self.create_payment_links:
                if element is not None:
                    dictionary['createPaymentLinks'].append(element.to_dictionary())
        if self.create_payments is not None:
            dictionary['createPayments'] = []
            for element in self.create_payments:
                if element is not None:
                    dictionary['createPayments'].append(element.to_dictionary())
        if self.create_payouts is not None:
            dictionary['createPayouts'] = []
            for element in self.create_payouts:
                if element is not None:
                    dictionary['createPayouts'].append(element.to_dictionary())
        if self.header is not None:
            dictionary['header'] = self.header.to_dictionary()
        if self.refund_payments is not None:
            dictionary['refundPayments'] = []
            for element in self.refund_payments:
                if element is not None:
                    dictionary['refundPayments'].append(element.to_dictionary())
        if self.subsequent_payments is not None:
            dictionary['subsequentPayments'] = []
            for element in self.subsequent_payments:
                if element is not None:
                    dictionary['subsequentPayments'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SubmitBatchRequestBody':
        super().from_dictionary(dictionary)
        if 'cancelPayments' in dictionary:
            if not isinstance(dictionary['cancelPayments'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['cancelPayments']))
            self.cancel_payments = []
            for element in dictionary['cancelPayments']:
                value = CancelPaymentBatchRequest()
                self.cancel_payments.append(value.from_dictionary(element))
        if 'capturePayments' in dictionary:
            if not isinstance(dictionary['capturePayments'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['capturePayments']))
            self.capture_payments = []
            for element in dictionary['capturePayments']:
                value = CapturePaymentBatchRequest()
                self.capture_payments.append(value.from_dictionary(element))
        if 'createPaymentLinks' in dictionary:
            if not isinstance(dictionary['createPaymentLinks'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['createPaymentLinks']))
            self.create_payment_links = []
            for element in dictionary['createPaymentLinks']:
                value = CreatePaymentLinkRequest()
                self.create_payment_links.append(value.from_dictionary(element))
        if 'createPayments' in dictionary:
            if not isinstance(dictionary['createPayments'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['createPayments']))
            self.create_payments = []
            for element in dictionary['createPayments']:
                value = CreatePaymentRequest()
                self.create_payments.append(value.from_dictionary(element))
        if 'createPayouts' in dictionary:
            if not isinstance(dictionary['createPayouts'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['createPayouts']))
            self.create_payouts = []
            for element in dictionary['createPayouts']:
                value = CreatePayoutRequest()
                self.create_payouts.append(value.from_dictionary(element))
        if 'header' in dictionary:
            if not isinstance(dictionary['header'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['header']))
            value = BatchMetadata()
            self.header = value.from_dictionary(dictionary['header'])
        if 'refundPayments' in dictionary:
            if not isinstance(dictionary['refundPayments'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['refundPayments']))
            self.refund_payments = []
            for element in dictionary['refundPayments']:
                value = RefundPaymentBatchRequest()
                self.refund_payments.append(value.from_dictionary(element))
        if 'subsequentPayments' in dictionary:
            if not isinstance(dictionary['subsequentPayments'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['subsequentPayments']))
            self.subsequent_payments = []
            for element in dictionary['subsequentPayments']:
                value = SubsequentPaymentBatchRequest()
                self.subsequent_payments.append(value.from_dictionary(element))
        return self

import uuid

from onlinepayments.sdk.domain.submit_batch_request_body import SubmitBatchRequestBody
from onlinepayments.sdk.domain.batch_metadata import BatchMetadata


class SubmitBatchRequestBodyBuilder:

    def __init__(self):
        self._merchant_batch_reference = "Ref-" + uuid.uuid4().hex
        self._operation_type = None
        self._item_count = None
        self._create_payment_requests = None

    def with_merchant_batch_reference(self, merchant_batch_reference):
        self._merchant_batch_reference = merchant_batch_reference
        return self

    def with_operation_type(self, operation_type):
        self._operation_type = operation_type
        return self

    def with_item_count(self, item_count):
        self._item_count = item_count
        return self

    def with_create_payment_requests(self, create_payment_requests):
        self._create_payment_requests = create_payment_requests
        return self

    def build(self):
        header = BatchMetadata()
        header.merchant_batch_reference = self._merchant_batch_reference
        header.operation_type = self._operation_type
        header.item_count = self._item_count

        request = SubmitBatchRequestBody()
        request.header = header
        request.create_payments = self._create_payment_requests

        return request

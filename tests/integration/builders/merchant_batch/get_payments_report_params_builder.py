from onlinepayments.sdk.merchant.merchantbatch.get_payments_report_params import GetPaymentsReportParams


class GetPaymentsReportParamsBuilder:

    def __init__(self):
        self._cursor = None
        self._limit = None

    def with_cursor(self, cursor):
        self._cursor = cursor
        return self

    def with_limit(self, limit):
        self._limit = limit
        return self

    def build(self):
        params = GetPaymentsReportParams()
        if self._cursor is not None:
            params.cursor = self._cursor
        if self._limit is not None:
            params.limit = self._limit
        return params

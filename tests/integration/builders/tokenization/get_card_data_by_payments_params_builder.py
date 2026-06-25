from onlinepayments.sdk.merchant.tokenization.get_card_data_by_payments_params import GetCardDataByPaymentsParams


class GetCardDataByPaymentsParamsBuilder:

    def __init__(self):
        self._payments = None

    def with_payments(self, payments):
        self._payments = payments
        return self

    def build(self):
        params = GetCardDataByPaymentsParams()

        if self._payments is not None:
            for payment in self._payments:
                params.add_payments(payment)

        return params

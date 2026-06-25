from onlinepayments.sdk.merchant.tokenization.get_card_data_by_tokens_params import GetCardDataByTokensParams


class GetCardDataByTokensParamsBuilder:

    def __init__(self):
        self._tokens = None

    def with_tokens(self, tokens):
        self._tokens = tokens
        return self

    def build(self):
        params = GetCardDataByTokensParams()

        if self._tokens is not None:
            for token in self._tokens:
                params.add_tokens(token)

        return params

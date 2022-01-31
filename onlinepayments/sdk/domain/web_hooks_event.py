from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.payment_response import PaymentResponse
from onlinepayments.sdk.domain.payout_response import PayoutResponse
from onlinepayments.sdk.domain.refund_response import RefundResponse
from onlinepayments.sdk.domain.token_response import TokenResponse


class WebhooksEvent(DataObject):
    __api_version = None
    __id = None
    __created = None
    __merchant_id = None
    __type = None
    __payment = None
    __payout = None
    __refund = None
    __token = None

    @property
    def api_version(self) -> str:
        return self.__api_version

    @api_version.setter
    def api_version(self, api_version: str):
        self.__api_version = api_version

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def created(self) -> str:
        return self.__created

    @created.setter
    def created(self, created: str):
        self.__created = created

    @property
    def merchant_id(self) -> str:
        return self.__merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id: str):
        self.__merchant_id = merchant_id

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def payment(self) -> PaymentResponse:
        return self.__payment

    @payment.setter
    def payment(self, payment: PaymentResponse):
        self.__payment = payment

    @property
    def payout(self) -> PayoutResponse:
        return self.__payout

    @payout.setter
    def payout(self, payout: PayoutResponse):
        self.__payout = payout

    @property
    def refund(self) -> RefundResponse:
        return self.__refund

    @refund.setter
    def refund(self, refund: RefundResponse):
        self.__refund = refund

    @property
    def token(self) -> TokenResponse:
        return self.__token

    @token.setter
    def token(self, token: TokenResponse):
        self.__token = token

    def to_dictionary(self):
        dictionary = super(WebhooksEvent, self).to_dictionary()
        if self.__api_version is not None:
            dictionary['apiVersion'] = self.__api_version
        if self.__id is not None:
            dictionary['id'] = self.__id
        if self.__created is not None:
            dictionary['created'] = self.__created
        if self.__merchant_id is not None:
            dictionary['merchantId'] = self.__merchant_id
        if self.__type is not None:
            dictionary['type'] = self.__type
        if self.__payment is not None:
            dictionary['payment'] = self.__payment
        if self.__payout is not None:
            dictionary['payout'] = self.__payout
        if self.__refund is not None:
            dictionary['refund'] = self.__refund
        if self.__token is not None:
            dictionary['token'] = self.__token
        return dictionary

    def from_dictionary(self, dictionary):
        super(WebhooksEvent, self).from_dictionary(dictionary)
        if 'apiVersion' in dictionary:
            self.__api_version = dictionary['apiVersion']
        if 'id' in dictionary:
            self.__id = dictionary['id']
        if 'created' in dictionary:
            self.__created = dictionary['created']
        if 'merchantId' in dictionary:
            self.__merchant_id = dictionary['merchantId']
        if 'type' in dictionary:
            self.__type = dictionary['type']
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = PaymentResponse()
            self.__payment = value.from_dictionary(dictionary['payment'])
        if 'payout' in dictionary:
            if not isinstance(dictionary['payout'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payout']))
            value = PayoutResponse()
            self.__payout = value.from_dictionary(dictionary['payout'])
        if 'refund' in dictionary:
            if not isinstance(dictionary['refund'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['refund']))
            value = RefundResponse()
            self.__refund = value.from_dictionary(dictionary['refund'])
        if 'token' in dictionary:
            if not isinstance(dictionary['token'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['token']))
            value = TokenResponse()
            self.__token = value.from_dictionary(dictionary['token'])
        return self

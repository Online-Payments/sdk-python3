from .data_object import DataObject
from .get_batch_status_response import GetBatchStatusResponse
from .payment_link_response import PaymentLinkResponse
from .payment_response import PaymentResponse
from .payout_response import PayoutResponse
from .refund_response import RefundResponse
from .token_response import TokenResponse

class WebhooksEvent(DataObject):

    __slots__ = (
        "__api_version",
        "__created",
        "__id",
        "__merchant_id",
        "__type",
        "__direct_batch",
        "__payment_link",
        "__payment",
        "__payout",
        "__refund",
        "__token",
    )

    __api_version: str | None
    __created: str | None
    __id: str | None
    __merchant_id: str | None
    __type: str | None
    __direct_batch: GetBatchStatusResponse | None
    __payment_link: PaymentLinkResponse | None
    __payment: PaymentResponse | None
    __payout: PayoutResponse | None
    __refund: RefundResponse | None
    __token: TokenResponse | None

    def __init__(self, *,
                 api_version: str | None = None,
                 created: str | None = None,
                 id: str | None = None,
                 merchant_id: str | None = None,
                 type: str | None = None,
                 direct_batch: GetBatchStatusResponse | None = None,
                 payment_link: PaymentLinkResponse | None = None,
                 payment: PaymentResponse | None = None,
                 payout: PayoutResponse | None = None,
                 refund: RefundResponse | None = None,
                 token: TokenResponse | None = None) -> None:
        self.api_version = api_version
        self.created = created
        self.id = id
        self.merchant_id = merchant_id
        self.type = type
        self.direct_batch = direct_batch
        self.payment_link = payment_link
        self.payment = payment
        self.payout = payout
        self.refund = refund
        self.token = token

    @property
    def api_version(self) -> str | None:
        """
        Type: str
        """
        return self.__api_version

    @api_version.setter
    def api_version(self, value: str | None) -> None:
        self.__api_version = value

    @property
    def created(self) -> str | None:
        """
        Type: str
        """
        return self.__created

    @created.setter
    def created(self, value: str | None) -> None:
        self.__created = value

    @property
    def id(self) -> str | None:
        """
        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: str | None) -> None:
        self.__id = value

    @property
    def merchant_id(self) -> str | None:
        """
        Type: str
        """
        return self.__merchant_id

    @merchant_id.setter
    def merchant_id(self, value: str | None) -> None:
        self.__merchant_id = value

    @property
    def type(self) -> str | None:
        """
        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value: str | None) -> None:
        self.__type = value

    @property
    def direct_batch(self) -> GetBatchStatusResponse | None:
        """
        Type: GetBatchStatusResponse
        """
        return self.__direct_batch

    @direct_batch.setter
    def direct_batch(self, value: GetBatchStatusResponse | None) -> None:
        self.__direct_batch = value

    @property
    def payment_link(self) -> PaymentLinkResponse | None:
        """
        Type: PaymentLinkResponse
        """
        return self.__payment_link

    @payment_link.setter
    def payment_link(self, value: PaymentLinkResponse | None) -> None:
        self.__payment_link = value

    @property
    def payment(self) -> PaymentResponse | None:
        """
        Type: PaymentResponse
        """
        return self.__payment

    @payment.setter
    def payment(self, value: PaymentResponse | None) -> None:
        self.__payment = value

    @property
    def payout(self) -> PayoutResponse | None:
        """
        Type: PayoutResponse
        """
        return self.__payout

    @payout.setter
    def payout(self, value: PayoutResponse | None) -> None:
        self.__payout = value

    @property
    def refund(self) -> RefundResponse | None:
        """
        Type: RefundResponse
        """
        return self.__refund

    @refund.setter
    def refund(self, value: RefundResponse | None) -> None:
        self.__refund = value

    @property
    def token(self) -> TokenResponse | None:
        """
        Type: TokenResponse
        """
        return self.__token

    @token.setter
    def token(self, value: TokenResponse | None) -> None:
        self.__token = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.api_version is not None:
            dictionary['apiVersion'] = self.api_version
        if self.created is not None:
            dictionary['created'] = self.created
        if self.id is not None:
            dictionary['id'] = self.id
        if self.merchant_id is not None:
            dictionary['merchantId'] = self.merchant_id
        if self.type is not None:
            dictionary['type'] = self.type
        if self.direct_batch is not None:
            dictionary['directBatch'] = self.direct_batch.to_dictionary()
        if self.payment_link is not None:
            dictionary['paymentLink'] = self.payment_link.to_dictionary()
        if self.payment is not None:
            dictionary['payment'] = self.payment.to_dictionary()
        if self.payout is not None:
            dictionary['payout'] = self.payout.to_dictionary()
        if self.refund is not None:
            dictionary['refund'] = self.refund.to_dictionary()
        if self.token is not None:
            dictionary['token'] = self.token.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'WebhooksEvent':
        super().from_dictionary(dictionary)
        if 'apiVersion' in dictionary:
            self.api_version = dictionary['apiVersion']
        if 'created' in dictionary:
            self.created = dictionary['created']
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'merchantId' in dictionary:
            self.merchant_id = dictionary['merchantId']
        if 'type' in dictionary:
            self.type = dictionary['type']
        if 'directBatch' in dictionary:
            if not isinstance(dictionary['directBatch'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['directBatch']))
            value = GetBatchStatusResponse()
            self.direct_batch = value.from_dictionary(dictionary['directBatch'])
        if 'paymentLink' in dictionary:
            if not isinstance(dictionary['paymentLink'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentLink']))
            value = PaymentLinkResponse()
            self.payment_link = value.from_dictionary(dictionary['paymentLink'])
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = PaymentResponse()
            self.payment = value.from_dictionary(dictionary['payment'])
        if 'payout' in dictionary:
            if not isinstance(dictionary['payout'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payout']))
            value = PayoutResponse()
            self.payout = value.from_dictionary(dictionary['payout'])
        if 'refund' in dictionary:
            if not isinstance(dictionary['refund'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['refund']))
            value = RefundResponse()
            self.refund = value.from_dictionary(dictionary['refund'])
        if 'token' in dictionary:
            if not isinstance(dictionary['token'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['token']))
            value = TokenResponse()
            self.token = value.from_dictionary(dictionary['token'])
        return self

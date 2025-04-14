from typing import Optional

from .data_object import DataObject
from .payment_response import PaymentResponse
from .payout_response import PayoutResponse
from .refund_response import RefundResponse
from .token_response import TokenResponse

class WebhooksEvent(DataObject):

    __api_version: Optional[str] = None
    __created: Optional[str] = None
    __id: Optional[str] = None
    __merchant_id: Optional[str] = None
    __type: Optional[str] = None
    __payment: Optional[PaymentResponse] = None
    __payout: Optional[PayoutResponse] = None
    __refund: Optional[RefundResponse] = None
    __token: Optional[TokenResponse] = None

    @property
    def api_version(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__api_version

    @api_version.setter
    def api_version(self, value: Optional[str]) -> None:
        self.__api_version = value

    @property
    def created(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__created

    @created.setter
    def created(self, value: Optional[str]) -> None:
        self.__created = value

    @property
    def id(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value: Optional[str]) -> None:
        self.__id = value

    @property
    def merchant_id(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__merchant_id

    @merchant_id.setter
    def merchant_id(self, value: Optional[str]) -> None:
        self.__merchant_id = value

    @property
    def type(self) -> Optional[str]:
        """
        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value: Optional[str]) -> None:
        self.__type = value

    @property
    def payment(self) -> Optional[PaymentResponse]:
        """
        Type: PaymentResponse
        """
        return self.__payment

    @payment.setter
    def payment(self, value: Optional[PaymentResponse]) -> None:
        self.__payment = value

    @property
    def payout(self) -> Optional[PayoutResponse]:
        """
        Type: PayoutResponse
        """
        return self.__payout

    @payout.setter
    def payout(self, value: Optional[PayoutResponse]) -> None:
        self.__payout = value

    @property
    def refund(self) -> Optional[RefundResponse]:
        """
        Type: RefundResponse
        """
        return self.__refund

    @refund.setter
    def refund(self, value: Optional[RefundResponse]) -> None:
        self.__refund = value

    @property
    def token(self) -> Optional[TokenResponse]:
        """
        Type: TokenResponse
        """
        return self.__token

    @token.setter
    def token(self, value: Optional[TokenResponse]) -> None:
        self.__token = value

    def to_dictionary(self) -> dict:
        dictionary = super(WebhooksEvent, self).to_dictionary()
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
        if self.payment is not None:
            dictionary['payment'] = self.payment
        if self.payout is not None:
            dictionary['payout'] = self.payout
        if self.refund is not None:
            dictionary['refund'] = self.refund
        if self.token is not None:
            dictionary['token'] = self.token
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'WebhooksEvent':
        super(WebhooksEvent, self).from_dictionary(dictionary)
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

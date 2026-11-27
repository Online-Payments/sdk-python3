#
# This file was automatically generated.
#
from datetime import datetime

from .data_object import DataObject
from .payment_link_event import PaymentLinkEvent
from .payment_link_order_output import PaymentLinkOrderOutput


class PaymentLinkResponse(DataObject):

    __slots__ = (
        "__expiration_date",
        "__is_reusable_link",
        "__payment_id",
        "__payment_link_events",
        "__payment_link_id",
        "__payment_link_order",
        "__qr_code_base64",
        "__recipient_name",
        "__redirection_url",
        "__status",
    )

    __expiration_date: datetime | None
    __is_reusable_link: bool | None
    __payment_id: str | None
    __payment_link_events: list[PaymentLinkEvent] | None
    __payment_link_id: str | None
    __payment_link_order: PaymentLinkOrderOutput | None
    __qr_code_base64: str | None
    __recipient_name: str | None
    __redirection_url: str | None
    __status: str | None

    def __init__(
        self,
        *,
        expiration_date: datetime | None = None,
        is_reusable_link: bool | None = None,
        payment_id: str | None = None,
        payment_link_events: list[PaymentLinkEvent] | None = None,
        payment_link_id: str | None = None,
        payment_link_order: PaymentLinkOrderOutput | None = None,
        qr_code_base64: str | None = None,
        recipient_name: str | None = None,
        redirection_url: str | None = None,
        status: str | None = None,
    ) -> None:
        self.expiration_date = expiration_date
        self.is_reusable_link = is_reusable_link
        self.payment_id = payment_id
        self.payment_link_events = payment_link_events
        self.payment_link_id = payment_link_id
        self.payment_link_order = payment_link_order
        self.qr_code_base64 = qr_code_base64
        self.recipient_name = recipient_name
        self.redirection_url = redirection_url
        self.status = status

    @property
    def expiration_date(self) -> datetime | None:
        """
        | The date after which the payment link will not be usable to complete the payment. The date will contain the UTC offset.

        Type: datetime
        """
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value: datetime | None) -> None:
        self.__expiration_date = value

    @property
    def is_reusable_link(self) -> bool | None:
        """
        | Indicates if the payment link can be used multiple times. The default value for this property is false

        Type: bool
        """
        return self.__is_reusable_link

    @is_reusable_link.setter
    def is_reusable_link(self, value: bool | None) -> None:
        self.__is_reusable_link = value

    @property
    def payment_id(self) -> str | None:
        """
        | The unique payment transaction identifier. This id is only set when a payment was processed with this payment link.

        Type: str
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value: str | None) -> None:
        self.__payment_id = value

    @property
    def payment_link_events(self) -> list[PaymentLinkEvent] | None:
        """
        Type: list[:class:`onlinepayments.sdk.domain.payment_link_event.PaymentLinkEvent`]
        """
        return self.__payment_link_events

    @payment_link_events.setter
    def payment_link_events(self, value: list[PaymentLinkEvent] | None) -> None:
        self.__payment_link_events = value

    @property
    def payment_link_id(self) -> str | None:
        """
        | The unique link identifier.

        Type: str
        """
        return self.__payment_link_id

    @payment_link_id.setter
    def payment_link_id(self, value: str | None) -> None:
        self.__payment_link_id = value

    @property
    def payment_link_order(self) -> PaymentLinkOrderOutput | None:
        """
        | An object containing the details of the related payment output.

        Type: :class:`onlinepayments.sdk.domain.payment_link_order_output.PaymentLinkOrderOutput`
        """
        return self.__payment_link_order

    @payment_link_order.setter
    def payment_link_order(self, value: PaymentLinkOrderOutput | None) -> None:
        self.__payment_link_order = value

    @property
    def qr_code_base64(self) -> str | None:
        """
        | Base64 encoded QR code image containing the payment link URL. This field is only included in the response when displayQRCode is set to true in the request.

        Type: str
        """
        return self.__qr_code_base64

    @qr_code_base64.setter
    def qr_code_base64(self, value: str | None) -> None:
        self.__qr_code_base64 = value

    @property
    def recipient_name(self) -> str | None:
        """
        | The payment link recipient name.

        Type: str
        """
        return self.__recipient_name

    @recipient_name.setter
    def recipient_name(self, value: str | None) -> None:
        self.__recipient_name = value

    @property
    def redirection_url(self) -> str | None:
        """
        | The URL that will redirect the customer to the Hosted Checkout page to process the payment.

        Type: str
        """
        return self.__redirection_url

    @redirection_url.setter
    def redirection_url(self, value: str | None) -> None:
        self.__redirection_url = value

    @property
    def status(self) -> str | None:
        """
        | The current status of a payment link in its lifecycle. A payment link transitions through these states from creation to completion or termination: * ACTIVE - The payment link is active and ready to be used by the customer to complete a payment. This is the initial status when a link is created. * PAID - The payment has been successfully completed by the customer. The link can no longer be used unless it was created as a reusable link (isReusableLink = true). * CANCELLED - The payment link has been manually cancelled by the merchant and can no longer be used. * EXPIRED - The payment link has passed its expiration date (expirationDate) and is no longer usable.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: str | None) -> None:
        self.__status = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.expiration_date is not None:
            dictionary['expirationDate'] = DataObject.format_datetime(self.expiration_date)
        if self.is_reusable_link is not None:
            dictionary['isReusableLink'] = self.is_reusable_link
        if self.payment_id is not None:
            dictionary['paymentId'] = self.payment_id
        if self.payment_link_events is not None:
            dictionary['paymentLinkEvents'] = []
            for element in self.payment_link_events:
                if element is not None:
                    dictionary['paymentLinkEvents'].append(element.to_dictionary())
        if self.payment_link_id is not None:
            dictionary['paymentLinkId'] = self.payment_link_id
        if self.payment_link_order is not None:
            dictionary['paymentLinkOrder'] = self.payment_link_order.to_dictionary()
        if self.qr_code_base64 is not None:
            dictionary['qrCodeBase64'] = self.qr_code_base64
        if self.recipient_name is not None:
            dictionary['recipientName'] = self.recipient_name
        if self.redirection_url is not None:
            dictionary['redirectionUrl'] = self.redirection_url
        if self.status is not None:
            dictionary['status'] = self.status
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentLinkResponse':
        super().from_dictionary(dictionary)
        if 'expirationDate' in dictionary:
            self.expiration_date = DataObject.parse_datetime(dictionary['expirationDate'])
        if 'isReusableLink' in dictionary:
            self.is_reusable_link = dictionary['isReusableLink']
        if 'paymentId' in dictionary:
            self.payment_id = dictionary['paymentId']
        if 'paymentLinkEvents' in dictionary:
            if not isinstance(dictionary['paymentLinkEvents'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['paymentLinkEvents']))
            self.payment_link_events = []
            for element in dictionary['paymentLinkEvents']:
                value = PaymentLinkEvent()
                self.payment_link_events.append(value.from_dictionary(element))
        if 'paymentLinkId' in dictionary:
            self.payment_link_id = dictionary['paymentLinkId']
        if 'paymentLinkOrder' in dictionary:
            if not isinstance(dictionary['paymentLinkOrder'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentLinkOrder']))
            value = PaymentLinkOrderOutput()
            self.payment_link_order = value.from_dictionary(dictionary['paymentLinkOrder'])
        if 'qrCodeBase64' in dictionary:
            self.qr_code_base64 = dictionary['qrCodeBase64']
        if 'recipientName' in dictionary:
            self.recipient_name = dictionary['recipientName']
        if 'redirectionUrl' in dictionary:
            self.redirection_url = dictionary['redirectionUrl']
        if 'status' in dictionary:
            self.status = dictionary['status']
        return self

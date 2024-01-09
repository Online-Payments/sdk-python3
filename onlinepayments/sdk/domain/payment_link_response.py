# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from typing import List

from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.payment_link_event import PaymentLinkEvent
from onlinepayments.sdk.domain.payment_link_order_output import PaymentLinkOrderOutput


class PaymentLinkResponse(DataObject):
    """
    | An object representing a payment link.
    """

    __expiration_date = None
    __payment_id = None
    __payment_link_events = None
    __payment_link_id = None
    __payment_link_order = None
    __recipient_name = None
    __redirection_url = None
    __status = None

    @property
    def expiration_date(self) -> str:
        """
        | The date after which the payment link will not be usable to complete the payment. The date will contain the UTC offset.

        Type: str
        """
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value: str):
        self.__expiration_date = value

    @property
    def payment_id(self) -> str:
        """
        | The unique payment transaction identifier. This id is only set when a payment was processed with this payment link.

        Type: str
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value: str):
        self.__payment_id = value

    @property
    def payment_link_events(self) -> List[PaymentLinkEvent]:
        """
        Type: list[:class:`onlinepayments.sdk.domain.payment_link_event.PaymentLinkEvent`]
        """
        return self.__payment_link_events

    @payment_link_events.setter
    def payment_link_events(self, value: List[PaymentLinkEvent]):
        self.__payment_link_events = value

    @property
    def payment_link_id(self) -> str:
        """
        | The unique link identifier.

        Type: str
        """
        return self.__payment_link_id

    @payment_link_id.setter
    def payment_link_id(self, value: str):
        self.__payment_link_id = value

    @property
    def payment_link_order(self) -> PaymentLinkOrderOutput:
        """
        | An object containing the details of the related payment output.

        Type: :class:`onlinepayments.sdk.domain.payment_link_order_output.PaymentLinkOrderOutput`
        """
        return self.__payment_link_order

    @payment_link_order.setter
    def payment_link_order(self, value: PaymentLinkOrderOutput):
        self.__payment_link_order = value

    @property
    def recipient_name(self) -> str:
        """
        | The payment link recipient name.

        Type: str
        """
        return self.__recipient_name

    @recipient_name.setter
    def recipient_name(self, value: str):
        self.__recipient_name = value

    @property
    def redirection_url(self) -> str:
        """
        | The URL that will redirect the customer to the Hosted Checkout page to process the payment.

        Type: str
        """
        return self.__redirection_url

    @redirection_url.setter
    def redirection_url(self, value: str):
        self.__redirection_url = value

    @property
    def status(self) -> str:
        """
        | The state of the payment link:
        |   * ACTIVE: The payment link is ready to be used.
        |   * PAID: The payment has been completed.
        |   * CANCELLED: The payment link has been manually cancelled.
        |   * EXPIRED: The payment link is not usable anymore.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: str):
        self.__status = value

    def to_dictionary(self):
        dictionary = super(PaymentLinkResponse, self).to_dictionary()
        if self.expiration_date is not None:
            dictionary['expirationDate'] = self.expiration_date
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
        if self.recipient_name is not None:
            dictionary['recipientName'] = self.recipient_name
        if self.redirection_url is not None:
            dictionary['redirectionUrl'] = self.redirection_url
        if self.status is not None:
            dictionary['status'] = self.status
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentLinkResponse, self).from_dictionary(dictionary)
        if 'expirationDate' in dictionary:
            self.expiration_date = dictionary['expirationDate']
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
        if 'recipientName' in dictionary:
            self.recipient_name = dictionary['recipientName']
        if 'redirectionUrl' in dictionary:
            self.redirection_url = dictionary['redirectionUrl']
        if 'status' in dictionary:
            self.status = dictionary['status']
        return self

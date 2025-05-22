# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from datetime import datetime
from typing import List, Optional

from .data_object import DataObject
from .payment_link_event import PaymentLinkEvent
from .payment_link_order_output import PaymentLinkOrderOutput


class PaymentLinkResponse(DataObject):

    __expiration_date: Optional[datetime] = None
    __is_reusable_link: Optional[bool] = None
    __payment_id: Optional[str] = None
    __payment_link_events: Optional[List[PaymentLinkEvent]] = None
    __payment_link_id: Optional[str] = None
    __payment_link_order: Optional[PaymentLinkOrderOutput] = None
    __recipient_name: Optional[str] = None
    __redirection_url: Optional[str] = None
    __status: Optional[str] = None

    @property
    def expiration_date(self) -> Optional[datetime]:
        """
        | The date after which the payment link will not be usable to complete the payment. The date will contain the UTC offset.

        Type: datetime
        """
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value: Optional[datetime]) -> None:
        self.__expiration_date = value

    @property
    def is_reusable_link(self) -> Optional[bool]:
        """
        | Indicates if the payment link can be used multiple times. The default value for this property is false

        Type: bool
        """
        return self.__is_reusable_link

    @is_reusable_link.setter
    def is_reusable_link(self, value: Optional[bool]) -> None:
        self.__is_reusable_link = value

    @property
    def payment_id(self) -> Optional[str]:
        """
        | The unique payment transaction identifier. This id is only set when a payment was processed with this payment link.

        Type: str
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value: Optional[str]) -> None:
        self.__payment_id = value

    @property
    def payment_link_events(self) -> Optional[List[PaymentLinkEvent]]:
        """
        Type: list[:class:`onlinepayments.sdk.domain.payment_link_event.PaymentLinkEvent`]
        """
        return self.__payment_link_events

    @payment_link_events.setter
    def payment_link_events(self, value: Optional[List[PaymentLinkEvent]]) -> None:
        self.__payment_link_events = value

    @property
    def payment_link_id(self) -> Optional[str]:
        """
        | The unique link identifier.

        Type: str
        """
        return self.__payment_link_id

    @payment_link_id.setter
    def payment_link_id(self, value: Optional[str]) -> None:
        self.__payment_link_id = value

    @property
    def payment_link_order(self) -> Optional[PaymentLinkOrderOutput]:
        """
        | An object containing the details of the related payment output.

        Type: :class:`onlinepayments.sdk.domain.payment_link_order_output.PaymentLinkOrderOutput`
        """
        return self.__payment_link_order

    @payment_link_order.setter
    def payment_link_order(self, value: Optional[PaymentLinkOrderOutput]) -> None:
        self.__payment_link_order = value

    @property
    def recipient_name(self) -> Optional[str]:
        """
        | The payment link recipient name.

        Type: str
        """
        return self.__recipient_name

    @recipient_name.setter
    def recipient_name(self, value: Optional[str]) -> None:
        self.__recipient_name = value

    @property
    def redirection_url(self) -> Optional[str]:
        """
        | The URL that will redirect the customer to the Hosted Checkout page to process the payment.

        Type: str
        """
        return self.__redirection_url

    @redirection_url.setter
    def redirection_url(self, value: Optional[str]) -> None:
        self.__redirection_url = value

    @property
    def status(self) -> Optional[str]:
        """
        | The state of the payment link:
        
        * ACTIVE: The payment link is ready to be used.
        * PAID: The payment has been completed.
        * CANCELLED: The payment link has been manually cancelled.
        * EXPIRED: The payment link is not usable anymore.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: Optional[str]) -> None:
        self.__status = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentLinkResponse, self).to_dictionary()
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
        if self.recipient_name is not None:
            dictionary['recipientName'] = self.recipient_name
        if self.redirection_url is not None:
            dictionary['redirectionUrl'] = self.redirection_url
        if self.status is not None:
            dictionary['status'] = self.status
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentLinkResponse':
        super(PaymentLinkResponse, self).from_dictionary(dictionary)
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
        if 'recipientName' in dictionary:
            self.recipient_name = dictionary['recipientName']
        if 'redirectionUrl' in dictionary:
            self.redirection_url = dictionary['redirectionUrl']
        if 'status' in dictionary:
            self.status = dictionary['status']
        return self

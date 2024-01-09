# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.payment_link_order_input import PaymentLinkOrderInput


class CreatePaymentLinkRequest(DataObject):
    """
    | An object containing the Create PaymentLink request.
    """

    __description = None
    __expiration_date = None
    __payment_link_order = None
    __recipient_name = None

    @property
    def description(self) -> str:
        """
        | A note related to the created payment link.

        Type: str
        """
        return self.__description

    @description.setter
    def description(self, value: str):
        self.__description = value

    @property
    def expiration_date(self) -> str:
        """
        | The date after which the payment link will not be usable to complete the payment. The date sent cannot be more than 30 days in the future or a past date. It must also contain the UTC offset.

        Type: str
        """
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value: str):
        self.__expiration_date = value

    @property
    def payment_link_order(self) -> PaymentLinkOrderInput:
        """
        | An object containing the details of the related payment input.

        Type: :class:`onlinepayments.sdk.domain.payment_link_order_input.PaymentLinkOrderInput`
        """
        return self.__payment_link_order

    @payment_link_order.setter
    def payment_link_order(self, value: PaymentLinkOrderInput):
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

    def to_dictionary(self):
        dictionary = super(CreatePaymentLinkRequest, self).to_dictionary()
        if self.description is not None:
            dictionary['description'] = self.description
        if self.expiration_date is not None:
            dictionary['expirationDate'] = self.expiration_date
        if self.payment_link_order is not None:
            dictionary['paymentLinkOrder'] = self.payment_link_order.to_dictionary()
        if self.recipient_name is not None:
            dictionary['recipientName'] = self.recipient_name
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreatePaymentLinkRequest, self).from_dictionary(dictionary)
        if 'description' in dictionary:
            self.description = dictionary['description']
        if 'expirationDate' in dictionary:
            self.expiration_date = dictionary['expirationDate']
        if 'paymentLinkOrder' in dictionary:
            if not isinstance(dictionary['paymentLinkOrder'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentLinkOrder']))
            value = PaymentLinkOrderInput()
            self.payment_link_order = value.from_dictionary(dictionary['paymentLinkOrder'])
        if 'recipientName' in dictionary:
            self.recipient_name = dictionary['recipientName']
        return self

#
# This file was automatically generated.
#
from datetime import datetime

from .amount_of_money import AmountOfMoney
from .data_object import DataObject


class PaymentLinkOverviewEntry(DataObject):

    __slots__ = (
        "__amount",
        "__created_by",
        "__creation_date",
        "__expiration_date",
        "__is_reusable_link",
        "__merchant_id",
        "__merchant_reference",
        "__payment_link_id",
        "__redirection_url",
        "__status",
    )

    __amount: AmountOfMoney | None
    __created_by: str | None
    __creation_date: datetime | None
    __expiration_date: datetime | None
    __is_reusable_link: bool | None
    __merchant_id: str | None
    __merchant_reference: str | None
    __payment_link_id: str | None
    __redirection_url: str | None
    __status: str | None

    def __init__(
        self,
        *,
        amount: AmountOfMoney | None = None,
        created_by: str | None = None,
        creation_date: datetime | None = None,
        expiration_date: datetime | None = None,
        is_reusable_link: bool | None = None,
        merchant_id: str | None = None,
        merchant_reference: str | None = None,
        payment_link_id: str | None = None,
        redirection_url: str | None = None,
        status: str | None = None,
    ) -> None:
        self.amount = amount
        self.created_by = created_by
        self.creation_date = creation_date
        self.expiration_date = expiration_date
        self.is_reusable_link = is_reusable_link
        self.merchant_id = merchant_id
        self.merchant_reference = merchant_reference
        self.payment_link_id = payment_link_id
        self.redirection_url = redirection_url
        self.status = status

    @property
    def amount(self) -> AmountOfMoney | None:
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__amount

    @amount.setter
    def amount(self, value: AmountOfMoney | None) -> None:
        self.__amount = value

    @property
    def created_by(self) -> str | None:
        """
        | The identifier of the user or entity that created the payment link.

        Type: str
        """
        return self.__created_by

    @created_by.setter
    def created_by(self, value: str | None) -> None:
        self.__created_by = value

    @property
    def creation_date(self) -> datetime | None:
        """
        | The date and time when the payment link was created. The date contains the UTC offset.

        Type: datetime
        """
        return self.__creation_date

    @creation_date.setter
    def creation_date(self, value: datetime | None) -> None:
        self.__creation_date = value

    @property
    def expiration_date(self) -> datetime | None:
        """
        | The date after which the payment link will not be usable to complete the payment. The date sent cannot be more than 6 months in the future or a past date. It must also contain the UTC offset.

        Type: datetime
        """
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value: datetime | None) -> None:
        self.__expiration_date = value

    @property
    def is_reusable_link(self) -> bool | None:
        """
        | Indicates if the payment link can be used multiple times.

        Type: bool
        """
        return self.__is_reusable_link

    @is_reusable_link.setter
    def is_reusable_link(self, value: bool | None) -> None:
        self.__is_reusable_link = value

    @property
    def merchant_id(self) -> str | None:
        """
        | The unique Merchant Id of the merchant associated with the payment link.

        Type: str
        """
        return self.__merchant_id

    @merchant_id.setter
    def merchant_id(self, value: str | None) -> None:
        self.__merchant_id = value

    @property
    def merchant_reference(self) -> str | None:
        """
        | Your unique reference of the transaction that is also returned in our report files. This is almost always used for your reconciliation of our report files. It is highly recommended to provide a single MerchantReference per unique order on your side

        Type: str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value: str | None) -> None:
        self.__merchant_reference = value

    @property
    def payment_link_id(self) -> str | None:
        """
        | The unique identifier of the payment link.

        Type: str
        """
        return self.__payment_link_id

    @payment_link_id.setter
    def payment_link_id(self, value: str | None) -> None:
        self.__payment_link_id = value

    @property
    def redirection_url(self) -> str | None:
        """
        | The URL that will redirect the customer to the payment page to process the payment.

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
        if self.amount is not None:
            dictionary['amount'] = self.amount.to_dictionary()
        if self.created_by is not None:
            dictionary['createdBy'] = self.created_by
        if self.creation_date is not None:
            dictionary['creationDate'] = DataObject.format_datetime(self.creation_date)
        if self.expiration_date is not None:
            dictionary['expirationDate'] = DataObject.format_datetime(self.expiration_date)
        if self.is_reusable_link is not None:
            dictionary['isReusableLink'] = self.is_reusable_link
        if self.merchant_id is not None:
            dictionary['merchantId'] = self.merchant_id
        if self.merchant_reference is not None:
            dictionary['merchantReference'] = self.merchant_reference
        if self.payment_link_id is not None:
            dictionary['paymentLinkId'] = self.payment_link_id
        if self.redirection_url is not None:
            dictionary['redirectionUrl'] = self.redirection_url
        if self.status is not None:
            dictionary['status'] = self.status
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentLinkOverviewEntry':
        super().from_dictionary(dictionary)
        if 'amount' in dictionary:
            if not isinstance(dictionary['amount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amount']))
            value = AmountOfMoney()
            self.amount = value.from_dictionary(dictionary['amount'])
        if 'createdBy' in dictionary:
            self.created_by = dictionary['createdBy']
        if 'creationDate' in dictionary:
            self.creation_date = DataObject.parse_datetime(dictionary['creationDate'])
        if 'expirationDate' in dictionary:
            self.expiration_date = DataObject.parse_datetime(dictionary['expirationDate'])
        if 'isReusableLink' in dictionary:
            self.is_reusable_link = dictionary['isReusableLink']
        if 'merchantId' in dictionary:
            self.merchant_id = dictionary['merchantId']
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        if 'paymentLinkId' in dictionary:
            self.payment_link_id = dictionary['paymentLinkId']
        if 'redirectionUrl' in dictionary:
            self.redirection_url = dictionary['redirectionUrl']
        if 'status' in dictionary:
            self.status = dictionary['status']
        return self

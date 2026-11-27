#
# This file was automatically generated.
#
from .apple_pay_line_item import ApplePayLineItem
from .data_object import DataObject


class ApplePayRecurringPaymentRequest(DataObject):

    __slots__ = (
        "__billing_agreement",
        "__management_url",
        "__payment_description",
        "__regular_billing",
        "__trial_billing",
    )

    __billing_agreement: str | None
    __management_url: str | None
    __payment_description: str | None
    __regular_billing: ApplePayLineItem | None
    __trial_billing: ApplePayLineItem | None

    def __init__(
        self,
        *,
        billing_agreement: str | None = None,
        management_url: str | None = None,
        payment_description: str | None = None,
        regular_billing: ApplePayLineItem | None = None,
        trial_billing: ApplePayLineItem | None = None,
    ) -> None:
        self.billing_agreement = billing_agreement
        self.management_url = management_url
        self.payment_description = payment_description
        self.regular_billing = regular_billing
        self.trial_billing = trial_billing

    @property
    def billing_agreement(self) -> str | None:
        """
        | A localized billing agreement that the payment sheet displays to the user before the user authorizes the payment.

        Type: str
        """
        return self.__billing_agreement

    @billing_agreement.setter
    def billing_agreement(self, value: str | None) -> None:
        self.__billing_agreement = value

    @property
    def management_url(self) -> str | None:
        """
        | A URL to a web page where the user can update or delete the payment method for the recurring payment.

        Type: str
        """
        return self.__management_url

    @management_url.setter
    def management_url(self, value: str | None) -> None:
        self.__management_url = value

    @property
    def payment_description(self) -> str | None:
        """
        | A description of the recurring payment that Apple Pay displays to the user in the payment sheet.

        Type: str
        """
        return self.__payment_description

    @payment_description.setter
    def payment_description(self, value: str | None) -> None:
        self.__payment_description = value

    @property
    def regular_billing(self) -> ApplePayLineItem | None:
        """
        | Object containing specific data regarding Apple Pay recurring regular payment

        Type: :class:`onlinepayments.sdk.domain.apple_pay_line_item.ApplePayLineItem`
        """
        return self.__regular_billing

    @regular_billing.setter
    def regular_billing(self, value: ApplePayLineItem | None) -> None:
        self.__regular_billing = value

    @property
    def trial_billing(self) -> ApplePayLineItem | None:
        """
        | Object containing specific data regarding Apple Pay recurring trial payment

        Type: :class:`onlinepayments.sdk.domain.apple_pay_line_item.ApplePayLineItem`
        """
        return self.__trial_billing

    @trial_billing.setter
    def trial_billing(self, value: ApplePayLineItem | None) -> None:
        self.__trial_billing = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.billing_agreement is not None:
            dictionary['billingAgreement'] = self.billing_agreement
        if self.management_url is not None:
            dictionary['managementUrl'] = self.management_url
        if self.payment_description is not None:
            dictionary['paymentDescription'] = self.payment_description
        if self.regular_billing is not None:
            dictionary['regularBilling'] = self.regular_billing.to_dictionary()
        if self.trial_billing is not None:
            dictionary['trialBilling'] = self.trial_billing.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ApplePayRecurringPaymentRequest':
        super().from_dictionary(dictionary)
        if 'billingAgreement' in dictionary:
            self.billing_agreement = dictionary['billingAgreement']
        if 'managementUrl' in dictionary:
            self.management_url = dictionary['managementUrl']
        if 'paymentDescription' in dictionary:
            self.payment_description = dictionary['paymentDescription']
        if 'regularBilling' in dictionary:
            if not isinstance(dictionary['regularBilling'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['regularBilling']))
            value = ApplePayLineItem()
            self.regular_billing = value.from_dictionary(dictionary['regularBilling'])
        if 'trialBilling' in dictionary:
            if not isinstance(dictionary['trialBilling'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['trialBilling']))
            value = ApplePayLineItem()
            self.trial_billing = value.from_dictionary(dictionary['trialBilling'])
        return self

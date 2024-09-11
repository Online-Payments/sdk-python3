# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class RedirectPaymentProduct3203SpecificInput(DataObject):
    """
    | Object containing specific input for PostFinancePay payments (Payment product ID 3203).
    """

    __checkout_type = None

    @property
    def checkout_type(self) -> str:
        """
        | Determines the type of the checkout that will be used for PostFinancePay. Allowed values:
        |   * default - The user will be redirected to the PostFinancePay application to complete the payment.
        |   * expressCheckout -  In order to accelerate the payment process, the shipping and billing addresses are requested 
        |                        from the payer's PostFinancePay account. These will be returned in the API response in 
        |                        paymentProduct3203SpecificOutput. Note that the payer must accept to provide his 
        |                        billing and shipping address during checkout in the PostFinancePay application. 
        |                        If not, the payment will be declined.

        Type: str
        """
        return self.__checkout_type

    @checkout_type.setter
    def checkout_type(self, value: str):
        self.__checkout_type = value

    def to_dictionary(self):
        dictionary = super(RedirectPaymentProduct3203SpecificInput, self).to_dictionary()
        if self.checkout_type is not None:
            dictionary['checkoutType'] = self.checkout_type
        return dictionary

    def from_dictionary(self, dictionary):
        super(RedirectPaymentProduct3203SpecificInput, self).from_dictionary(dictionary)
        if 'checkoutType' in dictionary:
            self.checkout_type = dictionary['checkoutType']
        return self

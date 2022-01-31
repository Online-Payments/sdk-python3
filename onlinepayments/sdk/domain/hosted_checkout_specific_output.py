# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class HostedCheckoutSpecificOutput(DataObject):
    """
    | Hosted Checkout specific information. Populated if the payment was created on the platform through a Hosted Checkout.
    """

    __hosted_checkout_id = None
    __variant = None

    @property
    def hosted_checkout_id(self) -> str:
        """
        | The ID of the Hosted Checkout Session in which the payment was made.

        Type: str
        """
        return self.__hosted_checkout_id

    @hosted_checkout_id.setter
    def hosted_checkout_id(self, value: str):
        self.__hosted_checkout_id = value

    @property
    def variant(self) -> str:
        """
        | Using the Back-Office it is possible to upload multiple templates of your HostedCheckout payment pages. You can force the use of another template by specifying it in the variant field. This allows you to test out the effect of certain changes to your hostedcheckout pages in a controlled manner. Please note that you need to specify the filename of the template.

        Type: str
        """
        return self.__variant

    @variant.setter
    def variant(self, value: str):
        self.__variant = value

    def to_dictionary(self):
        dictionary = super(HostedCheckoutSpecificOutput, self).to_dictionary()
        if self.hosted_checkout_id is not None:
            dictionary['hostedCheckoutId'] = self.hosted_checkout_id
        if self.variant is not None:
            dictionary['variant'] = self.variant
        return dictionary

    def from_dictionary(self, dictionary):
        super(HostedCheckoutSpecificOutput, self).from_dictionary(dictionary)
        if 'hostedCheckoutId' in dictionary:
            self.hosted_checkout_id = dictionary['hostedCheckoutId']
        if 'variant' in dictionary:
            self.variant = dictionary['variant']
        return self

# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class PaymentProduct5001SpecificOutput(DataObject):
    """
    | Bizum (payment product 5001) specific details
    """

    __authorisation_code = None

    @property
    def authorisation_code(self) -> str:
        """
        | The reference returned by redsys to identify the transaction

        Type: str
        """
        return self.__authorisation_code

    @authorisation_code.setter
    def authorisation_code(self, value: str):
        self.__authorisation_code = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct5001SpecificOutput, self).to_dictionary()
        if self.authorisation_code is not None:
            dictionary['authorisationCode'] = self.authorisation_code
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct5001SpecificOutput, self).from_dictionary(dictionary)
        if 'authorisationCode' in dictionary:
            self.authorisation_code = dictionary['authorisationCode']
        return self

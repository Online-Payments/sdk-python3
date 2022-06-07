# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class PaymentProduct3012SpecificInput(DataObject):
    """
    | Object containing specific input required for bancontact.
    """

    __force_authentication = None
    __is_wip_transaction = None

    @property
    def force_authentication(self) -> bool:
        """
        | Indicate whether authentication should be forced.

        Type: bool
        """
        return self.__force_authentication

    @force_authentication.setter
    def force_authentication(self, value: bool):
        self.__force_authentication = value

    @property
    def is_wip_transaction(self) -> bool:
        """
        | Indicate whether its wallet initiated payment.

        Type: bool
        """
        return self.__is_wip_transaction

    @is_wip_transaction.setter
    def is_wip_transaction(self, value: bool):
        self.__is_wip_transaction = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct3012SpecificInput, self).to_dictionary()
        if self.force_authentication is not None:
            dictionary['forceAuthentication'] = self.force_authentication
        if self.is_wip_transaction is not None:
            dictionary['isWipTransaction'] = self.is_wip_transaction
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct3012SpecificInput, self).from_dictionary(dictionary)
        if 'forceAuthentication' in dictionary:
            self.force_authentication = dictionary['forceAuthentication']
        if 'isWipTransaction' in dictionary:
            self.is_wip_transaction = dictionary['isWipTransaction']
        return self

# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .airline_data import AirlineData
from .data_object import DataObject
from .loan_recipient import LoanRecipient
from .lodging_data import LodgingData
from .order_type_information import OrderTypeInformation


class AdditionalOrderInput(DataObject):

    __airline_data: Optional[AirlineData] = None
    __loan_recipient: Optional[LoanRecipient] = None
    __lodging_data: Optional[LodgingData] = None
    __type_information: Optional[OrderTypeInformation] = None

    @property
    def airline_data(self) -> Optional[AirlineData]:
        """
        | Object that holds airline specific data

        Type: :class:`onlinepayments.sdk.domain.airline_data.AirlineData`
        """
        return self.__airline_data

    @airline_data.setter
    def airline_data(self, value: Optional[AirlineData]) -> None:
        self.__airline_data = value

    @property
    def loan_recipient(self) -> Optional[LoanRecipient]:
        """
        | Object containing specific data regarding the recipient of a loan in the UK

        Type: :class:`onlinepayments.sdk.domain.loan_recipient.LoanRecipient`
        """
        return self.__loan_recipient

    @loan_recipient.setter
    def loan_recipient(self, value: Optional[LoanRecipient]) -> None:
        self.__loan_recipient = value

    @property
    def lodging_data(self) -> Optional[LodgingData]:
        """
        | Object that holds lodging specific data

        Type: :class:`onlinepayments.sdk.domain.lodging_data.LodgingData`
        """
        return self.__lodging_data

    @lodging_data.setter
    def lodging_data(self, value: Optional[LodgingData]) -> None:
        self.__lodging_data = value

    @property
    def type_information(self) -> Optional[OrderTypeInformation]:
        """
        | Object that holds the purchase and usage type indicators

        Type: :class:`onlinepayments.sdk.domain.order_type_information.OrderTypeInformation`
        """
        return self.__type_information

    @type_information.setter
    def type_information(self, value: Optional[OrderTypeInformation]) -> None:
        self.__type_information = value

    def to_dictionary(self) -> dict:
        dictionary = super(AdditionalOrderInput, self).to_dictionary()
        if self.airline_data is not None:
            dictionary['airlineData'] = self.airline_data.to_dictionary()
        if self.loan_recipient is not None:
            dictionary['loanRecipient'] = self.loan_recipient.to_dictionary()
        if self.lodging_data is not None:
            dictionary['lodgingData'] = self.lodging_data.to_dictionary()
        if self.type_information is not None:
            dictionary['typeInformation'] = self.type_information.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AdditionalOrderInput':
        super(AdditionalOrderInput, self).from_dictionary(dictionary)
        if 'airlineData' in dictionary:
            if not isinstance(dictionary['airlineData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['airlineData']))
            value = AirlineData()
            self.airline_data = value.from_dictionary(dictionary['airlineData'])
        if 'loanRecipient' in dictionary:
            if not isinstance(dictionary['loanRecipient'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['loanRecipient']))
            value = LoanRecipient()
            self.loan_recipient = value.from_dictionary(dictionary['loanRecipient'])
        if 'lodgingData' in dictionary:
            if not isinstance(dictionary['lodgingData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['lodgingData']))
            value = LodgingData()
            self.lodging_data = value.from_dictionary(dictionary['lodgingData'])
        if 'typeInformation' in dictionary:
            if not isinstance(dictionary['typeInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['typeInformation']))
            value = OrderTypeInformation()
            self.type_information = value.from_dictionary(dictionary['typeInformation'])
        return self

# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.customer_device_output import CustomerDeviceOutput


class CustomerOutput(DataObject):
    """
    | Object containing the details of the customer
    """

    __device = None

    @property
    def device(self) -> CustomerDeviceOutput:
        """
        | Object containing information on the device and browser of the customer

        Type: :class:`onlinepayments.sdk.domain.customer_device_output.CustomerDeviceOutput`
        """
        return self.__device

    @device.setter
    def device(self, value: CustomerDeviceOutput):
        self.__device = value

    def to_dictionary(self):
        dictionary = super(CustomerOutput, self).to_dictionary()
        if self.device is not None:
            dictionary['device'] = self.device.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CustomerOutput, self).from_dictionary(dictionary)
        if 'device' in dictionary:
            if not isinstance(dictionary['device'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['device']))
            value = CustomerDeviceOutput()
            self.device = value.from_dictionary(dictionary['device'])
        return self

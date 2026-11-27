#
# This file was automatically generated.
#
from .customer_device_output import CustomerDeviceOutput
from .data_object import DataObject


class CustomerOutput(DataObject):

    __slots__ = (
        "__device",
    )

    __device: CustomerDeviceOutput | None

    def __init__(
        self,
        *,
        device: CustomerDeviceOutput | None = None,
    ) -> None:
        self.device = device

    @property
    def device(self) -> CustomerDeviceOutput | None:
        """
        | Object containing information on the device and browser of the customer

        Type: :class:`onlinepayments.sdk.domain.customer_device_output.CustomerDeviceOutput`
        """
        return self.__device

    @device.setter
    def device(self, value: CustomerDeviceOutput | None) -> None:
        self.__device = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.device is not None:
            dictionary['device'] = self.device.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CustomerOutput':
        super().from_dictionary(dictionary)
        if 'device' in dictionary:
            if not isinstance(dictionary['device'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['device']))
            value = CustomerDeviceOutput()
            self.device = value.from_dictionary(dictionary['device'])
        return self

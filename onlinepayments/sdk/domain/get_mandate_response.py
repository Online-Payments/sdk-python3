#
# This file was automatically generated.
#
from .data_object import DataObject
from .mandate_response import MandateResponse


class GetMandateResponse(DataObject):

    __slots__ = (
        "__mandate",
    )

    __mandate: MandateResponse | None

    def __init__(
        self,
        *,
        mandate: MandateResponse | None = None,
    ) -> None:
        self.mandate = mandate

    @property
    def mandate(self) -> MandateResponse | None:
        """
        | Object containing the created mandate.

        Type: :class:`onlinepayments.sdk.domain.mandate_response.MandateResponse`
        """
        return self.__mandate

    @mandate.setter
    def mandate(self, value: MandateResponse | None) -> None:
        self.__mandate = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.mandate is not None:
            dictionary['mandate'] = self.mandate.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'GetMandateResponse':
        super().from_dictionary(dictionary)
        if 'mandate' in dictionary:
            if not isinstance(dictionary['mandate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mandate']))
            value = MandateResponse()
            self.mandate = value.from_dictionary(dictionary['mandate'])
        return self

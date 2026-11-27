#
# This file was automatically generated.
#
from .data_object import DataObject


class FraudResults(DataObject):

    __slots__ = (
        "__fraud_service_result",
    )

    __fraud_service_result: str | None

    def __init__(
        self,
        *,
        fraud_service_result: str | None = None,
    ) -> None:
        self.fraud_service_result = fraud_service_result

    @property
    def fraud_service_result(self) -> str | None:
        """
        | Resulting advice of the fraud prevention checks. Possible values are:
        
        * accepted - Based on the checks performed the transaction can be accepted
        * challenged - Based on the checks performed the transaction should be manually reviewed
        * denied - Based on the checks performed the transaction should be rejected
        * no-advice - No fraud check was requested/performed
        * error - The fraud check resulted an error. Note that the fraud check was thus not performed.

        Type: str
        """
        return self.__fraud_service_result

    @fraud_service_result.setter
    def fraud_service_result(self, value: str | None) -> None:
        self.__fraud_service_result = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.fraud_service_result is not None:
            dictionary['fraudServiceResult'] = self.fraud_service_result
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'FraudResults':
        super().from_dictionary(dictionary)
        if 'fraudServiceResult' in dictionary:
            self.fraud_service_result = dictionary['fraudServiceResult']
        return self

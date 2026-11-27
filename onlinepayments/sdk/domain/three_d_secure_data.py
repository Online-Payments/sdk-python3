#
# This file was automatically generated.
#
from .data_object import DataObject


class ThreeDSecureData(DataObject):

    __slots__ = (
        "__acs_transaction_id",
        "__method",
        "__utc_timestamp",
    )

    __acs_transaction_id: str | None
    __method: str | None
    __utc_timestamp: str | None

    def __init__(
        self,
        *,
        acs_transaction_id: str | None = None,
        method: str | None = None,
        utc_timestamp: str | None = None,
    ) -> None:
        self.acs_transaction_id = acs_transaction_id
        self.method = method
        self.utc_timestamp = utc_timestamp

    @property
    def acs_transaction_id(self) -> str | None:
        """
        | The ACS Transaction ID for a prior 3-D Secure authenticated transaction (for example, the first recurring transaction that was authenticated with the customer)

        Type: str
        """
        return self.__acs_transaction_id

    @acs_transaction_id.setter
    def acs_transaction_id(self, value: str | None) -> None:
        self.__acs_transaction_id = value

    @property
    def method(self) -> str | None:
        """
        | Method of authentication used for this transaction. Possible values:
        
        * frictionless = The authentication went without a challenge
        * challenged = Cardholder was challenged
        * avs-verified = The authentication was verified by AVS
        * other = Another issuer method was used to authenticate this transaction

        Type: str
        """
        return self.__method

    @method.setter
    def method(self, value: str | None) -> None:
        self.__method = value

    @property
    def utc_timestamp(self) -> str | None:
        """
        | Timestamp in UTC (YYYYMMDDHHmm) of the 3-D Secure authentication of this transaction

        Type: str
        """
        return self.__utc_timestamp

    @utc_timestamp.setter
    def utc_timestamp(self, value: str | None) -> None:
        self.__utc_timestamp = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.acs_transaction_id is not None:
            dictionary['acsTransactionId'] = self.acs_transaction_id
        if self.method is not None:
            dictionary['method'] = self.method
        if self.utc_timestamp is not None:
            dictionary['utcTimestamp'] = self.utc_timestamp
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ThreeDSecureData':
        super().from_dictionary(dictionary)
        if 'acsTransactionId' in dictionary:
            self.acs_transaction_id = dictionary['acsTransactionId']
        if 'method' in dictionary:
            self.method = dictionary['method']
        if 'utcTimestamp' in dictionary:
            self.utc_timestamp = dictionary['utcTimestamp']
        return self

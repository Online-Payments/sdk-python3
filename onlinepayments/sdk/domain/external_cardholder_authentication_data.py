#
# This file was automatically generated.
#
from .data_object import DataObject


class ExternalCardholderAuthenticationData(DataObject):

    __slots__ = (
        "__acs_transaction_id",
        "__applied_exemption",
        "__cavv",
        "__cavv_algorithm",
        "__directory_server_transaction_id",
        "__eci",
        "__flow",
        "__scheme_risk_score",
        "__three_d_secure_version",
        "__xid",
    )

    __acs_transaction_id: str | None
    __applied_exemption: str | None
    __cavv: str | None
    __cavv_algorithm: str | None
    __directory_server_transaction_id: str | None
    __eci: int | None
    __flow: str | None
    __scheme_risk_score: int | None
    __three_d_secure_version: str | None
    __xid: str | None

    def __init__(
        self,
        *,
        acs_transaction_id: str | None = None,
        applied_exemption: str | None = None,
        cavv: str | None = None,
        cavv_algorithm: str | None = None,
        directory_server_transaction_id: str | None = None,
        eci: int | None = None,
        flow: str | None = None,
        scheme_risk_score: int | None = None,
        three_d_secure_version: str | None = None,
        xid: str | None = None,
    ) -> None:
        self.acs_transaction_id = acs_transaction_id
        self.applied_exemption = applied_exemption
        self.cavv = cavv
        self.cavv_algorithm = cavv_algorithm
        self.directory_server_transaction_id = directory_server_transaction_id
        self.eci = eci
        self.flow = flow
        self.scheme_risk_score = scheme_risk_score
        self.three_d_secure_version = three_d_secure_version
        self.xid = xid

    @property
    def acs_transaction_id(self) -> str | None:
        """
        | Identifier of the authenticated transaction at the ACS/Issuer.

        Type: str
        """
        return self.__acs_transaction_id

    @acs_transaction_id.setter
    def acs_transaction_id(self, value: str | None) -> None:
        self.__acs_transaction_id = value

    @property
    def applied_exemption(self) -> str | None:
        """
        | Exemption code from Carte Bancaire (130) (unknown possible values so far -free format).

        Type: str
        """
        return self.__applied_exemption

    @applied_exemption.setter
    def applied_exemption(self, value: str | None) -> None:
        self.__applied_exemption = value

    @property
    def cavv(self) -> str | None:
        """
        | The CAVV (cardholder authentication verification value) or AAV (accountholder authentication value) provides an authentication validation value. Note: This is mandatory for ECI 2 and 5.

        Type: str
        """
        return self.__cavv

    @cavv.setter
    def cavv(self, value: str | None) -> None:
        self.__cavv = value

    @property
    def cavv_algorithm(self) -> str | None:
        """
        | The algorithm, from your 3D Secure provider, used to generate the authentication CAVV. Note: Required when
        
        * The 3D Secure authentication for the transaction is managed by a third-party 3D Secure authentication provider
        * You process the transaction through Atos

        Type: str
        """
        return self.__cavv_algorithm

    @cavv_algorithm.setter
    def cavv_algorithm(self, value: str | None) -> None:
        self.__cavv_algorithm = value

    @property
    def directory_server_transaction_id(self) -> str | None:
        """
        | The 3-D Secure Directory Server transaction ID that is used for the 3D Authentication Example: d4c849f8-24c6-4673-bf34-d0f822c81b16

        Type: str
        """
        return self.__directory_server_transaction_id

    @directory_server_transaction_id.setter
    def directory_server_transaction_id(self, value: str | None) -> None:
        self.__directory_server_transaction_id = value

    @property
    def eci(self) -> int | None:
        """
        | Electronic Commerce Indicator provides authentication validation results returned after AUTHENTICATIONVALIDATION
        
        * 0 = No authentication, Internet (no liability shift, not a 3D Secure transaction)
        * 1 = Authentication attempted (MasterCard)
        * 2 = Successful authentication (MasterCard)
        * 5 = Successful authentication (Visa, Diners Club, Amex)
        * 6 = Authentication attempted (Visa, Diners Club, Amex)
        * 7 = No authentication, Internet (no liability shift, not a 3D Secure transaction)
        * (empty) = Not checked or not enrolled

        Type: int
        """
        return self.__eci

    @eci.setter
    def eci(self, value: int | None) -> None:
        self.__eci = value

    @property
    def flow(self) -> str | None:
        """
        | 3D Secure Flow used during this transaction.

        Type: str
        """
        return self.__flow

    @flow.setter
    def flow(self, value: str | None) -> None:
        self.__flow = value

    @property
    def scheme_risk_score(self) -> int | None:
        """
        | Global score calculated by the Carte Bancaire (130) Scoring platform. Possible values from 0 to 99.

        Type: int
        """
        return self.__scheme_risk_score

    @scheme_risk_score.setter
    def scheme_risk_score(self, value: int | None) -> None:
        self.__scheme_risk_score = value

    @property
    def three_d_secure_version(self) -> str | None:
        """
        | The 3-D Secure version used for the authentication. Possible values:
        
        * v1
        * v2
        * 1.0.2
        * 2.1.0
        * 2.2.0

        Type: str
        """
        return self.__three_d_secure_version

    @three_d_secure_version.setter
    def three_d_secure_version(self, value: str | None) -> None:
        self.__three_d_secure_version = value

    @property
    def xid(self) -> str | None:
        """
        | The transaction ID that is used for the 3D Authentication

        Type: str
        """
        return self.__xid

    @xid.setter
    def xid(self, value: str | None) -> None:
        self.__xid = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.acs_transaction_id is not None:
            dictionary['acsTransactionId'] = self.acs_transaction_id
        if self.applied_exemption is not None:
            dictionary['appliedExemption'] = self.applied_exemption
        if self.cavv is not None:
            dictionary['cavv'] = self.cavv
        if self.cavv_algorithm is not None:
            dictionary['cavvAlgorithm'] = self.cavv_algorithm
        if self.directory_server_transaction_id is not None:
            dictionary['directoryServerTransactionId'] = self.directory_server_transaction_id
        if self.eci is not None:
            dictionary['eci'] = self.eci
        if self.flow is not None:
            dictionary['flow'] = self.flow
        if self.scheme_risk_score is not None:
            dictionary['schemeRiskScore'] = self.scheme_risk_score
        if self.three_d_secure_version is not None:
            dictionary['threeDSecureVersion'] = self.three_d_secure_version
        if self.xid is not None:
            dictionary['xid'] = self.xid
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ExternalCardholderAuthenticationData':
        super().from_dictionary(dictionary)
        if 'acsTransactionId' in dictionary:
            self.acs_transaction_id = dictionary['acsTransactionId']
        if 'appliedExemption' in dictionary:
            self.applied_exemption = dictionary['appliedExemption']
        if 'cavv' in dictionary:
            self.cavv = dictionary['cavv']
        if 'cavvAlgorithm' in dictionary:
            self.cavv_algorithm = dictionary['cavvAlgorithm']
        if 'directoryServerTransactionId' in dictionary:
            self.directory_server_transaction_id = dictionary['directoryServerTransactionId']
        if 'eci' in dictionary:
            self.eci = dictionary['eci']
        if 'flow' in dictionary:
            self.flow = dictionary['flow']
        if 'schemeRiskScore' in dictionary:
            self.scheme_risk_score = dictionary['schemeRiskScore']
        if 'threeDSecureVersion' in dictionary:
            self.three_d_secure_version = dictionary['threeDSecureVersion']
        if 'xid' in dictionary:
            self.xid = dictionary['xid']
        return self

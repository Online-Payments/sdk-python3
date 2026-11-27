#
# This file was automatically generated.
#
from .data_object import DataObject


class CreateCertificateResponse(DataObject):

    __slots__ = (
        "__certificate_id",
        "__signed_certificate",
    )

    __certificate_id: str | None
    __signed_certificate: str | None

    def __init__(
        self,
        *,
        certificate_id: str | None = None,
        signed_certificate: str | None = None,
    ) -> None:
        self.certificate_id = certificate_id
        self.signed_certificate = signed_certificate

    @property
    def certificate_id(self) -> str | None:
        """
        | A unique identifier for the certificate generated on the GoPay platform, facilitating effective tracking and management of detokenization actions.

        Type: str
        """
        return self.__certificate_id

    @certificate_id.setter
    def certificate_id(self, value: str | None) -> None:
        self.__certificate_id = value

    @property
    def signed_certificate(self) -> str | None:
        """
        | The signed certificate in base64 encoded string format, used for secure communication and authentication in API transactions.

        Type: str
        """
        return self.__signed_certificate

    @signed_certificate.setter
    def signed_certificate(self, value: str | None) -> None:
        self.__signed_certificate = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.certificate_id is not None:
            dictionary['certificateId'] = self.certificate_id
        if self.signed_certificate is not None:
            dictionary['signedCertificate'] = self.signed_certificate
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreateCertificateResponse':
        super().from_dictionary(dictionary)
        if 'certificateId' in dictionary:
            self.certificate_id = dictionary['certificateId']
        if 'signedCertificate' in dictionary:
            self.signed_certificate = dictionary['signedCertificate']
        return self

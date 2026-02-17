# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class CreateCertificateResponse(DataObject):

    __certificate_id: Optional[str] = None
    __signed_certificate: Optional[str] = None

    @property
    def certificate_id(self) -> Optional[str]:
        """
        | A unique identifier for the certificate generated on the GoPay platform, facilitating effective tracking and management of detokenization actions.

        Type: str
        """
        return self.__certificate_id

    @certificate_id.setter
    def certificate_id(self, value: Optional[str]) -> None:
        self.__certificate_id = value

    @property
    def signed_certificate(self) -> Optional[str]:
        """
        | The signed certificate in base64 encoded string format, used for secure communication and authentication in API transactions.

        Type: str
        """
        return self.__signed_certificate

    @signed_certificate.setter
    def signed_certificate(self, value: Optional[str]) -> None:
        self.__signed_certificate = value

    def to_dictionary(self) -> dict:
        dictionary = super(CreateCertificateResponse, self).to_dictionary()
        if self.certificate_id is not None:
            dictionary['certificateId'] = self.certificate_id
        if self.signed_certificate is not None:
            dictionary['signedCertificate'] = self.signed_certificate
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CreateCertificateResponse':
        super(CreateCertificateResponse, self).from_dictionary(dictionary)
        if 'certificateId' in dictionary:
            self.certificate_id = dictionary['certificateId']
        if 'signedCertificate' in dictionary:
            self.signed_certificate = dictionary['signedCertificate']
        return self

import platform
import re
from base64 import b64encode
from typing import Optional, Sequence

from .i_metadata_provider import IMetadataProvider
from .request_header import RequestHeader

from onlinepayments.sdk.domain.data_object import DataObject
from onlinepayments.sdk.domain.shopping_cart_extension import ShoppingCartExtension
from onlinepayments.sdk.json.default_marshaller import DefaultMarshaller


class IterProperty(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return self.func(owner)


class MetadataProvider(IMetadataProvider):
    """
    Provides meta info about the server.
    """
    __sdk_version = "5.0.0"
    __server_meta_info_header = "X-GCS-ServerMetaInfo"
    __prohibited_headers = tuple(sorted([__server_meta_info_header, "X-GCS-Idempotence-Key", "Date", "Content-Type", "Authorization"],
                                        key=str.lower))
    __metadata_headers: Sequence[RequestHeader] = None

    class ServerMetaInfo(DataObject):
        platform_identifier = None
        sdk_identifier = None
        sdk_creator = None
        integrator = None
        shopping_cart_extension = None

        def to_dictionary(self) -> dict:
            dictionary = super(MetadataProvider.ServerMetaInfo, self).to_dictionary()
            if self.platform_identifier is not None:
                dictionary['platformIdentifier'] = self.platform_identifier
            if self.sdk_identifier is not None:
                dictionary['sdkIdentifier'] = self.sdk_identifier
            if self.sdk_creator is not None:
                dictionary['sdkCreator'] = self.sdk_creator
            if self.integrator is not None:
                dictionary['integrator'] = self.integrator
            if self.shopping_cart_extension is not None:
                dictionary['shoppingCartExtension'] = self.shopping_cart_extension.to_dictionary()
            return dictionary

        def from_dictionary(self, dictionary: dict) -> 'MetadataProvider.ServerMetaInfo':
            super(MetadataProvider.ServerMetaInfo, self).from_dictionary(dictionary)
            if 'platformIdentifier' in dictionary:
                self.platform_identifier = dictionary['platformIdentifier']
            if 'sdkIdentifier' in dictionary:
                self.sdk_identifier = dictionary['sdkIdentifier']
            if 'sdkCreator' in dictionary:
                self.sdk_creator = dictionary['sdkCreator']
            if 'integrator' in dictionary:
                self.integrator = dictionary['integrator']
            if 'shoppingCartExtension' in dictionary:
                if not isinstance(dictionary['shoppingCartExtension'], dict):
                    raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['shoppingCartExtension']))
                self.shopping_cart_extension = ShoppingCartExtension.create_from_dictionary(dictionary['shoppingCartExtension'])
            return self

    def __init__(self, integrator: Optional[str], shopping_cart_extension: Optional[ShoppingCartExtension] = None,
                 additional_request_headers: Optional[Sequence[RequestHeader]] = ()):
        if integrator is None or not integrator.strip():
            raise ValueError("integrator is required")

        MetadataProvider.__validate_additional_request_headers(additional_request_headers)

        def subber(name_or_value):
            return re.sub(r'\r?\n(?:(?![\r\n])\s)*', " ", name_or_value).strip()
        additional_request_headers = [RequestHeader(subber(header.name), subber(header.value)) for header in additional_request_headers]

        server_meta_info = self.ServerMetaInfo()
        server_meta_info.platform_identifier = self._platform_identifier
        server_meta_info.sdk_identifier = self._sdk_identifier
        server_meta_info.sdk_creator = "OnlinePayments"
        server_meta_info.integrator = integrator
        server_meta_info.shopping_cart_extension = shopping_cart_extension

        server_meta_info_string = DefaultMarshaller.instance().marshal(server_meta_info)
        server_meta_info_header = RequestHeader(self.__server_meta_info_header, b64encode(server_meta_info_string.encode('utf-8')).decode('utf-8'))
        if not additional_request_headers:
            self.__metadata_headers = tuple([server_meta_info_header])
        else:
            request_headers = [server_meta_info_header]
            request_headers.extend(additional_request_headers)
            self.__metadata_headers = tuple(request_headers)

    @staticmethod
    def __validate_additional_request_headers(additional_request_headers: Optional[Sequence[RequestHeader]]) -> None:
        if additional_request_headers is not None:
            for additional_request_header in additional_request_headers:
                MetadataProvider.__validate_additional_request_header(additional_request_header)

    @staticmethod
    def __validate_additional_request_header(additional_request_header: RequestHeader) -> None:
        try:
            if additional_request_header.name in MetadataProvider.__prohibited_headers:
                raise ValueError("request header not allowed: " + str(additional_request_header))
        except AttributeError:
            raise AttributeError("Each request header should have an attribute 'name' and an attribute 'value'")

    @IterProperty
    def prohibited_headers(self) -> Sequence[str]:
        return self.__prohibited_headers

    @property
    def metadata_headers(self) -> Sequence[RequestHeader]:
        """
        :return: The server related headers containing the metadata to be
         associated with the request (if any). This will always contain at least
         an automatically generated header X-GCS-ServerMetaInfo.
        """
        return self.__metadata_headers

    @property
    def _platform_identifier(self) -> str:
        return platform.system() + " " + platform.release() + "/" + \
               platform.version() + " Python/" + platform.python_version() + \
               " (" + platform.python_implementation() + "; " + \
               str(platform.python_compiler()) + ")"

    @property
    def _sdk_identifier(self) -> str:
        return "PythonServerSDK/v" + self.__sdk_version

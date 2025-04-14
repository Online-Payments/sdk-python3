import uuid

from typing import Mapping

from onlinepayments.sdk.domain.uploadable_file import UploadableFile


class MultipartFormDataObject(object):
    """
    A representation of a multipart/form-data object.
    """

    def __init__(self):
        self.__boundary = str(uuid.uuid4())
        self.__content_type = "multipart/form-data; boundary=" + self.__boundary
        self.__values = {}
        self.__files = {}

    @property
    def boundary(self) -> str:
        return self.__boundary

    @property
    def content_type(self) -> str:
        return self.__content_type

    @property
    def values(self) -> Mapping[str, str]:
        return self.__values

    @property
    def files(self) -> Mapping[str, UploadableFile]:
        return self.__files

    def add_value(self, parameter_name: str, value: str) -> None:
        if parameter_name is None or not parameter_name.strip():
            raise ValueError("parameter_name is required")
        if value is None:
            raise ValueError("value is required")
        if parameter_name in self.__values or parameter_name in self.__files:
            raise ValueError("duplicate parameterName: " + parameter_name)
        self.__values[parameter_name] = value

    def add_file(self, parameter_name: str, uploadable_file: UploadableFile) -> None:
        if parameter_name is None or not parameter_name.strip():
            raise ValueError("parameter_name is required")
        if uploadable_file is None:
            raise ValueError("uploadable_file is required")
        if parameter_name in self.__values or parameter_name in self.__files:
            raise ValueError("duplicate parameterName: " + parameter_name)
        self.__files[parameter_name] = uploadable_file

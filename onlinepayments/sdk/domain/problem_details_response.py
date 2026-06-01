# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class ProblemDetailsResponse(DataObject):

    __detail: Optional[str] = None
    __instance: Optional[str] = None
    __status: Optional[int] = None
    __title: Optional[str] = None
    __type: Optional[str] = None

    @property
    def detail(self) -> Optional[str]:
        """
        | A human-readable explanation specific to this occurrence of the problem.

        Type: str
        """
        return self.__detail

    @detail.setter
    def detail(self, value: Optional[str]) -> None:
        self.__detail = value

    @property
    def instance(self) -> Optional[str]:
        """
        | A URI reference that identifies the specific occurrence of the problem.

        Type: str
        """
        return self.__instance

    @instance.setter
    def instance(self, value: Optional[str]) -> None:
        self.__instance = value

    @property
    def status(self) -> Optional[int]:
        """
        | The HTTP status code.

        Type: int
        """
        return self.__status

    @status.setter
    def status(self, value: Optional[int]) -> None:
        self.__status = value

    @property
    def title(self) -> Optional[str]:
        """
        | A short, human-readable summary of the problem type.

        Type: str
        """
        return self.__title

    @title.setter
    def title(self, value: Optional[str]) -> None:
        self.__title = value

    @property
    def type(self) -> Optional[str]:
        """
        | A URI reference that identifies the problem type.

        Type: str
        """
        return self.__type

    @type.setter
    def type(self, value: Optional[str]) -> None:
        self.__type = value

    def to_dictionary(self) -> dict:
        dictionary = super(ProblemDetailsResponse, self).to_dictionary()
        if self.detail is not None:
            dictionary['detail'] = self.detail
        if self.instance is not None:
            dictionary['instance'] = self.instance
        if self.status is not None:
            dictionary['status'] = self.status
        if self.title is not None:
            dictionary['title'] = self.title
        if self.type is not None:
            dictionary['type'] = self.type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ProblemDetailsResponse':
        super(ProblemDetailsResponse, self).from_dictionary(dictionary)
        if 'detail' in dictionary:
            self.detail = dictionary['detail']
        if 'instance' in dictionary:
            self.instance = dictionary['instance']
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'title' in dictionary:
            self.title = dictionary['title']
        if 'type' in dictionary:
            self.type = dictionary['type']
        return self

# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from .data_object import DataObject


class EmptyValidator(DataObject):

    def to_dictionary(self) -> dict:
        dictionary = super(EmptyValidator, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'EmptyValidator':
        super(EmptyValidator, self).from_dictionary(dictionary)
        return self

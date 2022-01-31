# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.payment_product_field_validators import PaymentProductFieldValidators


class PaymentProductFieldDataRestrictions(DataObject):
    """
    | Object containing data restrictions that apply to this field, like minimum and/or maximum length
    """

    __is_required = None
    __validators = None

    @property
    def is_required(self) -> bool:
        """
        | * true - Indicates that this field is required
        | * false - Indicates that this field is optional

        Type: bool
        """
        return self.__is_required

    @is_required.setter
    def is_required(self, value: bool):
        self.__is_required = value

    @property
    def validators(self) -> PaymentProductFieldValidators:
        """
        | Object containing the details of the validations on the field

        Type: :class:`onlinepayments.sdk.domain.payment_product_field_validators.PaymentProductFieldValidators`
        """
        return self.__validators

    @validators.setter
    def validators(self, value: PaymentProductFieldValidators):
        self.__validators = value

    def to_dictionary(self):
        dictionary = super(PaymentProductFieldDataRestrictions, self).to_dictionary()
        if self.is_required is not None:
            dictionary['isRequired'] = self.is_required
        if self.validators is not None:
            dictionary['validators'] = self.validators.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductFieldDataRestrictions, self).from_dictionary(dictionary)
        if 'isRequired' in dictionary:
            self.is_required = dictionary['isRequired']
        if 'validators' in dictionary:
            if not isinstance(dictionary['validators'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['validators']))
            value = PaymentProductFieldValidators()
            self.validators = value.from_dictionary(dictionary['validators'])
        return self

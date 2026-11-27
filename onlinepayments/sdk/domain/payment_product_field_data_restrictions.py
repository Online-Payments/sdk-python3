#
# This file was automatically generated.
#
from .data_object import DataObject
from .payment_product_field_validators import PaymentProductFieldValidators


class PaymentProductFieldDataRestrictions(DataObject):

    __slots__ = (
        "__is_required",
        "__validators",
    )

    __is_required: bool | None
    __validators: PaymentProductFieldValidators | None

    def __init__(
        self,
        *,
        is_required: bool | None = None,
        validators: PaymentProductFieldValidators | None = None,
    ) -> None:
        self.is_required = is_required
        self.validators = validators

    @property
    def is_required(self) -> bool | None:
        """
        * true - Indicates that this field is required
        * false - Indicates that this field is optional

        Type: bool
        """
        return self.__is_required

    @is_required.setter
    def is_required(self, value: bool | None) -> None:
        self.__is_required = value

    @property
    def validators(self) -> PaymentProductFieldValidators | None:
        """
        | Object containing the details of the validations on the field

        Type: :class:`onlinepayments.sdk.domain.payment_product_field_validators.PaymentProductFieldValidators`
        """
        return self.__validators

    @validators.setter
    def validators(self, value: PaymentProductFieldValidators | None) -> None:
        self.__validators = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.is_required is not None:
            dictionary['isRequired'] = self.is_required
        if self.validators is not None:
            dictionary['validators'] = self.validators.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentProductFieldDataRestrictions':
        super().from_dictionary(dictionary)
        if 'isRequired' in dictionary:
            self.is_required = dictionary['isRequired']
        if 'validators' in dictionary:
            if not isinstance(dictionary['validators'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['validators']))
            value = PaymentProductFieldValidators()
            self.validators = value.from_dictionary(dictionary['validators'])
        return self

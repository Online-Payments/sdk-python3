# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class SurchargeRate(DataObject):
    """
    | A summary of surcharge details used in the calculation of the surcharge amount. null if result = NO_SURCHARGE
    """

    __ad_valorem_rate = None
    __specific_rate = None
    __surcharge_product_type_id = None
    __surcharge_product_type_version = None

    @property
    def ad_valorem_rate(self) -> float:
        """
        | A percentage rate defined on a merchant's configuration used in the calculation of a surcharge amount.

        Type: float
        """
        return self.__ad_valorem_rate

    @ad_valorem_rate.setter
    def ad_valorem_rate(self, value: float):
        self.__ad_valorem_rate = value

    @property
    def specific_rate(self) -> int:
        """
        | A specific, fixed rate in cents defined on a merchant's configuration that is used in the calculation of a surcharge amount.

        Type: int
        """
        return self.__specific_rate

    @specific_rate.setter
    def specific_rate(self, value: int):
        self.__specific_rate = value

    @property
    def surcharge_product_type_id(self) -> str:
        """
        | The name of the applicable surcharge rates for the relevant payment product

        Type: str
        """
        return self.__surcharge_product_type_id

    @surcharge_product_type_id.setter
    def surcharge_product_type_id(self, value: str):
        self.__surcharge_product_type_id = value

    @property
    def surcharge_product_type_version(self) -> str:
        """
        | A specific version identifier of the surcharge rates as applied for this request

        Type: str
        """
        return self.__surcharge_product_type_version

    @surcharge_product_type_version.setter
    def surcharge_product_type_version(self, value: str):
        self.__surcharge_product_type_version = value

    def to_dictionary(self):
        dictionary = super(SurchargeRate, self).to_dictionary()
        if self.ad_valorem_rate is not None:
            dictionary['adValoremRate'] = self.ad_valorem_rate
        if self.specific_rate is not None:
            dictionary['specificRate'] = self.specific_rate
        if self.surcharge_product_type_id is not None:
            dictionary['surchargeProductTypeId'] = self.surcharge_product_type_id
        if self.surcharge_product_type_version is not None:
            dictionary['surchargeProductTypeVersion'] = self.surcharge_product_type_version
        return dictionary

    def from_dictionary(self, dictionary):
        super(SurchargeRate, self).from_dictionary(dictionary)
        if 'adValoremRate' in dictionary:
            self.ad_valorem_rate = dictionary['adValoremRate']
        if 'specificRate' in dictionary:
            self.specific_rate = dictionary['specificRate']
        if 'surchargeProductTypeId' in dictionary:
            self.surcharge_product_type_id = dictionary['surchargeProductTypeId']
        if 'surchargeProductTypeVersion' in dictionary:
            self.surcharge_product_type_version = dictionary['surchargeProductTypeVersion']
        return self

#
# This file was automatically generated.
#
from .data_object import DataObject


class SurchargeRate(DataObject):

    __slots__ = (
        "__ad_valorem_rate",
        "__specific_rate",
        "__surcharge_product_type_id",
        "__surcharge_product_type_version",
    )

    __ad_valorem_rate: float | None
    __specific_rate: int | None
    __surcharge_product_type_id: str | None
    __surcharge_product_type_version: str | None

    def __init__(
        self,
        *,
        ad_valorem_rate: float | None = None,
        specific_rate: int | None = None,
        surcharge_product_type_id: str | None = None,
        surcharge_product_type_version: str | None = None,
    ) -> None:
        self.ad_valorem_rate = ad_valorem_rate
        self.specific_rate = specific_rate
        self.surcharge_product_type_id = surcharge_product_type_id
        self.surcharge_product_type_version = surcharge_product_type_version

    @property
    def ad_valorem_rate(self) -> float | None:
        """
        | A percentage rate defined on a merchant's configuration used in the calculation of a surcharge amount.

        Type: float
        """
        return self.__ad_valorem_rate

    @ad_valorem_rate.setter
    def ad_valorem_rate(self, value: float | None) -> None:
        self.__ad_valorem_rate = value

    @property
    def specific_rate(self) -> int | None:
        """
        | A specific, fixed rate in cents defined on a merchant's configuration that is used in the calculation of a surcharge amount.

        Type: int
        """
        return self.__specific_rate

    @specific_rate.setter
    def specific_rate(self, value: int | None) -> None:
        self.__specific_rate = value

    @property
    def surcharge_product_type_id(self) -> str | None:
        """
        | The name of the applicable surcharge rates for the relevant payment product

        Type: str
        """
        return self.__surcharge_product_type_id

    @surcharge_product_type_id.setter
    def surcharge_product_type_id(self, value: str | None) -> None:
        self.__surcharge_product_type_id = value

    @property
    def surcharge_product_type_version(self) -> str | None:
        """
        | A specific version identifier of the surcharge rates as applied for this request

        Type: str
        """
        return self.__surcharge_product_type_version

    @surcharge_product_type_version.setter
    def surcharge_product_type_version(self, value: str | None) -> None:
        self.__surcharge_product_type_version = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.ad_valorem_rate is not None:
            dictionary['adValoremRate'] = self.ad_valorem_rate
        if self.specific_rate is not None:
            dictionary['specificRate'] = self.specific_rate
        if self.surcharge_product_type_id is not None:
            dictionary['surchargeProductTypeId'] = self.surcharge_product_type_id
        if self.surcharge_product_type_version is not None:
            dictionary['surchargeProductTypeVersion'] = self.surcharge_product_type_version
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SurchargeRate':
        super().from_dictionary(dictionary)
        if 'adValoremRate' in dictionary:
            self.ad_valorem_rate = dictionary['adValoremRate']
        if 'specificRate' in dictionary:
            self.specific_rate = dictionary['specificRate']
        if 'surchargeProductTypeId' in dictionary:
            self.surcharge_product_type_id = dictionary['surchargeProductTypeId']
        if 'surchargeProductTypeVersion' in dictionary:
            self.surcharge_product_type_version = dictionary['surchargeProductTypeVersion']
        return self

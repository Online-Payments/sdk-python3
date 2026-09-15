# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .car_rental_pickup_return_data import CarRentalPickupReturnData
from .car_rental_vehicle_data import CarRentalVehicleData
from .data_object import DataObject


class CarRentalData(DataObject):

    __agreement_number: Optional[str] = None
    __cardholder_notified: Optional[bool] = None
    __charges_amount: Optional[int] = None
    __charges_category: Optional[str] = None
    __distance_measure: Optional[int] = None
    __distance_unit: Optional[str] = None
    __driver_identification_number: Optional[str] = None
    __driver_tax_number: Optional[str] = None
    __pickup: Optional[CarRentalPickupReturnData] = None
    __rental_rate_amount: Optional[int] = None
    __rental_rate_type: Optional[str] = None
    __renter_name: Optional[str] = None
    __return_: Optional[CarRentalPickupReturnData] = None
    __tax_exempt_indicator: Optional[bool] = None
    __toll_free_number: Optional[str] = None
    __vehicle: Optional[CarRentalVehicleData] = None

    @property
    def agreement_number(self) -> Optional[str]:
        """
        | This field contains the Auto Rental Agreement/Invoice Number (a.k.a., contract number) that corresponds to the rental agreement issued by the auto rental agency and signed by the cardholder. Amex =< an1-20 characters MasterCard =< an1-9 characters Visa =< an25 characters

        Type: str
        """
        return self.__agreement_number

    @agreement_number.setter
    def agreement_number(self, value: Optional[str]) -> None:
        self.__agreement_number = value

    @property
    def cardholder_notified(self) -> Optional[bool]:
        """
        | Cardholder has been notified of charge?

        Type: bool
        """
        return self.__cardholder_notified

    @cardholder_notified.setter
    def cardholder_notified(self, value: Optional[bool]) -> None:
        self.__cardholder_notified = value

    @property
    def charges_amount(self) -> Optional[int]:
        """
        | Fare amount (must be using currency of the transaction)

        Type: int
        """
        return self.__charges_amount

    @charges_amount.setter
    def charges_amount(self, value: Optional[int]) -> None:
        self.__charges_amount = value

    @property
    def charges_category(self) -> Optional[str]:
        """
        | Indicates type of additional charges added to an cardholder’s bill after return.

        Type: str
        """
        return self.__charges_category

    @charges_category.setter
    def charges_category(self, value: Optional[str]) -> None:
        self.__charges_category = value

    @property
    def distance_measure(self) -> Optional[int]:
        """
        | This field contains a value that corresponds to the distance traveled during the rental period. Amex =< n1-5 MasterCard =< n1-4 Visa =< n1-5

        Type: int
        """
        return self.__distance_measure

    @distance_measure.setter
    def distance_measure(self, value: Optional[int]) -> None:
        self.__distance_measure = value

    @property
    def distance_unit(self) -> Optional[str]:
        """
        | This field contains a code that corresponds to the unit of measure applicable to the distance traveled.

        Type: str
        """
        return self.__distance_unit

    @distance_unit.setter
    def distance_unit(self, value: Optional[str]) -> None:
        self.__distance_unit = value

    @property
    def driver_identification_number(self) -> Optional[str]:
        """
        | Unique identifier of the driver

        Type: str
        """
        return self.__driver_identification_number

    @driver_identification_number.setter
    def driver_identification_number(self, value: Optional[str]) -> None:
        self.__driver_identification_number = value

    @property
    def driver_tax_number(self) -> Optional[str]:
        """
        | This field contains the driver's Tax Identification Number (Tax ID). Amex =< an1-20 Visa =< an1-20

        Type: str
        """
        return self.__driver_tax_number

    @driver_tax_number.setter
    def driver_tax_number(self, value: Optional[str]) -> None:
        self.__driver_tax_number = value

    @property
    def pickup(self) -> Optional[CarRentalPickupReturnData]:
        """
        | Object containing specific data regarding the pickup or return of a rental car

        Type: :class:`onlinepayments.sdk.domain.car_rental_pickup_return_data.CarRentalPickupReturnData`
        """
        return self.__pickup

    @pickup.setter
    def pickup(self, value: Optional[CarRentalPickupReturnData]) -> None:
        self.__pickup = value

    @property
    def rental_rate_amount(self) -> Optional[int]:
        """
        | Fare amount.

        Type: int
        """
        return self.__rental_rate_amount

    @rental_rate_amount.setter
    def rental_rate_amount(self, value: Optional[int]) -> None:
        self.__rental_rate_amount = value

    @property
    def rental_rate_type(self) -> Optional[str]:
        """
        | Indicates daily, weekly or monthly rental rate

        Type: str
        """
        return self.__rental_rate_type

    @rental_rate_type.setter
    def rental_rate_type(self, value: Optional[str]) -> None:
        self.__rental_rate_type = value

    @property
    def renter_name(self) -> Optional[str]:
        """
        | This field contains the name of the person or business entity charged for the reservation or vehicle rental.

        Type: str
        """
        return self.__renter_name

    @renter_name.setter
    def renter_name(self, value: Optional[str]) -> None:
        self.__renter_name = value

    @property
    def return_(self) -> Optional[CarRentalPickupReturnData]:
        """
        | Object containing specific data regarding the pickup or return of a rental car

        Type: :class:`onlinepayments.sdk.domain.car_rental_pickup_return_data.CarRentalPickupReturnData`
        """
        return self.__return_

    @return_.setter
    def return_(self, value: Optional[CarRentalPickupReturnData]) -> None:
        self.__return_ = value

    @property
    def tax_exempt_indicator(self) -> Optional[bool]:
        """
        | This field indicate the taxable status (taxable/tax exempt).

        Type: bool
        """
        return self.__tax_exempt_indicator

    @tax_exempt_indicator.setter
    def tax_exempt_indicator(self, value: Optional[bool]) -> None:
        self.__tax_exempt_indicator = value

    @property
    def toll_free_number(self) -> Optional[str]:
        """
        | Customer service toll free number.

        Type: str
        """
        return self.__toll_free_number

    @toll_free_number.setter
    def toll_free_number(self, value: Optional[str]) -> None:
        self.__toll_free_number = value

    @property
    def vehicle(self) -> Optional[CarRentalVehicleData]:
        """
        | Object containing specific data regarding the vehicle

        Type: :class:`onlinepayments.sdk.domain.car_rental_vehicle_data.CarRentalVehicleData`
        """
        return self.__vehicle

    @vehicle.setter
    def vehicle(self, value: Optional[CarRentalVehicleData]) -> None:
        self.__vehicle = value

    def to_dictionary(self) -> dict:
        dictionary = super(CarRentalData, self).to_dictionary()
        if self.agreement_number is not None:
            dictionary['agreementNumber'] = self.agreement_number
        if self.cardholder_notified is not None:
            dictionary['cardholderNotified'] = self.cardholder_notified
        if self.charges_amount is not None:
            dictionary['chargesAmount'] = self.charges_amount
        if self.charges_category is not None:
            dictionary['chargesCategory'] = self.charges_category
        if self.distance_measure is not None:
            dictionary['distanceMeasure'] = self.distance_measure
        if self.distance_unit is not None:
            dictionary['distanceUnit'] = self.distance_unit
        if self.driver_identification_number is not None:
            dictionary['driverIdentificationNumber'] = self.driver_identification_number
        if self.driver_tax_number is not None:
            dictionary['driverTaxNumber'] = self.driver_tax_number
        if self.pickup is not None:
            dictionary['pickup'] = self.pickup.to_dictionary()
        if self.rental_rate_amount is not None:
            dictionary['rentalRateAmount'] = self.rental_rate_amount
        if self.rental_rate_type is not None:
            dictionary['rentalRateType'] = self.rental_rate_type
        if self.renter_name is not None:
            dictionary['renterName'] = self.renter_name
        if self.return_ is not None:
            dictionary['return'] = self.return_.to_dictionary()
        if self.tax_exempt_indicator is not None:
            dictionary['taxExemptIndicator'] = self.tax_exempt_indicator
        if self.toll_free_number is not None:
            dictionary['tollFreeNumber'] = self.toll_free_number
        if self.vehicle is not None:
            dictionary['vehicle'] = self.vehicle.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CarRentalData':
        super(CarRentalData, self).from_dictionary(dictionary)
        if 'agreementNumber' in dictionary:
            self.agreement_number = dictionary['agreementNumber']
        if 'cardholderNotified' in dictionary:
            self.cardholder_notified = dictionary['cardholderNotified']
        if 'chargesAmount' in dictionary:
            self.charges_amount = dictionary['chargesAmount']
        if 'chargesCategory' in dictionary:
            self.charges_category = dictionary['chargesCategory']
        if 'distanceMeasure' in dictionary:
            self.distance_measure = dictionary['distanceMeasure']
        if 'distanceUnit' in dictionary:
            self.distance_unit = dictionary['distanceUnit']
        if 'driverIdentificationNumber' in dictionary:
            self.driver_identification_number = dictionary['driverIdentificationNumber']
        if 'driverTaxNumber' in dictionary:
            self.driver_tax_number = dictionary['driverTaxNumber']
        if 'pickup' in dictionary:
            if not isinstance(dictionary['pickup'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['pickup']))
            value = CarRentalPickupReturnData()
            self.pickup = value.from_dictionary(dictionary['pickup'])
        if 'rentalRateAmount' in dictionary:
            self.rental_rate_amount = dictionary['rentalRateAmount']
        if 'rentalRateType' in dictionary:
            self.rental_rate_type = dictionary['rentalRateType']
        if 'renterName' in dictionary:
            self.renter_name = dictionary['renterName']
        if 'return' in dictionary:
            if not isinstance(dictionary['return'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['return']))
            value = CarRentalPickupReturnData()
            self.return_ = value.from_dictionary(dictionary['return'])
        if 'taxExemptIndicator' in dictionary:
            self.tax_exempt_indicator = dictionary['taxExemptIndicator']
        if 'tollFreeNumber' in dictionary:
            self.toll_free_number = dictionary['tollFreeNumber']
        if 'vehicle' in dictionary:
            if not isinstance(dictionary['vehicle'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['vehicle']))
            value = CarRentalVehicleData()
            self.vehicle = value.from_dictionary(dictionary['vehicle'])
        return self

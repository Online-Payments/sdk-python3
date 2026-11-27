#
# This file was automatically generated.
#
from .car_rental_pickup_return_data import CarRentalPickupReturnData
from .car_rental_vehicle_data import CarRentalVehicleData
from .data_object import DataObject


class CarRentalData(DataObject):

    __slots__ = (
        "__agreement_number",
        "__cardholder_notified",
        "__charges_amount",
        "__charges_category",
        "__distance_measure",
        "__distance_unit",
        "__driver_identification_number",
        "__driver_tax_number",
        "__pickup_details",
        "__rental_rate_amount",
        "__rental_rate_type",
        "__renter_name",
        "__return_details",
        "__tax_exempt_indicator",
        "__toll_free_number",
        "__vehicle",
    )

    __agreement_number: str | None
    __cardholder_notified: bool | None
    __charges_amount: int | None
    __charges_category: str | None
    __distance_measure: int | None
    __distance_unit: str | None
    __driver_identification_number: str | None
    __driver_tax_number: str | None
    __pickup_details: CarRentalPickupReturnData | None
    __rental_rate_amount: int | None
    __rental_rate_type: str | None
    __renter_name: str | None
    __return_details: CarRentalPickupReturnData | None
    __tax_exempt_indicator: bool | None
    __toll_free_number: str | None
    __vehicle: CarRentalVehicleData | None

    def __init__(
        self,
        *,
        agreement_number: str | None = None,
        cardholder_notified: bool | None = None,
        charges_amount: int | None = None,
        charges_category: str | None = None,
        distance_measure: int | None = None,
        distance_unit: str | None = None,
        driver_identification_number: str | None = None,
        driver_tax_number: str | None = None,
        pickup_details: CarRentalPickupReturnData | None = None,
        rental_rate_amount: int | None = None,
        rental_rate_type: str | None = None,
        renter_name: str | None = None,
        return_details: CarRentalPickupReturnData | None = None,
        tax_exempt_indicator: bool | None = None,
        toll_free_number: str | None = None,
        vehicle: CarRentalVehicleData | None = None,
    ) -> None:
        self.agreement_number = agreement_number
        self.cardholder_notified = cardholder_notified
        self.charges_amount = charges_amount
        self.charges_category = charges_category
        self.distance_measure = distance_measure
        self.distance_unit = distance_unit
        self.driver_identification_number = driver_identification_number
        self.driver_tax_number = driver_tax_number
        self.pickup_details = pickup_details
        self.rental_rate_amount = rental_rate_amount
        self.rental_rate_type = rental_rate_type
        self.renter_name = renter_name
        self.return_details = return_details
        self.tax_exempt_indicator = tax_exempt_indicator
        self.toll_free_number = toll_free_number
        self.vehicle = vehicle

    @property
    def agreement_number(self) -> str | None:
        """
        | This field contains the Auto Rental Agreement/Invoice Number (a.k.a., contract number) that corresponds to the rental agreement issued by the auto rental agency and signed by the cardholder. Amex =< an1-20 characters MasterCard =< an1-9 characters Visa =< an25 characters

        Type: str
        """
        return self.__agreement_number

    @agreement_number.setter
    def agreement_number(self, value: str | None) -> None:
        self.__agreement_number = value

    @property
    def cardholder_notified(self) -> bool | None:
        """
        | Cardholder has been notified of charge?

        Type: bool
        """
        return self.__cardholder_notified

    @cardholder_notified.setter
    def cardholder_notified(self, value: bool | None) -> None:
        self.__cardholder_notified = value

    @property
    def charges_amount(self) -> int | None:
        """
        | Fare amount (must be using currency of the transaction)

        Type: int
        """
        return self.__charges_amount

    @charges_amount.setter
    def charges_amount(self, value: int | None) -> None:
        self.__charges_amount = value

    @property
    def charges_category(self) -> str | None:
        """
        | Indicates type of additional charges added to an cardholder’s bill after return.

        Type: str
        """
        return self.__charges_category

    @charges_category.setter
    def charges_category(self, value: str | None) -> None:
        self.__charges_category = value

    @property
    def distance_measure(self) -> int | None:
        """
        | This field contains a value that corresponds to the distance traveled during the rental period. Amex =< n1-5 MasterCard =< n1-4 Visa =< n1-5

        Type: int
        """
        return self.__distance_measure

    @distance_measure.setter
    def distance_measure(self, value: int | None) -> None:
        self.__distance_measure = value

    @property
    def distance_unit(self) -> str | None:
        """
        | This field contains a code that corresponds to the unit of measure applicable to the distance traveled.

        Type: str
        """
        return self.__distance_unit

    @distance_unit.setter
    def distance_unit(self, value: str | None) -> None:
        self.__distance_unit = value

    @property
    def driver_identification_number(self) -> str | None:
        """
        | Unique identifier of the driver

        Type: str
        """
        return self.__driver_identification_number

    @driver_identification_number.setter
    def driver_identification_number(self, value: str | None) -> None:
        self.__driver_identification_number = value

    @property
    def driver_tax_number(self) -> str | None:
        """
        | This field contains the driver's Tax Identification Number (Tax ID). Amex =< an1-20 Visa =< an1-20

        Type: str
        """
        return self.__driver_tax_number

    @driver_tax_number.setter
    def driver_tax_number(self, value: str | None) -> None:
        self.__driver_tax_number = value

    @property
    def pickup_details(self) -> CarRentalPickupReturnData | None:
        """
        | Object containing specific data regarding the pickup or return of a rental car

        Type: :class:`onlinepayments.sdk.domain.car_rental_pickup_return_data.CarRentalPickupReturnData`
        """
        return self.__pickup_details

    @pickup_details.setter
    def pickup_details(self, value: CarRentalPickupReturnData | None) -> None:
        self.__pickup_details = value

    @property
    def rental_rate_amount(self) -> int | None:
        """
        | Fare amount.

        Type: int
        """
        return self.__rental_rate_amount

    @rental_rate_amount.setter
    def rental_rate_amount(self, value: int | None) -> None:
        self.__rental_rate_amount = value

    @property
    def rental_rate_type(self) -> str | None:
        """
        | Indicates daily, weekly or monthly rental rate

        Type: str
        """
        return self.__rental_rate_type

    @rental_rate_type.setter
    def rental_rate_type(self, value: str | None) -> None:
        self.__rental_rate_type = value

    @property
    def renter_name(self) -> str | None:
        """
        | This field contains the name of the person or business entity charged for the reservation or vehicle rental.

        Type: str
        """
        return self.__renter_name

    @renter_name.setter
    def renter_name(self, value: str | None) -> None:
        self.__renter_name = value

    @property
    def return_details(self) -> CarRentalPickupReturnData | None:
        """
        | Object containing specific data regarding the pickup or return of a rental car

        Type: :class:`onlinepayments.sdk.domain.car_rental_pickup_return_data.CarRentalPickupReturnData`
        """
        return self.__return_details

    @return_details.setter
    def return_details(self, value: CarRentalPickupReturnData | None) -> None:
        self.__return_details = value

    @property
    def tax_exempt_indicator(self) -> bool | None:
        """
        | This field indicate the taxable status (taxable/tax exempt).

        Type: bool
        """
        return self.__tax_exempt_indicator

    @tax_exempt_indicator.setter
    def tax_exempt_indicator(self, value: bool | None) -> None:
        self.__tax_exempt_indicator = value

    @property
    def toll_free_number(self) -> str | None:
        """
        | Customer service toll free number.

        Type: str
        """
        return self.__toll_free_number

    @toll_free_number.setter
    def toll_free_number(self, value: str | None) -> None:
        self.__toll_free_number = value

    @property
    def vehicle(self) -> CarRentalVehicleData | None:
        """
        | Object containing specific data regarding the vehicle

        Type: :class:`onlinepayments.sdk.domain.car_rental_vehicle_data.CarRentalVehicleData`
        """
        return self.__vehicle

    @vehicle.setter
    def vehicle(self, value: CarRentalVehicleData | None) -> None:
        self.__vehicle = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
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
        if self.pickup_details is not None:
            dictionary['pickupDetails'] = self.pickup_details.to_dictionary()
        if self.rental_rate_amount is not None:
            dictionary['rentalRateAmount'] = self.rental_rate_amount
        if self.rental_rate_type is not None:
            dictionary['rentalRateType'] = self.rental_rate_type
        if self.renter_name is not None:
            dictionary['renterName'] = self.renter_name
        if self.return_details is not None:
            dictionary['returnDetails'] = self.return_details.to_dictionary()
        if self.tax_exempt_indicator is not None:
            dictionary['taxExemptIndicator'] = self.tax_exempt_indicator
        if self.toll_free_number is not None:
            dictionary['tollFreeNumber'] = self.toll_free_number
        if self.vehicle is not None:
            dictionary['vehicle'] = self.vehicle.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CarRentalData':
        super().from_dictionary(dictionary)
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
        if 'pickupDetails' in dictionary:
            if not isinstance(dictionary['pickupDetails'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['pickupDetails']))
            value = CarRentalPickupReturnData()
            self.pickup_details = value.from_dictionary(dictionary['pickupDetails'])
        if 'rentalRateAmount' in dictionary:
            self.rental_rate_amount = dictionary['rentalRateAmount']
        if 'rentalRateType' in dictionary:
            self.rental_rate_type = dictionary['rentalRateType']
        if 'renterName' in dictionary:
            self.renter_name = dictionary['renterName']
        if 'returnDetails' in dictionary:
            if not isinstance(dictionary['returnDetails'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['returnDetails']))
            value = CarRentalPickupReturnData()
            self.return_details = value.from_dictionary(dictionary['returnDetails'])
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

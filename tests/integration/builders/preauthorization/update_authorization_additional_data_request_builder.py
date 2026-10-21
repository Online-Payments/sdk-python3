from onlinepayments.sdk.domain.car_rental_data import CarRentalData
from onlinepayments.sdk.domain.car_rental_pickup_return_data import CarRentalPickupReturnData
from onlinepayments.sdk.domain.car_rental_vehicle_data import CarRentalVehicleData
from onlinepayments.sdk.domain.update_authorization_additional_data_request import UpdateAuthorizationAdditionalDataRequest


class UpdateAuthorizationAdditionalDataRequestBuilder:

    def __init__(self):
        self._charges_category = "gas"
        self._minimal = False

    def with_charges_category(self, charges_category):
        self._charges_category = charges_category
        return self

    def with_minimal_car_rental_data(self):
        self._minimal = True
        return self

    def build(self):
        request = UpdateAuthorizationAdditionalDataRequest()
        request.car_rental_data = self._build_minimal_car_rental_data() if self._minimal else self._build_full_car_rental_data()

        return request

    def _build_minimal_car_rental_data(self):
        car_rental_data = CarRentalData()
        car_rental_data.agreement_number = "A1234567"
        car_rental_data.charges_amount = 0
        car_rental_data.charges_category = self._charges_category
        car_rental_data.pickup_details = self._build_pickup_return_details("2026-09-28T090000.000Z")
        car_rental_data.return_details = self._build_pickup_return_details("2026-09-30T090000.000Z")
        car_rental_data.rental_rate_amount = 1000
        car_rental_data.rental_rate_type = "daily"
        car_rental_data.renter_name = "Wile E. Coyote"

        return car_rental_data

    def _build_full_car_rental_data(self):
        vehicle = CarRentalVehicleData()
        vehicle.class_id = "CDMR"
        vehicle.identification_number = "VIN123456"

        car_rental_data = self._build_minimal_car_rental_data()
        car_rental_data.cardholder_notified = True
        car_rental_data.distance_measure = 250
        car_rental_data.distance_unit = "kilometers"
        car_rental_data.driver_identification_number = "DRV123456"
        car_rental_data.driver_tax_number = "BE0123456789"
        car_rental_data.tax_exempt_indicator = False
        car_rental_data.toll_free_number = "0800123456"
        car_rental_data.vehicle = vehicle

        return car_rental_data

    @staticmethod
    def _build_pickup_return_details(date):
        details = CarRentalPickupReturnData()
        details.address = "Da Vincilaan 3"
        details.city = "Brussels"
        details.country = 56
        details.date = date
        details.location = "Brussels Airport"
        details.postcode = "1930"
        details.state = "Flemish Brabant"

        return details

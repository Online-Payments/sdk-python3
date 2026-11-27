#
# This file was automatically generated.
#
from .data_object import DataObject


class AirlineFlightLeg(DataObject):

    __slots__ = (
        "__airline_class",
        "__arrival_airport",
        "__arrival_time",
        "__carrier_code",
        "__conjunction_ticket",
        "__coupon_number",
        "__date",
        "__departure_time",
        "__endorsement_or_restriction",
        "__exchange_ticket",
        "__fare",
        "__fare_basis",
        "__fee",
        "__flight_code",
        "__flight_number",
        "__leg_fare",
        "__number",
        "__origin_airport",
        "__passenger_class",
        "__stopover_code",
        "__taxes",
    )

    __airline_class: str | None
    __arrival_airport: str | None
    __arrival_time: str | None
    __carrier_code: str | None
    __conjunction_ticket: str | None
    __coupon_number: str | None
    __date: str | None
    __departure_time: str | None
    __endorsement_or_restriction: str | None
    __exchange_ticket: str | None
    __fare: str | None
    __fare_basis: str | None
    __fee: int | None
    __flight_code: str | None
    __flight_number: str | None
    __leg_fare: int | None
    __number: int | None
    __origin_airport: str | None
    __passenger_class: str | None
    __stopover_code: str | None
    __taxes: int | None

    def __init__(
        self,
        *,
        airline_class: str | None = None,
        arrival_airport: str | None = None,
        arrival_time: str | None = None,
        carrier_code: str | None = None,
        conjunction_ticket: str | None = None,
        coupon_number: str | None = None,
        date: str | None = None,
        departure_time: str | None = None,
        endorsement_or_restriction: str | None = None,
        exchange_ticket: str | None = None,
        fare: str | None = None,
        fare_basis: str | None = None,
        fee: int | None = None,
        flight_code: str | None = None,
        flight_number: str | None = None,
        leg_fare: int | None = None,
        number: int | None = None,
        origin_airport: str | None = None,
        passenger_class: str | None = None,
        stopover_code: str | None = None,
        taxes: int | None = None,
    ) -> None:
        self.airline_class = airline_class
        self.arrival_airport = arrival_airport
        self.arrival_time = arrival_time
        self.carrier_code = carrier_code
        self.conjunction_ticket = conjunction_ticket
        self.coupon_number = coupon_number
        self.date = date
        self.departure_time = departure_time
        self.endorsement_or_restriction = endorsement_or_restriction
        self.exchange_ticket = exchange_ticket
        self.fare = fare
        self.fare_basis = fare_basis
        self.fee = fee
        self.flight_code = flight_code
        self.flight_number = flight_number
        self.leg_fare = leg_fare
        self.number = number
        self.origin_airport = origin_airport
        self.passenger_class = passenger_class
        self.stopover_code = stopover_code
        self.taxes = taxes

    @property
    def airline_class(self) -> str | None:
        """
        | Reservation Booking Designator This field is used by the following payment products: cards

        Type: str
        """
        return self.__airline_class

    @airline_class.setter
    def airline_class(self, value: str | None) -> None:
        self.__airline_class = value

    @property
    def arrival_airport(self) -> str | None:
        """
        | Arrival airport/city code This field is used by the following payment products: 840

        Type: str
        """
        return self.__arrival_airport

    @arrival_airport.setter
    def arrival_airport(self, value: str | None) -> None:
        self.__arrival_airport = value

    @property
    def arrival_time(self) -> str | None:
        """
        | The arrival time in the local time zone Format: HH:MM This field is used by the following payment products: 840

        Type: str
        """
        return self.__arrival_time

    @arrival_time.setter
    def arrival_time(self, value: str | None) -> None:
        self.__arrival_time = value

    @property
    def carrier_code(self) -> str | None:
        """
        | IATA carrier code This field is used by the following payment products: cards, 840

        Type: str
        """
        return self.__carrier_code

    @carrier_code.setter
    def carrier_code(self, value: str | None) -> None:
        self.__carrier_code = value

    @property
    def conjunction_ticket(self) -> str | None:
        """
        | Identifying number of a ticket issued to a passenger in conjunction with this ticket and that constitutes a single contract of carriage This field is used by the following payment products: 840

        Type: str
        """
        return self.__conjunction_ticket

    @conjunction_ticket.setter
    def conjunction_ticket(self, value: str | None) -> None:
        self.__conjunction_ticket = value

    @property
    def coupon_number(self) -> str | None:
        """
        | The coupon number associated with this leg of the trip. A ticket can contain several legs of travel, and each leg of travel requires a separate coupon This field is used by the following payment products: 840

        Type: str
        """
        return self.__coupon_number

    @coupon_number.setter
    def coupon_number(self, value: str | None) -> None:
        self.__coupon_number = value

    @property
    def date(self) -> str | None:
        """
        | Date of the leg Format: YYYYMMDD This field is used by the following payment products: cards, 840

        Type: str
        """
        return self.__date

    @date.setter
    def date(self, value: str | None) -> None:
        self.__date = value

    @property
    def departure_time(self) -> str | None:
        """
        | The departure time in the local time at the departure airport Format: HH:MM This field is used by the following payment products: 840

        Type: str
        """
        return self.__departure_time

    @departure_time.setter
    def departure_time(self, value: str | None) -> None:
        self.__departure_time = value

    @property
    def endorsement_or_restriction(self) -> str | None:
        """
        | An endorsement can be an agency-added notation or a mandatory government required notation, such as value-added tax. A restriction is a limitation based on the type of fare, such as a ticket with a 3-day minimum stay This field is used by the following payment products: 840

        Type: str
        """
        return self.__endorsement_or_restriction

    @endorsement_or_restriction.setter
    def endorsement_or_restriction(self, value: str | None) -> None:
        self.__endorsement_or_restriction = value

    @property
    def exchange_ticket(self) -> str | None:
        """
        | New ticket number that is issued when a ticket is exchanged This field is used by the following payment products: 840

        Type: str
        """
        return self.__exchange_ticket

    @exchange_ticket.setter
    def exchange_ticket(self, value: str | None) -> None:
        self.__exchange_ticket = value

    @property
    def fare(self) -> str | None:
        """
        | Deprecated: Use legFare instead. Fare of this leg

        Type: str

        Deprecated; Use legFare instead. Fare of this leg
        """
        return self.__fare

    @fare.setter
    def fare(self, value: str | None) -> None:
        self.__fare = value

    @property
    def fare_basis(self) -> str | None:
        """
        | Fare Basis/Ticket Designator This field is used by the following payment products: 840

        Type: str
        """
        return self.__fare_basis

    @fare_basis.setter
    def fare_basis(self, value: str | None) -> None:
        self.__fare_basis = value

    @property
    def fee(self) -> int | None:
        """
        | Fee for this leg of the trip This field is used by the following payment products: 840

        Type: int
        """
        return self.__fee

    @fee.setter
    def fee(self, value: int | None) -> None:
        self.__fee = value

    @property
    def flight_code(self) -> str | None:
        """
        | The flight number of the current leg. This field is used by the following payment products: 840

        Type: str
        """
        return self.__flight_code

    @flight_code.setter
    def flight_code(self, value: str | None) -> None:
        self.__flight_code = value

    @property
    def flight_number(self) -> str | None:
        """
        | The flight number assigned by the airline carrier with no leading spaces Should be a numeric string This field is used by the following payment products: cards, 840

        Type: str
        """
        return self.__flight_number

    @flight_number.setter
    def flight_number(self, value: str | None) -> None:
        self.__flight_number = value

    @property
    def leg_fare(self) -> int | None:
        """
        | Fee for this leg of the trip This field is used by the following payment products: 840

        Type: int
        """
        return self.__leg_fare

    @leg_fare.setter
    def leg_fare(self, value: int | None) -> None:
        self.__leg_fare = value

    @property
    def number(self) -> int | None:
        """
        | Deprecated: This field is not used by any payment product Sequence number of the flight leg

        Type: int

        Deprecated; This field is not used by any payment product Sequence number of the flight leg
        """
        return self.__number

    @number.setter
    def number(self, value: int | None) -> None:
        self.__number = value

    @property
    def origin_airport(self) -> str | None:
        """
        | Origin airport/city code This field is used by the following payment products: cards, 840

        Type: str
        """
        return self.__origin_airport

    @origin_airport.setter
    def origin_airport(self, value: str | None) -> None:
        self.__origin_airport = value

    @property
    def passenger_class(self) -> str | None:
        """
        | PassengerClass if this leg This field is used by the following payment products: 840

        Type: str
        """
        return self.__passenger_class

    @passenger_class.setter
    def passenger_class(self, value: str | None) -> None:
        self.__passenger_class = value

    @property
    def stopover_code(self) -> str | None:
        """
        | Possible values are:
        
        * permitted = Stopover permitted
        * non-permitted = Stopover not permitted This field is used by the following payment products: cards, 840

        Type: str
        """
        return self.__stopover_code

    @stopover_code.setter
    def stopover_code(self, value: str | None) -> None:
        self.__stopover_code = value

    @property
    def taxes(self) -> int | None:
        """
        | Taxes for this leg of the trip This field is used by the following payment products: 840

        Type: int
        """
        return self.__taxes

    @taxes.setter
    def taxes(self, value: int | None) -> None:
        self.__taxes = value

    def to_dictionary(self) -> dict:
        dictionary = super().to_dictionary()
        if self.airline_class is not None:
            dictionary['airlineClass'] = self.airline_class
        if self.arrival_airport is not None:
            dictionary['arrivalAirport'] = self.arrival_airport
        if self.arrival_time is not None:
            dictionary['arrivalTime'] = self.arrival_time
        if self.carrier_code is not None:
            dictionary['carrierCode'] = self.carrier_code
        if self.conjunction_ticket is not None:
            dictionary['conjunctionTicket'] = self.conjunction_ticket
        if self.coupon_number is not None:
            dictionary['couponNumber'] = self.coupon_number
        if self.date is not None:
            dictionary['date'] = self.date
        if self.departure_time is not None:
            dictionary['departureTime'] = self.departure_time
        if self.endorsement_or_restriction is not None:
            dictionary['endorsementOrRestriction'] = self.endorsement_or_restriction
        if self.exchange_ticket is not None:
            dictionary['exchangeTicket'] = self.exchange_ticket
        if self.fare is not None:
            dictionary['fare'] = self.fare
        if self.fare_basis is not None:
            dictionary['fareBasis'] = self.fare_basis
        if self.fee is not None:
            dictionary['fee'] = self.fee
        if self.flight_code is not None:
            dictionary['flightCode'] = self.flight_code
        if self.flight_number is not None:
            dictionary['flightNumber'] = self.flight_number
        if self.leg_fare is not None:
            dictionary['legFare'] = self.leg_fare
        if self.number is not None:
            dictionary['number'] = self.number
        if self.origin_airport is not None:
            dictionary['originAirport'] = self.origin_airport
        if self.passenger_class is not None:
            dictionary['passengerClass'] = self.passenger_class
        if self.stopover_code is not None:
            dictionary['stopoverCode'] = self.stopover_code
        if self.taxes is not None:
            dictionary['taxes'] = self.taxes
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AirlineFlightLeg':
        super().from_dictionary(dictionary)
        if 'airlineClass' in dictionary:
            self.airline_class = dictionary['airlineClass']
        if 'arrivalAirport' in dictionary:
            self.arrival_airport = dictionary['arrivalAirport']
        if 'arrivalTime' in dictionary:
            self.arrival_time = dictionary['arrivalTime']
        if 'carrierCode' in dictionary:
            self.carrier_code = dictionary['carrierCode']
        if 'conjunctionTicket' in dictionary:
            self.conjunction_ticket = dictionary['conjunctionTicket']
        if 'couponNumber' in dictionary:
            self.coupon_number = dictionary['couponNumber']
        if 'date' in dictionary:
            self.date = dictionary['date']
        if 'departureTime' in dictionary:
            self.departure_time = dictionary['departureTime']
        if 'endorsementOrRestriction' in dictionary:
            self.endorsement_or_restriction = dictionary['endorsementOrRestriction']
        if 'exchangeTicket' in dictionary:
            self.exchange_ticket = dictionary['exchangeTicket']
        if 'fare' in dictionary:
            self.fare = dictionary['fare']
        if 'fareBasis' in dictionary:
            self.fare_basis = dictionary['fareBasis']
        if 'fee' in dictionary:
            self.fee = dictionary['fee']
        if 'flightCode' in dictionary:
            self.flight_code = dictionary['flightCode']
        if 'flightNumber' in dictionary:
            self.flight_number = dictionary['flightNumber']
        if 'legFare' in dictionary:
            self.leg_fare = dictionary['legFare']
        if 'number' in dictionary:
            self.number = dictionary['number']
        if 'originAirport' in dictionary:
            self.origin_airport = dictionary['originAirport']
        if 'passengerClass' in dictionary:
            self.passenger_class = dictionary['passengerClass']
        if 'stopoverCode' in dictionary:
            self.stopover_code = dictionary['stopoverCode']
        if 'taxes' in dictionary:
            self.taxes = dictionary['taxes']
        return self

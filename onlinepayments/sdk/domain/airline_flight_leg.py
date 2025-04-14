# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .data_object import DataObject


class AirlineFlightLeg(DataObject):

    __airline_class: Optional[str] = None
    __arrival_airport: Optional[str] = None
    __arrival_time: Optional[str] = None
    __carrier_code: Optional[str] = None
    __conjunction_ticket: Optional[str] = None
    __coupon_number: Optional[str] = None
    __date: Optional[str] = None
    __departure_time: Optional[str] = None
    __endorsement_or_restriction: Optional[str] = None
    __exchange_ticket: Optional[str] = None
    __fare: Optional[str] = None
    __fare_basis: Optional[str] = None
    __fee: Optional[int] = None
    __flight_number: Optional[str] = None
    __leg_fare: Optional[int] = None
    __number: Optional[int] = None
    __origin_airport: Optional[str] = None
    __passenger_class: Optional[str] = None
    __stopover_code: Optional[str] = None
    __taxes: Optional[int] = None

    @property
    def airline_class(self) -> Optional[str]:
        """
        | Reservation Booking Designator This field is used by the following payment products: cards

        Type: str
        """
        return self.__airline_class

    @airline_class.setter
    def airline_class(self, value: Optional[str]) -> None:
        self.__airline_class = value

    @property
    def arrival_airport(self) -> Optional[str]:
        """
        | Arrival airport/city code This field is used by the following payment products: 840

        Type: str
        """
        return self.__arrival_airport

    @arrival_airport.setter
    def arrival_airport(self, value: Optional[str]) -> None:
        self.__arrival_airport = value

    @property
    def arrival_time(self) -> Optional[str]:
        """
        | The arrival time in the local time zone Format: HH:MM This field is used by the following payment products: 840

        Type: str
        """
        return self.__arrival_time

    @arrival_time.setter
    def arrival_time(self, value: Optional[str]) -> None:
        self.__arrival_time = value

    @property
    def carrier_code(self) -> Optional[str]:
        """
        | IATA carrier code This field is used by the following payment products: cards, 840

        Type: str
        """
        return self.__carrier_code

    @carrier_code.setter
    def carrier_code(self, value: Optional[str]) -> None:
        self.__carrier_code = value

    @property
    def conjunction_ticket(self) -> Optional[str]:
        """
        | Identifying number of a ticket issued to a passenger in conjunction with this ticket and that constitutes a single contract of carriage This field is used by the following payment products: 840

        Type: str
        """
        return self.__conjunction_ticket

    @conjunction_ticket.setter
    def conjunction_ticket(self, value: Optional[str]) -> None:
        self.__conjunction_ticket = value

    @property
    def coupon_number(self) -> Optional[str]:
        """
        | The coupon number associated with this leg of the trip. A ticket can contain several legs of travel, and each leg of travel requires a separate coupon This field is used by the following payment products: 840

        Type: str
        """
        return self.__coupon_number

    @coupon_number.setter
    def coupon_number(self, value: Optional[str]) -> None:
        self.__coupon_number = value

    @property
    def date(self) -> Optional[str]:
        """
        | Date of the leg Format: YYYYMMDD This field is used by the following payment products: cards, 840

        Type: str
        """
        return self.__date

    @date.setter
    def date(self, value: Optional[str]) -> None:
        self.__date = value

    @property
    def departure_time(self) -> Optional[str]:
        """
        | The departure time in the local time at the departure airport Format: HH:MM This field is used by the following payment products: 840

        Type: str
        """
        return self.__departure_time

    @departure_time.setter
    def departure_time(self, value: Optional[str]) -> None:
        self.__departure_time = value

    @property
    def endorsement_or_restriction(self) -> Optional[str]:
        """
        | An endorsement can be an agency-added notation or a mandatory government required notation, such as value-added tax. A restriction is a limitation based on the type of fare, such as a ticket with a 3-day minimum stay This field is used by the following payment products: 840

        Type: str
        """
        return self.__endorsement_or_restriction

    @endorsement_or_restriction.setter
    def endorsement_or_restriction(self, value: Optional[str]) -> None:
        self.__endorsement_or_restriction = value

    @property
    def exchange_ticket(self) -> Optional[str]:
        """
        | New ticket number that is issued when a ticket is exchanged This field is used by the following payment products: 840

        Type: str
        """
        return self.__exchange_ticket

    @exchange_ticket.setter
    def exchange_ticket(self, value: Optional[str]) -> None:
        self.__exchange_ticket = value

    @property
    def fare(self) -> Optional[str]:
        """
        | Deprecated: Use legFare instead. Fare of this leg

        Type: str

        Deprecated; Use legFare instead. Fare of this leg
        """
        return self.__fare

    @fare.setter
    def fare(self, value: Optional[str]) -> None:
        self.__fare = value

    @property
    def fare_basis(self) -> Optional[str]:
        """
        | Fare Basis/Ticket Designator This field is used by the following payment products: 840

        Type: str
        """
        return self.__fare_basis

    @fare_basis.setter
    def fare_basis(self, value: Optional[str]) -> None:
        self.__fare_basis = value

    @property
    def fee(self) -> Optional[int]:
        """
        | Fee for this leg of the trip This field is used by the following payment products: 840

        Type: int
        """
        return self.__fee

    @fee.setter
    def fee(self, value: Optional[int]) -> None:
        self.__fee = value

    @property
    def flight_number(self) -> Optional[str]:
        """
        | The flight number assigned by the airline carrier with no leading spaces Should be a numeric string This field is used by the following payment products: cards, 840

        Type: str
        """
        return self.__flight_number

    @flight_number.setter
    def flight_number(self, value: Optional[str]) -> None:
        self.__flight_number = value

    @property
    def leg_fare(self) -> Optional[int]:
        """
        | Fee for this leg of the trip This field is used by the following payment products: 840

        Type: int
        """
        return self.__leg_fare

    @leg_fare.setter
    def leg_fare(self, value: Optional[int]) -> None:
        self.__leg_fare = value

    @property
    def number(self) -> Optional[int]:
        """
        | Deprecated: This field is not used by any payment product Sequence number of the flight leg

        Type: int

        Deprecated; This field is not used by any payment product Sequence number of the flight leg
        """
        return self.__number

    @number.setter
    def number(self, value: Optional[int]) -> None:
        self.__number = value

    @property
    def origin_airport(self) -> Optional[str]:
        """
        | Origin airport/city code This field is used by the following payment products: cards, 840

        Type: str
        """
        return self.__origin_airport

    @origin_airport.setter
    def origin_airport(self, value: Optional[str]) -> None:
        self.__origin_airport = value

    @property
    def passenger_class(self) -> Optional[str]:
        """
        | PassengerClass if this leg This field is used by the following payment products: 840

        Type: str
        """
        return self.__passenger_class

    @passenger_class.setter
    def passenger_class(self, value: Optional[str]) -> None:
        self.__passenger_class = value

    @property
    def stopover_code(self) -> Optional[str]:
        """
        | Possible values are:
        
        * permitted = Stopover permitted
        * non-permitted = Stopover not permitted This field is used by the following payment products: cards, 840

        Type: str
        """
        return self.__stopover_code

    @stopover_code.setter
    def stopover_code(self, value: Optional[str]) -> None:
        self.__stopover_code = value

    @property
    def taxes(self) -> Optional[int]:
        """
        | Taxes for this leg of the trip This field is used by the following payment products: 840

        Type: int
        """
        return self.__taxes

    @taxes.setter
    def taxes(self, value: Optional[int]) -> None:
        self.__taxes = value

    def to_dictionary(self) -> dict:
        dictionary = super(AirlineFlightLeg, self).to_dictionary()
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
        super(AirlineFlightLeg, self).from_dictionary(dictionary)
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

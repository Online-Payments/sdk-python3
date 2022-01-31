# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from typing import List

from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.airline_flight_leg import AirlineFlightLeg
from onlinepayments.sdk.domain.airline_passenger import AirlinePassenger


class AirlineData(DataObject):
    """
    | Object that holds airline specific data
    """

    __agent_numeric_code = None
    __code = None
    __flight_date = None
    __flight_legs = None
    __invoice_number = None
    __is_e_ticket = None
    __is_restricted_ticket = None
    __is_third_party = None
    __issue_date = None
    __merchant_customer_id = None
    __name = None
    __passenger_name = None
    __passengers = None
    __place_of_issue = None
    __pnr = None
    __point_of_sale = None
    __pos_city_code = None
    __ticket_delivery_method = None
    __ticket_number = None
    __total_fare = None
    __total_fee = None
    __total_taxes = None
    __travel_agency_name = None

    @property
    def agent_numeric_code(self) -> str:
        """
        | Numeric code identifying the agent
        | This field is used by the following payment products: 840

        Type: str
        """
        return self.__agent_numeric_code

    @agent_numeric_code.setter
    def agent_numeric_code(self, value: str):
        self.__agent_numeric_code = value

    @property
    def code(self) -> str:
        """
        | Airline numeric code
        | This field is used by the following payment products: 840

        Type: str
        """
        return self.__code

    @code.setter
    def code(self, value: str):
        self.__code = value

    @property
    def flight_date(self) -> str:
        """
        | Deprecated: This field is not used by any payment product
        | Date of the Flight
        | Format: YYYYMMDD

        Type: str
        """
        return self.__flight_date

    @flight_date.setter
    def flight_date(self, value: str):
        self.__flight_date = value

    @property
    def flight_legs(self) -> List[AirlineFlightLeg]:
        """
        | Object that holds the data on the individual legs of the flight ticket

        Type: list[:class:`onlinepayments.sdk.domain.airline_flight_leg.AirlineFlightLeg`]
        """
        return self.__flight_legs

    @flight_legs.setter
    def flight_legs(self, value: List[AirlineFlightLeg]):
        self.__flight_legs = value

    @property
    def invoice_number(self) -> str:
        """
        | Airline tracing number
        | This field is used by the following payment products: cards

        Type: str
        """
        return self.__invoice_number

    @invoice_number.setter
    def invoice_number(self, value: str):
        self.__invoice_number = value

    @property
    def is_e_ticket(self) -> bool:
        """
        | Deprecated: This field is not used by any payment product
        |  * true = The ticket is an E-Ticket
        |  * false = the ticket is not an E-Ticket'

        Type: bool
        """
        return self.__is_e_ticket

    @is_e_ticket.setter
    def is_e_ticket(self, value: bool):
        self.__is_e_ticket = value

    @property
    def is_restricted_ticket(self) -> bool:
        """
        | Indicates if the ticket is refundable or not.
        |  * true - Restricted, the ticket is non-refundable
        |  * false - No restrictions, the ticket is (partially) refundable
        | This field is used by the following payment products: 840

        Type: bool
        """
        return self.__is_restricted_ticket

    @is_restricted_ticket.setter
    def is_restricted_ticket(self, value: bool):
        self.__is_restricted_ticket = value

    @property
    def is_third_party(self) -> bool:
        """
        | Deprecated: This field is not used by any payment product
        |  * true - The payer is the ticket holder
        |  * false - The payer is not the ticket holder

        Type: bool
        """
        return self.__is_third_party

    @is_third_party.setter
    def is_third_party(self, value: bool):
        self.__is_third_party = value

    @property
    def issue_date(self) -> str:
        """
        | This is the date of issue recorded in the airline system In a case of multiple issuances of the same ticket to a cardholder, you should use the last ticket date.
        | Format: YYYYMMDD
        | This field is used by the following payment products: cards, 840

        Type: str
        """
        return self.__issue_date

    @issue_date.setter
    def issue_date(self, value: str):
        self.__issue_date = value

    @property
    def merchant_customer_id(self) -> str:
        """
        | Your ID of the customer in the context of the airline data
        | This field is used by the following payment products: 840

        Type: str
        """
        return self.__merchant_customer_id

    @merchant_customer_id.setter
    def merchant_customer_id(self, value: str):
        self.__merchant_customer_id = value

    @property
    def name(self) -> str:
        """
        | Deprecated: This field is not used by any payment product
        | Name of the airline

        Type: str
        """
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def passenger_name(self) -> str:
        """
        | Deprecated: Use passengers instead
        | Name of passenger

        Type: str
        """
        return self.__passenger_name

    @passenger_name.setter
    def passenger_name(self, value: str):
        self.__passenger_name = value

    @property
    def passengers(self) -> List[AirlinePassenger]:
        """
        | Object that holds the data on the individual passengers
        | This field is used by the following payment products: cards, 840

        Type: list[:class:`onlinepayments.sdk.domain.airline_passenger.AirlinePassenger`]
        """
        return self.__passengers

    @passengers.setter
    def passengers(self, value: List[AirlinePassenger]):
        self.__passengers = value

    @property
    def place_of_issue(self) -> str:
        """
        | Deprecated: This field is not used by any payment product
        | Place of issue
        | For sales in the US the last two characters (pos 14-15) must be the US state code.

        Type: str
        """
        return self.__place_of_issue

    @place_of_issue.setter
    def place_of_issue(self, value: str):
        self.__place_of_issue = value

    @property
    def pnr(self) -> str:
        """
        | Deprecated: This field is not used by any payment product
        | Passenger name record

        Type: str
        """
        return self.__pnr

    @pnr.setter
    def pnr(self, value: str):
        self.__pnr = value

    @property
    def point_of_sale(self) -> str:
        """
        | IATA point of sale name
        | This field is used by the following payment products: 840

        Type: str
        """
        return self.__point_of_sale

    @point_of_sale.setter
    def point_of_sale(self, value: str):
        self.__point_of_sale = value

    @property
    def pos_city_code(self) -> str:
        """
        | Deprecated: This field is not used by any payment product
        | City code of the point of sale

        Type: str
        """
        return self.__pos_city_code

    @pos_city_code.setter
    def pos_city_code(self, value: str):
        self.__pos_city_code = value

    @property
    def ticket_delivery_method(self) -> str:
        """
        | Deprecated: This field is not used by any payment product
        | Delivery method of the ticket

        Type: str
        """
        return self.__ticket_delivery_method

    @ticket_delivery_method.setter
    def ticket_delivery_method(self, value: str):
        self.__ticket_delivery_method = value

    @property
    def ticket_number(self) -> str:
        """
        | The ticket or document number contains:
        |  * Airline code: 3-digit airline code number
        |  * Form code: A maximum of 3 digits indicating the type of document, the source of issue and the number of coupons it contains
        |  * Serial number: A maximum of 8 digits allocated on a sequential basis, provided that the total number of digits allocated to the form code and serial number shall not exceed ten
        |  * TICKETNUMBER can be replaced with PNR if the ticket number is unavailable
        | This field is used by the following payment products: cards, 840

        Type: str
        """
        return self.__ticket_number

    @ticket_number.setter
    def ticket_number(self, value: str):
        self.__ticket_number = value

    @property
    def total_fare(self) -> int:
        """
        | Total fare for all legs on the ticket, excluding taxes and fees. If multiple tickets are purchased, this is the total fare for all tickets
        | This field is used by the following payment products: 840

        Type: int
        """
        return self.__total_fare

    @total_fare.setter
    def total_fare(self, value: int):
        self.__total_fare = value

    @property
    def total_fee(self) -> int:
        """
        | Total fee for all legs on the ticket. If multiple tickets are purchased, this is the total fee for all tickets
        | This field is used by the following payment products: 840

        Type: int
        """
        return self.__total_fee

    @total_fee.setter
    def total_fee(self, value: int):
        self.__total_fee = value

    @property
    def total_taxes(self) -> int:
        """
        | Total taxes for all legs on the ticket. If multiple tickets are purchased, this is the total taxes for all tickets
        | This field is used by the following payment products: 840

        Type: int
        """
        return self.__total_taxes

    @total_taxes.setter
    def total_taxes(self, value: int):
        self.__total_taxes = value

    @property
    def travel_agency_name(self) -> str:
        """
        | Name of the travel agency issuing the ticket. For direct airline integration, leave this property blank
        | This field is used by the following payment products: 840

        Type: str
        """
        return self.__travel_agency_name

    @travel_agency_name.setter
    def travel_agency_name(self, value: str):
        self.__travel_agency_name = value

    def to_dictionary(self):
        dictionary = super(AirlineData, self).to_dictionary()
        if self.agent_numeric_code is not None:
            dictionary['agentNumericCode'] = self.agent_numeric_code
        if self.code is not None:
            dictionary['code'] = self.code
        if self.flight_date is not None:
            dictionary['flightDate'] = self.flight_date
        if self.flight_legs is not None:
            dictionary['flightLegs'] = []
            for element in self.flight_legs:
                if element is not None:
                    dictionary['flightLegs'].append(element.to_dictionary())
        if self.invoice_number is not None:
            dictionary['invoiceNumber'] = self.invoice_number
        if self.is_e_ticket is not None:
            dictionary['isETicket'] = self.is_e_ticket
        if self.is_restricted_ticket is not None:
            dictionary['isRestrictedTicket'] = self.is_restricted_ticket
        if self.is_third_party is not None:
            dictionary['isThirdParty'] = self.is_third_party
        if self.issue_date is not None:
            dictionary['issueDate'] = self.issue_date
        if self.merchant_customer_id is not None:
            dictionary['merchantCustomerId'] = self.merchant_customer_id
        if self.name is not None:
            dictionary['name'] = self.name
        if self.passenger_name is not None:
            dictionary['passengerName'] = self.passenger_name
        if self.passengers is not None:
            dictionary['passengers'] = []
            for element in self.passengers:
                if element is not None:
                    dictionary['passengers'].append(element.to_dictionary())
        if self.place_of_issue is not None:
            dictionary['placeOfIssue'] = self.place_of_issue
        if self.pnr is not None:
            dictionary['pnr'] = self.pnr
        if self.point_of_sale is not None:
            dictionary['pointOfSale'] = self.point_of_sale
        if self.pos_city_code is not None:
            dictionary['posCityCode'] = self.pos_city_code
        if self.ticket_delivery_method is not None:
            dictionary['ticketDeliveryMethod'] = self.ticket_delivery_method
        if self.ticket_number is not None:
            dictionary['ticketNumber'] = self.ticket_number
        if self.total_fare is not None:
            dictionary['totalFare'] = self.total_fare
        if self.total_fee is not None:
            dictionary['totalFee'] = self.total_fee
        if self.total_taxes is not None:
            dictionary['totalTaxes'] = self.total_taxes
        if self.travel_agency_name is not None:
            dictionary['travelAgencyName'] = self.travel_agency_name
        return dictionary

    def from_dictionary(self, dictionary):
        super(AirlineData, self).from_dictionary(dictionary)
        if 'agentNumericCode' in dictionary:
            self.agent_numeric_code = dictionary['agentNumericCode']
        if 'code' in dictionary:
            self.code = dictionary['code']
        if 'flightDate' in dictionary:
            self.flight_date = dictionary['flightDate']
        if 'flightLegs' in dictionary:
            if not isinstance(dictionary['flightLegs'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['flightLegs']))
            self.flight_legs = []
            for element in dictionary['flightLegs']:
                value = AirlineFlightLeg()
                self.flight_legs.append(value.from_dictionary(element))
        if 'invoiceNumber' in dictionary:
            self.invoice_number = dictionary['invoiceNumber']
        if 'isETicket' in dictionary:
            self.is_e_ticket = dictionary['isETicket']
        if 'isRestrictedTicket' in dictionary:
            self.is_restricted_ticket = dictionary['isRestrictedTicket']
        if 'isThirdParty' in dictionary:
            self.is_third_party = dictionary['isThirdParty']
        if 'issueDate' in dictionary:
            self.issue_date = dictionary['issueDate']
        if 'merchantCustomerId' in dictionary:
            self.merchant_customer_id = dictionary['merchantCustomerId']
        if 'name' in dictionary:
            self.name = dictionary['name']
        if 'passengerName' in dictionary:
            self.passenger_name = dictionary['passengerName']
        if 'passengers' in dictionary:
            if not isinstance(dictionary['passengers'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['passengers']))
            self.passengers = []
            for element in dictionary['passengers']:
                value = AirlinePassenger()
                self.passengers.append(value.from_dictionary(element))
        if 'placeOfIssue' in dictionary:
            self.place_of_issue = dictionary['placeOfIssue']
        if 'pnr' in dictionary:
            self.pnr = dictionary['pnr']
        if 'pointOfSale' in dictionary:
            self.point_of_sale = dictionary['pointOfSale']
        if 'posCityCode' in dictionary:
            self.pos_city_code = dictionary['posCityCode']
        if 'ticketDeliveryMethod' in dictionary:
            self.ticket_delivery_method = dictionary['ticketDeliveryMethod']
        if 'ticketNumber' in dictionary:
            self.ticket_number = dictionary['ticketNumber']
        if 'totalFare' in dictionary:
            self.total_fare = dictionary['totalFare']
        if 'totalFee' in dictionary:
            self.total_fee = dictionary['totalFee']
        if 'totalTaxes' in dictionary:
            self.total_taxes = dictionary['totalTaxes']
        if 'travelAgencyName' in dictionary:
            self.travel_agency_name = dictionary['travelAgencyName']
        return self

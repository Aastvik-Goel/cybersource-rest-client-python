# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class Riskv1decisionsTravelInformation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'actual_final_destination': 'str',
        'complete_route': 'str',
        'departure_time': 'str',
        'journey_type': 'str',
        'legs': 'list[Riskv1decisionsTravelInformationLegs]',
        'number_of_passengers': 'int',
        'passengers': 'list[Riskv1decisionsTravelInformationPassengers]'
    }

    attribute_map = {
        'actual_final_destination': 'actualFinalDestination',
        'complete_route': 'completeRoute',
        'departure_time': 'departureTime',
        'journey_type': 'journeyType',
        'legs': 'legs',
        'number_of_passengers': 'numberOfPassengers',
        'passengers': 'passengers'
    }

    def __init__(self, actual_final_destination=None, complete_route=None, departure_time=None, journey_type=None, legs=None, number_of_passengers=None, passengers=None):
        """
        Riskv1decisionsTravelInformation - a model defined in Swagger
        """

        self._actual_final_destination = None
        self._complete_route = None
        self._departure_time = None
        self._journey_type = None
        self._legs = None
        self._number_of_passengers = None
        self._passengers = None

        if actual_final_destination is not None:
          self.actual_final_destination = actual_final_destination
        if complete_route is not None:
          self.complete_route = complete_route
        if departure_time is not None:
          self.departure_time = departure_time
        if journey_type is not None:
          self.journey_type = journey_type
        if legs is not None:
          self.legs = legs
        if number_of_passengers is not None:
          self.number_of_passengers = number_of_passengers
        if passengers is not None:
          self.passengers = passengers

    @property
    def actual_final_destination(self):
        """
        Gets the actual_final_destination of this Riskv1decisionsTravelInformation.
        IATA Code for the actual final destination that the customer intends to travel to. It should be a destination on the completeRoute. 

        :return: The actual_final_destination of this Riskv1decisionsTravelInformation.
        :rtype: str
        """
        return self._actual_final_destination

    @actual_final_destination.setter
    def actual_final_destination(self, actual_final_destination):
        """
        Sets the actual_final_destination of this Riskv1decisionsTravelInformation.
        IATA Code for the actual final destination that the customer intends to travel to. It should be a destination on the completeRoute. 

        :param actual_final_destination: The actual_final_destination of this Riskv1decisionsTravelInformation.
        :type: str
        """

        self._actual_final_destination = actual_final_destination

    @property
    def complete_route(self):
        """
        Gets the complete_route of this Riskv1decisionsTravelInformation.
        Concatenation of individual travel legs in the format ORIG1-DEST1[:ORIG2-DEST2...:ORIGn-DESTn], for example, SFO-JFK:JFK-LHR:LHR-CDG. For airport codes, see the IATA Airline and Airport Code Search. Note In your request, send either the complete route or the individual legs (_leg#_orig and _leg#_dest). If you send all the fields, the value of _complete_route takes precedence over that of the _leg# fields. 

        :return: The complete_route of this Riskv1decisionsTravelInformation.
        :rtype: str
        """
        return self._complete_route

    @complete_route.setter
    def complete_route(self, complete_route):
        """
        Sets the complete_route of this Riskv1decisionsTravelInformation.
        Concatenation of individual travel legs in the format ORIG1-DEST1[:ORIG2-DEST2...:ORIGn-DESTn], for example, SFO-JFK:JFK-LHR:LHR-CDG. For airport codes, see the IATA Airline and Airport Code Search. Note In your request, send either the complete route or the individual legs (_leg#_orig and _leg#_dest). If you send all the fields, the value of _complete_route takes precedence over that of the _leg# fields. 

        :param complete_route: The complete_route of this Riskv1decisionsTravelInformation.
        :type: str
        """

        self._complete_route = complete_route

    @property
    def departure_time(self):
        """
        Gets the departure_time of this Riskv1decisionsTravelInformation.
        Departure date and time of the first leg of the trip. Use one of the following formats:   - yyyy-MM-dd HH:mm z   - yyyy-MM-dd hh:mm a z   - yyyy-MM-dd hh:mma z   HH = hour in 24-hour format   hh = hour in 12-hour format   a = am or pm (case insensitive)   z = time zone of the departing flight, for example: If the   airline is based in city A, but the flight departs from city   B, z is the time zone of city B at the time of departure. Important For travel information, use GMT instead of UTC, or use the local time zone. Examples 2011-03-20 11:30 PM PDT 2011-03-20 11:30pm GMT 2011-03-20 11:30pm GMT-05:00 Eastern Standard Time: GMT-05:00 or EST Note When specifying an offset from GMT, the format must be exactly as specified in the example. Insert no spaces between the time zone and the offset. 

        :return: The departure_time of this Riskv1decisionsTravelInformation.
        :rtype: str
        """
        return self._departure_time

    @departure_time.setter
    def departure_time(self, departure_time):
        """
        Sets the departure_time of this Riskv1decisionsTravelInformation.
        Departure date and time of the first leg of the trip. Use one of the following formats:   - yyyy-MM-dd HH:mm z   - yyyy-MM-dd hh:mm a z   - yyyy-MM-dd hh:mma z   HH = hour in 24-hour format   hh = hour in 12-hour format   a = am or pm (case insensitive)   z = time zone of the departing flight, for example: If the   airline is based in city A, but the flight departs from city   B, z is the time zone of city B at the time of departure. Important For travel information, use GMT instead of UTC, or use the local time zone. Examples 2011-03-20 11:30 PM PDT 2011-03-20 11:30pm GMT 2011-03-20 11:30pm GMT-05:00 Eastern Standard Time: GMT-05:00 or EST Note When specifying an offset from GMT, the format must be exactly as specified in the example. Insert no spaces between the time zone and the offset. 

        :param departure_time: The departure_time of this Riskv1decisionsTravelInformation.
        :type: str
        """

        self._departure_time = departure_time

    @property
    def journey_type(self):
        """
        Gets the journey_type of this Riskv1decisionsTravelInformation.
        Type of travel, for example one way or round trip.

        :return: The journey_type of this Riskv1decisionsTravelInformation.
        :rtype: str
        """
        return self._journey_type

    @journey_type.setter
    def journey_type(self, journey_type):
        """
        Sets the journey_type of this Riskv1decisionsTravelInformation.
        Type of travel, for example one way or round trip.

        :param journey_type: The journey_type of this Riskv1decisionsTravelInformation.
        :type: str
        """

        self._journey_type = journey_type

    @property
    def legs(self):
        """
        Gets the legs of this Riskv1decisionsTravelInformation.

        :return: The legs of this Riskv1decisionsTravelInformation.
        :rtype: list[Riskv1decisionsTravelInformationLegs]
        """
        return self._legs

    @legs.setter
    def legs(self, legs):
        """
        Sets the legs of this Riskv1decisionsTravelInformation.

        :param legs: The legs of this Riskv1decisionsTravelInformation.
        :type: list[Riskv1decisionsTravelInformationLegs]
        """

        self._legs = legs

    @property
    def number_of_passengers(self):
        """
        Gets the number_of_passengers of this Riskv1decisionsTravelInformation.
        Number of passengers for whom the ticket was issued. If you do not include this field in your request, CyberSource uses a default value of 1. Required for American Express SafeKey (U.S.) for travel-related requests. 

        :return: The number_of_passengers of this Riskv1decisionsTravelInformation.
        :rtype: int
        """
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        """
        Sets the number_of_passengers of this Riskv1decisionsTravelInformation.
        Number of passengers for whom the ticket was issued. If you do not include this field in your request, CyberSource uses a default value of 1. Required for American Express SafeKey (U.S.) for travel-related requests. 

        :param number_of_passengers: The number_of_passengers of this Riskv1decisionsTravelInformation.
        :type: int
        """

        self._number_of_passengers = number_of_passengers

    @property
    def passengers(self):
        """
        Gets the passengers of this Riskv1decisionsTravelInformation.

        :return: The passengers of this Riskv1decisionsTravelInformation.
        :rtype: list[Riskv1decisionsTravelInformationPassengers]
        """
        return self._passengers

    @passengers.setter
    def passengers(self, passengers):
        """
        Sets the passengers of this Riskv1decisionsTravelInformation.

        :param passengers: The passengers of this Riskv1decisionsTravelInformation.
        :type: list[Riskv1decisionsTravelInformationPassengers]
        """

        self._passengers = passengers

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Riskv1decisionsTravelInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

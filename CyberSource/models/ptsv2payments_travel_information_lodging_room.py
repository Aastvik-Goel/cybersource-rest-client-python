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


class Ptsv2paymentsTravelInformationLodgingRoom(object):
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
        'daily_rate': 'str',
        'number_of_nights': 'int'
    }

    attribute_map = {
        'daily_rate': 'dailyRate',
        'number_of_nights': 'numberOfNights'
    }

    def __init__(self, daily_rate=None, number_of_nights=None):
        """
        Ptsv2paymentsTravelInformationLodgingRoom - a model defined in Swagger
        """

        self._daily_rate = None
        self._number_of_nights = None

        if daily_rate is not None:
          self.daily_rate = daily_rate
        if number_of_nights is not None:
          self.number_of_nights = number_of_nights

    @property
    def daily_rate(self):
        """
        Gets the daily_rate of this Ptsv2paymentsTravelInformationLodgingRoom.
        Daily cost of the room. 

        :return: The daily_rate of this Ptsv2paymentsTravelInformationLodgingRoom.
        :rtype: str
        """
        return self._daily_rate

    @daily_rate.setter
    def daily_rate(self, daily_rate):
        """
        Sets the daily_rate of this Ptsv2paymentsTravelInformationLodgingRoom.
        Daily cost of the room. 

        :param daily_rate: The daily_rate of this Ptsv2paymentsTravelInformationLodgingRoom.
        :type: str
        """



        self._daily_rate = daily_rate

    @property
    def number_of_nights(self):
        """
        Gets the number_of_nights of this Ptsv2paymentsTravelInformationLodgingRoom.
        Number of nights billed at the rate specified by `travelInformation.lodging.room[].dailyRate`. 

        :return: The number_of_nights of this Ptsv2paymentsTravelInformationLodgingRoom.
        :rtype: int
        """
        return self._number_of_nights

    @number_of_nights.setter
    def number_of_nights(self, number_of_nights):
        """
        Sets the number_of_nights of this Ptsv2paymentsTravelInformationLodgingRoom.
        Number of nights billed at the rate specified by `travelInformation.lodging.room[].dailyRate`. 

        :param number_of_nights: The number_of_nights of this Ptsv2paymentsTravelInformationLodgingRoom.
        :type: int
        """



        self._number_of_nights = number_of_nights

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
        if not isinstance(other, Ptsv2paymentsTravelInformationLodgingRoom):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

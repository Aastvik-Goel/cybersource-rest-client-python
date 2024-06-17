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


class PtsV2PaymentsPost201ResponseRiskInformationTravel(object):
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
        'actual_final_destination': 'PtsV2PaymentsPost201ResponseRiskInformationTravelActualFinalDestination',
        'first_departure': 'PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDeparture',
        'first_destination': 'PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination',
        'last_destination': 'PtsV2PaymentsPost201ResponseRiskInformationTravelLastDestination'
    }

    attribute_map = {
        'actual_final_destination': 'actualFinalDestination',
        'first_departure': 'firstDeparture',
        'first_destination': 'firstDestination',
        'last_destination': 'lastDestination'
    }

    def __init__(self, actual_final_destination=None, first_departure=None, first_destination=None, last_destination=None):
        """
        PtsV2PaymentsPost201ResponseRiskInformationTravel - a model defined in Swagger
        """

        self._actual_final_destination = None
        self._first_departure = None
        self._first_destination = None
        self._last_destination = None

        if actual_final_destination is not None:
          self.actual_final_destination = actual_final_destination
        if first_departure is not None:
          self.first_departure = first_departure
        if first_destination is not None:
          self.first_destination = first_destination
        if last_destination is not None:
          self.last_destination = last_destination

    @property
    def actual_final_destination(self):
        """
        Gets the actual_final_destination of this PtsV2PaymentsPost201ResponseRiskInformationTravel.

        :return: The actual_final_destination of this PtsV2PaymentsPost201ResponseRiskInformationTravel.
        :rtype: PtsV2PaymentsPost201ResponseRiskInformationTravelActualFinalDestination
        """
        return self._actual_final_destination

    @actual_final_destination.setter
    def actual_final_destination(self, actual_final_destination):
        """
        Sets the actual_final_destination of this PtsV2PaymentsPost201ResponseRiskInformationTravel.

        :param actual_final_destination: The actual_final_destination of this PtsV2PaymentsPost201ResponseRiskInformationTravel.
        :type: PtsV2PaymentsPost201ResponseRiskInformationTravelActualFinalDestination
        """



        self._actual_final_destination = actual_final_destination

    @property
    def first_departure(self):
        """
        Gets the first_departure of this PtsV2PaymentsPost201ResponseRiskInformationTravel.

        :return: The first_departure of this PtsV2PaymentsPost201ResponseRiskInformationTravel.
        :rtype: PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDeparture
        """
        return self._first_departure

    @first_departure.setter
    def first_departure(self, first_departure):
        """
        Sets the first_departure of this PtsV2PaymentsPost201ResponseRiskInformationTravel.

        :param first_departure: The first_departure of this PtsV2PaymentsPost201ResponseRiskInformationTravel.
        :type: PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDeparture
        """



        self._first_departure = first_departure

    @property
    def first_destination(self):
        """
        Gets the first_destination of this PtsV2PaymentsPost201ResponseRiskInformationTravel.

        :return: The first_destination of this PtsV2PaymentsPost201ResponseRiskInformationTravel.
        :rtype: PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination
        """
        return self._first_destination

    @first_destination.setter
    def first_destination(self, first_destination):
        """
        Sets the first_destination of this PtsV2PaymentsPost201ResponseRiskInformationTravel.

        :param first_destination: The first_destination of this PtsV2PaymentsPost201ResponseRiskInformationTravel.
        :type: PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination
        """



        self._first_destination = first_destination

    @property
    def last_destination(self):
        """
        Gets the last_destination of this PtsV2PaymentsPost201ResponseRiskInformationTravel.

        :return: The last_destination of this PtsV2PaymentsPost201ResponseRiskInformationTravel.
        :rtype: PtsV2PaymentsPost201ResponseRiskInformationTravelLastDestination
        """
        return self._last_destination

    @last_destination.setter
    def last_destination(self, last_destination):
        """
        Sets the last_destination of this PtsV2PaymentsPost201ResponseRiskInformationTravel.

        :param last_destination: The last_destination of this PtsV2PaymentsPost201ResponseRiskInformationTravel.
        :type: PtsV2PaymentsPost201ResponseRiskInformationTravelLastDestination
        """



        self._last_destination = last_destination

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
        if not isinstance(other, PtsV2PaymentsPost201ResponseRiskInformationTravel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

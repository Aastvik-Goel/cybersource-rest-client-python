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


class Ptsv2paymentsTravelInformationAgency(object):
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
        'code': 'str',
        'name': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name'
    }

    def __init__(self, code=None, name=None):
        """
        Ptsv2paymentsTravelInformationAgency - a model defined in Swagger
        """

        self._code = None
        self._name = None

        if code is not None:
          self.code = code
        if name is not None:
          self.name = name

    @property
    def code(self):
        """
        Gets the code of this Ptsv2paymentsTravelInformationAgency.
        International Air Transport Association (IATA) code of travel agency that made the vehicle rental reservation. 

        :return: The code of this Ptsv2paymentsTravelInformationAgency.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Ptsv2paymentsTravelInformationAgency.
        International Air Transport Association (IATA) code of travel agency that made the vehicle rental reservation. 

        :param code: The code of this Ptsv2paymentsTravelInformationAgency.
        :type: str
        """



        self._code = code

    @property
    def name(self):
        """
        Gets the name of this Ptsv2paymentsTravelInformationAgency.
        Name of travel agency that made the reservation. 

        :return: The name of this Ptsv2paymentsTravelInformationAgency.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Ptsv2paymentsTravelInformationAgency.
        Name of travel agency that made the reservation. 

        :param name: The name of this Ptsv2paymentsTravelInformationAgency.
        :type: str
        """



        self._name = name

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
        if not isinstance(other, Ptsv2paymentsTravelInformationAgency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

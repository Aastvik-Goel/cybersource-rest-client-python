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


class InlineResponse412Errors(object):
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
        'type': 'str',
        'message': 'str'
    }

    attribute_map = {
        'type': 'type',
        'message': 'message'
    }

    def __init__(self, type=None, message=None):
        """
        InlineResponse412Errors - a model defined in Swagger
        """

        self._type = None
        self._message = None

        if type is not None:
          self.type = type
        if message is not None:
          self.message = message

    @property
    def type(self):
        """
        Gets the type of this InlineResponse412Errors.
        The type of error.  Possible Values:   - conflict 

        :return: The type of this InlineResponse412Errors.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this InlineResponse412Errors.
        The type of error.  Possible Values:   - conflict 

        :param type: The type of this InlineResponse412Errors.
        :type: str
        """

        self._type = type

    @property
    def message(self):
        """
        Gets the message of this InlineResponse412Errors.
        The detailed message related to the type.

        :return: The message of this InlineResponse412Errors.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this InlineResponse412Errors.
        The detailed message related to the type.

        :param message: The message of this InlineResponse412Errors.
        :type: str
        """

        self._message = message

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
        if not isinstance(other, InlineResponse412Errors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

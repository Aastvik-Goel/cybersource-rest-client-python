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


class Tmsv2customersEmbeddedDefaultShippingAddressMetadata(object):
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
        'creator': 'str'
    }

    attribute_map = {
        'creator': 'creator'
    }

    def __init__(self, creator=None):
        """
        Tmsv2customersEmbeddedDefaultShippingAddressMetadata - a model defined in Swagger
        """

        self._creator = None

        if creator is not None:
          self.creator = creator

    @property
    def creator(self):
        """
        Gets the creator of this Tmsv2customersEmbeddedDefaultShippingAddressMetadata.
        The creator of the Shipping Address.

        :return: The creator of this Tmsv2customersEmbeddedDefaultShippingAddressMetadata.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """
        Sets the creator of this Tmsv2customersEmbeddedDefaultShippingAddressMetadata.
        The creator of the Shipping Address.

        :param creator: The creator of this Tmsv2customersEmbeddedDefaultShippingAddressMetadata.
        :type: str
        """

        self._creator = creator

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
        if not isinstance(other, Tmsv2customersEmbeddedDefaultShippingAddressMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

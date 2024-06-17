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


class Tmsv2customersEmbeddedDefaultShippingAddressLinks(object):
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
        '_self': 'Tmsv2customersEmbeddedDefaultShippingAddressLinksSelf',
        'customer': 'Tmsv2customersEmbeddedDefaultShippingAddressLinksCustomer'
    }

    attribute_map = {
        '_self': 'self',
        'customer': 'customer'
    }

    def __init__(self, _self=None, customer=None):
        """
        Tmsv2customersEmbeddedDefaultShippingAddressLinks - a model defined in Swagger
        """

        self.__self = None
        self._customer = None

        if _self is not None:
          self._self = _self
        if customer is not None:
          self.customer = customer

    @property
    def _self(self):
        """
        Gets the _self of this Tmsv2customersEmbeddedDefaultShippingAddressLinks.

        :return: The _self of this Tmsv2customersEmbeddedDefaultShippingAddressLinks.
        :rtype: Tmsv2customersEmbeddedDefaultShippingAddressLinksSelf
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this Tmsv2customersEmbeddedDefaultShippingAddressLinks.

        :param _self: The _self of this Tmsv2customersEmbeddedDefaultShippingAddressLinks.
        :type: Tmsv2customersEmbeddedDefaultShippingAddressLinksSelf
        """



        self.__self = _self

    @property
    def customer(self):
        """
        Gets the customer of this Tmsv2customersEmbeddedDefaultShippingAddressLinks.

        :return: The customer of this Tmsv2customersEmbeddedDefaultShippingAddressLinks.
        :rtype: Tmsv2customersEmbeddedDefaultShippingAddressLinksCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Sets the customer of this Tmsv2customersEmbeddedDefaultShippingAddressLinks.

        :param customer: The customer of this Tmsv2customersEmbeddedDefaultShippingAddressLinks.
        :type: Tmsv2customersEmbeddedDefaultShippingAddressLinksCustomer
        """



        self._customer = customer

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
        if not isinstance(other, Tmsv2customersEmbeddedDefaultShippingAddressLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

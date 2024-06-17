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


class ShippingAddressListForCustomerEmbedded(object):
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
        'shipping_addresses': 'list[Tmsv2customersEmbeddedDefaultShippingAddress]'
    }

    attribute_map = {
        'shipping_addresses': 'shippingAddresses'
    }

    def __init__(self, shipping_addresses=None):
        """
        ShippingAddressListForCustomerEmbedded - a model defined in Swagger
        """

        self._shipping_addresses = None

        if shipping_addresses is not None:
          self.shipping_addresses = shipping_addresses

    @property
    def shipping_addresses(self):
        """
        Gets the shipping_addresses of this ShippingAddressListForCustomerEmbedded.

        :return: The shipping_addresses of this ShippingAddressListForCustomerEmbedded.
        :rtype: list[Tmsv2customersEmbeddedDefaultShippingAddress]
        """
        return self._shipping_addresses

    @shipping_addresses.setter
    def shipping_addresses(self, shipping_addresses):
        """
        Sets the shipping_addresses of this ShippingAddressListForCustomerEmbedded.

        :param shipping_addresses: The shipping_addresses of this ShippingAddressListForCustomerEmbedded.
        :type: list[Tmsv2customersEmbeddedDefaultShippingAddress]
        """



        self._shipping_addresses = shipping_addresses

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
        if not isinstance(other, ShippingAddressListForCustomerEmbedded):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

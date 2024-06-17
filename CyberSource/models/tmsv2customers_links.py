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


class Tmsv2customersLinks(object):
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
        '_self': 'Tmsv2customersLinksSelf',
        'payment_instruments': 'Tmsv2customersLinksPaymentInstruments',
        'shipping_address': 'Tmsv2customersLinksShippingAddress'
    }

    attribute_map = {
        '_self': 'self',
        'payment_instruments': 'paymentInstruments',
        'shipping_address': 'shippingAddress'
    }

    def __init__(self, _self=None, payment_instruments=None, shipping_address=None):
        """
        Tmsv2customersLinks - a model defined in Swagger
        """

        self.__self = None
        self._payment_instruments = None
        self._shipping_address = None

        if _self is not None:
          self._self = _self
        if payment_instruments is not None:
          self.payment_instruments = payment_instruments
        if shipping_address is not None:
          self.shipping_address = shipping_address

    @property
    def _self(self):
        """
        Gets the _self of this Tmsv2customersLinks.

        :return: The _self of this Tmsv2customersLinks.
        :rtype: Tmsv2customersLinksSelf
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this Tmsv2customersLinks.

        :param _self: The _self of this Tmsv2customersLinks.
        :type: Tmsv2customersLinksSelf
        """



        self.__self = _self

    @property
    def payment_instruments(self):
        """
        Gets the payment_instruments of this Tmsv2customersLinks.

        :return: The payment_instruments of this Tmsv2customersLinks.
        :rtype: Tmsv2customersLinksPaymentInstruments
        """
        return self._payment_instruments

    @payment_instruments.setter
    def payment_instruments(self, payment_instruments):
        """
        Sets the payment_instruments of this Tmsv2customersLinks.

        :param payment_instruments: The payment_instruments of this Tmsv2customersLinks.
        :type: Tmsv2customersLinksPaymentInstruments
        """



        self._payment_instruments = payment_instruments

    @property
    def shipping_address(self):
        """
        Gets the shipping_address of this Tmsv2customersLinks.

        :return: The shipping_address of this Tmsv2customersLinks.
        :rtype: Tmsv2customersLinksShippingAddress
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """
        Sets the shipping_address of this Tmsv2customersLinks.

        :param shipping_address: The shipping_address of this Tmsv2customersLinks.
        :type: Tmsv2customersLinksShippingAddress
        """



        self._shipping_address = shipping_address

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
        if not isinstance(other, Tmsv2customersLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

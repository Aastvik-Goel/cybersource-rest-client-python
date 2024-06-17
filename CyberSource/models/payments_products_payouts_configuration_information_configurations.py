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


class PaymentsProductsPayoutsConfigurationInformationConfigurations(object):
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
        'pullfunds': 'dict(str, PaymentsProductsPayoutsConfigurationInformationConfigurationsPullfunds)',
        'pushfunds': 'dict(str, PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds)'
    }

    attribute_map = {
        'pullfunds': 'pullfunds',
        'pushfunds': 'pushfunds'
    }

    def __init__(self, pullfunds=None, pushfunds=None):
        """
        PaymentsProductsPayoutsConfigurationInformationConfigurations - a model defined in Swagger
        """

        self._pullfunds = None
        self._pushfunds = None

        if pullfunds is not None:
          self.pullfunds = pullfunds
        if pushfunds is not None:
          self.pushfunds = pushfunds

    @property
    def pullfunds(self):
        """
        Gets the pullfunds of this PaymentsProductsPayoutsConfigurationInformationConfigurations.

        :return: The pullfunds of this PaymentsProductsPayoutsConfigurationInformationConfigurations.
        :rtype: dict(str, PaymentsProductsPayoutsConfigurationInformationConfigurationsPullfunds)
        """
        return self._pullfunds

    @pullfunds.setter
    def pullfunds(self, pullfunds):
        """
        Sets the pullfunds of this PaymentsProductsPayoutsConfigurationInformationConfigurations.

        :param pullfunds: The pullfunds of this PaymentsProductsPayoutsConfigurationInformationConfigurations.
        :type: dict(str, PaymentsProductsPayoutsConfigurationInformationConfigurationsPullfunds)
        """



        self._pullfunds = pullfunds

    @property
    def pushfunds(self):
        """
        Gets the pushfunds of this PaymentsProductsPayoutsConfigurationInformationConfigurations.

        :return: The pushfunds of this PaymentsProductsPayoutsConfigurationInformationConfigurations.
        :rtype: dict(str, PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds)
        """
        return self._pushfunds

    @pushfunds.setter
    def pushfunds(self, pushfunds):
        """
        Sets the pushfunds of this PaymentsProductsPayoutsConfigurationInformationConfigurations.

        :param pushfunds: The pushfunds of this PaymentsProductsPayoutsConfigurationInformationConfigurations.
        :type: dict(str, PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds)
        """



        self._pushfunds = pushfunds

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
        if not isinstance(other, PaymentsProductsPayoutsConfigurationInformationConfigurations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

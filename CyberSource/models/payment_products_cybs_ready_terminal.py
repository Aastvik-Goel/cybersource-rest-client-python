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


class PaymentProductsCybsReadyTerminal(object):
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
        'subscription_information': 'PaymentProductsCardPresentConnectSubscriptionInformation'
    }

    attribute_map = {
        'subscription_information': 'subscriptionInformation'
    }

    def __init__(self, subscription_information=None):
        """
        PaymentProductsCybsReadyTerminal - a model defined in Swagger
        """

        self._subscription_information = None

        if subscription_information is not None:
          self.subscription_information = subscription_information

    @property
    def subscription_information(self):
        """
        Gets the subscription_information of this PaymentProductsCybsReadyTerminal.

        :return: The subscription_information of this PaymentProductsCybsReadyTerminal.
        :rtype: PaymentProductsCardPresentConnectSubscriptionInformation
        """
        return self._subscription_information

    @subscription_information.setter
    def subscription_information(self, subscription_information):
        """
        Sets the subscription_information of this PaymentProductsCybsReadyTerminal.

        :param subscription_information: The subscription_information of this PaymentProductsCybsReadyTerminal.
        :type: PaymentProductsCardPresentConnectSubscriptionInformation
        """

        self._subscription_information = subscription_information

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
        if not isinstance(other, PaymentProductsCybsReadyTerminal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

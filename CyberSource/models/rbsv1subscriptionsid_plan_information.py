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


class Rbsv1subscriptionsidPlanInformation(object):
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
        'billing_cycles': 'Rbsv1plansPlanInformationBillingCycles'
    }

    attribute_map = {
        'billing_cycles': 'billingCycles'
    }

    def __init__(self, billing_cycles=None):
        """
        Rbsv1subscriptionsidPlanInformation - a model defined in Swagger
        """

        self._billing_cycles = None

        if billing_cycles is not None:
          self.billing_cycles = billing_cycles

    @property
    def billing_cycles(self):
        """
        Gets the billing_cycles of this Rbsv1subscriptionsidPlanInformation.

        :return: The billing_cycles of this Rbsv1subscriptionsidPlanInformation.
        :rtype: Rbsv1plansPlanInformationBillingCycles
        """
        return self._billing_cycles

    @billing_cycles.setter
    def billing_cycles(self, billing_cycles):
        """
        Sets the billing_cycles of this Rbsv1subscriptionsidPlanInformation.

        :param billing_cycles: The billing_cycles of this Rbsv1subscriptionsidPlanInformation.
        :type: Rbsv1plansPlanInformationBillingCycles
        """

        self._billing_cycles = billing_cycles

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
        if not isinstance(other, Rbsv1subscriptionsidPlanInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
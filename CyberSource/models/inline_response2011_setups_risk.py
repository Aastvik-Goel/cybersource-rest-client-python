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


class InlineResponse2011SetupsRisk(object):
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
        'fraud_management_essentials': 'InlineResponse2011SetupsPaymentsCardProcessing',
        'decision_manager': 'InlineResponse2011SetupsPaymentsCardProcessing'
    }

    attribute_map = {
        'fraud_management_essentials': 'fraudManagementEssentials',
        'decision_manager': 'decisionManager'
    }

    def __init__(self, fraud_management_essentials=None, decision_manager=None):
        """
        InlineResponse2011SetupsRisk - a model defined in Swagger
        """

        self._fraud_management_essentials = None
        self._decision_manager = None

        if fraud_management_essentials is not None:
          self.fraud_management_essentials = fraud_management_essentials
        if decision_manager is not None:
          self.decision_manager = decision_manager

    @property
    def fraud_management_essentials(self):
        """
        Gets the fraud_management_essentials of this InlineResponse2011SetupsRisk.

        :return: The fraud_management_essentials of this InlineResponse2011SetupsRisk.
        :rtype: InlineResponse2011SetupsPaymentsCardProcessing
        """
        return self._fraud_management_essentials

    @fraud_management_essentials.setter
    def fraud_management_essentials(self, fraud_management_essentials):
        """
        Sets the fraud_management_essentials of this InlineResponse2011SetupsRisk.

        :param fraud_management_essentials: The fraud_management_essentials of this InlineResponse2011SetupsRisk.
        :type: InlineResponse2011SetupsPaymentsCardProcessing
        """



        self._fraud_management_essentials = fraud_management_essentials

    @property
    def decision_manager(self):
        """
        Gets the decision_manager of this InlineResponse2011SetupsRisk.

        :return: The decision_manager of this InlineResponse2011SetupsRisk.
        :rtype: InlineResponse2011SetupsPaymentsCardProcessing
        """
        return self._decision_manager

    @decision_manager.setter
    def decision_manager(self, decision_manager):
        """
        Sets the decision_manager of this InlineResponse2011SetupsRisk.

        :param decision_manager: The decision_manager of this InlineResponse2011SetupsRisk.
        :type: InlineResponse2011SetupsPaymentsCardProcessing
        """



        self._decision_manager = decision_manager

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
        if not isinstance(other, InlineResponse2011SetupsRisk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

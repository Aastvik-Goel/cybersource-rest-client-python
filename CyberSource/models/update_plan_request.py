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


class UpdatePlanRequest(object):
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
        'plan_information': 'Rbsv1plansidPlanInformation',
        'processing_information': 'Rbsv1plansidProcessingInformation',
        'order_information': 'GetAllPlansResponseOrderInformation'
    }

    attribute_map = {
        'plan_information': 'planInformation',
        'processing_information': 'processingInformation',
        'order_information': 'orderInformation'
    }

    def __init__(self, plan_information=None, processing_information=None, order_information=None):
        """
        UpdatePlanRequest - a model defined in Swagger
        """

        self._plan_information = None
        self._processing_information = None
        self._order_information = None

        if plan_information is not None:
          self.plan_information = plan_information
        if processing_information is not None:
          self.processing_information = processing_information
        if order_information is not None:
          self.order_information = order_information

    @property
    def plan_information(self):
        """
        Gets the plan_information of this UpdatePlanRequest.

        :return: The plan_information of this UpdatePlanRequest.
        :rtype: Rbsv1plansidPlanInformation
        """
        return self._plan_information

    @plan_information.setter
    def plan_information(self, plan_information):
        """
        Sets the plan_information of this UpdatePlanRequest.

        :param plan_information: The plan_information of this UpdatePlanRequest.
        :type: Rbsv1plansidPlanInformation
        """

        self._plan_information = plan_information

    @property
    def processing_information(self):
        """
        Gets the processing_information of this UpdatePlanRequest.

        :return: The processing_information of this UpdatePlanRequest.
        :rtype: Rbsv1plansidProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this UpdatePlanRequest.

        :param processing_information: The processing_information of this UpdatePlanRequest.
        :type: Rbsv1plansidProcessingInformation
        """

        self._processing_information = processing_information

    @property
    def order_information(self):
        """
        Gets the order_information of this UpdatePlanRequest.

        :return: The order_information of this UpdatePlanRequest.
        :rtype: GetAllPlansResponseOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this UpdatePlanRequest.

        :param order_information: The order_information of this UpdatePlanRequest.
        :type: GetAllPlansResponseOrderInformation
        """

        self._order_information = order_information

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
        if not isinstance(other, UpdatePlanRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

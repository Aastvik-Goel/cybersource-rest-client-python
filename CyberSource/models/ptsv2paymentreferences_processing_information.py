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


class Ptsv2paymentreferencesProcessingInformation(object):
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
        'session_type': 'str',
        'payment_flow_mode': 'str',
        'action_list': 'list[str]'
    }

    attribute_map = {
        'session_type': 'sessionType',
        'payment_flow_mode': 'paymentFlowMode',
        'action_list': 'actionList'
    }

    def __init__(self, session_type=None, payment_flow_mode=None, action_list=None):
        """
        Ptsv2paymentreferencesProcessingInformation - a model defined in Swagger
        """

        self._session_type = None
        self._payment_flow_mode = None
        self._action_list = None

        if session_type is not None:
          self.session_type = session_type
        if payment_flow_mode is not None:
          self.payment_flow_mode = payment_flow_mode
        if action_list is not None:
          self.action_list = action_list

    @property
    def session_type(self):
        """
        Gets the session_type of this Ptsv2paymentreferencesProcessingInformation.
        Will have 2 values, 'U' (Update) , 'N' (New). Any other values will be rejected. Default will be 'N' 

        :return: The session_type of this Ptsv2paymentreferencesProcessingInformation.
        :rtype: str
        """
        return self._session_type

    @session_type.setter
    def session_type(self, session_type):
        """
        Sets the session_type of this Ptsv2paymentreferencesProcessingInformation.
        Will have 2 values, 'U' (Update) , 'N' (New). Any other values will be rejected. Default will be 'N' 

        :param session_type: The session_type of this Ptsv2paymentreferencesProcessingInformation.
        :type: str
        """

        self._session_type = session_type

    @property
    def payment_flow_mode(self):
        """
        Gets the payment_flow_mode of this Ptsv2paymentreferencesProcessingInformation.
        Whether merchant wants to pass the flow Inline or want to invoke Klarna Hosted Page 

        :return: The payment_flow_mode of this Ptsv2paymentreferencesProcessingInformation.
        :rtype: str
        """
        return self._payment_flow_mode

    @payment_flow_mode.setter
    def payment_flow_mode(self, payment_flow_mode):
        """
        Sets the payment_flow_mode of this Ptsv2paymentreferencesProcessingInformation.
        Whether merchant wants to pass the flow Inline or want to invoke Klarna Hosted Page 

        :param payment_flow_mode: The payment_flow_mode of this Ptsv2paymentreferencesProcessingInformation.
        :type: str
        """

        self._payment_flow_mode = payment_flow_mode

    @property
    def action_list(self):
        """
        Gets the action_list of this Ptsv2paymentreferencesProcessingInformation.
        Possible values are one or more of follows:   - `AP_SESSIONS`: Use this when Alternative Payment Sessions service is requested. 

        :return: The action_list of this Ptsv2paymentreferencesProcessingInformation.
        :rtype: list[str]
        """
        return self._action_list

    @action_list.setter
    def action_list(self, action_list):
        """
        Sets the action_list of this Ptsv2paymentreferencesProcessingInformation.
        Possible values are one or more of follows:   - `AP_SESSIONS`: Use this when Alternative Payment Sessions service is requested. 

        :param action_list: The action_list of this Ptsv2paymentreferencesProcessingInformation.
        :type: list[str]
        """

        self._action_list = action_list

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
        if not isinstance(other, Ptsv2paymentreferencesProcessingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

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


class Notificationsubscriptionsv1webhooksSecurityPolicy(object):
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
        'security_type': 'str',
        'config': 'Notificationsubscriptionsv1webhooksSecurityPolicyConfig'
    }

    attribute_map = {
        'security_type': 'securityType',
        'config': 'config'
    }

    def __init__(self, security_type=None, config=None):
        """
        Notificationsubscriptionsv1webhooksSecurityPolicy - a model defined in Swagger
        """

        self._security_type = None
        self._config = None

        if security_type is not None:
          self.security_type = security_type
        if config is not None:
          self.config = config

    @property
    def security_type(self):
        """
        Gets the security_type of this Notificationsubscriptionsv1webhooksSecurityPolicy.
        Security Policy of the client server.

        :return: The security_type of this Notificationsubscriptionsv1webhooksSecurityPolicy.
        :rtype: str
        """
        return self._security_type

    @security_type.setter
    def security_type(self, security_type):
        """
        Sets the security_type of this Notificationsubscriptionsv1webhooksSecurityPolicy.
        Security Policy of the client server.

        :param security_type: The security_type of this Notificationsubscriptionsv1webhooksSecurityPolicy.
        :type: str
        """

        self._security_type = security_type

    @property
    def config(self):
        """
        Gets the config of this Notificationsubscriptionsv1webhooksSecurityPolicy.

        :return: The config of this Notificationsubscriptionsv1webhooksSecurityPolicy.
        :rtype: Notificationsubscriptionsv1webhooksSecurityPolicyConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this Notificationsubscriptionsv1webhooksSecurityPolicy.

        :param config: The config of this Notificationsubscriptionsv1webhooksSecurityPolicy.
        :type: Notificationsubscriptionsv1webhooksSecurityPolicyConfig
        """

        self._config = config

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
        if not isinstance(other, Notificationsubscriptionsv1webhooksSecurityPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
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


class Notificationsubscriptionsv1webhooksNotificationScope(object):
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
        'scope': 'str',
        'scope_data': 'list[str]'
    }

    attribute_map = {
        'scope': 'scope',
        'scope_data': 'scopeData'
    }

    def __init__(self, scope='SELF', scope_data=None):
        """
        Notificationsubscriptionsv1webhooksNotificationScope - a model defined in Swagger
        """

        self._scope = None
        self._scope_data = None

        if scope is not None:
          self.scope = scope
        if scope_data is not None:
          self.scope_data = scope_data

    @property
    def scope(self):
        """
        Gets the scope of this Notificationsubscriptionsv1webhooksNotificationScope.
        The webhook scope. 1. SELF The Webhook is used to deliver webhooks for only this Organization (or Merchant). 2. DESCENDANTS The Webhook is used to deliver webhooks for this Organization and its children. 3. CUSTOM The Webhook is used to deliver webhooks for the OrgIds (or MiDs) explicitly listed in scopeData field

        :return: The scope of this Notificationsubscriptionsv1webhooksNotificationScope.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this Notificationsubscriptionsv1webhooksNotificationScope.
        The webhook scope. 1. SELF The Webhook is used to deliver webhooks for only this Organization (or Merchant). 2. DESCENDANTS The Webhook is used to deliver webhooks for this Organization and its children. 3. CUSTOM The Webhook is used to deliver webhooks for the OrgIds (or MiDs) explicitly listed in scopeData field

        :param scope: The scope of this Notificationsubscriptionsv1webhooksNotificationScope.
        :type: str
        """



        self._scope = scope

    @property
    def scope_data(self):
        """
        Gets the scope_data of this Notificationsubscriptionsv1webhooksNotificationScope.
        Applicable only if scope=CUSTOM. This should contains a Set of MIDs or OrgIDs for which this subscription is applicable.

        :return: The scope_data of this Notificationsubscriptionsv1webhooksNotificationScope.
        :rtype: list[str]
        """
        return self._scope_data

    @scope_data.setter
    def scope_data(self, scope_data):
        """
        Sets the scope_data of this Notificationsubscriptionsv1webhooksNotificationScope.
        Applicable only if scope=CUSTOM. This should contains a Set of MIDs or OrgIDs for which this subscription is applicable.

        :param scope_data: The scope_data of this Notificationsubscriptionsv1webhooksNotificationScope.
        :type: list[str]
        """



        self._scope_data = scope_data

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
        if not isinstance(other, Notificationsubscriptionsv1webhooksNotificationScope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

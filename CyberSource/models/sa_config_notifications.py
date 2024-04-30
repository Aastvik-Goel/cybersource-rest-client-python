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


class SAConfigNotifications(object):
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
        'merchant_notifications': 'SAConfigNotificationsMerchantNotifications',
        'customer_notifications': 'SAConfigNotificationsCustomerNotifications'
    }

    attribute_map = {
        'merchant_notifications': 'merchantNotifications',
        'customer_notifications': 'customerNotifications'
    }

    def __init__(self, merchant_notifications=None, customer_notifications=None):
        """
        SAConfigNotifications - a model defined in Swagger
        """

        self._merchant_notifications = None
        self._customer_notifications = None

        if merchant_notifications is not None:
          self.merchant_notifications = merchant_notifications
        if customer_notifications is not None:
          self.customer_notifications = customer_notifications

    @property
    def merchant_notifications(self):
        """
        Gets the merchant_notifications of this SAConfigNotifications.

        :return: The merchant_notifications of this SAConfigNotifications.
        :rtype: SAConfigNotificationsMerchantNotifications
        """
        return self._merchant_notifications

    @merchant_notifications.setter
    def merchant_notifications(self, merchant_notifications):
        """
        Sets the merchant_notifications of this SAConfigNotifications.

        :param merchant_notifications: The merchant_notifications of this SAConfigNotifications.
        :type: SAConfigNotificationsMerchantNotifications
        """

        self._merchant_notifications = merchant_notifications

    @property
    def customer_notifications(self):
        """
        Gets the customer_notifications of this SAConfigNotifications.

        :return: The customer_notifications of this SAConfigNotifications.
        :rtype: SAConfigNotificationsCustomerNotifications
        """
        return self._customer_notifications

    @customer_notifications.setter
    def customer_notifications(self, customer_notifications):
        """
        Sets the customer_notifications of this SAConfigNotifications.

        :param customer_notifications: The customer_notifications of this SAConfigNotifications.
        :type: SAConfigNotificationsCustomerNotifications
        """

        self._customer_notifications = customer_notifications

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
        if not isinstance(other, SAConfigNotifications):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

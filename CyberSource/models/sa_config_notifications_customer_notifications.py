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


class SAConfigNotificationsCustomerNotifications(object):
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
        'custom_receipt_page_enabled': 'bool',
        'receipt_email_address': 'str',
        'customer_receipt_email_enabled': 'bool',
        'custom_cancel_page': 'str',
        'custom_receipt_page': 'str',
        'custom_cancel_page_enabled': 'bool',
        'notification_receipt_email_enabled': 'bool'
    }

    attribute_map = {
        'custom_receipt_page_enabled': 'customReceiptPageEnabled',
        'receipt_email_address': 'receiptEmailAddress',
        'customer_receipt_email_enabled': 'customerReceiptEmailEnabled',
        'custom_cancel_page': 'customCancelPage',
        'custom_receipt_page': 'customReceiptPage',
        'custom_cancel_page_enabled': 'customCancelPageEnabled',
        'notification_receipt_email_enabled': 'notificationReceiptEmailEnabled'
    }

    def __init__(self, custom_receipt_page_enabled=None, receipt_email_address=None, customer_receipt_email_enabled=None, custom_cancel_page=None, custom_receipt_page=None, custom_cancel_page_enabled=None, notification_receipt_email_enabled=None):
        """
        SAConfigNotificationsCustomerNotifications - a model defined in Swagger
        """

        self._custom_receipt_page_enabled = None
        self._receipt_email_address = None
        self._customer_receipt_email_enabled = None
        self._custom_cancel_page = None
        self._custom_receipt_page = None
        self._custom_cancel_page_enabled = None
        self._notification_receipt_email_enabled = None

        if custom_receipt_page_enabled is not None:
          self.custom_receipt_page_enabled = custom_receipt_page_enabled
        if receipt_email_address is not None:
          self.receipt_email_address = receipt_email_address
        if customer_receipt_email_enabled is not None:
          self.customer_receipt_email_enabled = customer_receipt_email_enabled
        if custom_cancel_page is not None:
          self.custom_cancel_page = custom_cancel_page
        if custom_receipt_page is not None:
          self.custom_receipt_page = custom_receipt_page
        if custom_cancel_page_enabled is not None:
          self.custom_cancel_page_enabled = custom_cancel_page_enabled
        if notification_receipt_email_enabled is not None:
          self.notification_receipt_email_enabled = notification_receipt_email_enabled

    @property
    def custom_receipt_page_enabled(self):
        """
        Gets the custom_receipt_page_enabled of this SAConfigNotificationsCustomerNotifications.
        Toggles the custom receipt page, where merchants can receive the results of the transaction and display appropriate messaging. Usually set by web developers integrating to Secure Acceptance.

        :return: The custom_receipt_page_enabled of this SAConfigNotificationsCustomerNotifications.
        :rtype: bool
        """
        return self._custom_receipt_page_enabled

    @custom_receipt_page_enabled.setter
    def custom_receipt_page_enabled(self, custom_receipt_page_enabled):
        """
        Sets the custom_receipt_page_enabled of this SAConfigNotificationsCustomerNotifications.
        Toggles the custom receipt page, where merchants can receive the results of the transaction and display appropriate messaging. Usually set by web developers integrating to Secure Acceptance.

        :param custom_receipt_page_enabled: The custom_receipt_page_enabled of this SAConfigNotificationsCustomerNotifications.
        :type: bool
        """

        self._custom_receipt_page_enabled = custom_receipt_page_enabled

    @property
    def receipt_email_address(self):
        """
        Gets the receipt_email_address of this SAConfigNotificationsCustomerNotifications.
        Email address where a copy of the payer's receipt email is sent, when notificationReceiptEmailEnabled is true.

        :return: The receipt_email_address of this SAConfigNotificationsCustomerNotifications.
        :rtype: str
        """
        return self._receipt_email_address

    @receipt_email_address.setter
    def receipt_email_address(self, receipt_email_address):
        """
        Sets the receipt_email_address of this SAConfigNotificationsCustomerNotifications.
        Email address where a copy of the payer's receipt email is sent, when notificationReceiptEmailEnabled is true.

        :param receipt_email_address: The receipt_email_address of this SAConfigNotificationsCustomerNotifications.
        :type: str
        """

        self._receipt_email_address = receipt_email_address

    @property
    def customer_receipt_email_enabled(self):
        """
        Gets the customer_receipt_email_enabled of this SAConfigNotificationsCustomerNotifications.
        Toggles an email receipt sent to the payer's email address on payment success.

        :return: The customer_receipt_email_enabled of this SAConfigNotificationsCustomerNotifications.
        :rtype: bool
        """
        return self._customer_receipt_email_enabled

    @customer_receipt_email_enabled.setter
    def customer_receipt_email_enabled(self, customer_receipt_email_enabled):
        """
        Sets the customer_receipt_email_enabled of this SAConfigNotificationsCustomerNotifications.
        Toggles an email receipt sent to the payer's email address on payment success.

        :param customer_receipt_email_enabled: The customer_receipt_email_enabled of this SAConfigNotificationsCustomerNotifications.
        :type: bool
        """

        self._customer_receipt_email_enabled = customer_receipt_email_enabled

    @property
    def custom_cancel_page(self):
        """
        Gets the custom_cancel_page of this SAConfigNotificationsCustomerNotifications.
        URL to which transaction results are POSTed when the payer clicks 'Cancel' on the Hosted Checkout. Triggered when customCancelPageEnabled is true. Usually set by web developers integrating to Secure Acceptance.

        :return: The custom_cancel_page of this SAConfigNotificationsCustomerNotifications.
        :rtype: str
        """
        return self._custom_cancel_page

    @custom_cancel_page.setter
    def custom_cancel_page(self, custom_cancel_page):
        """
        Sets the custom_cancel_page of this SAConfigNotificationsCustomerNotifications.
        URL to which transaction results are POSTed when the payer clicks 'Cancel' on the Hosted Checkout. Triggered when customCancelPageEnabled is true. Usually set by web developers integrating to Secure Acceptance.

        :param custom_cancel_page: The custom_cancel_page of this SAConfigNotificationsCustomerNotifications.
        :type: str
        """

        self._custom_cancel_page = custom_cancel_page

    @property
    def custom_receipt_page(self):
        """
        Gets the custom_receipt_page of this SAConfigNotificationsCustomerNotifications.
        URL to which transaction results are POSTed when the payer requests a payment on the Hosted Checkout. Triggered when customCancelPageEnabled is true. Usually set by web developers integrating to Secure Acceptance.

        :return: The custom_receipt_page of this SAConfigNotificationsCustomerNotifications.
        :rtype: str
        """
        return self._custom_receipt_page

    @custom_receipt_page.setter
    def custom_receipt_page(self, custom_receipt_page):
        """
        Sets the custom_receipt_page of this SAConfigNotificationsCustomerNotifications.
        URL to which transaction results are POSTed when the payer requests a payment on the Hosted Checkout. Triggered when customCancelPageEnabled is true. Usually set by web developers integrating to Secure Acceptance.

        :param custom_receipt_page: The custom_receipt_page of this SAConfigNotificationsCustomerNotifications.
        :type: str
        """

        self._custom_receipt_page = custom_receipt_page

    @property
    def custom_cancel_page_enabled(self):
        """
        Gets the custom_cancel_page_enabled of this SAConfigNotificationsCustomerNotifications.
        Toggles the custom cancel page, where merchants can receive notice that the payer has canceled, and display appropriate messaging and direction. Usually set by web developers integrating to Secure Acceptance.

        :return: The custom_cancel_page_enabled of this SAConfigNotificationsCustomerNotifications.
        :rtype: bool
        """
        return self._custom_cancel_page_enabled

    @custom_cancel_page_enabled.setter
    def custom_cancel_page_enabled(self, custom_cancel_page_enabled):
        """
        Sets the custom_cancel_page_enabled of this SAConfigNotificationsCustomerNotifications.
        Toggles the custom cancel page, where merchants can receive notice that the payer has canceled, and display appropriate messaging and direction. Usually set by web developers integrating to Secure Acceptance.

        :param custom_cancel_page_enabled: The custom_cancel_page_enabled of this SAConfigNotificationsCustomerNotifications.
        :type: bool
        """

        self._custom_cancel_page_enabled = custom_cancel_page_enabled

    @property
    def notification_receipt_email_enabled(self):
        """
        Gets the notification_receipt_email_enabled of this SAConfigNotificationsCustomerNotifications.
        Toggles whether merchant receives a copy of the payer's receipt email.

        :return: The notification_receipt_email_enabled of this SAConfigNotificationsCustomerNotifications.
        :rtype: bool
        """
        return self._notification_receipt_email_enabled

    @notification_receipt_email_enabled.setter
    def notification_receipt_email_enabled(self, notification_receipt_email_enabled):
        """
        Sets the notification_receipt_email_enabled of this SAConfigNotificationsCustomerNotifications.
        Toggles whether merchant receives a copy of the payer's receipt email.

        :param notification_receipt_email_enabled: The notification_receipt_email_enabled of this SAConfigNotificationsCustomerNotifications.
        :type: bool
        """

        self._notification_receipt_email_enabled = notification_receipt_email_enabled

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
        if not isinstance(other, SAConfigNotificationsCustomerNotifications):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

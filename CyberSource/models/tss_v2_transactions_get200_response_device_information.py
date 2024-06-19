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


class TssV2TransactionsGet200ResponseDeviceInformation(object):
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
        'ip_address': 'str',
        'host_name': 'str',
        'cookies_accepted': 'str'
    }

    attribute_map = {
        'ip_address': 'ipAddress',
        'host_name': 'hostName',
        'cookies_accepted': 'cookiesAccepted'
    }

    def __init__(self, ip_address=None, host_name=None, cookies_accepted=None):
        """
        TssV2TransactionsGet200ResponseDeviceInformation - a model defined in Swagger
        """

        self._ip_address = None
        self._host_name = None
        self._cookies_accepted = None

        if ip_address is not None:
          self.ip_address = ip_address
        if host_name is not None:
          self.host_name = host_name
        if cookies_accepted is not None:
          self.cookies_accepted = cookies_accepted

    @property
    def ip_address(self):
        """
        Gets the ip_address of this TssV2TransactionsGet200ResponseDeviceInformation.
        IP address of the customer.  #### Used by **Authorization, Capture, and Credit** Optional field. 

        :return: The ip_address of this TssV2TransactionsGet200ResponseDeviceInformation.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this TssV2TransactionsGet200ResponseDeviceInformation.
        IP address of the customer.  #### Used by **Authorization, Capture, and Credit** Optional field. 

        :param ip_address: The ip_address of this TssV2TransactionsGet200ResponseDeviceInformation.
        :type: str
        """

        self._ip_address = ip_address

    @property
    def host_name(self):
        """
        Gets the host_name of this TssV2TransactionsGet200ResponseDeviceInformation.
        DNS resolved hostname from `ipAddress`.

        :return: The host_name of this TssV2TransactionsGet200ResponseDeviceInformation.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this TssV2TransactionsGet200ResponseDeviceInformation.
        DNS resolved hostname from `ipAddress`.

        :param host_name: The host_name of this TssV2TransactionsGet200ResponseDeviceInformation.
        :type: str
        """

        self._host_name = host_name

    @property
    def cookies_accepted(self):
        """
        Gets the cookies_accepted of this TssV2TransactionsGet200ResponseDeviceInformation.
        Whether the customer's browser accepts cookies. This field can contain one of the following values: - `yes`: The customer's browser accepts cookies. - `no`: The customer's browser does not accept cookies. 

        :return: The cookies_accepted of this TssV2TransactionsGet200ResponseDeviceInformation.
        :rtype: str
        """
        return self._cookies_accepted

    @cookies_accepted.setter
    def cookies_accepted(self, cookies_accepted):
        """
        Sets the cookies_accepted of this TssV2TransactionsGet200ResponseDeviceInformation.
        Whether the customer's browser accepts cookies. This field can contain one of the following values: - `yes`: The customer's browser accepts cookies. - `no`: The customer's browser does not accept cookies. 

        :param cookies_accepted: The cookies_accepted of this TssV2TransactionsGet200ResponseDeviceInformation.
        :type: str
        """

        self._cookies_accepted = cookies_accepted

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
        if not isinstance(other, TssV2TransactionsGet200ResponseDeviceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

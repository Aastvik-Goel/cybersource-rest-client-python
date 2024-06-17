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


class Ptsv2paymentsidcapturesDeviceInformation(object):
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
        'host_name': 'str',
        'ip_address': 'str',
        'user_agent': 'str'
    }

    attribute_map = {
        'host_name': 'hostName',
        'ip_address': 'ipAddress',
        'user_agent': 'userAgent'
    }

    def __init__(self, host_name=None, ip_address=None, user_agent=None):
        """
        Ptsv2paymentsidcapturesDeviceInformation - a model defined in Swagger
        """

        self._host_name = None
        self._ip_address = None
        self._user_agent = None

        if host_name is not None:
          self.host_name = host_name
        if ip_address is not None:
          self.ip_address = ip_address
        if user_agent is not None:
          self.user_agent = user_agent

    @property
    def host_name(self):
        """
        Gets the host_name of this Ptsv2paymentsidcapturesDeviceInformation.
        DNS resolved hostname from `ipAddress`.

        :return: The host_name of this Ptsv2paymentsidcapturesDeviceInformation.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this Ptsv2paymentsidcapturesDeviceInformation.
        DNS resolved hostname from `ipAddress`.

        :param host_name: The host_name of this Ptsv2paymentsidcapturesDeviceInformation.
        :type: str
        """



        self._host_name = host_name

    @property
    def ip_address(self):
        """
        Gets the ip_address of this Ptsv2paymentsidcapturesDeviceInformation.
        IP address of the customer.  #### Used by **Authorization, Capture, and Credit** Optional field. 

        :return: The ip_address of this Ptsv2paymentsidcapturesDeviceInformation.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Ptsv2paymentsidcapturesDeviceInformation.
        IP address of the customer.  #### Used by **Authorization, Capture, and Credit** Optional field. 

        :param ip_address: The ip_address of this Ptsv2paymentsidcapturesDeviceInformation.
        :type: str
        """



        self._ip_address = ip_address

    @property
    def user_agent(self):
        """
        Gets the user_agent of this Ptsv2paymentsidcapturesDeviceInformation.
        Customer's browser as identified from the HTTP header data. For example, `Mozilla` is the value that identifies the Netscape browser. 

        :return: The user_agent of this Ptsv2paymentsidcapturesDeviceInformation.
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """
        Sets the user_agent of this Ptsv2paymentsidcapturesDeviceInformation.
        Customer's browser as identified from the HTTP header data. For example, `Mozilla` is the value that identifies the Netscape browser. 

        :param user_agent: The user_agent of this Ptsv2paymentsidcapturesDeviceInformation.
        :type: str
        """



        self._user_agent = user_agent

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
        if not isinstance(other, Ptsv2paymentsidcapturesDeviceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

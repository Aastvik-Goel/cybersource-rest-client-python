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


class RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddressAddress1(object):
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
        'with_apartment': 'str',
        'without_apartment': 'str'
    }

    attribute_map = {
        'with_apartment': 'withApartment',
        'without_apartment': 'withoutApartment'
    }

    def __init__(self, with_apartment=None, without_apartment=None):
        """
        RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddressAddress1 - a model defined in Swagger
        """

        self._with_apartment = None
        self._without_apartment = None

        if with_apartment is not None:
          self.with_apartment = with_apartment
        if without_apartment is not None:
          self.without_apartment = without_apartment

    @property
    def with_apartment(self):
        """
        Gets the with_apartment of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddressAddress1.
        First line of the standardized address, including apartment information.

        :return: The with_apartment of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddressAddress1.
        :rtype: str
        """
        return self._with_apartment

    @with_apartment.setter
    def with_apartment(self, with_apartment):
        """
        Sets the with_apartment of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddressAddress1.
        First line of the standardized address, including apartment information.

        :param with_apartment: The with_apartment of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddressAddress1.
        :type: str
        """

        self._with_apartment = with_apartment

    @property
    def without_apartment(self):
        """
        Gets the without_apartment of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddressAddress1.
        First line of the standardized address, without apartment information. Returned for U.S. and Canadian addresses. 

        :return: The without_apartment of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddressAddress1.
        :rtype: str
        """
        return self._without_apartment

    @without_apartment.setter
    def without_apartment(self, without_apartment):
        """
        Sets the without_apartment of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddressAddress1.
        First line of the standardized address, without apartment information. Returned for U.S. and Canadian addresses. 

        :param without_apartment: The without_apartment of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddressAddress1.
        :type: str
        """

        self._without_apartment = without_apartment

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
        if not isinstance(other, RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddressAddress1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

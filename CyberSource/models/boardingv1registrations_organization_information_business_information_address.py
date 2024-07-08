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


class Boardingv1registrationsOrganizationInformationBusinessInformationAddress(object):
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
        'country': 'str',
        'address1': 'str',
        'address2': 'str',
        'locality': 'str',
        'administrative_area': 'str',
        'postal_code': 'str'
    }

    attribute_map = {
        'country': 'country',
        'address1': 'address1',
        'address2': 'address2',
        'locality': 'locality',
        'administrative_area': 'administrativeArea',
        'postal_code': 'postalCode'
    }

    def __init__(self, country=None, address1=None, address2=None, locality=None, administrative_area=None, postal_code=None):
        """
        Boardingv1registrationsOrganizationInformationBusinessInformationAddress - a model defined in Swagger
        """

        self._country = None
        self._address1 = None
        self._address2 = None
        self._locality = None
        self._administrative_area = None
        self._postal_code = None

        self.country = country
        self.address1 = address1
        if address2 is not None:
          self.address2 = address2
        self.locality = locality
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if postal_code is not None:
          self.postal_code = postal_code

    @property
    def country(self):
        """
        Gets the country of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.

        :return: The country of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.

        :param country: The country of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.
        :type: str
        """

        self._country = country

    @property
    def address1(self):
        """
        Gets the address1 of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.

        :return: The address1 of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.

        :param address1: The address1 of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.

        :return: The address2 of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.

        :param address2: The address2 of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.
        :type: str
        """

        self._address2 = address2

    @property
    def locality(self):
        """
        Gets the locality of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.
        City of the billing address.

        :return: The locality of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.
        City of the billing address.

        :param locality: The locality of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.
        :type: str
        """

        self._locality = locality

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.
        State or province of the billing address. Required for United States and Canada.

        :return: The administrative_area of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.
        State or province of the billing address. Required for United States and Canada.

        :param administrative_area: The administrative_area of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.
        :type: str
        """

        self._administrative_area = administrative_area

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.
        Postal code for the billing address. The postal code must consist of 5 to 9 digits. Required for United States and Canada.

        :return: The postal_code of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.
        Postal code for the billing address. The postal code must consist of 5 to 9 digits. Required for United States and Canada.

        :param postal_code: The postal_code of this Boardingv1registrationsOrganizationInformationBusinessInformationAddress.
        :type: str
        """

        self._postal_code = postal_code

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
        if not isinstance(other, Boardingv1registrationsOrganizationInformationBusinessInformationAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

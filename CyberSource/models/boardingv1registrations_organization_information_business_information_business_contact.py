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


class Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact(object):
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
        'first_name': 'str',
        'middle_name': 'str',
        'last_name': 'str',
        'phone_number': 'str',
        'email': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'middle_name': 'middleName',
        'last_name': 'lastName',
        'phone_number': 'phoneNumber',
        'email': 'email'
    }

    def __init__(self, first_name=None, middle_name=None, last_name=None, phone_number=None, email=None):
        """
        Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact - a model defined in Swagger
        """

        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._phone_number = None
        self._email = None

        self.first_name = first_name
        if middle_name is not None:
          self.middle_name = middle_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    @property
    def first_name(self):
        """
        Gets the first_name of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.

        :return: The first_name of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.

        :param first_name: The first_name of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.
        :type: str
        """



        self._first_name = first_name

    @property
    def middle_name(self):
        """
        Gets the middle_name of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.

        :return: The middle_name of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """
        Sets the middle_name of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.

        :param middle_name: The middle_name of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.
        :type: str
        """



        self._middle_name = middle_name

    @property
    def last_name(self):
        """
        Gets the last_name of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.

        :return: The last_name of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.

        :param last_name: The last_name of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.
        :type: str
        """



        self._last_name = last_name

    @property
    def phone_number(self):
        """
        Gets the phone_number of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.

        :return: The phone_number of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.

        :param phone_number: The phone_number of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.
        :type: str
        """



        self._phone_number = phone_number

    @property
    def email(self):
        """
        Gets the email of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.

        :return: The email of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.

        :param email: The email of this Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact.
        :type: str
        """



        self._email = email

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
        if not isinstance(other, Boardingv1registrationsOrganizationInformationBusinessInformationBusinessContact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

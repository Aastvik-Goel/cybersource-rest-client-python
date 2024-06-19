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


class Ptsv2payoutsRecipientInformation(object):
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
        'middle_initial': 'str',
        'middle_name': 'str',
        'last_name': 'str',
        'address1': 'str',
        'locality': 'str',
        'administrative_area': 'str',
        'country': 'str',
        'postal_code': 'str',
        'phone_number': 'str',
        'date_of_birth': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'middle_initial': 'middleInitial',
        'middle_name': 'middleName',
        'last_name': 'lastName',
        'address1': 'address1',
        'locality': 'locality',
        'administrative_area': 'administrativeArea',
        'country': 'country',
        'postal_code': 'postalCode',
        'phone_number': 'phoneNumber',
        'date_of_birth': 'dateOfBirth'
    }

    def __init__(self, first_name=None, middle_initial=None, middle_name=None, last_name=None, address1=None, locality=None, administrative_area=None, country=None, postal_code=None, phone_number=None, date_of_birth=None):
        """
        Ptsv2payoutsRecipientInformation - a model defined in Swagger
        """

        self._first_name = None
        self._middle_initial = None
        self._middle_name = None
        self._last_name = None
        self._address1 = None
        self._locality = None
        self._administrative_area = None
        self._country = None
        self._postal_code = None
        self._phone_number = None
        self._date_of_birth = None

        if first_name is not None:
          self.first_name = first_name
        if middle_initial is not None:
          self.middle_initial = middle_initial
        if middle_name is not None:
          self.middle_name = middle_name
        if last_name is not None:
          self.last_name = last_name
        if address1 is not None:
          self.address1 = address1
        if locality is not None:
          self.locality = locality
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if country is not None:
          self.country = country
        if postal_code is not None:
          self.postal_code = postal_code
        if phone_number is not None:
          self.phone_number = phone_number
        if date_of_birth is not None:
          self.date_of_birth = date_of_birth

    @property
    def first_name(self):
        """
        Gets the first_name of this Ptsv2payoutsRecipientInformation.
        First name of recipient. characters. * CTV (14) * Paymentech (30) 

        :return: The first_name of this Ptsv2payoutsRecipientInformation.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this Ptsv2payoutsRecipientInformation.
        First name of recipient. characters. * CTV (14) * Paymentech (30) 

        :param first_name: The first_name of this Ptsv2payoutsRecipientInformation.
        :type: str
        """

        self._first_name = first_name

    @property
    def middle_initial(self):
        """
        Gets the middle_initial of this Ptsv2payoutsRecipientInformation.
        Middle Initial of recipient. Required only for FDCCompass. 

        :return: The middle_initial of this Ptsv2payoutsRecipientInformation.
        :rtype: str
        """
        return self._middle_initial

    @middle_initial.setter
    def middle_initial(self, middle_initial):
        """
        Sets the middle_initial of this Ptsv2payoutsRecipientInformation.
        Middle Initial of recipient. Required only for FDCCompass. 

        :param middle_initial: The middle_initial of this Ptsv2payoutsRecipientInformation.
        :type: str
        """

        self._middle_initial = middle_initial

    @property
    def middle_name(self):
        """
        Gets the middle_name of this Ptsv2payoutsRecipientInformation.
        Recipient's middle name. This field is a _passthrough_, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor. 

        :return: The middle_name of this Ptsv2payoutsRecipientInformation.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """
        Sets the middle_name of this Ptsv2payoutsRecipientInformation.
        Recipient's middle name. This field is a _passthrough_, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor. 

        :param middle_name: The middle_name of this Ptsv2payoutsRecipientInformation.
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """
        Gets the last_name of this Ptsv2payoutsRecipientInformation.
        Last name of recipient. characters. * CTV (14) * Paymentech (30) 

        :return: The last_name of this Ptsv2payoutsRecipientInformation.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this Ptsv2payoutsRecipientInformation.
        Last name of recipient. characters. * CTV (14) * Paymentech (30) 

        :param last_name: The last_name of this Ptsv2payoutsRecipientInformation.
        :type: str
        """

        self._last_name = last_name

    @property
    def address1(self):
        """
        Gets the address1 of this Ptsv2payoutsRecipientInformation.
        Recipient address information. Required only for FDCCompass.

        :return: The address1 of this Ptsv2payoutsRecipientInformation.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this Ptsv2payoutsRecipientInformation.
        Recipient address information. Required only for FDCCompass.

        :param address1: The address1 of this Ptsv2payoutsRecipientInformation.
        :type: str
        """

        self._address1 = address1

    @property
    def locality(self):
        """
        Gets the locality of this Ptsv2payoutsRecipientInformation.
        Recipient city. Required only for FDCCompass.

        :return: The locality of this Ptsv2payoutsRecipientInformation.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this Ptsv2payoutsRecipientInformation.
        Recipient city. Required only for FDCCompass.

        :param locality: The locality of this Ptsv2payoutsRecipientInformation.
        :type: str
        """

        self._locality = locality

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this Ptsv2payoutsRecipientInformation.
        Recipient State. Required only for FDCCompass.

        :return: The administrative_area of this Ptsv2payoutsRecipientInformation.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this Ptsv2payoutsRecipientInformation.
        Recipient State. Required only for FDCCompass.

        :param administrative_area: The administrative_area of this Ptsv2payoutsRecipientInformation.
        :type: str
        """

        self._administrative_area = administrative_area

    @property
    def country(self):
        """
        Gets the country of this Ptsv2payoutsRecipientInformation.
        Recipient country code. Required only for FDCCompass.

        :return: The country of this Ptsv2payoutsRecipientInformation.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Ptsv2payoutsRecipientInformation.
        Recipient country code. Required only for FDCCompass.

        :param country: The country of this Ptsv2payoutsRecipientInformation.
        :type: str
        """

        self._country = country

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Ptsv2payoutsRecipientInformation.
        Recipient postal code. Required only for FDCCompass.

        :return: The postal_code of this Ptsv2payoutsRecipientInformation.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Ptsv2payoutsRecipientInformation.
        Recipient postal code. Required only for FDCCompass.

        :param postal_code: The postal_code of this Ptsv2payoutsRecipientInformation.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def phone_number(self):
        """
        Gets the phone_number of this Ptsv2payoutsRecipientInformation.
        Recipient phone number. Required only for FDCCompass.

        :return: The phone_number of this Ptsv2payoutsRecipientInformation.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this Ptsv2payoutsRecipientInformation.
        Recipient phone number. Required only for FDCCompass.

        :param phone_number: The phone_number of this Ptsv2payoutsRecipientInformation.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def date_of_birth(self):
        """
        Gets the date_of_birth of this Ptsv2payoutsRecipientInformation.
        Recipient date of birth in YYYYMMDD format. Required only for FDCCompass.

        :return: The date_of_birth of this Ptsv2payoutsRecipientInformation.
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """
        Sets the date_of_birth of this Ptsv2payoutsRecipientInformation.
        Recipient date of birth in YYYYMMDD format. Required only for FDCCompass.

        :param date_of_birth: The date_of_birth of this Ptsv2payoutsRecipientInformation.
        :type: str
        """

        self._date_of_birth = date_of_birth

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
        if not isinstance(other, Ptsv2payoutsRecipientInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

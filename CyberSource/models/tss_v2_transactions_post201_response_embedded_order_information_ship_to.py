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


class TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo(object):
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
        'last_name': 'str',
        'address1': 'str',
        'country': 'str',
        'phone_number': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'address1': 'address1',
        'country': 'country',
        'phone_number': 'phoneNumber'
    }

    def __init__(self, first_name=None, last_name=None, address1=None, country=None, phone_number=None):
        """
        TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo - a model defined in Swagger
        """

        self._first_name = None
        self._last_name = None
        self._address1 = None
        self._country = None
        self._phone_number = None

        if first_name is not None:
          self.first_name = first_name
        if last_name is not None:
          self.last_name = last_name
        if address1 is not None:
          self.address1 = address1
        if country is not None:
          self.country = country
        if phone_number is not None:
          self.phone_number = phone_number

    @property
    def first_name(self):
        """
        Gets the first_name of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        First name of the recipient.  #### Litle Maximum length: 25  #### All other processors Maximum length: 60  Optional field. 

        :return: The first_name of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        First name of the recipient.  #### Litle Maximum length: 25  #### All other processors Maximum length: 60  Optional field. 

        :param first_name: The first_name of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        Last name of the recipient.  #### Litle Maximum length: 25  #### All other processors Maximum length: 60  Optional field. 

        :return: The last_name of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        Last name of the recipient.  #### Litle Maximum length: 25  #### All other processors Maximum length: 60  Optional field. 

        :param last_name: The last_name of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        :type: str
        """

        self._last_name = last_name

    @property
    def address1(self):
        """
        Gets the address1 of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        First line of the shipping address.  Required field for authorization if any shipping address information is included in the request; otherwise, optional.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. Billing address objects will be used to determine the cardholder's location when shipTo objects are not present. 

        :return: The address1 of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        First line of the shipping address.  Required field for authorization if any shipping address information is included in the request; otherwise, optional.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. Billing address objects will be used to determine the cardholder's location when shipTo objects are not present. 

        :param address1: The address1 of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        :type: str
        """

        self._address1 = address1

    @property
    def country(self):
        """
        Gets the country of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        Country of the shipping address. Use the two-character [ISO Standard Country Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf)  Required field for authorization if any shipping address information is included in the request; otherwise, optional.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes. Billing address objects will be used to determine the cardholder's location when shipTo objects are not present. 

        :return: The country of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        Country of the shipping address. Use the two-character [ISO Standard Country Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf)  Required field for authorization if any shipping address information is included in the request; otherwise, optional.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes. Billing address objects will be used to determine the cardholder's location when shipTo objects are not present. 

        :param country: The country of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        :type: str
        """

        self._country = country

    @property
    def phone_number(self):
        """
        Gets the phone_number of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        Phone number associated with the shipping address.

        :return: The phone_number of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        Phone number associated with the shipping address.

        :param phone_number: The phone_number of this TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo.
        :type: str
        """

        self._phone_number = phone_number

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
        if not isinstance(other, TssV2TransactionsPost201ResponseEmbeddedOrderInformationShipTo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

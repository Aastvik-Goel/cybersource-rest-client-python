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


class InlineResponse2011IssuerInformation(object):
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
        'name': 'str',
        'country': 'str',
        'bin_length': 'str',
        'account_prefix': 'str',
        'phone_number': 'str'
    }

    attribute_map = {
        'name': 'name',
        'country': 'country',
        'bin_length': 'binLength',
        'account_prefix': 'accountPrefix',
        'phone_number': 'phoneNumber'
    }

    def __init__(self, name=None, country=None, bin_length=None, account_prefix=None, phone_number=None):
        """
        InlineResponse2011IssuerInformation - a model defined in Swagger
        """

        self._name = None
        self._country = None
        self._bin_length = None
        self._account_prefix = None
        self._phone_number = None

        if name is not None:
          self.name = name
        if country is not None:
          self.country = country
        if bin_length is not None:
          self.bin_length = bin_length
        if account_prefix is not None:
          self.account_prefix = account_prefix
        if phone_number is not None:
          self.phone_number = phone_number

    @property
    def name(self):
        """
        Gets the name of this InlineResponse2011IssuerInformation.
        This field contains the issuer name. 

        :return: The name of this InlineResponse2011IssuerInformation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InlineResponse2011IssuerInformation.
        This field contains the issuer name. 

        :param name: The name of this InlineResponse2011IssuerInformation.
        :type: str
        """

        self._name = name

    @property
    def country(self):
        """
        Gets the country of this InlineResponse2011IssuerInformation.
        This field contains [2-character ISO Country Codes](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf) for the issuer. 

        :return: The country of this InlineResponse2011IssuerInformation.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this InlineResponse2011IssuerInformation.
        This field contains [2-character ISO Country Codes](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf) for the issuer. 

        :param country: The country of this InlineResponse2011IssuerInformation.
        :type: str
        """

        self._country = country

    @property
    def bin_length(self):
        """
        Gets the bin_length of this InlineResponse2011IssuerInformation.
        This field contains the length of the BIN. 

        :return: The bin_length of this InlineResponse2011IssuerInformation.
        :rtype: str
        """
        return self._bin_length

    @bin_length.setter
    def bin_length(self, bin_length):
        """
        Sets the bin_length of this InlineResponse2011IssuerInformation.
        This field contains the length of the BIN. 

        :param bin_length: The bin_length of this InlineResponse2011IssuerInformation.
        :type: str
        """

        self._bin_length = bin_length

    @property
    def account_prefix(self):
        """
        Gets the account_prefix of this InlineResponse2011IssuerInformation.
        This field contains the first 6 to 8 digits of a primary account number (PAN). The length of the field is determined by [PCI-DSS standards for truncation](https://pcissc.secure.force.com/faq/articles/Frequently_Asked_Question/What-are-acceptable-formats-for-truncation-of-primary-account-numbers). 

        :return: The account_prefix of this InlineResponse2011IssuerInformation.
        :rtype: str
        """
        return self._account_prefix

    @account_prefix.setter
    def account_prefix(self, account_prefix):
        """
        Sets the account_prefix of this InlineResponse2011IssuerInformation.
        This field contains the first 6 to 8 digits of a primary account number (PAN). The length of the field is determined by [PCI-DSS standards for truncation](https://pcissc.secure.force.com/faq/articles/Frequently_Asked_Question/What-are-acceptable-formats-for-truncation-of-primary-account-numbers). 

        :param account_prefix: The account_prefix of this InlineResponse2011IssuerInformation.
        :type: str
        """

        self._account_prefix = account_prefix

    @property
    def phone_number(self):
        """
        Gets the phone_number of this InlineResponse2011IssuerInformation.
        This field contains the customer service phone number for the issuer. 

        :return: The phone_number of this InlineResponse2011IssuerInformation.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this InlineResponse2011IssuerInformation.
        This field contains the customer service phone number for the issuer. 

        :param phone_number: The phone_number of this InlineResponse2011IssuerInformation.
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
        if not isinstance(other, InlineResponse2011IssuerInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

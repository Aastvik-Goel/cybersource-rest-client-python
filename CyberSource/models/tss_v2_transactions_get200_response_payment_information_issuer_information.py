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


class TssV2TransactionsGet200ResponsePaymentInformationIssuerInformation(object):
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
        'phone_number': 'str'
    }

    attribute_map = {
        'name': 'name',
        'country': 'country',
        'bin_length': 'binLength',
        'phone_number': 'phoneNumber'
    }

    def __init__(self, name=None, country=None, bin_length=None, phone_number=None):
        """
        TssV2TransactionsGet200ResponsePaymentInformationIssuerInformation - a model defined in Swagger
        """

        self._name = None
        self._country = None
        self._bin_length = None
        self._phone_number = None

        if name is not None:
          self.name = name
        if country is not None:
          self.country = country
        if bin_length is not None:
          self.bin_length = bin_length
        if phone_number is not None:
          self.phone_number = phone_number

    @property
    def name(self):
        """
        Gets the name of this TssV2TransactionsGet200ResponsePaymentInformationIssuerInformation.
        This field contains the issuer name. 

        :return: The name of this TssV2TransactionsGet200ResponsePaymentInformationIssuerInformation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TssV2TransactionsGet200ResponsePaymentInformationIssuerInformation.
        This field contains the issuer name. 

        :param name: The name of this TssV2TransactionsGet200ResponsePaymentInformationIssuerInformation.
        :type: str
        """

        self._name = name

    @property
    def country(self):
        """
        Gets the country of this TssV2TransactionsGet200ResponsePaymentInformationIssuerInformation.
        This field contains [2-character ISO Country Codes](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf) for the issuer. 

        :return: The country of this TssV2TransactionsGet200ResponsePaymentInformationIssuerInformation.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this TssV2TransactionsGet200ResponsePaymentInformationIssuerInformation.
        This field contains [2-character ISO Country Codes](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf) for the issuer. 

        :param country: The country of this TssV2TransactionsGet200ResponsePaymentInformationIssuerInformation.
        :type: str
        """

        self._country = country

    @property
    def bin_length(self):
        """
        Gets the bin_length of this TssV2TransactionsGet200ResponsePaymentInformationIssuerInformation.
        This field contains the length of the BIN. 

        :return: The bin_length of this TssV2TransactionsGet200ResponsePaymentInformationIssuerInformation.
        :rtype: str
        """
        return self._bin_length

    @bin_length.setter
    def bin_length(self, bin_length):
        """
        Sets the bin_length of this TssV2TransactionsGet200ResponsePaymentInformationIssuerInformation.
        This field contains the length of the BIN. 

        :param bin_length: The bin_length of this TssV2TransactionsGet200ResponsePaymentInformationIssuerInformation.
        :type: str
        """

        self._bin_length = bin_length

    @property
    def phone_number(self):
        """
        Gets the phone_number of this TssV2TransactionsGet200ResponsePaymentInformationIssuerInformation.
        This field contains the customer service phone number for the issuer. 

        :return: The phone_number of this TssV2TransactionsGet200ResponsePaymentInformationIssuerInformation.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this TssV2TransactionsGet200ResponsePaymentInformationIssuerInformation.
        This field contains the customer service phone number for the issuer. 

        :param phone_number: The phone_number of this TssV2TransactionsGet200ResponsePaymentInformationIssuerInformation.
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
        if not isinstance(other, TssV2TransactionsGet200ResponsePaymentInformationIssuerInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
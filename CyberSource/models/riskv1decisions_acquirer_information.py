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


class Riskv1decisionsAcquirerInformation(object):
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
        'acquirer_bin': 'str',
        'country': 'str',
        'password': 'str',
        'merchant_id': 'str'
    }

    attribute_map = {
        'acquirer_bin': 'acquirerBin',
        'country': 'country',
        'password': 'password',
        'merchant_id': 'merchantId'
    }

    def __init__(self, acquirer_bin=None, country=None, password=None, merchant_id=None):
        """
        Riskv1decisionsAcquirerInformation - a model defined in Swagger
        """

        self._acquirer_bin = None
        self._country = None
        self._password = None
        self._merchant_id = None

        if acquirer_bin is not None:
          self.acquirer_bin = acquirer_bin
        if country is not None:
          self.country = country
        if password is not None:
          self.password = password
        if merchant_id is not None:
          self.merchant_id = merchant_id

    @property
    def acquirer_bin(self):
        """
        Gets the acquirer_bin of this Riskv1decisionsAcquirerInformation.
        Acquirer bank ID number that  corresponds to a certificate that Cybersource already has.This ID has this format. 4XXXXX for Visa and 5XXXXX for Mastercard. 

        :return: The acquirer_bin of this Riskv1decisionsAcquirerInformation.
        :rtype: str
        """
        return self._acquirer_bin

    @acquirer_bin.setter
    def acquirer_bin(self, acquirer_bin):
        """
        Sets the acquirer_bin of this Riskv1decisionsAcquirerInformation.
        Acquirer bank ID number that  corresponds to a certificate that Cybersource already has.This ID has this format. 4XXXXX for Visa and 5XXXXX for Mastercard. 

        :param acquirer_bin: The acquirer_bin of this Riskv1decisionsAcquirerInformation.
        :type: str
        """

        self._acquirer_bin = acquirer_bin

    @property
    def country(self):
        """
        Gets the country of this Riskv1decisionsAcquirerInformation.
        Issuers need to be aware of the Acquirer's Country Code when the Acquirer country differs from the Merchant country and the Acquirer is in the EEA (European Economic Area). 

        :return: The country of this Riskv1decisionsAcquirerInformation.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Riskv1decisionsAcquirerInformation.
        Issuers need to be aware of the Acquirer's Country Code when the Acquirer country differs from the Merchant country and the Acquirer is in the EEA (European Economic Area). 

        :param country: The country of this Riskv1decisionsAcquirerInformation.
        :type: str
        """

        self._country = country

    @property
    def password(self):
        """
        Gets the password of this Riskv1decisionsAcquirerInformation.
        Registered password for the Visa directory server. 

        :return: The password of this Riskv1decisionsAcquirerInformation.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this Riskv1decisionsAcquirerInformation.
        Registered password for the Visa directory server. 

        :param password: The password of this Riskv1decisionsAcquirerInformation.
        :type: str
        """

        self._password = password

    @property
    def merchant_id(self):
        """
        Gets the merchant_id of this Riskv1decisionsAcquirerInformation.
        Username for the visa directory server that is created when your acquirer sets up your account. This ID might be the same as your merchant ID. the username can be 15 or 23 characters. 

        :return: The merchant_id of this Riskv1decisionsAcquirerInformation.
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """
        Sets the merchant_id of this Riskv1decisionsAcquirerInformation.
        Username for the visa directory server that is created when your acquirer sets up your account. This ID might be the same as your merchant ID. the username can be 15 or 23 characters. 

        :param merchant_id: The merchant_id of this Riskv1decisionsAcquirerInformation.
        :type: str
        """

        self._merchant_id = merchant_id

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
        if not isinstance(other, Riskv1decisionsAcquirerInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

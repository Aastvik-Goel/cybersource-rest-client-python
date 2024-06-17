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


class Accountupdaterv1batchesIncludedTokens(object):
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
        'id': 'str',
        'expiration_month': 'str',
        'expiration_year': 'str'
    }

    attribute_map = {
        'id': 'id',
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear'
    }

    def __init__(self, id=None, expiration_month=None, expiration_year=None):
        """
        Accountupdaterv1batchesIncludedTokens - a model defined in Swagger
        """

        self._id = None
        self._expiration_month = None
        self._expiration_year = None

        self.id = id
        if expiration_month is not None:
          self.expiration_month = expiration_month
        if expiration_year is not None:
          self.expiration_year = expiration_year

    @property
    def id(self):
        """
        Gets the id of this Accountupdaterv1batchesIncludedTokens.

        :return: The id of this Accountupdaterv1batchesIncludedTokens.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Accountupdaterv1batchesIncludedTokens.

        :param id: The id of this Accountupdaterv1batchesIncludedTokens.
        :type: str
        """



        self._id = id

    @property
    def expiration_month(self):
        """
        Gets the expiration_month of this Accountupdaterv1batchesIncludedTokens.

        :return: The expiration_month of this Accountupdaterv1batchesIncludedTokens.
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """
        Sets the expiration_month of this Accountupdaterv1batchesIncludedTokens.

        :param expiration_month: The expiration_month of this Accountupdaterv1batchesIncludedTokens.
        :type: str
        """



        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """
        Gets the expiration_year of this Accountupdaterv1batchesIncludedTokens.

        :return: The expiration_year of this Accountupdaterv1batchesIncludedTokens.
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """
        Sets the expiration_year of this Accountupdaterv1batchesIncludedTokens.

        :param expiration_year: The expiration_year of this Accountupdaterv1batchesIncludedTokens.
        :type: str
        """



        self._expiration_year = expiration_year

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
        if not isinstance(other, Accountupdaterv1batchesIncludedTokens):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

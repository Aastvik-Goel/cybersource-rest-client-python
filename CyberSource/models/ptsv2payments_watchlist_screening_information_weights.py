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


class Ptsv2paymentsWatchlistScreeningInformationWeights(object):
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
        'address': 'str',
        'company': 'str',
        'name': 'str'
    }

    attribute_map = {
        'address': 'address',
        'company': 'company',
        'name': 'name'
    }

    def __init__(self, address=None, company=None, name=None):
        """
        Ptsv2paymentsWatchlistScreeningInformationWeights - a model defined in Swagger
        """

        self._address = None
        self._company = None
        self._name = None

        if address is not None:
          self.address = address
        if company is not None:
          self.company = company
        if name is not None:
          self.name = name

    @property
    def address(self):
        """
        Gets the address of this Ptsv2paymentsWatchlistScreeningInformationWeights.
        Degree of correlation between a customer's address and an entry in the DPL before a match occurs. This field can contain one of the following values: - exact: The address must be identical to the entry in the DPL. - high: (default) The address cannot differ significantly from the entry in the DPL. - medium: The address can differ slightly more from the entry in the DPL. - low: The address can differ significantly from the entry in the DPL. 

        :return: The address of this Ptsv2paymentsWatchlistScreeningInformationWeights.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Ptsv2paymentsWatchlistScreeningInformationWeights.
        Degree of correlation between a customer's address and an entry in the DPL before a match occurs. This field can contain one of the following values: - exact: The address must be identical to the entry in the DPL. - high: (default) The address cannot differ significantly from the entry in the DPL. - medium: The address can differ slightly more from the entry in the DPL. - low: The address can differ significantly from the entry in the DPL. 

        :param address: The address of this Ptsv2paymentsWatchlistScreeningInformationWeights.
        :type: str
        """



        self._address = address

    @property
    def company(self):
        """
        Gets the company of this Ptsv2paymentsWatchlistScreeningInformationWeights.
        Degree of correlation between a company address and an entry in the DPL before a match occurs. This field can contain one of the following values: - exact: The company name must be identical to the entry in the DPL. - high: (default) The company name cannot differ significantly from the entry in the DPL. - medium: The company name can differ slightly more from the entry in the DPL. - low: The company name can differ significantly from the entry in the DPL. 

        :return: The company of this Ptsv2paymentsWatchlistScreeningInformationWeights.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this Ptsv2paymentsWatchlistScreeningInformationWeights.
        Degree of correlation between a company address and an entry in the DPL before a match occurs. This field can contain one of the following values: - exact: The company name must be identical to the entry in the DPL. - high: (default) The company name cannot differ significantly from the entry in the DPL. - medium: The company name can differ slightly more from the entry in the DPL. - low: The company name can differ significantly from the entry in the DPL. 

        :param company: The company of this Ptsv2paymentsWatchlistScreeningInformationWeights.
        :type: str
        """



        self._company = company

    @property
    def name(self):
        """
        Gets the name of this Ptsv2paymentsWatchlistScreeningInformationWeights.
        Degree of correlation between a customer's name and an entry in the DPL before a match occurs. This field can contain one of the following values: - exact: The name must be identical to the entry in the DPL. - high: (default) The name cannot differ significantly from the entry in the DPL. - medium: The name can differ slightly more from the entry in the DPL. - low: The name can differ significantly the entry in the DPL. 

        :return: The name of this Ptsv2paymentsWatchlistScreeningInformationWeights.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Ptsv2paymentsWatchlistScreeningInformationWeights.
        Degree of correlation between a customer's name and an entry in the DPL before a match occurs. This field can contain one of the following values: - exact: The name must be identical to the entry in the DPL. - high: (default) The name cannot differ significantly from the entry in the DPL. - medium: The name can differ slightly more from the entry in the DPL. - low: The name can differ significantly the entry in the DPL. 

        :param name: The name of this Ptsv2paymentsWatchlistScreeningInformationWeights.
        :type: str
        """



        self._name = name

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
        if not isinstance(other, Ptsv2paymentsWatchlistScreeningInformationWeights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

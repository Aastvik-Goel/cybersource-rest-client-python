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


class DmConfigPortfolioControls(object):
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
        'hide_risk_menus': 'bool',
        'hide_risk_transaction_data': 'bool'
    }

    attribute_map = {
        'hide_risk_menus': 'hideRiskMenus',
        'hide_risk_transaction_data': 'hideRiskTransactionData'
    }

    def __init__(self, hide_risk_menus=None, hide_risk_transaction_data=None):
        """
        DmConfigPortfolioControls - a model defined in Swagger
        """

        self._hide_risk_menus = None
        self._hide_risk_transaction_data = None

        if hide_risk_menus is not None:
          self.hide_risk_menus = hide_risk_menus
        if hide_risk_transaction_data is not None:
          self.hide_risk_transaction_data = hide_risk_transaction_data

    @property
    def hide_risk_menus(self):
        """
        Gets the hide_risk_menus of this DmConfigPortfolioControls.

        :return: The hide_risk_menus of this DmConfigPortfolioControls.
        :rtype: bool
        """
        return self._hide_risk_menus

    @hide_risk_menus.setter
    def hide_risk_menus(self, hide_risk_menus):
        """
        Sets the hide_risk_menus of this DmConfigPortfolioControls.

        :param hide_risk_menus: The hide_risk_menus of this DmConfigPortfolioControls.
        :type: bool
        """



        self._hide_risk_menus = hide_risk_menus

    @property
    def hide_risk_transaction_data(self):
        """
        Gets the hide_risk_transaction_data of this DmConfigPortfolioControls.

        :return: The hide_risk_transaction_data of this DmConfigPortfolioControls.
        :rtype: bool
        """
        return self._hide_risk_transaction_data

    @hide_risk_transaction_data.setter
    def hide_risk_transaction_data(self, hide_risk_transaction_data):
        """
        Sets the hide_risk_transaction_data of this DmConfigPortfolioControls.

        :param hide_risk_transaction_data: The hide_risk_transaction_data of this DmConfigPortfolioControls.
        :type: bool
        """



        self._hide_risk_transaction_data = hide_risk_transaction_data

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
        if not isinstance(other, DmConfigPortfolioControls):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

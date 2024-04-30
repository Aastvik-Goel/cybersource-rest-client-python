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


class Ptsv2paymentsProcessorInformationAuthorizationOptions(object):
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
        'pan_return_indicator': 'str'
    }

    attribute_map = {
        'pan_return_indicator': 'panReturnIndicator'
    }

    def __init__(self, pan_return_indicator=None):
        """
        Ptsv2paymentsProcessorInformationAuthorizationOptions - a model defined in Swagger
        """

        self._pan_return_indicator = None

        if pan_return_indicator is not None:
          self.pan_return_indicator = pan_return_indicator

    @property
    def pan_return_indicator(self):
        """
        Gets the pan_return_indicator of this Ptsv2paymentsProcessorInformationAuthorizationOptions.
        #### Visa Platform Connect The field contains the PAN translation indicator for American Express Contactless Transaction. Valid value is   1- Expresspay Translation, PAN request 2- Expresspay Translation, PAN and Expiry date request 

        :return: The pan_return_indicator of this Ptsv2paymentsProcessorInformationAuthorizationOptions.
        :rtype: str
        """
        return self._pan_return_indicator

    @pan_return_indicator.setter
    def pan_return_indicator(self, pan_return_indicator):
        """
        Sets the pan_return_indicator of this Ptsv2paymentsProcessorInformationAuthorizationOptions.
        #### Visa Platform Connect The field contains the PAN translation indicator for American Express Contactless Transaction. Valid value is   1- Expresspay Translation, PAN request 2- Expresspay Translation, PAN and Expiry date request 

        :param pan_return_indicator: The pan_return_indicator of this Ptsv2paymentsProcessorInformationAuthorizationOptions.
        :type: str
        """

        self._pan_return_indicator = pan_return_indicator

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
        if not isinstance(other, Ptsv2paymentsProcessorInformationAuthorizationOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

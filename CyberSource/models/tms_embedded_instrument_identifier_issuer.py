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


class TmsEmbeddedInstrumentIdentifierIssuer(object):
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
        'payment_account_reference': 'str'
    }

    attribute_map = {
        'payment_account_reference': 'paymentAccountReference'
    }

    def __init__(self, payment_account_reference=None):
        """
        TmsEmbeddedInstrumentIdentifierIssuer - a model defined in Swagger
        """

        self._payment_account_reference = None

        if payment_account_reference is not None:
          self.payment_account_reference = payment_account_reference

    @property
    def payment_account_reference(self):
        """
        Gets the payment_account_reference of this TmsEmbeddedInstrumentIdentifierIssuer.
        This reference number serves as a link to the cardholder account and to all transactions for that account. 

        :return: The payment_account_reference of this TmsEmbeddedInstrumentIdentifierIssuer.
        :rtype: str
        """
        return self._payment_account_reference

    @payment_account_reference.setter
    def payment_account_reference(self, payment_account_reference):
        """
        Sets the payment_account_reference of this TmsEmbeddedInstrumentIdentifierIssuer.
        This reference number serves as a link to the cardholder account and to all transactions for that account. 

        :param payment_account_reference: The payment_account_reference of this TmsEmbeddedInstrumentIdentifierIssuer.
        :type: str
        """



        self._payment_account_reference = payment_account_reference

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
        if not isinstance(other, TmsEmbeddedInstrumentIdentifierIssuer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

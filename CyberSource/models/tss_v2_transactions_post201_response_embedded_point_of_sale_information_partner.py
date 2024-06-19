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


class TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformationPartner(object):
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
        'original_transaction_id': 'str'
    }

    attribute_map = {
        'original_transaction_id': 'originalTransactionId'
    }

    def __init__(self, original_transaction_id=None):
        """
        TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformationPartner - a model defined in Swagger
        """

        self._original_transaction_id = None

        if original_transaction_id is not None:
          self.original_transaction_id = original_transaction_id

    @property
    def original_transaction_id(self):
        """
        Gets the original_transaction_id of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformationPartner.
        Value that links the previous transaction to the current follow-on request. This value is assigned by the client software that is installed on the POS terminal, which makes it available to the terminal's software and to CyberSource. Therefore, you can use this value to reconcile transactions between CyberSource and the terminal's software.  CyberSource does not forward this value to the processor. Instead, the value is forwarded to the CyberSource reporting functionality.  This field is supported only on American Express Direct, FDC Nashville Global, and SIX. 

        :return: The original_transaction_id of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformationPartner.
        :rtype: str
        """
        return self._original_transaction_id

    @original_transaction_id.setter
    def original_transaction_id(self, original_transaction_id):
        """
        Sets the original_transaction_id of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformationPartner.
        Value that links the previous transaction to the current follow-on request. This value is assigned by the client software that is installed on the POS terminal, which makes it available to the terminal's software and to CyberSource. Therefore, you can use this value to reconcile transactions between CyberSource and the terminal's software.  CyberSource does not forward this value to the processor. Instead, the value is forwarded to the CyberSource reporting functionality.  This field is supported only on American Express Direct, FDC Nashville Global, and SIX. 

        :param original_transaction_id: The original_transaction_id of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformationPartner.
        :type: str
        """

        self._original_transaction_id = original_transaction_id

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
        if not isinstance(other, TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformationPartner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

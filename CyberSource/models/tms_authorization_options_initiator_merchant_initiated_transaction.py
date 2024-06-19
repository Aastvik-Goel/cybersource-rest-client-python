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


class TmsAuthorizationOptionsInitiatorMerchantInitiatedTransaction(object):
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
        'previous_transaction_id': 'str',
        'original_authorized_amount': 'str'
    }

    attribute_map = {
        'previous_transaction_id': 'previousTransactionId',
        'original_authorized_amount': 'originalAuthorizedAmount'
    }

    def __init__(self, previous_transaction_id=None, original_authorized_amount=None):
        """
        TmsAuthorizationOptionsInitiatorMerchantInitiatedTransaction - a model defined in Swagger
        """

        self._previous_transaction_id = None
        self._original_authorized_amount = None

        if previous_transaction_id is not None:
          self.previous_transaction_id = previous_transaction_id
        if original_authorized_amount is not None:
          self.original_authorized_amount = original_authorized_amount

    @property
    def previous_transaction_id(self):
        """
        Gets the previous_transaction_id of this TmsAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        Network transaction identifier that was returned in the payment response field _processorInformation.transactionID_ in the reply message for either the original merchant-initiated payment in the series or the previous merchant-initiated payment in the series. 

        :return: The previous_transaction_id of this TmsAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        :rtype: str
        """
        return self._previous_transaction_id

    @previous_transaction_id.setter
    def previous_transaction_id(self, previous_transaction_id):
        """
        Sets the previous_transaction_id of this TmsAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        Network transaction identifier that was returned in the payment response field _processorInformation.transactionID_ in the reply message for either the original merchant-initiated payment in the series or the previous merchant-initiated payment in the series. 

        :param previous_transaction_id: The previous_transaction_id of this TmsAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        :type: str
        """

        self._previous_transaction_id = previous_transaction_id

    @property
    def original_authorized_amount(self):
        """
        Gets the original_authorized_amount of this TmsAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        Amount of the original authorization. 

        :return: The original_authorized_amount of this TmsAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        :rtype: str
        """
        return self._original_authorized_amount

    @original_authorized_amount.setter
    def original_authorized_amount(self, original_authorized_amount):
        """
        Sets the original_authorized_amount of this TmsAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        Amount of the original authorization. 

        :param original_authorized_amount: The original_authorized_amount of this TmsAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        :type: str
        """

        self._original_authorized_amount = original_authorized_amount

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
        if not isinstance(other, TmsAuthorizationOptionsInitiatorMerchantInitiatedTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

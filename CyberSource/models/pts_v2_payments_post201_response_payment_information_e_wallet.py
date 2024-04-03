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


class PtsV2PaymentsPost201ResponsePaymentInformationEWallet(object):
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
        'funding_source': 'str',
        'account_id': 'str'
    }

    attribute_map = {
        'funding_source': 'fundingSource',
        'account_id': 'accountId'
    }

    def __init__(self, funding_source=None, account_id=None):
        """
        PtsV2PaymentsPost201ResponsePaymentInformationEWallet - a model defined in Swagger
        """

        self._funding_source = None
        self._account_id = None

        if funding_source is not None:
          self.funding_source = funding_source
        if account_id is not None:
          self.account_id = account_id

    @property
    def funding_source(self):
        """
        Gets the funding_source of this PtsV2PaymentsPost201ResponsePaymentInformationEWallet.
        Payment mode for the reference transaction. Possible values: - `INSTANT_TRANSFER` - `MANUAL_BANK_TRANSFER` - `DELAYED_TRANSFER` - `ECHECK` 

        :return: The funding_source of this PtsV2PaymentsPost201ResponsePaymentInformationEWallet.
        :rtype: str
        """
        return self._funding_source

    @funding_source.setter
    def funding_source(self, funding_source):
        """
        Sets the funding_source of this PtsV2PaymentsPost201ResponsePaymentInformationEWallet.
        Payment mode for the reference transaction. Possible values: - `INSTANT_TRANSFER` - `MANUAL_BANK_TRANSFER` - `DELAYED_TRANSFER` - `ECHECK` 

        :param funding_source: The funding_source of this PtsV2PaymentsPost201ResponsePaymentInformationEWallet.
        :type: str
        """

        self._funding_source = funding_source

    @property
    def account_id(self):
        """
        Gets the account_id of this PtsV2PaymentsPost201ResponsePaymentInformationEWallet.
        The ID of the customer, passed in the return_url field by PayPal after customer approval. 

        :return: The account_id of this PtsV2PaymentsPost201ResponsePaymentInformationEWallet.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this PtsV2PaymentsPost201ResponsePaymentInformationEWallet.
        The ID of the customer, passed in the return_url field by PayPal after customer approval. 

        :param account_id: The account_id of this PtsV2PaymentsPost201ResponsePaymentInformationEWallet.
        :type: str
        """

        self._account_id = account_id

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
        if not isinstance(other, PtsV2PaymentsPost201ResponsePaymentInformationEWallet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
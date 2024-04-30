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


class PtsV2PaymentsOrderPost201ResponseProcessorInformationSellerProtection(object):
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
        'eligibilty': 'str',
        'type': 'str'
    }

    attribute_map = {
        'eligibilty': 'eligibilty',
        'type': 'type'
    }

    def __init__(self, eligibilty=None, type=None):
        """
        PtsV2PaymentsOrderPost201ResponseProcessorInformationSellerProtection - a model defined in Swagger
        """

        self._eligibilty = None
        self._type = None

        if eligibilty is not None:
          self.eligibilty = eligibilty
        if type is not None:
          self.type = type

    @property
    def eligibilty(self):
        """
        Gets the eligibilty of this PtsV2PaymentsOrderPost201ResponseProcessorInformationSellerProtection.
        The level of seller protection in force for the transaction. Possible values: - `ELIGIBLE` - `PARTIALLY_ELIGIBLE` - `INELIGIBLE` 

        :return: The eligibilty of this PtsV2PaymentsOrderPost201ResponseProcessorInformationSellerProtection.
        :rtype: str
        """
        return self._eligibilty

    @eligibilty.setter
    def eligibilty(self, eligibilty):
        """
        Sets the eligibilty of this PtsV2PaymentsOrderPost201ResponseProcessorInformationSellerProtection.
        The level of seller protection in force for the transaction. Possible values: - `ELIGIBLE` - `PARTIALLY_ELIGIBLE` - `INELIGIBLE` 

        :param eligibilty: The eligibilty of this PtsV2PaymentsOrderPost201ResponseProcessorInformationSellerProtection.
        :type: str
        """

        self._eligibilty = eligibilty

    @property
    def type(self):
        """
        Gets the type of this PtsV2PaymentsOrderPost201ResponseProcessorInformationSellerProtection.
        The kind of seller protection in force for the transaction. This field is returned only when the protection eligibility is set to ELIGIBLE or PARTIALLY_ELIGIBLE. Possible values: - `ITEM_NOT_RECEIVED_ELIGIBLE: Sellers are protected against claims for items not received.` - `UNAUTHORIZED_PAYMENT_ELIGIBLE: Sellers are protected against claims for unauthorized payments.One or both values can be returned.` 

        :return: The type of this PtsV2PaymentsOrderPost201ResponseProcessorInformationSellerProtection.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PtsV2PaymentsOrderPost201ResponseProcessorInformationSellerProtection.
        The kind of seller protection in force for the transaction. This field is returned only when the protection eligibility is set to ELIGIBLE or PARTIALLY_ELIGIBLE. Possible values: - `ITEM_NOT_RECEIVED_ELIGIBLE: Sellers are protected against claims for items not received.` - `UNAUTHORIZED_PAYMENT_ELIGIBLE: Sellers are protected against claims for unauthorized payments.One or both values can be returned.` 

        :param type: The type of this PtsV2PaymentsOrderPost201ResponseProcessorInformationSellerProtection.
        :type: str
        """

        self._type = type

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
        if not isinstance(other, PtsV2PaymentsOrderPost201ResponseProcessorInformationSellerProtection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

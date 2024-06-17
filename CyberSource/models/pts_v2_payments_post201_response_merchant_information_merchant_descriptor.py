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


class PtsV2PaymentsPost201ResponseMerchantInformationMerchantDescriptor(object):
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
        'store_id': 'str',
        'store_name': 'str'
    }

    attribute_map = {
        'store_id': 'storeId',
        'store_name': 'storeName'
    }

    def __init__(self, store_id=None, store_name=None):
        """
        PtsV2PaymentsPost201ResponseMerchantInformationMerchantDescriptor - a model defined in Swagger
        """

        self._store_id = None
        self._store_name = None

        if store_id is not None:
          self.store_id = store_id
        if store_name is not None:
          self.store_name = store_name

    @property
    def store_id(self):
        """
        Gets the store_id of this PtsV2PaymentsPost201ResponseMerchantInformationMerchantDescriptor.
        The identifier of the store. 

        :return: The store_id of this PtsV2PaymentsPost201ResponseMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """
        Sets the store_id of this PtsV2PaymentsPost201ResponseMerchantInformationMerchantDescriptor.
        The identifier of the store. 

        :param store_id: The store_id of this PtsV2PaymentsPost201ResponseMerchantInformationMerchantDescriptor.
        :type: str
        """



        self._store_id = store_id

    @property
    def store_name(self):
        """
        Gets the store_name of this PtsV2PaymentsPost201ResponseMerchantInformationMerchantDescriptor.
        The name of the store. 

        :return: The store_name of this PtsV2PaymentsPost201ResponseMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        """
        Sets the store_name of this PtsV2PaymentsPost201ResponseMerchantInformationMerchantDescriptor.
        The name of the store. 

        :param store_name: The store_name of this PtsV2PaymentsPost201ResponseMerchantInformationMerchantDescriptor.
        :type: str
        """



        self._store_name = store_name

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
        if not isinstance(other, PtsV2PaymentsPost201ResponseMerchantInformationMerchantDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

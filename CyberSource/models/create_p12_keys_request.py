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


class CreateP12KeysRequest(object):
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
        'client_reference_information': 'Kmsv2keyssymClientReferenceInformation',
        'key_information': 'list[Kmsv2keysasymKeyInformation]'
    }

    attribute_map = {
        'client_reference_information': 'clientReferenceInformation',
        'key_information': 'keyInformation'
    }

    def __init__(self, client_reference_information=None, key_information=None):
        """
        CreateP12KeysRequest - a model defined in Swagger
        """

        self._client_reference_information = None
        self._key_information = None

        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if key_information is not None:
          self.key_information = key_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this CreateP12KeysRequest.

        :return: The client_reference_information of this CreateP12KeysRequest.
        :rtype: Kmsv2keyssymClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this CreateP12KeysRequest.

        :param client_reference_information: The client_reference_information of this CreateP12KeysRequest.
        :type: Kmsv2keyssymClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def key_information(self):
        """
        Gets the key_information of this CreateP12KeysRequest.

        :return: The key_information of this CreateP12KeysRequest.
        :rtype: list[Kmsv2keysasymKeyInformation]
        """
        return self._key_information

    @key_information.setter
    def key_information(self, key_information):
        """
        Sets the key_information of this CreateP12KeysRequest.

        :param key_information: The key_information of this CreateP12KeysRequest.
        :type: list[Kmsv2keysasymKeyInformation]
        """

        self._key_information = key_information

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
        if not isinstance(other, CreateP12KeysRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
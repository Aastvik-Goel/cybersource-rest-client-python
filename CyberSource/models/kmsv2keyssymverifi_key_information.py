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


class Kmsv2keyssymverifiKeyInformation(object):
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
        'organization_id': 'str',
        'reference_number': 'str',
        'digest_algorithm': 'str'
    }

    attribute_map = {
        'organization_id': 'organizationId',
        'reference_number': 'referenceNumber',
        'digest_algorithm': 'digestAlgorithm'
    }

    def __init__(self, organization_id=None, reference_number=None, digest_algorithm='HMACSHA2'):
        """
        Kmsv2keyssymverifiKeyInformation - a model defined in Swagger
        """

        self._organization_id = None
        self._reference_number = None
        self._digest_algorithm = None

        self.organization_id = organization_id
        if reference_number is not None:
          self.reference_number = reference_number
        if digest_algorithm is not None:
          self.digest_algorithm = digest_algorithm

    @property
    def organization_id(self):
        """
        Gets the organization_id of this Kmsv2keyssymverifiKeyInformation.
        Merchant Id 

        :return: The organization_id of this Kmsv2keyssymverifiKeyInformation.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this Kmsv2keyssymverifiKeyInformation.
        Merchant Id 

        :param organization_id: The organization_id of this Kmsv2keyssymverifiKeyInformation.
        :type: str
        """
        if organization_id is None:
            raise ValueError("Invalid value for `organization_id`, must not be `None`")

        self._organization_id = organization_id

    @property
    def reference_number(self):
        """
        Gets the reference_number of this Kmsv2keyssymverifiKeyInformation.
        Reference number is a unique identifier provided by the client along with the organization Id. This is an optional field provided solely for the client’s convenience. If client specifies value for this field in the request, it is expected to be available in the response. 

        :return: The reference_number of this Kmsv2keyssymverifiKeyInformation.
        :rtype: str
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """
        Sets the reference_number of this Kmsv2keyssymverifiKeyInformation.
        Reference number is a unique identifier provided by the client along with the organization Id. This is an optional field provided solely for the client’s convenience. If client specifies value for this field in the request, it is expected to be available in the response. 

        :param reference_number: The reference_number of this Kmsv2keyssymverifiKeyInformation.
        :type: str
        """

        self._reference_number = reference_number

    @property
    def digest_algorithm(self):
        """
        Gets the digest_algorithm of this Kmsv2keyssymverifiKeyInformation.
        Algorithm for message signature authentication 

        :return: The digest_algorithm of this Kmsv2keyssymverifiKeyInformation.
        :rtype: str
        """
        return self._digest_algorithm

    @digest_algorithm.setter
    def digest_algorithm(self, digest_algorithm):
        """
        Sets the digest_algorithm of this Kmsv2keyssymverifiKeyInformation.
        Algorithm for message signature authentication 

        :param digest_algorithm: The digest_algorithm of this Kmsv2keyssymverifiKeyInformation.
        :type: str
        """
        allowed_values = ["HMACSHA1", "HMACSHA2"]
        if digest_algorithm not in allowed_values:
            raise ValueError(
                "Invalid value for `digest_algorithm` ({0}), must be one of {1}"
                .format(digest_algorithm, allowed_values)
            )

        self._digest_algorithm = digest_algorithm

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
        if not isinstance(other, Kmsv2keyssymverifiKeyInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
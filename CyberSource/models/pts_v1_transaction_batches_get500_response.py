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


class PtsV1TransactionBatchesGet500Response(object):
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
        'error_information': 'PtsV1TransactionBatchesGet500ResponseErrorInformation',
        'submit_time_utc': 'str'
    }

    attribute_map = {
        'error_information': 'errorInformation',
        'submit_time_utc': 'submitTimeUtc'
    }

    def __init__(self, error_information=None, submit_time_utc=None):
        """
        PtsV1TransactionBatchesGet500Response - a model defined in Swagger
        """

        self._error_information = None
        self._submit_time_utc = None

        if error_information is not None:
          self.error_information = error_information
        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc

    @property
    def error_information(self):
        """
        Gets the error_information of this PtsV1TransactionBatchesGet500Response.

        :return: The error_information of this PtsV1TransactionBatchesGet500Response.
        :rtype: PtsV1TransactionBatchesGet500ResponseErrorInformation
        """
        return self._error_information

    @error_information.setter
    def error_information(self, error_information):
        """
        Sets the error_information of this PtsV1TransactionBatchesGet500Response.

        :param error_information: The error_information of this PtsV1TransactionBatchesGet500Response.
        :type: PtsV1TransactionBatchesGet500ResponseErrorInformation
        """

        self._error_information = error_information

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this PtsV1TransactionBatchesGet500Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :return: The submit_time_utc of this PtsV1TransactionBatchesGet500Response.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this PtsV1TransactionBatchesGet500Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :param submit_time_utc: The submit_time_utc of this PtsV1TransactionBatchesGet500Response.
        :type: str
        """

        self._submit_time_utc = submit_time_utc

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
        if not isinstance(other, PtsV1TransactionBatchesGet500Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

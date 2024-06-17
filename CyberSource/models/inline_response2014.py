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


class InlineResponse2014(object):
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
        'submit_time_utc': 'str',
        'status': 'str',
        'client_reference_information': 'Kmsegressv2keyssymClientReferenceInformation',
        'key_information': 'Kmsegressv2keysasymKeyInformation'
    }

    attribute_map = {
        'submit_time_utc': 'submitTimeUtc',
        'status': 'status',
        'client_reference_information': 'clientReferenceInformation',
        'key_information': 'keyInformation'
    }

    def __init__(self, submit_time_utc=None, status=None, client_reference_information=None, key_information=None):
        """
        InlineResponse2014 - a model defined in Swagger
        """

        self._submit_time_utc = None
        self._status = None
        self._client_reference_information = None
        self._key_information = None

        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if status is not None:
          self.status = status
        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if key_information is not None:
          self.key_information = key_information

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this InlineResponse2014.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` Example `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC. 

        :return: The submit_time_utc of this InlineResponse2014.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this InlineResponse2014.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` Example `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC. 

        :param submit_time_utc: The submit_time_utc of this InlineResponse2014.
        :type: str
        """



        self._submit_time_utc = submit_time_utc

    @property
    def status(self):
        """
        Gets the status of this InlineResponse2014.
        The status of the submitted transaction. Possible values:  - ACCEPTED 

        :return: The status of this InlineResponse2014.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InlineResponse2014.
        The status of the submitted transaction. Possible values:  - ACCEPTED 

        :param status: The status of this InlineResponse2014.
        :type: str
        """



        self._status = status

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this InlineResponse2014.

        :return: The client_reference_information of this InlineResponse2014.
        :rtype: Kmsegressv2keyssymClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this InlineResponse2014.

        :param client_reference_information: The client_reference_information of this InlineResponse2014.
        :type: Kmsegressv2keyssymClientReferenceInformation
        """



        self._client_reference_information = client_reference_information

    @property
    def key_information(self):
        """
        Gets the key_information of this InlineResponse2014.

        :return: The key_information of this InlineResponse2014.
        :rtype: Kmsegressv2keysasymKeyInformation
        """
        return self._key_information

    @key_information.setter
    def key_information(self, key_information):
        """
        Sets the key_information of this InlineResponse2014.

        :param key_information: The key_information of this InlineResponse2014.
        :type: Kmsegressv2keysasymKeyInformation
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
        if not isinstance(other, InlineResponse2014):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

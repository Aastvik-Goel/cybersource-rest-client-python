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


class InlineResponse20012EmbeddedTotals(object):
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
        'accepted_records': 'int',
        'rejected_records': 'int',
        'updated_records': 'int',
        'ca_responses': 'int',
        'ca_responses_omitted': 'int'
    }

    attribute_map = {
        'accepted_records': 'acceptedRecords',
        'rejected_records': 'rejectedRecords',
        'updated_records': 'updatedRecords',
        'ca_responses': 'caResponses',
        'ca_responses_omitted': 'caResponsesOmitted'
    }

    def __init__(self, accepted_records=None, rejected_records=None, updated_records=None, ca_responses=None, ca_responses_omitted=None):
        """
        InlineResponse20012EmbeddedTotals - a model defined in Swagger
        """

        self._accepted_records = None
        self._rejected_records = None
        self._updated_records = None
        self._ca_responses = None
        self._ca_responses_omitted = None

        if accepted_records is not None:
          self.accepted_records = accepted_records
        if rejected_records is not None:
          self.rejected_records = rejected_records
        if updated_records is not None:
          self.updated_records = updated_records
        if ca_responses is not None:
          self.ca_responses = ca_responses
        if ca_responses_omitted is not None:
          self.ca_responses_omitted = ca_responses_omitted

    @property
    def accepted_records(self):
        """
        Gets the accepted_records of this InlineResponse20012EmbeddedTotals.

        :return: The accepted_records of this InlineResponse20012EmbeddedTotals.
        :rtype: int
        """
        return self._accepted_records

    @accepted_records.setter
    def accepted_records(self, accepted_records):
        """
        Sets the accepted_records of this InlineResponse20012EmbeddedTotals.

        :param accepted_records: The accepted_records of this InlineResponse20012EmbeddedTotals.
        :type: int
        """

        self._accepted_records = accepted_records

    @property
    def rejected_records(self):
        """
        Gets the rejected_records of this InlineResponse20012EmbeddedTotals.

        :return: The rejected_records of this InlineResponse20012EmbeddedTotals.
        :rtype: int
        """
        return self._rejected_records

    @rejected_records.setter
    def rejected_records(self, rejected_records):
        """
        Sets the rejected_records of this InlineResponse20012EmbeddedTotals.

        :param rejected_records: The rejected_records of this InlineResponse20012EmbeddedTotals.
        :type: int
        """

        self._rejected_records = rejected_records

    @property
    def updated_records(self):
        """
        Gets the updated_records of this InlineResponse20012EmbeddedTotals.

        :return: The updated_records of this InlineResponse20012EmbeddedTotals.
        :rtype: int
        """
        return self._updated_records

    @updated_records.setter
    def updated_records(self, updated_records):
        """
        Sets the updated_records of this InlineResponse20012EmbeddedTotals.

        :param updated_records: The updated_records of this InlineResponse20012EmbeddedTotals.
        :type: int
        """

        self._updated_records = updated_records

    @property
    def ca_responses(self):
        """
        Gets the ca_responses of this InlineResponse20012EmbeddedTotals.

        :return: The ca_responses of this InlineResponse20012EmbeddedTotals.
        :rtype: int
        """
        return self._ca_responses

    @ca_responses.setter
    def ca_responses(self, ca_responses):
        """
        Sets the ca_responses of this InlineResponse20012EmbeddedTotals.

        :param ca_responses: The ca_responses of this InlineResponse20012EmbeddedTotals.
        :type: int
        """

        self._ca_responses = ca_responses

    @property
    def ca_responses_omitted(self):
        """
        Gets the ca_responses_omitted of this InlineResponse20012EmbeddedTotals.

        :return: The ca_responses_omitted of this InlineResponse20012EmbeddedTotals.
        :rtype: int
        """
        return self._ca_responses_omitted

    @ca_responses_omitted.setter
    def ca_responses_omitted(self, ca_responses_omitted):
        """
        Sets the ca_responses_omitted of this InlineResponse20012EmbeddedTotals.

        :param ca_responses_omitted: The ca_responses_omitted of this InlineResponse20012EmbeddedTotals.
        :type: int
        """

        self._ca_responses_omitted = ca_responses_omitted

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
        if not isinstance(other, InlineResponse20012EmbeddedTotals):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

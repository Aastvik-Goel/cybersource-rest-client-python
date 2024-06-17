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


class InlineResponseDefaultResponseStatus(object):
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
        'status': 'float',
        'reason': 'str',
        'message': 'str',
        'correlation_id': 'str',
        'details': 'list[InlineResponseDefaultResponseStatusDetails]'
    }

    attribute_map = {
        'status': 'status',
        'reason': 'reason',
        'message': 'message',
        'correlation_id': 'correlationId',
        'details': 'details'
    }

    def __init__(self, status=None, reason=None, message=None, correlation_id=None, details=None):
        """
        InlineResponseDefaultResponseStatus - a model defined in Swagger
        """

        self._status = None
        self._reason = None
        self._message = None
        self._correlation_id = None
        self._details = None

        if status is not None:
          self.status = status
        if reason is not None:
          self.reason = reason
        if message is not None:
          self.message = message
        if correlation_id is not None:
          self.correlation_id = correlation_id
        if details is not None:
          self.details = details

    @property
    def status(self):
        """
        Gets the status of this InlineResponseDefaultResponseStatus.
        HTTP Status code.

        :return: The status of this InlineResponseDefaultResponseStatus.
        :rtype: float
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InlineResponseDefaultResponseStatus.
        HTTP Status code.

        :param status: The status of this InlineResponseDefaultResponseStatus.
        :type: float
        """



        self._status = status

    @property
    def reason(self):
        """
        Gets the reason of this InlineResponseDefaultResponseStatus.
        Error Reason Code.

        :return: The reason of this InlineResponseDefaultResponseStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this InlineResponseDefaultResponseStatus.
        Error Reason Code.

        :param reason: The reason of this InlineResponseDefaultResponseStatus.
        :type: str
        """



        self._reason = reason

    @property
    def message(self):
        """
        Gets the message of this InlineResponseDefaultResponseStatus.
        Error Message.

        :return: The message of this InlineResponseDefaultResponseStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this InlineResponseDefaultResponseStatus.
        Error Message.

        :param message: The message of this InlineResponseDefaultResponseStatus.
        :type: str
        """



        self._message = message

    @property
    def correlation_id(self):
        """
        Gets the correlation_id of this InlineResponseDefaultResponseStatus.
        API correlation ID.

        :return: The correlation_id of this InlineResponseDefaultResponseStatus.
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """
        Sets the correlation_id of this InlineResponseDefaultResponseStatus.
        API correlation ID.

        :param correlation_id: The correlation_id of this InlineResponseDefaultResponseStatus.
        :type: str
        """



        self._correlation_id = correlation_id

    @property
    def details(self):
        """
        Gets the details of this InlineResponseDefaultResponseStatus.

        :return: The details of this InlineResponseDefaultResponseStatus.
        :rtype: list[InlineResponseDefaultResponseStatusDetails]
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this InlineResponseDefaultResponseStatus.

        :param details: The details of this InlineResponseDefaultResponseStatus.
        :type: list[InlineResponseDefaultResponseStatusDetails]
        """



        self._details = details

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
        if not isinstance(other, InlineResponseDefaultResponseStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

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


class InlineResponse4003(object):
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
        'correlation_id': 'str',
        'details': 'list[InlineResponse4003Details]',
        'information_link': 'str',
        'message': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'correlation_id': 'correlationId',
        'details': 'details',
        'information_link': 'informationLink',
        'message': 'message',
        'reason': 'reason'
    }

    def __init__(self, correlation_id=None, details=None, information_link=None, message=None, reason=None):
        """
        InlineResponse4003 - a model defined in Swagger
        """

        self._correlation_id = None
        self._details = None
        self._information_link = None
        self._message = None
        self._reason = None

        if correlation_id is not None:
          self.correlation_id = correlation_id
        if details is not None:
          self.details = details
        if information_link is not None:
          self.information_link = information_link
        self.message = message
        self.reason = reason

    @property
    def correlation_id(self):
        """
        Gets the correlation_id of this InlineResponse4003.

        :return: The correlation_id of this InlineResponse4003.
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """
        Sets the correlation_id of this InlineResponse4003.

        :param correlation_id: The correlation_id of this InlineResponse4003.
        :type: str
        """

        self._correlation_id = correlation_id

    @property
    def details(self):
        """
        Gets the details of this InlineResponse4003.

        :return: The details of this InlineResponse4003.
        :rtype: list[InlineResponse4003Details]
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this InlineResponse4003.

        :param details: The details of this InlineResponse4003.
        :type: list[InlineResponse4003Details]
        """

        self._details = details

    @property
    def information_link(self):
        """
        Gets the information_link of this InlineResponse4003.

        :return: The information_link of this InlineResponse4003.
        :rtype: str
        """
        return self._information_link

    @information_link.setter
    def information_link(self, information_link):
        """
        Sets the information_link of this InlineResponse4003.

        :param information_link: The information_link of this InlineResponse4003.
        :type: str
        """

        self._information_link = information_link

    @property
    def message(self):
        """
        Gets the message of this InlineResponse4003.

        :return: The message of this InlineResponse4003.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this InlineResponse4003.

        :param message: The message of this InlineResponse4003.
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

    @property
    def reason(self):
        """
        Gets the reason of this InlineResponse4003.

        :return: The reason of this InlineResponse4003.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this InlineResponse4003.

        :param reason: The reason of this InlineResponse4003.
        :type: str
        """
        if reason is None:
            raise ValueError("Invalid value for `reason`, must not be `None`")
        allowed_values = ["INVALID_APIKEY", "INVALID_SHIPPING_INPUT_PARAMS", "CAPTURE_CONTEXT_INVALID", "CAPTURE_CONTEXT_EXPIRED", "SDK_XHR_ERROR", "UNIFIEDPAYMENTS_VALIDATION_PARAMS", "UNIFIEDPAYMENTS_VALIDATION_FIELDS", "UNIFIEDPAYMENT_PAYMENT_PARAMITERS", "CREATE_TOKEN_TIMEOUT", "CREATE_TOKEN_XHR_ERROR", "SHOW_LOAD_CONTAINER_SELECTOR", "SHOW_LOAD_INVALID_CONTAINER", "SHOW_TOKEN_TIMEOUT", "SHOW_TOKEN_XHR_ERROR", "SHOW_PAYMENT_TIMEOUT"]
        if reason not in allowed_values:
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"
                .format(reason, allowed_values)
            )

        self._reason = reason

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
        if not isinstance(other, InlineResponse4003):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

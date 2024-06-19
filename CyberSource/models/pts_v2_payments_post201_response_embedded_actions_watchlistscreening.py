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


class PtsV2PaymentsPost201ResponseEmbeddedActionsWATCHLISTSCREENING(object):
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
        'status': 'str',
        'reason': 'str',
        'message': 'str'
    }

    attribute_map = {
        'status': 'status',
        'reason': 'reason',
        'message': 'message'
    }

    def __init__(self, status=None, reason=None, message=None):
        """
        PtsV2PaymentsPost201ResponseEmbeddedActionsWATCHLISTSCREENING - a model defined in Swagger
        """

        self._status = None
        self._reason = None
        self._message = None

        if status is not None:
          self.status = status
        if reason is not None:
          self.reason = reason
        if message is not None:
          self.message = message

    @property
    def status(self):
        """
        Gets the status of this PtsV2PaymentsPost201ResponseEmbeddedActionsWATCHLISTSCREENING.
        The status for the call can be: - COMPLETED - INVALID_REQUEST - DECLINED 

        :return: The status of this PtsV2PaymentsPost201ResponseEmbeddedActionsWATCHLISTSCREENING.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PtsV2PaymentsPost201ResponseEmbeddedActionsWATCHLISTSCREENING.
        The status for the call can be: - COMPLETED - INVALID_REQUEST - DECLINED 

        :param status: The status of this PtsV2PaymentsPost201ResponseEmbeddedActionsWATCHLISTSCREENING.
        :type: str
        """

        self._status = status

    @property
    def reason(self):
        """
        Gets the reason of this PtsV2PaymentsPost201ResponseEmbeddedActionsWATCHLISTSCREENING.
        The reason of the status. Value can be   - `CUSTOMER_WATCHLIST_MATCH`   - `ADDRESS_COUNTRY_WATCHLIST_MATCH`   - `EMAIL_COUNTRY_WATCHLIST_MATCH`   - `IP_COUNTRY_WATCHLIST_MATCH`   - `INVALID_MERCHANT_CONFIGURATION` 

        :return: The reason of this PtsV2PaymentsPost201ResponseEmbeddedActionsWATCHLISTSCREENING.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this PtsV2PaymentsPost201ResponseEmbeddedActionsWATCHLISTSCREENING.
        The reason of the status. Value can be   - `CUSTOMER_WATCHLIST_MATCH`   - `ADDRESS_COUNTRY_WATCHLIST_MATCH`   - `EMAIL_COUNTRY_WATCHLIST_MATCH`   - `IP_COUNTRY_WATCHLIST_MATCH`   - `INVALID_MERCHANT_CONFIGURATION` 

        :param reason: The reason of this PtsV2PaymentsPost201ResponseEmbeddedActionsWATCHLISTSCREENING.
        :type: str
        """

        self._reason = reason

    @property
    def message(self):
        """
        Gets the message of this PtsV2PaymentsPost201ResponseEmbeddedActionsWATCHLISTSCREENING.
        The message describing the reason of the status. Value can be   - The customer matched the Denied Parties List   - The Export bill_country/ship_country  match   - Export email_country match   - Export hostname_country/ip_country match 

        :return: The message of this PtsV2PaymentsPost201ResponseEmbeddedActionsWATCHLISTSCREENING.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this PtsV2PaymentsPost201ResponseEmbeddedActionsWATCHLISTSCREENING.
        The message describing the reason of the status. Value can be   - The customer matched the Denied Parties List   - The Export bill_country/ship_country  match   - Export email_country match   - Export hostname_country/ip_country match 

        :param message: The message of this PtsV2PaymentsPost201ResponseEmbeddedActionsWATCHLISTSCREENING.
        :type: str
        """

        self._message = message

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
        if not isinstance(other, PtsV2PaymentsPost201ResponseEmbeddedActionsWATCHLISTSCREENING):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

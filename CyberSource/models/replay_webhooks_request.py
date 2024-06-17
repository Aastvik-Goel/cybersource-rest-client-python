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


class ReplayWebhooksRequest(object):
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
        'by_transaction_trace_identifiers': 'list[str]',
        'by_delivery_status': 'Nrtfv1webhookswebhookIdreplaysByDeliveryStatus'
    }

    attribute_map = {
        'by_transaction_trace_identifiers': 'byTransactionTraceIdentifiers',
        'by_delivery_status': 'byDeliveryStatus'
    }

    def __init__(self, by_transaction_trace_identifiers=None, by_delivery_status=None):
        """
        ReplayWebhooksRequest - a model defined in Swagger
        """

        self._by_transaction_trace_identifiers = None
        self._by_delivery_status = None

        if by_transaction_trace_identifiers is not None:
          self.by_transaction_trace_identifiers = by_transaction_trace_identifiers
        if by_delivery_status is not None:
          self.by_delivery_status = by_delivery_status

    @property
    def by_transaction_trace_identifiers(self):
        """
        Gets the by_transaction_trace_identifiers of this ReplayWebhooksRequest.

        :return: The by_transaction_trace_identifiers of this ReplayWebhooksRequest.
        :rtype: list[str]
        """
        return self._by_transaction_trace_identifiers

    @by_transaction_trace_identifiers.setter
    def by_transaction_trace_identifiers(self, by_transaction_trace_identifiers):
        """
        Sets the by_transaction_trace_identifiers of this ReplayWebhooksRequest.

        :param by_transaction_trace_identifiers: The by_transaction_trace_identifiers of this ReplayWebhooksRequest.
        :type: list[str]
        """



        self._by_transaction_trace_identifiers = by_transaction_trace_identifiers

    @property
    def by_delivery_status(self):
        """
        Gets the by_delivery_status of this ReplayWebhooksRequest.

        :return: The by_delivery_status of this ReplayWebhooksRequest.
        :rtype: Nrtfv1webhookswebhookIdreplaysByDeliveryStatus
        """
        return self._by_delivery_status

    @by_delivery_status.setter
    def by_delivery_status(self, by_delivery_status):
        """
        Sets the by_delivery_status of this ReplayWebhooksRequest.

        :param by_delivery_status: The by_delivery_status of this ReplayWebhooksRequest.
        :type: Nrtfv1webhookswebhookIdreplaysByDeliveryStatus
        """



        self._by_delivery_status = by_delivery_status

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
        if not isinstance(other, ReplayWebhooksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

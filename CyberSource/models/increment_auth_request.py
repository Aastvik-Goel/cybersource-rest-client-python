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


class IncrementAuthRequest(object):
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
        'client_reference_information': 'Ptsv2paymentsidClientReferenceInformation',
        'processing_information': 'Ptsv2paymentsidProcessingInformation',
        'order_information': 'Ptsv2paymentsidOrderInformation',
        'merchant_information': 'Ptsv2paymentsidMerchantInformation',
        'travel_information': 'Ptsv2paymentsidTravelInformation'
    }

    attribute_map = {
        'client_reference_information': 'clientReferenceInformation',
        'processing_information': 'processingInformation',
        'order_information': 'orderInformation',
        'merchant_information': 'merchantInformation',
        'travel_information': 'travelInformation'
    }

    def __init__(self, client_reference_information=None, processing_information=None, order_information=None, merchant_information=None, travel_information=None):
        """
        IncrementAuthRequest - a model defined in Swagger
        """

        self._client_reference_information = None
        self._processing_information = None
        self._order_information = None
        self._merchant_information = None
        self._travel_information = None

        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if processing_information is not None:
          self.processing_information = processing_information
        if order_information is not None:
          self.order_information = order_information
        if merchant_information is not None:
          self.merchant_information = merchant_information
        if travel_information is not None:
          self.travel_information = travel_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this IncrementAuthRequest.

        :return: The client_reference_information of this IncrementAuthRequest.
        :rtype: Ptsv2paymentsidClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this IncrementAuthRequest.

        :param client_reference_information: The client_reference_information of this IncrementAuthRequest.
        :type: Ptsv2paymentsidClientReferenceInformation
        """



        self._client_reference_information = client_reference_information

    @property
    def processing_information(self):
        """
        Gets the processing_information of this IncrementAuthRequest.

        :return: The processing_information of this IncrementAuthRequest.
        :rtype: Ptsv2paymentsidProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this IncrementAuthRequest.

        :param processing_information: The processing_information of this IncrementAuthRequest.
        :type: Ptsv2paymentsidProcessingInformation
        """



        self._processing_information = processing_information

    @property
    def order_information(self):
        """
        Gets the order_information of this IncrementAuthRequest.

        :return: The order_information of this IncrementAuthRequest.
        :rtype: Ptsv2paymentsidOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this IncrementAuthRequest.

        :param order_information: The order_information of this IncrementAuthRequest.
        :type: Ptsv2paymentsidOrderInformation
        """



        self._order_information = order_information

    @property
    def merchant_information(self):
        """
        Gets the merchant_information of this IncrementAuthRequest.

        :return: The merchant_information of this IncrementAuthRequest.
        :rtype: Ptsv2paymentsidMerchantInformation
        """
        return self._merchant_information

    @merchant_information.setter
    def merchant_information(self, merchant_information):
        """
        Sets the merchant_information of this IncrementAuthRequest.

        :param merchant_information: The merchant_information of this IncrementAuthRequest.
        :type: Ptsv2paymentsidMerchantInformation
        """



        self._merchant_information = merchant_information

    @property
    def travel_information(self):
        """
        Gets the travel_information of this IncrementAuthRequest.

        :return: The travel_information of this IncrementAuthRequest.
        :rtype: Ptsv2paymentsidTravelInformation
        """
        return self._travel_information

    @travel_information.setter
    def travel_information(self, travel_information):
        """
        Sets the travel_information of this IncrementAuthRequest.

        :param travel_information: The travel_information of this IncrementAuthRequest.
        :type: Ptsv2paymentsidTravelInformation
        """



        self._travel_information = travel_information

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
        if not isinstance(other, IncrementAuthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

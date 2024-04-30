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


class AuthReversalRequest(object):
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
        'client_reference_information': 'Ptsv2paymentsidreversalsClientReferenceInformation',
        'reversal_information': 'Ptsv2paymentsidreversalsReversalInformation',
        'processing_information': 'Ptsv2paymentsidreversalsProcessingInformation',
        'order_information': 'Ptsv2paymentsidreversalsOrderInformation',
        'point_of_sale_information': 'Ptsv2paymentsidreversalsPointOfSaleInformation',
        'payment_information': 'Ptsv2paymentsidreversalsPaymentInformation',
        'processor_information': 'Ptsv2paymentsProcessorInformationReversal'
    }

    attribute_map = {
        'client_reference_information': 'clientReferenceInformation',
        'reversal_information': 'reversalInformation',
        'processing_information': 'processingInformation',
        'order_information': 'orderInformation',
        'point_of_sale_information': 'pointOfSaleInformation',
        'payment_information': 'paymentInformation',
        'processor_information': 'processorInformation'
    }

    def __init__(self, client_reference_information=None, reversal_information=None, processing_information=None, order_information=None, point_of_sale_information=None, payment_information=None, processor_information=None):
        """
        AuthReversalRequest - a model defined in Swagger
        """

        self._client_reference_information = None
        self._reversal_information = None
        self._processing_information = None
        self._order_information = None
        self._point_of_sale_information = None
        self._payment_information = None
        self._processor_information = None

        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if reversal_information is not None:
          self.reversal_information = reversal_information
        if processing_information is not None:
          self.processing_information = processing_information
        if order_information is not None:
          self.order_information = order_information
        if point_of_sale_information is not None:
          self.point_of_sale_information = point_of_sale_information
        if payment_information is not None:
          self.payment_information = payment_information
        if processor_information is not None:
          self.processor_information = processor_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this AuthReversalRequest.

        :return: The client_reference_information of this AuthReversalRequest.
        :rtype: Ptsv2paymentsidreversalsClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this AuthReversalRequest.

        :param client_reference_information: The client_reference_information of this AuthReversalRequest.
        :type: Ptsv2paymentsidreversalsClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def reversal_information(self):
        """
        Gets the reversal_information of this AuthReversalRequest.

        :return: The reversal_information of this AuthReversalRequest.
        :rtype: Ptsv2paymentsidreversalsReversalInformation
        """
        return self._reversal_information

    @reversal_information.setter
    def reversal_information(self, reversal_information):
        """
        Sets the reversal_information of this AuthReversalRequest.

        :param reversal_information: The reversal_information of this AuthReversalRequest.
        :type: Ptsv2paymentsidreversalsReversalInformation
        """

        self._reversal_information = reversal_information

    @property
    def processing_information(self):
        """
        Gets the processing_information of this AuthReversalRequest.

        :return: The processing_information of this AuthReversalRequest.
        :rtype: Ptsv2paymentsidreversalsProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this AuthReversalRequest.

        :param processing_information: The processing_information of this AuthReversalRequest.
        :type: Ptsv2paymentsidreversalsProcessingInformation
        """

        self._processing_information = processing_information

    @property
    def order_information(self):
        """
        Gets the order_information of this AuthReversalRequest.

        :return: The order_information of this AuthReversalRequest.
        :rtype: Ptsv2paymentsidreversalsOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this AuthReversalRequest.

        :param order_information: The order_information of this AuthReversalRequest.
        :type: Ptsv2paymentsidreversalsOrderInformation
        """

        self._order_information = order_information

    @property
    def point_of_sale_information(self):
        """
        Gets the point_of_sale_information of this AuthReversalRequest.

        :return: The point_of_sale_information of this AuthReversalRequest.
        :rtype: Ptsv2paymentsidreversalsPointOfSaleInformation
        """
        return self._point_of_sale_information

    @point_of_sale_information.setter
    def point_of_sale_information(self, point_of_sale_information):
        """
        Sets the point_of_sale_information of this AuthReversalRequest.

        :param point_of_sale_information: The point_of_sale_information of this AuthReversalRequest.
        :type: Ptsv2paymentsidreversalsPointOfSaleInformation
        """

        self._point_of_sale_information = point_of_sale_information

    @property
    def payment_information(self):
        """
        Gets the payment_information of this AuthReversalRequest.

        :return: The payment_information of this AuthReversalRequest.
        :rtype: Ptsv2paymentsidreversalsPaymentInformation
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """
        Sets the payment_information of this AuthReversalRequest.

        :param payment_information: The payment_information of this AuthReversalRequest.
        :type: Ptsv2paymentsidreversalsPaymentInformation
        """

        self._payment_information = payment_information

    @property
    def processor_information(self):
        """
        Gets the processor_information of this AuthReversalRequest.

        :return: The processor_information of this AuthReversalRequest.
        :rtype: Ptsv2paymentsProcessorInformationReversal
        """
        return self._processor_information

    @processor_information.setter
    def processor_information(self, processor_information):
        """
        Sets the processor_information of this AuthReversalRequest.

        :param processor_information: The processor_information of this AuthReversalRequest.
        :type: Ptsv2paymentsProcessorInformationReversal
        """

        self._processor_information = processor_information

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
        if not isinstance(other, AuthReversalRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

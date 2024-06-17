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


class VoidPaymentRequest(object):
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
        'payment_information': 'Ptsv2paymentsidvoidsPaymentInformation',
        'order_information': 'Ptsv2paymentsidvoidsOrderInformation',
        'agreement_information': 'Ptsv2paymentsidvoidsAgreementInformation',
        'merchant_information': 'Ptsv2paymentsidvoidsMerchantInformation',
        'processing_information': 'Ptsv2paymentsidvoidsProcessingInformation'
    }

    attribute_map = {
        'client_reference_information': 'clientReferenceInformation',
        'payment_information': 'paymentInformation',
        'order_information': 'orderInformation',
        'agreement_information': 'agreementInformation',
        'merchant_information': 'merchantInformation',
        'processing_information': 'processingInformation'
    }

    def __init__(self, client_reference_information=None, payment_information=None, order_information=None, agreement_information=None, merchant_information=None, processing_information=None):
        """
        VoidPaymentRequest - a model defined in Swagger
        """

        self._client_reference_information = None
        self._payment_information = None
        self._order_information = None
        self._agreement_information = None
        self._merchant_information = None
        self._processing_information = None

        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if payment_information is not None:
          self.payment_information = payment_information
        if order_information is not None:
          self.order_information = order_information
        if agreement_information is not None:
          self.agreement_information = agreement_information
        if merchant_information is not None:
          self.merchant_information = merchant_information
        if processing_information is not None:
          self.processing_information = processing_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this VoidPaymentRequest.

        :return: The client_reference_information of this VoidPaymentRequest.
        :rtype: Ptsv2paymentsidreversalsClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this VoidPaymentRequest.

        :param client_reference_information: The client_reference_information of this VoidPaymentRequest.
        :type: Ptsv2paymentsidreversalsClientReferenceInformation
        """



        self._client_reference_information = client_reference_information

    @property
    def payment_information(self):
        """
        Gets the payment_information of this VoidPaymentRequest.

        :return: The payment_information of this VoidPaymentRequest.
        :rtype: Ptsv2paymentsidvoidsPaymentInformation
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """
        Sets the payment_information of this VoidPaymentRequest.

        :param payment_information: The payment_information of this VoidPaymentRequest.
        :type: Ptsv2paymentsidvoidsPaymentInformation
        """



        self._payment_information = payment_information

    @property
    def order_information(self):
        """
        Gets the order_information of this VoidPaymentRequest.

        :return: The order_information of this VoidPaymentRequest.
        :rtype: Ptsv2paymentsidvoidsOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this VoidPaymentRequest.

        :param order_information: The order_information of this VoidPaymentRequest.
        :type: Ptsv2paymentsidvoidsOrderInformation
        """



        self._order_information = order_information

    @property
    def agreement_information(self):
        """
        Gets the agreement_information of this VoidPaymentRequest.

        :return: The agreement_information of this VoidPaymentRequest.
        :rtype: Ptsv2paymentsidvoidsAgreementInformation
        """
        return self._agreement_information

    @agreement_information.setter
    def agreement_information(self, agreement_information):
        """
        Sets the agreement_information of this VoidPaymentRequest.

        :param agreement_information: The agreement_information of this VoidPaymentRequest.
        :type: Ptsv2paymentsidvoidsAgreementInformation
        """



        self._agreement_information = agreement_information

    @property
    def merchant_information(self):
        """
        Gets the merchant_information of this VoidPaymentRequest.

        :return: The merchant_information of this VoidPaymentRequest.
        :rtype: Ptsv2paymentsidvoidsMerchantInformation
        """
        return self._merchant_information

    @merchant_information.setter
    def merchant_information(self, merchant_information):
        """
        Sets the merchant_information of this VoidPaymentRequest.

        :param merchant_information: The merchant_information of this VoidPaymentRequest.
        :type: Ptsv2paymentsidvoidsMerchantInformation
        """



        self._merchant_information = merchant_information

    @property
    def processing_information(self):
        """
        Gets the processing_information of this VoidPaymentRequest.

        :return: The processing_information of this VoidPaymentRequest.
        :rtype: Ptsv2paymentsidvoidsProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this VoidPaymentRequest.

        :param processing_information: The processing_information of this VoidPaymentRequest.
        :type: Ptsv2paymentsidvoidsProcessingInformation
        """



        self._processing_information = processing_information

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
        if not isinstance(other, VoidPaymentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

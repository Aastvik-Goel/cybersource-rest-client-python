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


class IntimateBillingAgreement(object):
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
        'client_reference_information': 'Ptsv2paymentsClientReferenceInformation',
        'installment_information': 'Ptsv2billingagreementsInstallmentInformation',
        'merchant_information': 'Ptsv2billingagreementsMerchantInformation',
        'order_information': 'Ptsv2billingagreementsOrderInformation',
        'payment_information': 'Ptsv2billingagreementsPaymentInformation'
    }

    attribute_map = {
        'client_reference_information': 'clientReferenceInformation',
        'installment_information': 'installmentInformation',
        'merchant_information': 'merchantInformation',
        'order_information': 'orderInformation',
        'payment_information': 'paymentInformation'
    }

    def __init__(self, client_reference_information=None, installment_information=None, merchant_information=None, order_information=None, payment_information=None):
        """
        IntimateBillingAgreement - a model defined in Swagger
        """

        self._client_reference_information = None
        self._installment_information = None
        self._merchant_information = None
        self._order_information = None
        self._payment_information = None

        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if installment_information is not None:
          self.installment_information = installment_information
        if merchant_information is not None:
          self.merchant_information = merchant_information
        if order_information is not None:
          self.order_information = order_information
        if payment_information is not None:
          self.payment_information = payment_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this IntimateBillingAgreement.

        :return: The client_reference_information of this IntimateBillingAgreement.
        :rtype: Ptsv2paymentsClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this IntimateBillingAgreement.

        :param client_reference_information: The client_reference_information of this IntimateBillingAgreement.
        :type: Ptsv2paymentsClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def installment_information(self):
        """
        Gets the installment_information of this IntimateBillingAgreement.

        :return: The installment_information of this IntimateBillingAgreement.
        :rtype: Ptsv2billingagreementsInstallmentInformation
        """
        return self._installment_information

    @installment_information.setter
    def installment_information(self, installment_information):
        """
        Sets the installment_information of this IntimateBillingAgreement.

        :param installment_information: The installment_information of this IntimateBillingAgreement.
        :type: Ptsv2billingagreementsInstallmentInformation
        """

        self._installment_information = installment_information

    @property
    def merchant_information(self):
        """
        Gets the merchant_information of this IntimateBillingAgreement.

        :return: The merchant_information of this IntimateBillingAgreement.
        :rtype: Ptsv2billingagreementsMerchantInformation
        """
        return self._merchant_information

    @merchant_information.setter
    def merchant_information(self, merchant_information):
        """
        Sets the merchant_information of this IntimateBillingAgreement.

        :param merchant_information: The merchant_information of this IntimateBillingAgreement.
        :type: Ptsv2billingagreementsMerchantInformation
        """

        self._merchant_information = merchant_information

    @property
    def order_information(self):
        """
        Gets the order_information of this IntimateBillingAgreement.

        :return: The order_information of this IntimateBillingAgreement.
        :rtype: Ptsv2billingagreementsOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this IntimateBillingAgreement.

        :param order_information: The order_information of this IntimateBillingAgreement.
        :type: Ptsv2billingagreementsOrderInformation
        """

        self._order_information = order_information

    @property
    def payment_information(self):
        """
        Gets the payment_information of this IntimateBillingAgreement.

        :return: The payment_information of this IntimateBillingAgreement.
        :rtype: Ptsv2billingagreementsPaymentInformation
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """
        Sets the payment_information of this IntimateBillingAgreement.

        :param payment_information: The payment_information of this IntimateBillingAgreement.
        :type: Ptsv2billingagreementsPaymentInformation
        """

        self._payment_information = payment_information

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
        if not isinstance(other, IntimateBillingAgreement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

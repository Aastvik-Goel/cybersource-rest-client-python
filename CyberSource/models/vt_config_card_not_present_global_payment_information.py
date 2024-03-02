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


class VTConfigCardNotPresentGlobalPaymentInformation(object):
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
        'basic_information': 'VTConfigCardNotPresentGlobalPaymentInformationBasicInformation',
        'payment_information': 'VTConfigCardNotPresentGlobalPaymentInformationPaymentInformation',
        'merchant_defined_data_fields': 'VTConfigCardNotPresentGlobalPaymentInformationMerchantDefinedDataFields'
    }

    attribute_map = {
        'basic_information': 'basicInformation',
        'payment_information': 'paymentInformation',
        'merchant_defined_data_fields': 'merchantDefinedDataFields'
    }

    def __init__(self, basic_information=None, payment_information=None, merchant_defined_data_fields=None):
        """
        VTConfigCardNotPresentGlobalPaymentInformation - a model defined in Swagger
        """

        self._basic_information = None
        self._payment_information = None
        self._merchant_defined_data_fields = None

        if basic_information is not None:
          self.basic_information = basic_information
        if payment_information is not None:
          self.payment_information = payment_information
        if merchant_defined_data_fields is not None:
          self.merchant_defined_data_fields = merchant_defined_data_fields

    @property
    def basic_information(self):
        """
        Gets the basic_information of this VTConfigCardNotPresentGlobalPaymentInformation.

        :return: The basic_information of this VTConfigCardNotPresentGlobalPaymentInformation.
        :rtype: VTConfigCardNotPresentGlobalPaymentInformationBasicInformation
        """
        return self._basic_information

    @basic_information.setter
    def basic_information(self, basic_information):
        """
        Sets the basic_information of this VTConfigCardNotPresentGlobalPaymentInformation.

        :param basic_information: The basic_information of this VTConfigCardNotPresentGlobalPaymentInformation.
        :type: VTConfigCardNotPresentGlobalPaymentInformationBasicInformation
        """

        self._basic_information = basic_information

    @property
    def payment_information(self):
        """
        Gets the payment_information of this VTConfigCardNotPresentGlobalPaymentInformation.

        :return: The payment_information of this VTConfigCardNotPresentGlobalPaymentInformation.
        :rtype: VTConfigCardNotPresentGlobalPaymentInformationPaymentInformation
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """
        Sets the payment_information of this VTConfigCardNotPresentGlobalPaymentInformation.

        :param payment_information: The payment_information of this VTConfigCardNotPresentGlobalPaymentInformation.
        :type: VTConfigCardNotPresentGlobalPaymentInformationPaymentInformation
        """

        self._payment_information = payment_information

    @property
    def merchant_defined_data_fields(self):
        """
        Gets the merchant_defined_data_fields of this VTConfigCardNotPresentGlobalPaymentInformation.

        :return: The merchant_defined_data_fields of this VTConfigCardNotPresentGlobalPaymentInformation.
        :rtype: VTConfigCardNotPresentGlobalPaymentInformationMerchantDefinedDataFields
        """
        return self._merchant_defined_data_fields

    @merchant_defined_data_fields.setter
    def merchant_defined_data_fields(self, merchant_defined_data_fields):
        """
        Sets the merchant_defined_data_fields of this VTConfigCardNotPresentGlobalPaymentInformation.

        :param merchant_defined_data_fields: The merchant_defined_data_fields of this VTConfigCardNotPresentGlobalPaymentInformation.
        :type: VTConfigCardNotPresentGlobalPaymentInformationMerchantDefinedDataFields
        """

        self._merchant_defined_data_fields = merchant_defined_data_fields

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
        if not isinstance(other, VTConfigCardNotPresentGlobalPaymentInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
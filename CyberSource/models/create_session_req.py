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


class CreateSessionReq(object):
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
        'client_reference_information': 'Ptsv2refreshpaymentstatusidClientReferenceInformation',
        'processing_information': 'Ptsv2paymentreferencesProcessingInformation',
        'payment_information': 'Ptsv2paymentreferencesPaymentInformation',
        'order_information': 'Ptsv2paymentreferencesOrderInformation',
        'buyer_information': 'Ptsv2paymentreferencesBuyerInformation',
        'device_information': 'Ptsv2paymentreferencesDeviceInformation',
        'merchant_information': 'Ptsv2paymentreferencesMerchantInformation',
        'user_interface': 'Ptsv2paymentreferencesUserInterface',
        'merchant_defined_information': 'list[Ptsv2paymentsMerchantDefinedInformation]',
        'agreement_information': 'Ptsv2paymentreferencesAgreementInformation',
        'travel_information': 'Ptsv2paymentreferencesTravelInformation'
    }

    attribute_map = {
        'client_reference_information': 'clientReferenceInformation',
        'processing_information': 'processingInformation',
        'payment_information': 'paymentInformation',
        'order_information': 'orderInformation',
        'buyer_information': 'buyerInformation',
        'device_information': 'deviceInformation',
        'merchant_information': 'merchantInformation',
        'user_interface': 'userInterface',
        'merchant_defined_information': 'merchantDefinedInformation',
        'agreement_information': 'agreementInformation',
        'travel_information': 'travelInformation'
    }

    def __init__(self, client_reference_information=None, processing_information=None, payment_information=None, order_information=None, buyer_information=None, device_information=None, merchant_information=None, user_interface=None, merchant_defined_information=None, agreement_information=None, travel_information=None):
        """
        CreateSessionReq - a model defined in Swagger
        """

        self._client_reference_information = None
        self._processing_information = None
        self._payment_information = None
        self._order_information = None
        self._buyer_information = None
        self._device_information = None
        self._merchant_information = None
        self._user_interface = None
        self._merchant_defined_information = None
        self._agreement_information = None
        self._travel_information = None

        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if processing_information is not None:
          self.processing_information = processing_information
        if payment_information is not None:
          self.payment_information = payment_information
        if order_information is not None:
          self.order_information = order_information
        if buyer_information is not None:
          self.buyer_information = buyer_information
        if device_information is not None:
          self.device_information = device_information
        if merchant_information is not None:
          self.merchant_information = merchant_information
        if user_interface is not None:
          self.user_interface = user_interface
        if merchant_defined_information is not None:
          self.merchant_defined_information = merchant_defined_information
        if agreement_information is not None:
          self.agreement_information = agreement_information
        if travel_information is not None:
          self.travel_information = travel_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this CreateSessionReq.

        :return: The client_reference_information of this CreateSessionReq.
        :rtype: Ptsv2refreshpaymentstatusidClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this CreateSessionReq.

        :param client_reference_information: The client_reference_information of this CreateSessionReq.
        :type: Ptsv2refreshpaymentstatusidClientReferenceInformation
        """



        self._client_reference_information = client_reference_information

    @property
    def processing_information(self):
        """
        Gets the processing_information of this CreateSessionReq.

        :return: The processing_information of this CreateSessionReq.
        :rtype: Ptsv2paymentreferencesProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this CreateSessionReq.

        :param processing_information: The processing_information of this CreateSessionReq.
        :type: Ptsv2paymentreferencesProcessingInformation
        """



        self._processing_information = processing_information

    @property
    def payment_information(self):
        """
        Gets the payment_information of this CreateSessionReq.

        :return: The payment_information of this CreateSessionReq.
        :rtype: Ptsv2paymentreferencesPaymentInformation
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """
        Sets the payment_information of this CreateSessionReq.

        :param payment_information: The payment_information of this CreateSessionReq.
        :type: Ptsv2paymentreferencesPaymentInformation
        """



        self._payment_information = payment_information

    @property
    def order_information(self):
        """
        Gets the order_information of this CreateSessionReq.

        :return: The order_information of this CreateSessionReq.
        :rtype: Ptsv2paymentreferencesOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this CreateSessionReq.

        :param order_information: The order_information of this CreateSessionReq.
        :type: Ptsv2paymentreferencesOrderInformation
        """



        self._order_information = order_information

    @property
    def buyer_information(self):
        """
        Gets the buyer_information of this CreateSessionReq.

        :return: The buyer_information of this CreateSessionReq.
        :rtype: Ptsv2paymentreferencesBuyerInformation
        """
        return self._buyer_information

    @buyer_information.setter
    def buyer_information(self, buyer_information):
        """
        Sets the buyer_information of this CreateSessionReq.

        :param buyer_information: The buyer_information of this CreateSessionReq.
        :type: Ptsv2paymentreferencesBuyerInformation
        """



        self._buyer_information = buyer_information

    @property
    def device_information(self):
        """
        Gets the device_information of this CreateSessionReq.

        :return: The device_information of this CreateSessionReq.
        :rtype: Ptsv2paymentreferencesDeviceInformation
        """
        return self._device_information

    @device_information.setter
    def device_information(self, device_information):
        """
        Sets the device_information of this CreateSessionReq.

        :param device_information: The device_information of this CreateSessionReq.
        :type: Ptsv2paymentreferencesDeviceInformation
        """



        self._device_information = device_information

    @property
    def merchant_information(self):
        """
        Gets the merchant_information of this CreateSessionReq.

        :return: The merchant_information of this CreateSessionReq.
        :rtype: Ptsv2paymentreferencesMerchantInformation
        """
        return self._merchant_information

    @merchant_information.setter
    def merchant_information(self, merchant_information):
        """
        Sets the merchant_information of this CreateSessionReq.

        :param merchant_information: The merchant_information of this CreateSessionReq.
        :type: Ptsv2paymentreferencesMerchantInformation
        """



        self._merchant_information = merchant_information

    @property
    def user_interface(self):
        """
        Gets the user_interface of this CreateSessionReq.

        :return: The user_interface of this CreateSessionReq.
        :rtype: Ptsv2paymentreferencesUserInterface
        """
        return self._user_interface

    @user_interface.setter
    def user_interface(self, user_interface):
        """
        Sets the user_interface of this CreateSessionReq.

        :param user_interface: The user_interface of this CreateSessionReq.
        :type: Ptsv2paymentreferencesUserInterface
        """



        self._user_interface = user_interface

    @property
    def merchant_defined_information(self):
        """
        Gets the merchant_defined_information of this CreateSessionReq.
        The object containing the custom data that the merchant defines. 

        :return: The merchant_defined_information of this CreateSessionReq.
        :rtype: list[Ptsv2paymentsMerchantDefinedInformation]
        """
        return self._merchant_defined_information

    @merchant_defined_information.setter
    def merchant_defined_information(self, merchant_defined_information):
        """
        Sets the merchant_defined_information of this CreateSessionReq.
        The object containing the custom data that the merchant defines. 

        :param merchant_defined_information: The merchant_defined_information of this CreateSessionReq.
        :type: list[Ptsv2paymentsMerchantDefinedInformation]
        """



        self._merchant_defined_information = merchant_defined_information

    @property
    def agreement_information(self):
        """
        Gets the agreement_information of this CreateSessionReq.

        :return: The agreement_information of this CreateSessionReq.
        :rtype: Ptsv2paymentreferencesAgreementInformation
        """
        return self._agreement_information

    @agreement_information.setter
    def agreement_information(self, agreement_information):
        """
        Sets the agreement_information of this CreateSessionReq.

        :param agreement_information: The agreement_information of this CreateSessionReq.
        :type: Ptsv2paymentreferencesAgreementInformation
        """



        self._agreement_information = agreement_information

    @property
    def travel_information(self):
        """
        Gets the travel_information of this CreateSessionReq.

        :return: The travel_information of this CreateSessionReq.
        :rtype: Ptsv2paymentreferencesTravelInformation
        """
        return self._travel_information

    @travel_information.setter
    def travel_information(self, travel_information):
        """
        Sets the travel_information of this CreateSessionReq.

        :param travel_information: The travel_information of this CreateSessionReq.
        :type: Ptsv2paymentreferencesTravelInformation
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
        if not isinstance(other, CreateSessionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

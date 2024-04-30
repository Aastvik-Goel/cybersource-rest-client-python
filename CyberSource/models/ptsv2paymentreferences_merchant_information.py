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


class Ptsv2paymentreferencesMerchantInformation(object):
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
        'merchant_descriptor': 'Ptsv2paymentsMerchantInformationMerchantDescriptor',
        'cancel_url': 'str',
        'success_url': 'str',
        'failure_url': 'str',
        'note_to_buyer': 'str'
    }

    attribute_map = {
        'merchant_descriptor': 'merchantDescriptor',
        'cancel_url': 'cancelUrl',
        'success_url': 'successUrl',
        'failure_url': 'failureUrl',
        'note_to_buyer': 'noteToBuyer'
    }

    def __init__(self, merchant_descriptor=None, cancel_url=None, success_url=None, failure_url=None, note_to_buyer=None):
        """
        Ptsv2paymentreferencesMerchantInformation - a model defined in Swagger
        """

        self._merchant_descriptor = None
        self._cancel_url = None
        self._success_url = None
        self._failure_url = None
        self._note_to_buyer = None

        if merchant_descriptor is not None:
          self.merchant_descriptor = merchant_descriptor
        if cancel_url is not None:
          self.cancel_url = cancel_url
        if success_url is not None:
          self.success_url = success_url
        if failure_url is not None:
          self.failure_url = failure_url
        if note_to_buyer is not None:
          self.note_to_buyer = note_to_buyer

    @property
    def merchant_descriptor(self):
        """
        Gets the merchant_descriptor of this Ptsv2paymentreferencesMerchantInformation.

        :return: The merchant_descriptor of this Ptsv2paymentreferencesMerchantInformation.
        :rtype: Ptsv2paymentsMerchantInformationMerchantDescriptor
        """
        return self._merchant_descriptor

    @merchant_descriptor.setter
    def merchant_descriptor(self, merchant_descriptor):
        """
        Sets the merchant_descriptor of this Ptsv2paymentreferencesMerchantInformation.

        :param merchant_descriptor: The merchant_descriptor of this Ptsv2paymentreferencesMerchantInformation.
        :type: Ptsv2paymentsMerchantInformationMerchantDescriptor
        """

        self._merchant_descriptor = merchant_descriptor

    @property
    def cancel_url(self):
        """
        Gets the cancel_url of this Ptsv2paymentreferencesMerchantInformation.
        customer would be redirected to this url based on the decision of the transaction

        :return: The cancel_url of this Ptsv2paymentreferencesMerchantInformation.
        :rtype: str
        """
        return self._cancel_url

    @cancel_url.setter
    def cancel_url(self, cancel_url):
        """
        Sets the cancel_url of this Ptsv2paymentreferencesMerchantInformation.
        customer would be redirected to this url based on the decision of the transaction

        :param cancel_url: The cancel_url of this Ptsv2paymentreferencesMerchantInformation.
        :type: str
        """

        self._cancel_url = cancel_url

    @property
    def success_url(self):
        """
        Gets the success_url of this Ptsv2paymentreferencesMerchantInformation.
        customer would be redirected to this url based on the decision of the transaction

        :return: The success_url of this Ptsv2paymentreferencesMerchantInformation.
        :rtype: str
        """
        return self._success_url

    @success_url.setter
    def success_url(self, success_url):
        """
        Sets the success_url of this Ptsv2paymentreferencesMerchantInformation.
        customer would be redirected to this url based on the decision of the transaction

        :param success_url: The success_url of this Ptsv2paymentreferencesMerchantInformation.
        :type: str
        """

        self._success_url = success_url

    @property
    def failure_url(self):
        """
        Gets the failure_url of this Ptsv2paymentreferencesMerchantInformation.
        customer would be redirected to this url based on the decision of the transaction

        :return: The failure_url of this Ptsv2paymentreferencesMerchantInformation.
        :rtype: str
        """
        return self._failure_url

    @failure_url.setter
    def failure_url(self, failure_url):
        """
        Sets the failure_url of this Ptsv2paymentreferencesMerchantInformation.
        customer would be redirected to this url based on the decision of the transaction

        :param failure_url: The failure_url of this Ptsv2paymentreferencesMerchantInformation.
        :type: str
        """

        self._failure_url = failure_url

    @property
    def note_to_buyer(self):
        """
        Gets the note_to_buyer of this Ptsv2paymentreferencesMerchantInformation.
        Free-form text field.

        :return: The note_to_buyer of this Ptsv2paymentreferencesMerchantInformation.
        :rtype: str
        """
        return self._note_to_buyer

    @note_to_buyer.setter
    def note_to_buyer(self, note_to_buyer):
        """
        Sets the note_to_buyer of this Ptsv2paymentreferencesMerchantInformation.
        Free-form text field.

        :param note_to_buyer: The note_to_buyer of this Ptsv2paymentreferencesMerchantInformation.
        :type: str
        """

        self._note_to_buyer = note_to_buyer

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
        if not isinstance(other, Ptsv2paymentreferencesMerchantInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

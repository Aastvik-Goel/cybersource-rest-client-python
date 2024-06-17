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


class Ptsv1pushfundstransferSenderInformationPaymentInformation(object):
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
        'card': 'Ptsv1pushfundstransferSenderInformationPaymentInformationCard'
    }

    attribute_map = {
        'card': 'card'
    }

    def __init__(self, card=None):
        """
        Ptsv1pushfundstransferSenderInformationPaymentInformation - a model defined in Swagger
        """

        self._card = None

        if card is not None:
          self.card = card

    @property
    def card(self):
        """
        Gets the card of this Ptsv1pushfundstransferSenderInformationPaymentInformation.

        :return: The card of this Ptsv1pushfundstransferSenderInformationPaymentInformation.
        :rtype: Ptsv1pushfundstransferSenderInformationPaymentInformationCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this Ptsv1pushfundstransferSenderInformationPaymentInformation.

        :param card: The card of this Ptsv1pushfundstransferSenderInformationPaymentInformation.
        :type: Ptsv1pushfundstransferSenderInformationPaymentInformationCard
        """



        self._card = card

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
        if not isinstance(other, Ptsv1pushfundstransferSenderInformationPaymentInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

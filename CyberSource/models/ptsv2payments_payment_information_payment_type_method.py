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


class Ptsv2paymentsPaymentInformationPaymentTypeMethod(object):
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
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, name=None, type=None):
        """
        Ptsv2paymentsPaymentInformationPaymentTypeMethod - a model defined in Swagger
        """

        self._name = None
        self._type = None

        if name is not None:
          self.name = name
        if type is not None:
          self.type = type

    @property
    def name(self):
        """
        Gets the name of this Ptsv2paymentsPaymentInformationPaymentTypeMethod.
        A Payment Type is enabled through a Method. Examples: Visa, Master Card, ApplePay, iDeal, 7Eleven, alfamart, etc  For Japan Payment Processing Valid Values: - 1 Banking Data - 2 Authorization Data  #### Via KCP - `KCP` : Local Card, Bank Transfer and Carrier Billing. - `PAYCO` - `KAKAOPAY` - `NAVERPAY` 

        :return: The name of this Ptsv2paymentsPaymentInformationPaymentTypeMethod.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Ptsv2paymentsPaymentInformationPaymentTypeMethod.
        A Payment Type is enabled through a Method. Examples: Visa, Master Card, ApplePay, iDeal, 7Eleven, alfamart, etc  For Japan Payment Processing Valid Values: - 1 Banking Data - 2 Authorization Data  #### Via KCP - `KCP` : Local Card, Bank Transfer and Carrier Billing. - `PAYCO` - `KAKAOPAY` - `NAVERPAY` 

        :param name: The name of this Ptsv2paymentsPaymentInformationPaymentTypeMethod.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this Ptsv2paymentsPaymentInformationPaymentTypeMethod.
        The payment channel that facilitates the transactions. This parameter can be used if the payment channels are listed on the merchant’s site, and the payment channel is known.  Possible Values:  #### Via PPRO - `alfaVa` - `kredivo` - `consumerBarCode` - `merchantQrCode` - `dokuWallet` 

        :return: The type of this Ptsv2paymentsPaymentInformationPaymentTypeMethod.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Ptsv2paymentsPaymentInformationPaymentTypeMethod.
        The payment channel that facilitates the transactions. This parameter can be used if the payment channels are listed on the merchant’s site, and the payment channel is known.  Possible Values:  #### Via PPRO - `alfaVa` - `kredivo` - `consumerBarCode` - `merchantQrCode` - `dokuWallet` 

        :param type: The type of this Ptsv2paymentsPaymentInformationPaymentTypeMethod.
        :type: str
        """

        self._type = type

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
        if not isinstance(other, Ptsv2paymentsPaymentInformationPaymentTypeMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

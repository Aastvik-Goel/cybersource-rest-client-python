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


class Ptsv2paymentsTokenInformation(object):
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
        'jti': 'str',
        'transient_token_jwt': 'str',
        'payment_instrument': 'Ptsv2paymentsTokenInformationPaymentInstrument',
        'shipping_address': 'Ptsv2paymentsTokenInformationShippingAddress',
        'network_token_option': 'str'
    }

    attribute_map = {
        'jti': 'jti',
        'transient_token_jwt': 'transientTokenJwt',
        'payment_instrument': 'paymentInstrument',
        'shipping_address': 'shippingAddress',
        'network_token_option': 'networkTokenOption'
    }

    def __init__(self, jti=None, transient_token_jwt=None, payment_instrument=None, shipping_address=None, network_token_option=None):
        """
        Ptsv2paymentsTokenInformation - a model defined in Swagger
        """

        self._jti = None
        self._transient_token_jwt = None
        self._payment_instrument = None
        self._shipping_address = None
        self._network_token_option = None

        if jti is not None:
          self.jti = jti
        if transient_token_jwt is not None:
          self.transient_token_jwt = transient_token_jwt
        if payment_instrument is not None:
          self.payment_instrument = payment_instrument
        if shipping_address is not None:
          self.shipping_address = shipping_address
        if network_token_option is not None:
          self.network_token_option = network_token_option

    @property
    def jti(self):
        """
        Gets the jti of this Ptsv2paymentsTokenInformation.
        TMS Transient Token, 64 hexadecimal id value representing captured payment credentials (including Sensitive Authentication Data, e.g. CVV). 

        :return: The jti of this Ptsv2paymentsTokenInformation.
        :rtype: str
        """
        return self._jti

    @jti.setter
    def jti(self, jti):
        """
        Sets the jti of this Ptsv2paymentsTokenInformation.
        TMS Transient Token, 64 hexadecimal id value representing captured payment credentials (including Sensitive Authentication Data, e.g. CVV). 

        :param jti: The jti of this Ptsv2paymentsTokenInformation.
        :type: str
        """



        self._jti = jti

    @property
    def transient_token_jwt(self):
        """
        Gets the transient_token_jwt of this Ptsv2paymentsTokenInformation.
        Flex API Transient Token encoded as JWT (JSON Web Token), e.g. Flex microform or Unified Payment checkout result. 

        :return: The transient_token_jwt of this Ptsv2paymentsTokenInformation.
        :rtype: str
        """
        return self._transient_token_jwt

    @transient_token_jwt.setter
    def transient_token_jwt(self, transient_token_jwt):
        """
        Sets the transient_token_jwt of this Ptsv2paymentsTokenInformation.
        Flex API Transient Token encoded as JWT (JSON Web Token), e.g. Flex microform or Unified Payment checkout result. 

        :param transient_token_jwt: The transient_token_jwt of this Ptsv2paymentsTokenInformation.
        :type: str
        """



        self._transient_token_jwt = transient_token_jwt

    @property
    def payment_instrument(self):
        """
        Gets the payment_instrument of this Ptsv2paymentsTokenInformation.

        :return: The payment_instrument of this Ptsv2paymentsTokenInformation.
        :rtype: Ptsv2paymentsTokenInformationPaymentInstrument
        """
        return self._payment_instrument

    @payment_instrument.setter
    def payment_instrument(self, payment_instrument):
        """
        Sets the payment_instrument of this Ptsv2paymentsTokenInformation.

        :param payment_instrument: The payment_instrument of this Ptsv2paymentsTokenInformation.
        :type: Ptsv2paymentsTokenInformationPaymentInstrument
        """



        self._payment_instrument = payment_instrument

    @property
    def shipping_address(self):
        """
        Gets the shipping_address of this Ptsv2paymentsTokenInformation.

        :return: The shipping_address of this Ptsv2paymentsTokenInformation.
        :rtype: Ptsv2paymentsTokenInformationShippingAddress
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """
        Sets the shipping_address of this Ptsv2paymentsTokenInformation.

        :param shipping_address: The shipping_address of this Ptsv2paymentsTokenInformation.
        :type: Ptsv2paymentsTokenInformationShippingAddress
        """



        self._shipping_address = shipping_address

    @property
    def network_token_option(self):
        """
        Gets the network_token_option of this Ptsv2paymentsTokenInformation.
        Indicates whether a payment network token associated with a TMS token should be used for authorization. This field can contain one of following values:  - `ignore`: Use a tokenized card number for an authorization, even if the TMS token has an associated payment network token. - `prefer`: (Default) Use an associated payment network token for an authorization if the TMS token has one; otherwise, use the tokenized card number. 

        :return: The network_token_option of this Ptsv2paymentsTokenInformation.
        :rtype: str
        """
        return self._network_token_option

    @network_token_option.setter
    def network_token_option(self, network_token_option):
        """
        Sets the network_token_option of this Ptsv2paymentsTokenInformation.
        Indicates whether a payment network token associated with a TMS token should be used for authorization. This field can contain one of following values:  - `ignore`: Use a tokenized card number for an authorization, even if the TMS token has an associated payment network token. - `prefer`: (Default) Use an associated payment network token for an authorization if the TMS token has one; otherwise, use the tokenized card number. 

        :param network_token_option: The network_token_option of this Ptsv2paymentsTokenInformation.
        :type: str
        """



        self._network_token_option = network_token_option

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
        if not isinstance(other, Ptsv2paymentsTokenInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
